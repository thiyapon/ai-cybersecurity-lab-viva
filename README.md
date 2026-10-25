# CAPSTONE 28 — AI Cybersecurity Lab Manual and Viva Preparation System

A beginner-friendly Streamlit prototype for turning cybersecurity lab topics into structured revision and viva practice. Includes 5 topics, 50 draft questions, flashcards, question bank, prompt library, study guide and verification/testing templates.

## Important academic note
The included question bank is a **draft**, not a claim that every answer has already been verified against your college syllabus. Replace or adjust topics to match your actual lab manual. Check each answer against course material and current official references, then update its verification status. Do not invent student testing results.

## Features
- Dashboard with topic and question counts
- Viva practice with answer reveal and self-assessment
- Flashcards
- Searchable-by-topic question bank
- Prompt library
- CSV-based content so questions can be edited without changing Python code

## Run locally (Windows)
1. Install Python 3.10 or newer from https://www.python.org/downloads/
2. Download or clone this repository.
3. Open Command Prompt or terminal in the project folder.
4. Create a virtual environment:
   `python -m venv .venv`
5. Activate it:
   `.venv\Scripts\activate`
6. Install dependencies:
   `pip install -r requirements.txt`
7. Start the app:
   `streamlit run app.py`
8. Open the local URL shown in the terminal, usually http://localhost:8501

## Upload to GitHub
1. Create a new repository at https://github.com/new
2. Use a clear name such as `ai-cybersecurity-lab-viva`.
3. Do not upload passwords, API keys, private logs or personal data.
4. Either use GitHub's **Add file → Upload files** to upload the extracted project files, or use Git:
   `git init`
   `git add .`
   `git commit -m "Add CyberLab Viva capstone prototype"`
   `git branch -M main`
   `git remote add origin https://github.com/YOUR-USERNAME/ai-cybersecurity-lab-viva.git`
   `git push -u origin main`
   Replace `YOUR-USERNAME` with your GitHub username and use the repository URL GitHub gives you.

## Optional: deploy with Streamlit Community Cloud
1. Push the project to GitHub.
2. Visit https://share.streamlit.io/ and sign in.
3. Choose the repository, branch `main`, and main file `app.py`.
4. Deploy. Check the current platform requirements and privacy implications before using it for any non-public data.

## AI workflow
Use ChatGPT/Gemini/NotebookLM to summarize the syllabus and draft questions. Use official documentation for verification. The prototype itself uses a curated CSV question bank and does not call a live AI API. This makes the demo work without an API key and avoids unexpected API costs. Describe it accurately in the presentation.

## Suggested four AI tools
- ChatGPT — draft summaries, question bank and feedback prompts
- Gemini — independent review / alternative explanations
- NotebookLM — syllabus-grounded study with uploaded source material
- Canva or Gamma — slide design
Other tools in the workflow include Python, Streamlit and Google Sheets.

## Project structure
- `app.py` — Streamlit app
- `data/viva_questions.csv` — editable question bank
- `docs/study_guide.md` — five topic summaries and 50 questions
- `docs/prompt_library.md` — reusable prompts
- `docs/verification_report_template.md` — evidence tracking
- `docs/testing_plan.md` — 10-session pilot plan
- `presentation/CAPSTONE28_Presentation.pptx` — project presentation

## Testing
Run `streamlit run app.py`, check each navigation page, test topic switching, reveal answers, self-score questions and flip cards. Record actual bugs and actual student-session results in your report.
