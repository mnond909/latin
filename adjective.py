import streamlit as st
import random
from latin_data import nouns_db, adjectives_db

# --- SESSION STATE INITIALIZATION ---
if 'current_q' not in st.session_state:
    st.session_state.current_q = None
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

def generate_question():
    noun_lemma = random.choice(list(nouns_db.keys()))
    adj_lemma = random.choice(list(adjectives_db.keys()))
    number = random.choice(["singular", "plural"])
    case = random.choice(["nominative", "genitive", "dative", "accusative", "ablative", "vocative"])
    
    st.session_state.current_q = {
        "noun_lemma": noun_lemma,
        "adj_lemma": adj_lemma,
        "number": number,
        "case": case,
        "gender": nouns_db[noun_lemma]["gender"]
    }
    st.session_state.feedback = ""
    # Clear input fields by updating their session state keys
    st.session_state.user_noun = ""
    st.session_state.user_adj = ""

def check_answer():
    q = st.session_state.current_q
    
    # Fetch correct answers from the imported databases
    correct_noun = nouns_db[q["noun_lemma"]][q["number"]][q["case"]]
    
    # The adjective must match the noun's gender (convert to lowercase to match the adj dict keys)
    target_gender = q["gender"].lower()
    correct_adj = adjectives_db[q["adj_lemma"]][target_gender][q["number"]][q["case"]]
    
    # Get user inputs
    u_noun = st.session_state.user_noun.strip().lower()
    u_adj = st.session_state.user_adj.strip().lower()
    
    st.session_state.attempts += 1
    
    if u_noun == correct_noun and u_adj == correct_adj:
        st.session_state.score += 1
        st.session_state.feedback = f"✅ Correct! **{correct_noun} {correct_adj}**"
        # Delay slightly or let user click next manually. We'll leave it for manual next.
    else:
        st.session_state.feedback = f"❌ Incorrect. The correct form is: **{correct_noun} {correct_adj}**\n\n(You entered: *{u_noun} {u_adj}*)"

# --- UI LAYOUT ---
st.set_page_config(page_title="Latin Noun & Adjective Practice", layout="centered")

st.title("🏛️ Latin Declension Practice")
st.markdown("Test your noun-adjective agreement across all declensions.")

# Generate the first question if none exists
if st.session_state.current_q is None:
    generate_question()

q = st.session_state.current_q

# Scoreboard
st.sidebar.metric("Score", f"{st.session_state.score} / {st.session_state.attempts}")
if st.sidebar.button("Reset Score"):
    st.session_state.score = 0
    st.session_state.attempts = 0
    generate_question()

# Display Prompt
st.subheader("Decline the following pair:")
st.markdown(f"**Noun:** {q['noun_lemma']} ({q['gender']})")
st.markdown(f"**Adjective:** {q['adj_lemma']}")
st.markdown(f"**Target Form:** {q['case'].capitalize()} {q['number'].capitalize()}")

st.write("---")

# Input Fields
col1, col2 = st.columns(2)
with col1:
    st.text_input("Noun Form:", key="user_noun")
with col2:
    st.text_input("Adjective Form:", key="user_adj")

# Buttons
btn_col1, btn_col2 = st.columns([1, 4])
with btn_col1:
    st.button("Submit", on_click=check_answer, type="primary")
with btn_col2:
    st.button("Next Question", on_click=generate_question)

# Display Feedback
if st.session_state.feedback:
    if "✅" in st.session_state.feedback:
        st.success(st.session_state.feedback)
    else:
        st.error(st.session_state.feedback)
