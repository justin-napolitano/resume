---
slug: github-resume-writing-overview
id: github-resume-writing-overview
title: 'My LaTeX Resume: A Straightforward Approach'
repo: justin-napolitano/resume
githubUrl: https://github.com/justin-napolitano/resume
generatedAt: '2025-11-24T17:55:23.158Z'
source: github-auto
summary: >-
  I created a LaTeX-based resume project to solve a common problem: getting my
  resume to look neat, professional, and easy to customize. It's designed for
  software developers, so it leverages LaTeX templates and fonts, making sure
  you can tweak it exactly to your taste without sacrificing a clean layout.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: writing
entryLayout: writing
showInProjects: false
showInNotes: false
showInWriting: true
showInLogs: false
---

I created a LaTeX-based resume project to solve a common problem: getting my resume to look neat, professional, and easy to customize. It's designed for software developers, so it leverages LaTeX templates and fonts, making sure you can tweak it exactly to your taste without sacrificing a clean layout.

## Why This Repo Exists

I’ve been through my fair share of resume templates, and honestly, many of them were a pain to modify. I wanted a solution that kept the formatting consistent while allowing for easy customization. I also wanted to minimize all the manual work that usually goes with building and maintaining a resume. This repo aims to do just that. 

With this project, I can focus on the content rather than the formatting. It’s streamlined, efficient, and integrates well with tools I already use.

## Key Design Decisions

When I set out to build this repo, I had a few priorities in mind:

1. **Single-Page Layout**: I opted for a one-column, single-page format optimized for clarity. No wall of text, just the essentials.
2. **Consistent Formatting**: I heavily utilize LaTeX templates and custom commands. This ensures your headers, bullets, and other elements have the same style throughout the document. 
3. **Automation**: I built in automated scripts for building and deploying the resume. I wanted the whole process to be as hands-off as possible.
4. **Backup Integration**: With everything online, a backup is crucial, so I added a Dropbox integration for easy preservation of the HTML build.

## Tech Stack

Here’s what I used:

- **LaTeX**: For formatting the resume.
- **Python (3.5+)**: For build automation and backup scripts.
- **Bash**: Yes, I'm still a fan of good ol’ Bash for setup and deployment tasks.
- **Docker**: To create a consistent build environment and avoid "it works on my machine" issues.
- **GitHub Pages**: To deploy the HTML version of the resume with a nice, clean URL.

## Getting Started

If you want to give it a shot, here’s how to get set up:

### Prerequisites

- Python 3.5 or higher.
- Docker (optional, but it makes life easier).
- Make (to automate builds).
- A Dropbox account and API token for backups.

### Installation

Just clone the repository:

```bash
git clone https://github.com/justin-napolitano/resume.git
cd resume
```

Then, install the Python dependencies:

```bash
pip install -r requirements.txt
```

### Building the Resume

Building the HTML version is straightforward:

```bash
make html
```

### Deployment

Deploying to GitHub Pages? Easy peasy:

```bash
./deploy.sh
```

### Backup

For Dropbox backups, update `backup_html.py` with your access token and run:

```bash
python backup_html.py
```

## Project Structure

Here’s a quick breakdown of how the files are organized:

```
/latex           # LaTeX source files for the resume
/source          # Documentation source (probably for the project docs)
acp.sh           # Bash script for automation
backup_html.py   # Python script for backing up HTML builds
deploy.sh        # Bash script for deploying to GitHub Pages
Dockerfile       # Dockerfile for the build environment
Makefile         # Build automation for cleaning and building
README.md        # This file
requirements.txt # Python dependencies
...              # Other scripts for setup, deployment, and maintenance
```

## Tradeoffs

Every repo comes with its quirks. Here are a few I navigated during development:

- **Learning Curve**: LaTeX is powerful, but it can be a bit verbose compared to markdown or HTML. Expect a little ramp-up time.
- **Complexity of Docker**: While Docker eliminates a lot of environment issues, it does add more complexity to your setup. If you’re not familiar, you might find it a bit daunting.
- **Dependency Management**: Keeping your Python packages updated inside the Docker container can be a pain. I’d recommend pinning versions to avoid surprises.

## Future Work / Roadmap

This project is a work in progress, and here’s what I’m looking to tackle next:

- **Documentation Overhaul**: I want to improve the existing documentation and add inline comments in the scripts. Clarity is key.
- **Automated Testing**: I plan to implement some basic automated tests for the build scripts. Quality assurance is a must.
- **Enhanced Backup Script**: The Dropbox backup method could benefit from better error handling and logging.
- **Full CI/CD Integration**: I aim to incorporate continuous integration/continuous deployment so any changes I push get reflected immediately.
- **Docker Expansion**: Adding more comprehensive Docker support for the entire build and deployment pipeline is high on my list.

## In Closing

I hope this walking you through my LaTeX resume project has sparked some interest. If you have any questions or suggestions, feel free to ping me. I share updates about this project and others on Mastodon, Bluesky, and Twitter/X, so follow along if you’re keen to see what I’m working on next.

Check out the repo on GitHub [here](https://github.com/justin-napolitano/resume). Happy coding!
