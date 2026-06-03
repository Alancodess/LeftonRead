from pdf_export import create_recovery_pdf
from memory import save_checkin, load_checkins
from no_contact import no_contact_coach
from screenshot_analyzer import analyze_chat_screenshot
from healing_score import calculate_healing_score
from agents import run_recovery_team
import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="💔 Left On Read",
    page_icon="💔",
    layout="wide"
)
st.markdown("""
<style>

.main .block-container{
    max-width:1100px;
    padding-top:2rem;
}

.hero-card{
    background:#FFF5F6;
    border:1px solid #F0E4E6;
    border-radius:16px;
    padding:20px;
    margin-bottom:12px;
}

.hero-title{
    font-size:48px;
    font-weight:800;
    color:#E11D48;
    margin-bottom:8px;
}

.hero-subtitle{
    font-size:18px;
    color:#6B5B61;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="hero-card">

<div class="hero-title">
💔 LeftOnRead.com
</div>

<div style="
font-size:22px;
font-weight:600;
color:#555;
margin-top:-8px;
margin-bottom:18px;
">
Because the gym wasn't enough.
</div>

<div style="
font-size:16px;
font-weight:700;
color:#E11D48;
text-transform:uppercase;
letter-spacing:1px;
margin-bottom:10px;
">
Heartbreak Recovery Assistant
</div>

<div style="
color:#666;
font-size:15px;
line-height:1.7;
">
</div>

</div>
""", unsafe_allow_html=True)


# ==================================
# DAILY CHECK-IN
# ==================================

with st.sidebar:

    st.header("📅 Daily Check-In")

    mood = st.slider(
        "How are you feeling today?",
        1,
        10,
        5
    )

    daily_note = st.text_area(
        "Daily Reflection",
        height=100
    )

    if st.button("Save Daily Check-In"):

        save_checkin(
            mood,
            daily_note
        )

        st.success("Saved!")

    checkins = load_checkins()

    if len(checkins) > 0:

        df = pd.DataFrame(checkins)

        st.subheader("📈 Recovery Progress")

        st.line_chart(
            df.set_index("date")["mood"]
        )

st.divider()

# ==================================
# MAIN ANALYSIS
# ==================================
st.markdown("""
### Tell us what happened

The more context you provide,
the better the recovery analysis.
""")
story = st.text_area(
    "What happened?",
    height=200
)

uploaded_file = st.file_uploader(
    "📷 Upload chat screenshot (optional)",
    type=["png", "jpg", "jpeg"]
)

st.subheader("🚫 No Contact Coach")

days_no_contact = st.number_input(
    "Days of No Contact",
    min_value=0,
    value=0
)

temptation = st.text_area(
    "Why do you want to text them?",
    height=100
)

if st.button("Analyze My Situation"):

    if story.strip():

        with st.spinner("Reading the emotional damage..."):

            score_data = calculate_healing_score(
                story
            )

            results = run_recovery_team(
                story
            )

            no_contact_result = no_contact_coach(
                f"""
Days of No Contact: {days_no_contact}

Reason:
{temptation}
"""
            )

            chat_analysis = None

            if uploaded_file is not None:

                chat_analysis = analyze_chat_screenshot(
                    uploaded_file
                )

        # ==========================
        # HEALING SCORE
        # ==========================

        st.header("📊 Healing Score")

        st.progress(
            score_data["healing_score"] / 100
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Healing Score",
                f"{score_data['healing_score']}%"
            )

            st.metric(
                "Acceptance",
                score_data["acceptance"]
            )

            st.metric(
                "Self Worth",
                score_data["self_worth"]
            )

        with col2:

            st.metric(
                "Attachment",
                score_data["attachment"]
            )

            st.metric(
                "Recovery Momentum",
                score_data["momentum"]
            )

        st.divider()

        # ==========================
        # SCREENSHOT ANALYSIS
        # ==========================

        if chat_analysis:

            st.header("📷 Chat Screenshot Analysis")

            st.write(chat_analysis)

            st.divider()

        # ==========================
        # NO CONTACT COACH
        # ==========================

        st.header("🚫 No Contact Coach")

        st.write(no_contact_result)

        st.divider()

        tabs = st.tabs([
            "👑 Coach",
            "🧠 Therapist",
            "💌 Letter",
            "🔥 Reality",
            "📅 Plan",
            "🚩 Flags"
        ])

        with tabs[0]:
            st.write(results["coach"])

        with tabs[1]:
            st.write(results["therapist"])

        with tabs[2]:
            st.write(results["unsent_letter"])

        with tabs[3]:
            st.write(results["reality_check"])
        with tabs[4]:
            st.write(results["recovery_plan"])

        with tabs[5]:
            st.write(results["red_flags"])

    # ==========================
    # PDF EXPORT
    # ==========================

    pdf_file = "recovery_report.pdf"

    create_recovery_pdf(
        pdf_file,
        results["coach"],
        results["therapist"],
        results["recovery_plan"],
        results["red_flags"],
        no_contact_result
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download Recovery Report",
            data=file,
            file_name="Left_On_Read_Recovery_Report.pdf",
            mime="application/pdf"
        )

else:
    st.warning(
        "Tell us what happened first."
    )
