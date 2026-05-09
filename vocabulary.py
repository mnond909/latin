import streamlit as st
import random

# IMPORT THE DATABASE FROM THE OTHER FILE
try:
    from vocab_db import vocab_db
except ImportError:
    st.error("Error: Could not find 'vocab_db.py'. Make sure it is in the same directory as this file.")
    st.stop()

# --- SMART CHECKER FUNCTION ---
def check_meaning(user_input, correct_meanings_str):
    """
    Checks the user's input against a comma-separated list of accepted meanings.
    Ignores case, leading/trailing whitespace, and ignores "to " for verbs.
    """
    user_val = user_input.lower().strip()
    if user_val.startswith("to "):
        user_val = user_val[3:]

    # Split accepted meanings by comma and clean them up
    accepted_options = [m.strip().lower() for m in correct_meanings_str.split(',')]
    
    for option in accepted_options:
        if option.startswith("to "):
            option = option[3:]
        # Exact match of one of the valid meanings
        if user_val == option:
            return True
        # Also allow if the user typed the exact full string
        if user_val == correct_meanings_str.lower().strip():
            return True
            
    return False

# --- STREAMLIT UI ---
st.set_page_config(page_title="Latin Vocab Master", page_icon="🏛️")
st.title("🏛️ Latin Core Vocabulary Master")

# --- SCORE TRACKER INITIALIZATION ---
if "vocab_score" not in st.session_state:
    st.session_state.vocab_score = 0
if "vocab_attempts" not in st.session_state:
    st.session_state.vocab_attempts = 0
if "vocab_streak" not in st.session_state:
    st.session_state.vocab_streak = 0
if "vocab_max_streak" not in st.session_state:
    st.session_state.vocab_max_streak = 0
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False

# --- ACCURACY CALCULATION ---
if st.session_state.vocab_attempts > 0:
    accuracy = (st.session_state.vocab_score / st.session_state.vocab_attempts) * 100
else:
    accuracy = 0.0

# --- TOTAL WORD COUNT ---
total_words = sum(len(words) for words in vocab_db.values())

# --- SCORE DISPLAY ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Correct ✅", st.session_state.vocab_score)
col2.metric("Attempts 📝", st.session_state.vocab_attempts)
col3.metric("Accuracy 🎯", f"{accuracy:.1f}%")
col4.metric("Streak 🔥", f"{st.session_state.vocab_streak} (Max: {st.session_state.vocab_max_streak})")
st.divider()

with st.sidebar:
    st.header("Study Settings")
    st.caption(f"Database contains {total_words} words.")
    
    package_choice = st.selectbox(
        "Select Vocabulary Package:", 
        ["All Packages"] + list(vocab_db.keys())
    )

    if st.button("Skip / Next Word"):
        if "vocab_current_q" in st.session_state:
            del st.session_state.vocab_current_q
        if "vocab_last_result" in st.session_state:
            del st.session_state.vocab_last_result
        st.session_state.vocab_streak = 0
        st.session_state.show_hint = False
        st.rerun()

    st.divider()

    if st.button("Reset Score"):
        st.session_state.vocab_score = 0
        st.session_state.vocab_attempts = 0
        st.session_state.vocab_streak = 0
        st.session_state.vocab_max_streak = 0
        if "vocab_last_result" in st.session_state:
            del st.session_state.vocab_last_result
        st.session_state.show_hint = False
        st.rerun()

# --- PREVIOUS RESULT DISPLAY ---
if "vocab_last_result" in st.session_state:
    res = st.session_state.vocab_last_result
    if res["correct"]:
        st.success(f"**Optimē!** {res['lemma']} → **{res['meaning']}**")
    else:
        st.error(f"**Errāstī.** {res['lemma']} → **{res['meaning']}** (You answered: '{res['user_input']}')")

# --- SELECTION LOGIC ---
if "vocab_current_q" not in st.session_state:
    word_pool = []
    
    if package_choice == "All Packages":
        for pkg_words in vocab_db.values():
            word_pool.extend(pkg_words)
    else:
        word_pool.extend(vocab_db[package_choice])

    if word_pool:
        st.session_state.vocab_current_q = random.choice(word_pool)

# --- DISPLAY & FORM ---
if "vocab_current_q" in st.session_state:
    q = st.session_state.vocab_current_q
    
    st.info(f"### What is the meaning of: **{q['lemma']}**?")
    
    if st.session_state.show_hint:
        st.warning(f"**Hint / Accepted Meanings:** {q['meaning']}")

    with st.form(key='vocab_form', clear_on_submit=True):
        user_input = st.text_input("Your Answer (English):")
        
        c1, c2 = st.columns([1, 4])
        with c1:
            submit_button = st.form_submit_button(label='Submit')
        with c2:
            hint_button = st.form_submit_button(label='Show Meaning')

    if hint_button:
        st.session_state.show_hint = True
        st.session_state.vocab_streak = 0
        st.rerun()

    if submit_button:
        if user_input.strip() == "":
            st.warning("Please enter a translation.")
        else:
            is_correct = check_meaning(user_input, q['meaning'])

            st.session_state.vocab_attempts += 1
            
            if is_correct:
                st.session_state.vocab_score += 1
                st.session_state.vocab_streak += 1
                if st.session_state.vocab_streak > st.session_state.vocab_max_streak:
                    st.session_state.vocab_max_streak = st.session_state.vocab_streak
            else:
                st.session_state.vocab_streak = 0

            st.session_state.vocab_last_result = {
                "lemma": q['lemma'],
                "meaning": q['meaning'],
                "user_input": user_input,
                "correct": is_correct
            }

            del st.session_state.vocab_current_q
            st.session_state.show_hint = False
            st.rerun()
