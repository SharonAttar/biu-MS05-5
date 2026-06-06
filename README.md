\# AI LinkedIn Content Crew



\## Project Description

This project demonstrates a multi-agent AI system using CrewAI and Ollama.

The system creates a professional LinkedIn post based on a topic entered by the user.



\## Main Goal

The goal of the system is to show how several AI agents can work together in a sequential workflow.



\## Agents



1\. AI Topic Researcher  

Collects 5–7 key points about the selected topic.



2\. LinkedIn Content Writer  

Writes a first draft of a LinkedIn post based on the research.



3\. Professional Editor  

Improves the post, makes it clearer, more polished, and better structured.



4\. LinkedIn Optimization Specialist  

Adds a stronger opening, a call to action, and relevant hashtags.



\## Workflow

The system uses a sequential process.

Each agent receives the result of the previous agent through context and continues the work.



\## Technologies

\- Python

\- CrewAI

\- Ollama

\- Qwen2.5:3b local model

\- uv



\## How to Run



```bash

uv run python main.py

