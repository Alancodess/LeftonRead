# LeftOnRead

### Because the gym wasn't enough.

LeftOnRead is an AI-powered breakup recovery assistant designed to help people process emotional setbacks, gain clarity, and move forward with actionable recovery guidance.

Instead of generic advice, LeftOnRead uses multiple specialized AI agents that work together to analyze a user's situation, identify emotional patterns, and generate personalized recovery recommendations.

---

## ✨ Features

### 📊 Healing Score

Measures recovery progress using:

* Attachment Level
* Acceptance
* Self-Worth
* Recovery Momentum

Generates an overall Healing Score to track emotional recovery.

---

### 🚫 No Contact Coach

Provides:

* Motivation to stay committed
* Personalized no-contact guidance
* Alternative actions during moments of weakness
* Daily recovery challenges

---

### 🧠 AI Therapist

Offers supportive reflection and emotional processing to help users better understand their situation.

---

### 💌 Unsent Letter Generator

Helps users express thoughts and emotions without sending messages they may later regret.

---

### 🔥 Reality Check

Challenges unhealthy thought patterns and emotional bias by providing objective observations about the relationship.

---

### 📅 Recovery Planner

Creates actionable next steps focused on:

* Self-improvement
* Emotional detachment
* Habit rebuilding
* Long-term recovery

---

### 🚩 Red Flag Analysis

Identifies unhealthy relationship dynamics and recurring warning signs from the user's story.

---

### 📷 Chat Screenshot Analysis

Upload chat screenshots for additional relationship context and conversation analysis.

---

### 📄 PDF Recovery Reports

Generate downloadable recovery reports containing:

* Therapist feedback
* Recovery coaching
* Recovery plans
* No-contact guidance
* Red flag analysis

---

## 🏗️ Architecture

The application uses a multi-agent architecture where specialized AI agents perform different roles:

```text
User Story
    │
    ▼
Recovery Team
    │
    ├── Therapist
    ├── Reality Check
    ├── Recovery Planner
    ├── Red Flag Detector
    ├── Unsent Letter Writer
    ▼
Recovery Coach
    │
    ▼
Final Personalized Guidance
```

---

## 🛠️ Tech Stack

| Technology    | Purpose           |
| ------------- | ----------------- |
| Python        | Core application  |
| Streamlit     | Frontend UI       |
| Groq API      | LLM inference     |
| Llama 3.3 70B | AI reasoning      |
| ReportLab     | PDF generation    |
| PIL           | Image processing  |
| JSON          | Local persistence |

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/Alancodess/LeftonRead.git
cd LeftonRead
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots of:

* Homepage
* Healing Score Dashboard
* AI Analysis Results
* No Contact Coach

---

## 🎯 Project Goals

LeftOnRead was built as an exploration of:

* Multi-agent AI systems
* LLM orchestration
* Prompt engineering
* Emotional support applications
* Rapid AI product development

---

## ⚠️ Disclaimer

LeftOnRead is intended for educational and self-reflection purposes only.

It is not a substitute for professional mental health services, therapy, medical advice, or crisis intervention.

---

## 👨‍💻 Author

**Alan Abraham Anil**

Building AI products and exploring multi-agent systems, LLM applications, and intelligent workflows.
