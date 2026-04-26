import streamlit as st
import random
from latin_data import nouns_db, adjectives_db

# --- SESSION STATE INITIALIZATION ---
if 'current_q' not in st.session_state:
    st.session_state.current_q = None
if 'feedback_msg' not in st.session_state:
    st.session_state.feedback_msg = ""
if 'feedback_type' not in st.session_state:
    st.session_state.feedback_type = ""
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'streak' not in st.session_state:
    st.session_state.streak = 0

def strip_macrons(text):
    """Removes macrons from vowels for flexible grading."""
    return text.translate(str.maketrans("āēīōūȳ", "aeiouy"))

def generate_question():
    """Selects a new random noun, adjective, case, and number."""
    noun_lemma = random.choice(list(nouns_db.keys()))
    adj_lemma = random.choice(list(adjectives_db.keys()))
    number = random.choice(["singular", "plural"])
    case = random.choice(["nominative", "genitive", "dative", "accusative", "ablative", "vocative"])
    
    # Fetch the genitive singular directly from the database for display
    noun_genitive = nouns_db[noun_lemma]["singular"]["genitive"]
    
    st.session_state.current_q = {
        "noun_lemma": noun_lemma,
        "noun_genitive": noun_genitive,
        "adj_lemma": adj_lemma,
        "number": number,
        "case": case,
        "gender": nouns_db[noun_lemma]["gender"],
        "noun_decl": nouns_db[noun_lemma]["declension"],
        "adj_decl": adjectives_db[adj_lemma]["type"]
    }

def process_answer():
    """Checks the answer, updates stats, sets feedback, and advances the question."""
    q = st.session_state.current_q
    
    # Fetch correct answers
    correct_noun = nouns_db[q["noun_lemma"]][q["number"]][q["case"]]
    target_gender = q["gender"].lower()
    correct_adj = adjectives_db[q["adj_lemma"]][target_gender][q["number"]][q["case"]]
    
    # Get user inputs (Streamlit forms store these in session state automatically)
    u_noun = st.session_state.user_noun.strip().lower()
    u_adj = st.session_state.user_adj.strip().lower()
    
    st.session_state.attempts += 1
    
    # Check correctness (ignoring macrons)
    if strip_macrons(u_noun) == strip_macrons(correct_noun) and strip_macrons(u_adj) == strip_macrons(correct_adj):
        st.session_state.score += 1
        st.session_state.streak += 1
        st.session_state.feedback_msg = f"✅ **Correct!** The exact form is **{correct_noun} {correct_adj}**."
        st.session_state.feedback_type = "success"
    else:
        st.session_state.streak = 0  # Reset streak on failure
        st.session_state.feedback_msg = f"❌ **Incorrect.** You wrote *{u_noun} {u_adj}*. The correct form was **{correct_noun} {correct_adj}**."
        st.session_state.feedback_type = "error"
        
    # Auto-advance to the next question
    generate_question()

# --- UI LAYOUT ---
st.set_page_config(page_title="Latin Noun & Adjective Practice", layout="centered")

st.title("🏛️ Latin Declension Practice")

# Generate the first question if none exists
if st.session_state.current_q is None:
    generate_question()

# --- NOTIFICATION AREA (Shows feedback from the PREVIOUS question) ---
if st.session_state.feedback_msg:
    if st.session_state.feedback_type == "success":
        st.success(st.session_state.feedback_msg)
    else:
        st.error(st.session_state.feedback_msg)

# --- SIDEBAR (Settings & Stats) ---
st.sidebar.header("⚙️ Settings")
hide_gender = st.sidebar.checkbox("Hide Noun Genders (Hard Mode)")

st.sidebar.divider()

# Calculate percentage safely to avoid division by zero
win_rate = (st.session_state.score / st.session_state.attempts * 100) if st.session_state.attempts > 0 else 0.0

st.sidebar.header("📊 Statistics")
st.sidebar.metric("Score", f"{st.session_state.score} / {st.session_state.attempts}")
st.sidebar.metric("Accuracy", f"{win_rate:.1f}%")
st.sidebar.metric("🔥 Current Streak", st.session_state.streak)

if st.sidebar.button("Reset Stats"):
    st.session_state.score = 0
    st.session_state.attempts = 0
    st.session_state.streak = 0
    st.session_state.feedback_msg = ""
    generate_question()

# --- MAIN QUESTION AREA ---
q = st.session_state.current_q

# Determine whether to show the gender based on the checkbox
display_gender = "Hidden" if hide_gender else q['gender']

st.subheader("Decline the following pair:")
# Now displaying the dictionary format: nominative, genitive
st.markdown(f"**Noun:** {q['noun_lemma']}, {q['noun_genitive']} *({q['noun_decl']} Declension, {display_gender})*")
st.markdown(f"**Adjective:** {q['adj_lemma']} *({q['adj_decl']} Declension)*")
st.markdown(f"**Target Form:** {q['case'].capitalize()} {q['number'].capitalize()}")

st.write("---")

# --- FORM BATCHES INPUTS TOGETHER ---
with st.form(key="declension_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Noun Form:", key="user_noun")
    with col2:
        st.text_input("Adjective Form:", key="user_adj")
    
    st.form_submit_button("Submit Answer", on_click=process_answer)
