\# PRD – AI LinkedIn Content Crew



\## 1. Project Name



AI LinkedIn Content Crew



\## 2. Project Overview



This project is a multi-agent AI system built with CrewAI.

The system receives a topic from the user and creates a professional LinkedIn post through a sequential workflow of four AI agents.



The project demonstrates how AI agents can cooperate as a team, where each agent is responsible for a different stage in the content creation process.



\## 3. Problem Statement



Writing a professional LinkedIn post requires several steps:



\* Understanding the topic

\* Collecting relevant points

\* Writing a clear draft

\* Editing the text

\* Optimizing the post for LinkedIn



Doing all these steps manually can take time.

The goal of this project is to automate the process using several AI agents.



\## 4. Project Goal



The goal is to build a simple working CrewAI system that creates a LinkedIn post using four connected agents.



\## 5. Target Users



The system is intended for:



\* Students

\* Managers

\* Content creators

\* Professionals who want to create LinkedIn posts quickly

\* Organizations that want to demonstrate AI-based content workflows



\## 6. Main Features



The system includes the following features:



1\. User enters a LinkedIn post topic.

2\. Research Agent collects key points about the topic.

3\. Writer Agent writes the first draft.

4\. Editor Agent improves the text.

5\. LinkedIn Optimization Agent adds a stronger structure and hashtags.

6\. The final post is printed in the terminal.



\## 7. Agents



\### Agent 1: AI Topic Researcher



Role: Researcher

Goal: Collect 5–7 clear and useful points about the selected topic.

Output: A list of key points.



\### Agent 2: LinkedIn Content Writer



Role: Content Writer

Goal: Write a first draft of a LinkedIn post based on the research.

Output: First draft of the post.



\### Agent 3: Professional Editor



Role: Editor

Goal: Improve the post and make it clear, polished, and professional.

Output: Edited LinkedIn post.



\### Agent 4: LinkedIn Optimization Specialist



Role: Optimization Specialist

Goal: Add a strong opening, call to action, and relevant hashtags.

Output: Final LinkedIn post ready for publishing.



\## 8. Workflow



The workflow is sequential.



The output of each agent becomes the input for the next agent through CrewAI context.



Workflow:



1\. Research

2\. Writing

3\. Editing

4\. LinkedIn Optimization

5\. Final Output



\## 9. Technologies



\* Python

\* CrewAI

\* Ollama

\* Qwen2.5:3b local model

\* uv

\* PowerShell



\## 10. System Requirements



\* Windows computer

\* Python installed

\* uv installed

\* Ollama installed

\* qwen2.5:3b model downloaded locally



\## 11. How to Run



Run the project from PowerShell:



```bash

uv run python main.py

```



Then enter a topic, for example:



```text

AI agents in modern organizations

```



\## 12. Expected Output



The system should produce a complete professional LinkedIn post that includes:



\* Opening paragraph

\* Main body

\* Business value

\* Practical considerations

\* Final conclusion

\* Hashtags



\## 13. Success Criteria



The project is considered successful if:



\* The system runs from one terminal.

\* All four agents are executed.

\* Each agent completes its task.

\* The final LinkedIn post is generated.

\* The output is visible in the terminal.

\* The project can run locally without paid OpenAI API usage.



\## 14. Limitations



\* The local model may be slower than cloud models.

\* The quality of the output depends on the local model.

\* The system does not publish directly to LinkedIn.

\* The system currently supports text generation only.



\## 15. Future Improvements



Possible future improvements:



\* Add automatic saving of the final post to a file.

\* Add Hebrew language support.

\* Add a user interface.

\* Add more content formats, such as Facebook posts or blog posts.

\* Add automatic quality scoring.

\* Add support for multiple topics in one run.



