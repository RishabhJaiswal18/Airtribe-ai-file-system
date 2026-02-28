# """
# llm_file_assistant.py

# AI File Assistant using OpenAI LLM Tool Calling.

# This module integrates file system tools with an LLM.

# The assistant can understand natural language queries and
# automatically call tools to:

# - Read resume files
# - List files
# - Search keywords
# - Write files

# Example Queries:

# - List files in resumes folder
# - Find resumes with Python experience
# - Read resumes/resume_john_doe.txt
# - Create file summary.txt containing Python developer
# """

import json
import os

from openai import OpenAI
import fs_tools


# Use environment variable (Professional way)
client = OpenAI(
    # api_key=os.getenv("OPENAI_API_KEY")
    api_key="YOUR_OPENAI_KEY"
)


# ===============================
# TOOL DEFINITIONS
# ===============================

tools = [
    # LIST FILES
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List files in a directory. Can filter by extension like .pdf .txt .docx .doc",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {"type": "string"},
                    "extension": {"type": "string"},
                },
                "required": ["directory"],
            },
        },
    },
    # READ FILE
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read TXT PDF or DOCX resume file",
            "parameters": {
                "type": "object",
                "properties": {"filepath": {"type": "string"}},
                "required": ["filepath"],
            },
        },
    },
    # SEARCH FILE
    {
        "type": "function",
        "function": {
            "name": "search_in_file",
            "description": "Search keyword inside a resume file",
            "parameters": {
                "type": "object",
                "properties": {
                    "filepath": {"type": "string"},
                    "keyword": {"type": "string"},
                },
                "required": ["filepath", "keyword"],
            },
        },
    },
    # SEARCH DIRECTORY
    {
        "type": "function",
        "function": {
            "name": "search_in_directory",
            "description": "Search keyword across all resumes in a directory",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {"type": "string"},
                    "keyword": {"type": "string"},
                },
                "required": ["directory", "keyword"],
            },
        },
    },
    # WRITE FILE
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write content to TXT or DOCX file and create folders if needed",
            "parameters": {
                "type": "object",
                "properties": {
                    "filepath": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["filepath", "content"],
            },
        },
    },
]


# ===============================
# MAIN LLM FUNCTION
# ===============================


def ask_llm(user_question):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a file assistant. Always use tools when user asks about files, resumes, search, read, write or list.",
            },
            {"role": "user", "content": user_question},
        ],
        tools=tools,
        tool_choice="auto",
    )

    message = response.choices[0].message

    if message.tool_calls:

        tool_call = message.tool_calls[0]

        function_name = tool_call.function.name

        arguments = json.loads(tool_call.function.arguments)

        function = getattr(fs_tools, function_name)

        result = function(**arguments)

        return result

    else:

        return message.content


# ===============================
# TERMINAL LOOP
# ===============================

if __name__ == "__main__":

    while True:

        question = input("Ask: ")

        output = ask_llm(question)

        print(json.dumps(output, indent=2))
