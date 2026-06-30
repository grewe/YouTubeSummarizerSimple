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
* **Project ID**: The project ID currently set in `app.py` is `XXXXXX`. YOU must change it

* **Authentication**: Locally, you should have Application Default Credentials configured via `gcloud auth application-default login`.




---
# Getting Started

## Requirements

- Python 3.11 or newer
- Google Cloud Project
- Vertex AI API enabled
- Billing enabled on the Google Cloud project
- A Google Cloud account with permission to use Vertex AI

---

## Clone Repository
```bash
git clone https://github.com/grewe/YouTubeSummarizerSimple.git
cd amazing-gemini-app
```

---

## Create Virtual Environment

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```cmd
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Google Cloud

Authenticate:

```bash
gcloud auth application-default login
```

Select your project:

```bash
gcloud config set project YOUR_PROJECT_ID
```

Enable Vertex AI API:

```bash
gcloud services enable aiplatform.googleapis.com
```



OR edit and run setup-cloud.sh
```
bash setup-cloud.sh
```

---

## Update app.py

Replace

```python
PROJECT_ID = "REPLACE_WITH_YOUR_PROJECT_ID"
```

with

```python
PROJECT_ID = "YOUR_PROJECT_ID"
```

Alternatively, modify the application to read the project ID from an environment variable.

---
# Run Application

### Run the app locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt


2. run app
```bash
python app.py
```

### Deployment to Google Cloud Run

make sure project set correctly if not
```bash
gcloud config set project [PROJECT_ID]
```


now deploy

```bash
gcloud run deploy --source .
```

OR
```bash
gcloud run deploy youtube-summarizer --source . --region us-central1 
```

OR
```bash
gcloud run deploy youtube-summarizer \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```
NOTE: Depending on your choice above it will prompt you to enter a name for your service, let's say "youtube-summarizer". Choose the corresponding number for the region "us-central1". Say "y" when it asks if you want to allow unauthenticated invocations. Note that we are allowing unauthenticated access here because this is a demo application. Recommendation is to use appropriate authentication for your enterprise and production applications.


# (CLEANUP) Remove the Cloud Run Service

### Option 1: Using the Google Cloud CLI

List all Cloud Run services in the deployment region:

```bash
gcloud run services list --region us-central1
```
s
Example output:

```text
SERVICE               REGION
youtube-summarizer    us-central1
```

Delete the Cloud Run service:

```bash
gcloud run services delete youtube-summarizer \
    --region us-central1
```

When prompted:

```text
Do you want to continue (Y/n)?
```

Type:

```text
Y
```

to permanently delete the service.

---

### Option 2: Using the Google Cloud Console

1. Open **Google Cloud Console**.
2. Navigate to **Cloud Run**.
3. Select the service (e.g., `youtube-summarizer`).
4. Click **Delete**.
5. Confirm the deletion.

---

## Verify the Service Has Been Removed

```bash
gcloud run services list --region us-central1
```

The deleted service should no longer appear in the list.

---

## What Is Deleted?

Deleting the Cloud Run service removes:

- The deployed web application
- The Cloud Run service configuration
- The public Cloud Run URL

The following resources are **not** deleted:

- Source code
- GitHub repository
- Cloud Shell project files
- Cloud Storage buckets
- Firestore databases
- Artifact Registry container images

---

## Optional: Remove Container Images

Cloud Run stores built container images in **Artifact Registry**. These images remain after the Cloud Run service is deleted.

To list Artifact Registry repositories:

```bash
gcloud artifacts repositories list
```

You can later delete unused repositories or container images if you wish to reclaim storage.