# AI File Assistant

## Overview

This project implements an AI-powered File Assistant using Python and OpenAI LLM tool calling.

The assistant understands natural language queries and uses structured tools to perform file system operations.

Supported file formats:

- TXT
- PDF
- DOCX

---

## Features

- Read resume files
- List files
- Filter files by extension
- Search keywords in resumes
- Write TXT and DOCX files
- Case-insensitive search
- Tool-based LLM integration

---

## Project Structure

ai_file_assistant/

    fs_tools.py
    llm_file_assistant.py
    requirements.txt
    README.md

    resumes/

---

## Installation

Install dependencies:
pip install -r requirements.txt

## Setup API Key

Create OpenAI API key:

https://platform.openai.com/api-keys

Set environment variable.

Windows:

setx OPENAI_API_KEY "your_api_key"


Restart terminal after setting key.

---

## Run Application

Restart terminal after setting key.

---

## Run Application
You will see:


---

## Example Queries

### List files
List files in resumes folder

### Filter files

List files in resumes folder extension .txt


### Search keyword

Find resumes with Python experience


### Write file

Create file output/test.txt containing Python developer


---

## Tools Implemented

### read_file()

- Supports TXT, PDF, DOCX
- Extracts text
- Returns metadata

### list_files()

- Lists files
- Extension filter
- Metadata output

### write_file()

- Writes TXT/DOCX
- Auto creates directories

### search_in_file()

- Case insensitive search
- Returns context

### search_in_directory()

- Searches all resumes

---

## Author

Rishabh Jaiswal