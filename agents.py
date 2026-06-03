from prompts import (
    THERAPIST_PROMPT,
    UNSENT_LETTER_PROMPT,
    REALITY_CHECK_PROMPT,
    RECOVERY_PLANNER_PROMPT,
    NO_CONTACT_PROMPT,
    RED_FLAG_PROMPT,
    TEAM_LEADER_PROMPT
)
import os
from dotenv import load_dotenv
from groq import Groq
print("USING GROQ")


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"


def run_agent(system_prompt, user_input):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return response.choices[0].message.content


def run_recovery_team(user_input):

    therapist = run_agent(
        THERAPIST_PROMPT,
        user_input
    )

    unsent_letter = run_agent(
        UNSENT_LETTER_PROMPT,
        user_input
    )

    reality_check = run_agent(
        REALITY_CHECK_PROMPT,
        user_input
    )

    recovery_plan = run_agent(
        RECOVERY_PLANNER_PROMPT,
        user_input
    )

    red_flags = run_agent(
        RED_FLAG_PROMPT,
        user_input
    )

    combined_results = f"""
THERAPIST:
{therapist}

UNSENT LETTER:
{unsent_letter}

REALITY CHECK:
{reality_check}

RECOVERY PLAN:
{recovery_plan}

RED FLAGS:
{red_flags}
"""

    coach = run_agent(
        TEAM_LEADER_PROMPT,
        combined_results
    )

    return {
        "therapist": therapist,
        "unsent_letter": unsent_letter,
        "reality_check": reality_check,
        "recovery_plan": recovery_plan,
        "red_flags": red_flags,
        "coach": coach
    }
