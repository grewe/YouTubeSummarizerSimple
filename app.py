import os

from flask import Flask, render_template, request, redirect
from google import genai
from google.genai import types

# Initialize the Flask application.
app = Flask(__name__)

# Automatically detect the project ID from the environment or use the hardcoded fallback
# Default project ID
DEFAULT_PROJECT_ID = "affable-anagram-500422-u4"

# Use the environment variable if it exists
PROJECT_ID = os.environ.get(
    "GOOGLE_CLOUD_PROJECT",
    DEFAULT_PROJECT_ID
)

print(f"Starting app with Project ID: {PROJECT_ID}")


# Initialize the Gemini GenAI client using Vertex AI.
client = genai.Client(
   vertexai=True,  # Set to False if you want to use a Gemini API Key instead of Vertex AI
   project=PROJECT_ID,
   location="us-central1",
)

# Define the home page route.
@app.route('/', methods=['GET'])
def index():
   '''
   Renders the home page.
   Returns:The rendered template.
   '''
   return render_template('index.html')


def generate(youtube_link, model, additional_prompt):
   '''
   Interacts with the Gemini model to generate a summary of a YouTube video.
   
   Args:
       youtube_link (str): The Cloud Storage URI of the video file (e.g., gs://bucket/video.mp4).
       model (str): The specific Gemini model ID to use.
       additional_prompt (str): Optional user-provided instructions.
   '''

   # Prepare youtube video using the provided link
   youtube_video = types.Part.from_uri(
       file_uri=youtube_link,
       mime_type="video/*",
   )

   # If addtional prompt is not provided, just append a space
   if not additional_prompt:
       additional_prompt = " "

   # Prepare content to send to the model
   contents = [
       youtube_video,
       types.Part.from_text(text="""Provide a summary of the video."""),
       types.Part.from_text(text=additional_prompt),
   ]

   # Define content configuration
   generate_content_config = types.GenerateContentConfig(
       temperature = 1,
       top_p = 0.95,
       max_output_tokens = 8192,
       response_modalities = ["TEXT"],
   )

   # Call the Gemini API and return the resulting text.
   return client.models.generate_content(
       model = model,
       contents = contents,
       config = generate_content_config,
   ).text

@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
   '''
   Summarize the user provided YouTube video.
   Returns: Summary.
   '''

   # If the request is a POST request, process the form data.
   if request.method == 'POST':
       youtube_link = request.form['youtube_link']
       model = request.form['model']
       additional_prompt = request.form['additional_prompt']
       print(f"Processing summary request for {youtube_link} using model: {model}")
     
       # Generate the summary.
       try:
           summary = generate(youtube_link, model, additional_prompt)
           return summary

       except Exception as e:
           return f"Error generating summary: {str(e)}", 500
 
   # If the request is a GET request, redirect to the home page.
   else:
       return redirect('/')


# Run the Flask app on the port specified by the environment, or 8080 by default.
if __name__ == '__main__':
   server_port = int(os.environ.get('PORT', '8080'))
   app.run(debug=False, port=server_port, host='0.0.0.0')