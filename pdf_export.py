from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_recovery_pdf(
    filename,
    coach,
    therapist,
    recovery_plan,
    red_flags,
    no_contact
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "💔 Left On Read Recovery Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    sections = [
        ("Recovery Coach", coach),
        ("Therapist", therapist),
        ("Recovery Plan", recovery_plan),
        ("Red Flags", red_flags),
        ("No Contact Coach", no_contact)
    ]

    for title, text in sections:

        content.append(
            Paragraph(
                f"<b>{title}</b>",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                str(text),
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

    doc.build(content)
