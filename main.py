from crewai import Agent, Task, Crew, Process, LLM


# =========================
# Local LLM with Ollama
# =========================

local_llm = LLM(
    model="ollama/qwen2.5:3b",
    base_url="http://localhost:11434"
)


# =========================
# Organization Style
# =========================

ORGANIZATION_STYLE = """
You are part of a professional AI content team.
The writing style should be clear, practical, professional, and suitable for LinkedIn.
Avoid exaggerated marketing language.
Use simple language and provide value to the reader.
"""


# =========================
# Agents
# =========================

research_agent = Agent(
    role="AI Topic Researcher",
    goal="Collect clear and useful points about the requested LinkedIn post topic.",
    backstory=(
        "You are a professional research assistant who explains technology topics "
        "in a simple and business-oriented way. "
        + ORGANIZATION_STYLE
    ),
    llm=local_llm,
    verbose=True
)

writer_agent = Agent(
    role="LinkedIn Content Writer",
    goal="Write a first draft of a professional LinkedIn post based on the research.",
    backstory=(
        "You are an experienced LinkedIn content writer who writes posts for "
        "technology managers and business professionals. "
        + ORGANIZATION_STYLE
    ),
    llm=local_llm,
    verbose=True
)

editor_agent = Agent(
    role="Professional Editor",
    goal="Improve the LinkedIn post so it is clear, focused, and polished.",
    backstory=(
        "You are a senior editor. Your job is to improve structure, wording, "
        "clarity, and flow without changing the original meaning. "
        + ORGANIZATION_STYLE
    ),
    llm=local_llm,
    verbose=True
)

hashtag_agent = Agent(
    role="LinkedIn Optimization Specialist",
    goal="Add a strong opening line, call to action, and relevant hashtags.",
    backstory=(
        "You are a LinkedIn optimization specialist. You know how to make posts "
        "more engaging while keeping them professional and not exaggerated. "
        + ORGANIZATION_STYLE
    ),
    llm=local_llm,
    verbose=True
)


# =========================
# User Input
# =========================

topic = input("Enter the LinkedIn post topic: ")


# =========================
# Tasks
# =========================

research_task = Task(
    description=(
        f"Research the following topic for a LinkedIn post: {topic}. "
        "Create 5-7 key points that explain the topic clearly. "
        "Focus on business value, practical use, and possible challenges."
    ),
    expected_output="A clear bullet list of 5-7 key points about the topic.",
    agent=research_agent
)

writing_task = Task(
    description=(
        "Using the research points from the previous task, write a first draft "
        "of a LinkedIn post. The post should be professional, easy to read, "
        "and suitable for managers."
    ),
    expected_output="A complete first draft of a LinkedIn post.",
    agent=writer_agent,
    context=[research_task]
)

editing_task = Task(
    description=(
        "Edit and improve the LinkedIn post. Make it clearer, more polished, "
        "and better structured. Keep the tone professional and practical."
    ),
    expected_output="An improved and polished LinkedIn post.",
    agent=editor_agent,
    context=[writing_task]
)

hashtag_task = Task(
    description=(
        "Add a strong opening sentence, a short call to action, and 5-8 relevant hashtags. "
        "Return the final post ready for publishing on LinkedIn."
    ),
    expected_output="Final LinkedIn post including opening, body, call to action, and hashtags.",
    agent=hashtag_agent,
    context=[editing_task]
)


# =========================
# Crew
# =========================

crew = Crew(
    agents=[
        research_agent,
        writer_agent,
        editor_agent,
        hashtag_agent
    ],
    tasks=[
        research_task,
        writing_task,
        editing_task,
        hashtag_task
    ],
    process=Process.sequential,
    verbose=True
)


# =========================
# Kickoff
# =========================

result = crew.kickoff()

print("\n\n================ FINAL LINKEDIN POST ================\n")
print(result)