# Oligopoly Study Tool – NotebookLM Style

An interactive study tool inspired by NotebookLM, built for the Markaroo AI + Full Stack Intern assignment.  
The app helps students revise **oligopoly** (kinked demand curve and game theory) using a teacher–student chat and video-based summaries. [web:29][web:41]

---

## Live Demo

Streamlit App: https://econ-study-tool.streamlit.app/


## Demo Video

- Short demo recording (Google Drive): https://drive.google.com/file/d/1_o2uV85faGN33AWlpKAawCPiLPYrOxqD/view?usp=sharing

> If the teacher–student chat shows a **quota error**, plug in your own OpenAI API key with credits and it will work normally. My free-tier quota is currently exhausted. [web:26][web:28]

---

## Features

- **Teacher–Student Dialogue Mode**
  - Simulated two-person conversation where the student asks doubts about oligopoly.
  - The “teacher” answers using structured context: definition of oligopoly, kinked demand curve, price rigidity, game theory, and Nash equilibrium.

- **Video Summaries Mode**
  - Embeds the two provided YouTube videos:
    - Oligopoly – Kinked Demand Curve.
    - Oligopoly – Game Theory.
  - Shows short written summaries and exam tips next to each video.

- **NotebookLM-style UX**
  - Sidebar to select mode and enter API key.
  - Central chat area using `st.chat_message` and `st.chat_input` for conversational flow. [web:29][web:49]

---

## Tech Stack

- **Frontend / App:** Streamlit
- **Language:** Python 3.14
- **LLM Provider:** OpenAI Chat Completions API (`gpt-4o-mini`)
- **Runtime:** Local (Streamlit) and optionally Streamlit Community Cloud

---

## Local Setup

1. **Clone the repository**
```
git clone https://github.com/YOUR_GITHUB_USERNAME/econ-study-tool.git
cd econ-study-tool
```
2. **Create virtual environment (optional but recommended)**

```
python -m venv .venv
```

Windows (Command Prompt):

```
.venv\\Scripts\\activate.bat
```

Windows (PowerShell):

```
.\\.venv\\Scripts\\Activate.ps1
```

macOS / Linux:

```
source .venv/bin/activate
```


3. **Install dependencies**

```
pip install -r requirements.txt
```

Or install the main dependencies directly:

```
pip install streamlit openai
```

4. **Run the app**

```
streamlit run app.py
```

The app will open in your browser at [http://localhost:8501](http://localhost:8501). [web:41]

5. **Provide your OpenAI API key**
- Get a key from: https://platform.openai.com/api-keys. [web:26]
- Paste it into the **“Enter OpenAI API Key”** field in the sidebar.

---

## Usage Guide

### 1. Teacher–Student Dialogue Mode

1. In the sidebar, select **“Teacher-Student Chat”**.
2. Ask questions like:
- “Explain the kinked demand curve.”
- “Why is price rigid in an oligopoly?”
- “What is Nash equilibrium in the petrol station example?”
3. The assistant replies as a teacher and keeps the conversation in simple exam language.

### 2. Video Summaries Mode

1. In the sidebar, select **“Video Summaries”**.
2. Watch:
- **Video 1:** Kinked demand curve.
- **Video 2:** Game theory / prisoners’ dilemma in oligopoly.
3. Read the bullet-point explanation and **exam tips** next to each video.

---

## API Quota Note

The app is fully integrated with the OpenAI Chat Completions API.  
If you see an error like **`insufficient_quota`**:

- It means the current API key has no remaining credits or free-tier quota. [web:26][web:28]
- Replace it with an API key that has an active billing plan and available balance.
- The UI and interaction flow will work the same; only the LLM response is blocked when quota is exceeded.

---

## Assignment Notes

This project is built specifically for:

- **Company:** Markaroo  
- **Role:** AI and Full Stack Intern  
- **Task:** NotebookLM-inspired interactive study tool using:
- Given economics book chapter (oligopoly).
- Two YouTube videos (kinked demand curve and game theory).

The code is structured so it can be extended into a full RAG system (PDF + video transcripts) in future iterations. [web:46][web:53]

