---
slug: github-resume-note-technical-overview
id: github-resume-note-technical-overview
title: Resume Repo Overview
repo: justin-napolitano/resume
githubUrl: https://github.com/justin-napolitano/resume
generatedAt: '2025-11-24T18:45:07.465Z'
source: github-auto
summary: >-
  This repo is all about crafting a professional LaTeX resume for developers. It
  features a single-page layout with custom commands for easy formatting. Key
  components include:
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

This repo is all about crafting a professional LaTeX resume for developers. It features a single-page layout with custom commands for easy formatting. Key components include:

- **Tech Stack**: LaTeX for formatting, Python for automation, and Bash for deployment. Docker is available for containerized builds.
- **Scripts**: There are automated deployment scripts and a Python backup for Dropbox integration.
  
## Getting Started

1. **Clone the Repo**:

    ```bash
    git clone https://github.com/justin-napolitano/resume.git
    cd resume
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Build the Resume**:

    ```bash
    make html
    ```

4. **Deploy**:

    ```bash
    ./deploy.sh
    ```

### Gotchas

- You'll need a Dropbox API token for backups. Update it in `backup_html.py`. 
- Ensure Python is 3.5 or higher.
