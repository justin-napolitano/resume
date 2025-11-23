---
slug: "github-resume"
title: "resume"
repo: "justin-napolitano/resume"
githubUrl: "https://github.com/justin-napolitano/resume"
generatedAt: "2025-11-23T09:33:01.693908Z"
source: "github-auto"
---


# Technical Overview of the Resume Repository

This repository contains a LaTeX-based resume project tailored for software developers, emphasizing automation and maintainability. The core deliverable is a single-page, one-column resume built using LaTeX templates with custom commands for consistent formatting.

## Motivation and Problem Statement

Maintaining a professional resume that is both visually appealing and easy to update is a common challenge. This project addresses that by leveraging LaTeX for high-quality typesetting combined with automation scripts to streamline building, deploying, and backing up the resume. The goal is to reduce manual effort and ensure consistency across different formats and deployments.

## Architecture and Components

### LaTeX Source

The resume content and formatting reside in the `/latex` directory, structured with base templates and custom commands. This approach allows for modular updates to sections such as education, experience, and projects.

### Build Automation

A `Makefile` orchestrates the build process, primarily generating HTML output from the LaTeX source. Python scripts like `python_build.py` automate dependency installation and invoke build commands, wrapping system calls to `make` and Git operations.

### Deployment

Deployment is handled via Bash scripts (`deploy.sh`, `deployz.sh`) that use `ghp-import` to push the generated HTML to GitHub Pages. This enables hosting the resume at a custom domain (`cv.jnapolitano.io`).

### Backup

The `backup_html.py` script integrates with the Dropbox API to upload the built HTML version of the resume. It requires a Dropbox app and access token for authentication. The script includes error handling for quota limits and API errors, ensuring reliable backups.

### Environment Setup

Additional shell scripts (`install.sh`, `mac_setup.sh`, `uninstall.sh`) assist with environment configuration, dependency installation, and cleanup. A `Dockerfile` provides a containerized environment for consistent builds across systems.

## Implementation Details

- The Python build pipeline (`python_build.py`) uses subprocess calls to invoke `make` commands and manage Git operations like add, commit, and push, facilitating continuous integration workflows.
- The backup script uses the official Dropbox SDK for Python, reading the local HTML build directory and uploading it with overwrite mode.
- The repository includes multiple shell scripts for various automation tasks, indicating an emphasis on scripting to reduce manual intervention.
- The Sphinx documentation configuration (`source/conf.py`) suggests additional project documentation is maintained, although details are limited.

## Practical Considerations

- The project assumes familiarity with LaTeX, Python, Bash scripting, and Git.
- To use the backup feature, one must create a Dropbox app and generate an access token, which is then inserted into the script.
- The deployment relies on GitHub Pages and the `ghp-import` tool, which requires appropriate permissions and setup.

## Summary

This repository exemplifies a practical approach to managing a LaTeX resume with automation for building, deploying, and backing up. The combination of scripting, containerization, and cloud storage integration reflects a mature workflow aimed at reducing manual overhead and ensuring reliability. Returning to this project, one should focus on the build scripts and deployment pipeline as the core mechanisms enabling continuous updates and hosting.

---