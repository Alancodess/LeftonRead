from agents import run_agent

HEALING_SCORE_PROMPT = """
Analyze the breakup situation.

Return ONLY:

Attachment: X
Acceptance: X
SelfWorth: X
RecoveryMomentum: X

Scores must be 1-10.
"""


def calculate_healing_score(user_input):

    response = run_agent(
        HEALING_SCORE_PROMPT,
        user_input
    )

    try:
        lines = response.strip().split("\n")

        attachment = int(lines[0].split(":")[1].strip())
        acceptance = int(lines[1].split(":")[1].strip())
        self_worth = int(lines[2].split(":")[1].strip())
        momentum = int(lines[3].split(":")[1].strip())

        score = (
            (10 - attachment)
            + acceptance
            + self_worth
            + momentum
        ) / 40 * 100

        return {
            "attachment": attachment,
            "acceptance": acceptance,
            "self_worth": self_worth,
            "momentum": momentum,
            "healing_score": round(score)
        }

    except:
        return {
            "attachment": 5,
            "acceptance": 5,
            "self_worth": 5,
            "momentum": 5,
            "healing_score": 50
        }
