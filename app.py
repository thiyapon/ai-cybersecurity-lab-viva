import csv
import random
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).parent
CSV_PATH = ROOT / "data" / "viva_questions.csv"

st.set_page_config(page_title="CyberLab Viva", page_icon="🛡️", layout="wide")

@st.cache_data
def load_questions():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

questions = load_questions()
topics = sorted({q["topic"] for q in questions})

st.title("🛡️ CyberLab Viva")
st.caption("AI-assisted cybersecurity lab study prototype • verify content against your syllabus")

with st.sidebar:
    st.header("Navigation")
    page = st.radio("Choose a mode", ["Dashboard", "Viva Practice", "Flashcards", "Question Bank", "Prompt Library"])
    st.divider()
    st.warning("The included answer bank is a draft. Review it against your syllabus and current official references before academic submission.")

if page == "Dashboard":
    st.subheader("Your lab preparation workspace")
    a, b, c = st.columns(3)
    a.metric("Lab topics", len(topics))
    b.metric("Viva questions", len(questions))
    c.metric("Modes", 4)
    st.markdown("### Included topics")
    for topic in topics:
        st.markdown(f"- **{topic}** — 10 draft viva questions")
    st.info("Workflow: upload syllabus to an AI tool → generate notes/questions → verify sources → update the CSV → practice here.")
    st.markdown("### Responsible AI")
    st.write("AI can hallucinate or omit syllabus-specific details. Do not upload real passwords, confidential logs or personal data. Keep a record of sources and corrections.")

elif page == "Viva Practice":
    st.subheader("Viva practice")
    topic = st.selectbox("Choose a topic", topics)
    bank = [q for q in questions if q["topic"] == topic]
    order = st.selectbox("Question order", ["Sequential", "Random"])
    if "viva_order" not in st.session_state or st.session_state.get("viva_topic") != topic or st.session_state.get("viva_order_type") != order:
        st.session_state.viva_order = bank.copy()
        if order == "Random":
            random.shuffle(st.session_state.viva_order)
        st.session_state.viva_index = 0
        st.session_state.viva_score = 0
        st.session_state.viva_attempts = 0
        st.session_state.viva_topic = topic
        st.session_state.viva_order_type = order
        st.session_state.viva_revealed = False
    if st.session_state.viva_index < len(st.session_state.viva_order):
        item = st.session_state.viva_order[st.session_state.viva_index]
        st.progress(st.session_state.viva_index / len(st.session_state.viva_order))
        st.caption(f"Question {st.session_state.viva_index + 1} of {len(st.session_state.viva_order)}")
        st.markdown(f"### {item['question']}")
        st.text_area("Your answer (for your own practice)", key=f"answer_{topic}_{st.session_state.viva_index}")
        if st.button("Reveal model answer"):
            st.session_state.viva_revealed = True
        if st.session_state.viva_revealed:
            st.success(item["model_answer"])
            st.caption(f"Reference to check: {item['reference']}")
            score = st.radio("Self-assessment", ["Not yet (0)", "Partly (1)", "Mostly (2)"], horizontal=True, key=f"score_{topic}_{st.session_state.viva_index}")
            if st.button("Save score and next question"):
                st.session_state.viva_score += int(score[0])
                st.session_state.viva_attempts += 1
                st.session_state.viva_index += 1
                st.session_state.viva_revealed = False
                st.rerun()
    else:
        st.success("Practice set completed!")
        st.metric("Self-assessment score", f"{st.session_state.viva_score}/{st.session_state.viva_attempts * 2}")
        st.write("Revise any questions you marked Not yet or Partly.")
        if st.button("Restart this topic"):
            for key in ["viva_order", "viva_index", "viva_score", "viva_attempts", "viva_topic", "viva_order_type", "viva_revealed"]:
                st.session_state.pop(key, None)
            st.rerun()

elif page == "Flashcards":
    st.subheader("Flashcards")
    topic = st.selectbox("Choose a topic", topics, key="flash_topic")
    cards = [q for q in questions if q["topic"] == topic]
    if "flash_index" not in st.session_state or st.session_state.get("flash_topic_saved") != topic:
        st.session_state.flash_index = 0
        st.session_state.flash_revealed = False
        st.session_state.flash_topic_saved = topic
    item = cards[st.session_state.flash_index % len(cards)]
    st.caption(f"Card {st.session_state.flash_index % len(cards) + 1} of {len(cards)}")
    st.markdown(f"### {item['question']}")
    if st.button("Flip card"):
        st.session_state.flash_revealed = not st.session_state.flash_revealed
    if st.session_state.flash_revealed:
        st.info(item["model_answer"])
    col1, col2 = st.columns(2)
    if col1.button("← Previous"):
        st.session_state.flash_index = (st.session_state.flash_index - 1) % len(cards)
        st.session_state.flash_revealed = False
        st.rerun()
    if col2.button("Next →"):
        st.session_state.flash_index = (st.session_state.flash_index + 1) % len(cards)
        st.session_state.flash_revealed = False
        st.rerun()

elif page == "Question Bank":
    st.subheader("Question bank")
    topic = st.selectbox("Filter topic", ["All topics"] + topics, key="bank_topic")
    filtered = questions if topic == "All topics" else [q for q in questions if q["topic"] == topic]
    for item in filtered:
        with st.expander(f"{item['topic']} — {item['question_id']}: {item['question']}"):
            st.write("**Draft model answer:**", item["model_answer"])
            st.write("**Reference to check:**", item["reference"])
            st.warning(item["status"])

elif page == "Prompt Library":
    st.subheader("Reusable AI prompts")
    prompt_file = ROOT / "docs" / "prompt_library.md"
    st.markdown(prompt_file.read_text(encoding="utf-8"))
