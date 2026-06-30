#FIRST make sure prior to running this you have set google cloud project id



# List projects
gcloud projects list

# Set project
gcloud config set project affable-anagram-500422-u4

# Verify project
gcloud config get-value project

# Verify login
gcloud auth list

# Verify ADC
gcloud auth application-default print-access-token

# Check Vertex AI API
gcloud services list --enabled | grep aiplatform

# Enable Vertex AI API if needed
gcloud services enable aiplatform.googleapis.com