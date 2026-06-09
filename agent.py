from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from ai_engine import generate_study_plan


def study_planner(topic: str, days: int, level: str):
    return generate_study_plan(topic, days, level)


study_tool = FunctionTool.from_function(study_planner)


agent = Agent(
    name="student_agent",
    description="AI Study Planner Agent",
    tools=[study_tool],
)
