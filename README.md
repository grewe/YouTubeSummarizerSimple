# Amazing Gemini Video Summarizer

This application is a Flask-based web service that leverages **Google Gemini** multimodal models (via Vertex AI) to analyze and summarize videos. Users can provide a Cloud Storage URI for a video file, select a Gemini model, and optionally provide custom instructions to guide the AI's summary.

### Features
* **Multimodal Summarization**: Uses Gemini's ability to "watch" videos and understand audio/visual context.
* **Vertex AI Integration**: Uses the `google-genai` SDK to interact with enterprise Gemini models.
* **Customizable Prompts**: Users can add specific directions (e.g., "Summarize as a bulleted list" or "Focus on the technical aspects").

### Table of Contents
* Prerequisites
* Getting Started
* Deployment

---
## Prerequisites
* **Google Cloud Project**: An active project with the **Vertex AI API** enabled.
* **Project ID**: The project ID currently set in `app.py` is `affable-anagram-500422-u4`.
* **Cloud Storage**: Videos must be stored in a GCS bucket (e.g., `gs://bucket-name/video.mp4`) that the service account has permissions to read.
* **Authentication**: Locally, you should have Application Default Credentials configured via `gcloud auth application-default login`.

---
## Getting Started

### Run the app locally
1. Install dependencies:
   ```bash
   pip install flask google-genai

### Deployment
gcloud config set project [PROJECT_ID]
gcloud run deploy --source .
OR gcloud run deploy youtube-summarizer --source . --region us-central1 

NOTE: It will prompt you to enter a name for your service, let's say "youtube-summarizer". Choose the corresponding number for the region "us-central1". Say "y" when it asks if you want to allow unauthenticated invocations. Note that we are allowing unauthenticated access here because this is a demo application. Recommendation is to use appropriate authentication for your enterprise and production applications.
