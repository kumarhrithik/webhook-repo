# Webhook Repository

The `webhook-repo` is a Flask-based web application designed to receive webhook events from a GitHub repository (`action-repo`) and store them in a MongoDB database. The application also provides a minimal user interface that displays the latest actions performed on the repository.

## Overview

This repository receives webhook events from a GitHub repository (`action-repo`) for actions such as Push, Pull Request, and Merge. It stores the events in MongoDB and displays the latest actions in a user-friendly web interface.

## Installation
### Prerequisites

- Python 3.8+
- MongoDB instance (local or cloud-based)

### Steps

1. **Clone the repository**:
2. **Install the required packages**:
    pip install -r requirements.txt


## Configuration

### MongoDB Setup

Ensure you have a running MongoDB instance. You can use a local MongoDB server or a cloud-based service like MongoDB Atlas.

### Flask Configuration

The MongoDB connection string is hardcoded in `app.py`. Update it to match your MongoDB setup:
client = MongoClient('mongodb://localhost:27017/')

### Setting Up Webhook in GitHub
Navigate to your GitHub repository.
Go to Settings > Webhooks > Add webhook.
Enter the payload URL: http://your-server-url/webhook.
Set the content type to application/json.
Choose the events you want to trigger the webhook (Push, Pull Request, Merge).
Save the webhook.
