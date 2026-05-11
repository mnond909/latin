import streamlit as st
import random
from verb_db import verb_conjugations, verbs_db, verb_english_forms

# --- HELPER FUNCTIONS ---
def remove_macrons(text):
    replacements = {'ā': 'a', 'ē': 'e', 'ī': 'i', 'ō': 'o', 'ū': 'u', 'Ā': 'A', 'Ē': 'E', 'Ī': 'I', 'Ō': 'O', 'Ū': 'U'}
    for macron, plain in replacements.items():
        text = text.replace(macron, plain)
    return text.lower().strip()

def get_english_translation(verb_name, mood, tense, voice=None, person=None, number=None):
    """Generates the English meaning based on grammatical tags."""
    forms = verb_english_forms.get(verb_name, {"base": "do", "s": "does", "ing": "doing", "past": "did", "pp": "done"})

    pronouns = {
        (1, "singular"): "I",
        (2, "singular"): "You",
        (3, "singular"): "He/She/It",
        (1, "plural"): "We",
        (2, "plural"): "Y'all",
        (3, "plural"): "They"
    }

    if mood == "indicative":
        subject = pronouns.get((person, number), "")

        if voice == "active":
            if tense == "present":
                verb_str = forms["s"] if person == 3 and number == "singular" else forms["base"]
                return f"{subject} {verb_str}"
            elif tense == "imperfect":
                aux = "was" if number == "singular" and person in [1, 3] else "were"
                return f"{subject} {aux} {forms['ing']}"
            elif tense == "future":
                return f"{subject} will {forms['base']}"
            elif tense == "perfect":
                return f"{subject} {forms['past']} (or have {forms['pp']})"
            elif tense == "pluperfect":
                return f"{subject} had {forms['pp']}"
            elif tense == "future perfect":
                return f"{subject} will have {forms['pp']}"

        elif voice == "passive":
            if tense == "present":
                aux = "am" if person == 1 and number == "singular" else "is" if person == 3 and number == "singular" else "are"
                return f"{subject} {aux} {forms['pp']}"
            elif tense == "imperfect":
                aux = "was" if number == "singular" and person in [1, 3] else "were"
                return f"{subject} {aux} being {forms['pp']}"
            elif tense == "future":
                return f"{subject} will be {forms['pp']}"
            elif tense == "perfect":
                aux = "was" if number == "singular" and person in [1, 3] else "were"
                return f"{subject} {aux} {forms['pp']} (or have been {forms['pp']})"
            elif tense == "pluperfect":
                return f"{subject} had been {forms['pp']}"
            elif tense == "future perfect":
                return f"{subject} will have been {forms['pp']}"

    elif mood == "imperative":
        if tense == "present":
            if voice == "active":
                pl = " (pl.)" if number == "plural" else ""
                return f"{forms['base'].capitalize()}!{pl}"
            elif voice == "passive":
                pl = " (pl.)" if number == "plural" else ""
                return f"Be {forms['pp']}!{pl}"
        elif tense == "future":
            subject = "You" if person == 2 else "He/They"
            if voice == "active":
                return f"{subject} shall {forms['base']}!"
            elif voice == "passive":
                return f"{subject} shall be {forms['pp']}!"

    elif mood == "infinitives":
        if tense == "present active":
            return f"to {forms['base']}"
        elif tense == "present passive":
            return f"to be {forms['pp']}"
        elif tense == "perfect active":
            return f"to have {forms['pp']}"
        elif tense == "perfect passive":
            return f"to have been {forms['pp']}"
        elif tense == "future active":
            return f"to be about to {forms['base']}"
        elif tense == "future passive":
            return f"to be about to be {forms['pp']}"

    return "Translation not available"


# --- STREAMLIT UI ---
st.set_page_config(page_title="Latin Verb Master", page_icon="🏛️")
st.title("🏛️ Latin Verb Master")

# --- SCORE TRACKER INITIALIZATION ---
if "score" not in st.session_state:
    st.session_state.score = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "max_streak" not in st.session_state:
    st.session_state.max_streak = 0

# --- ACCURACY CALCULATION ---
if st.session_state.attempts > 0:
    accuracy = (st.session_state.score / st.session_state.attempts) * 100
else:
    accuracy = 0.0

# --- SCORE DISPLAY ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Correct ✅", st.session_state.score)
col2.metric("Attempts 📝", st.session_state.attempts)
col3.metric("Accuracy 🎯", f"{accuracy:.1f}%")
col4.metric("Streak 🔥", f"{st.session_state.streak} (Max: {st.session_state.max_streak})")
st.divider()

with st.sidebar:
    st.header("Quiz Settings")
    
    # Conjugation selection logic
    conj_choice = st.selectbox("Select Conjugation:", ["All", "1st", "2nd", "3rd", "3rd i-stem", "4th"])
    if conj_choice == "All":
        available_verbs = list(verbs_db.keys())
    else:
        available_verbs = [v for v, c in verb_conjugations.items() if c == conj_choice]
        
    verb_choice = st.selectbox("Select Verb:", ["All"] + available_verbs)
    
    include_passive = st.checkbox("Include Passive Voice?", value=True)
    include_inf = st.checkbox("Include Infinitives?", value=True)
    include_imp = st.checkbox("Include Imperatives?", value=True)

    if st.button("Skip / New Question"):
        if "current_q" in st.session_state:
            del st.session_state.current_q
        if "last_result" in st.session_state:
            del st.session_state.last_result
        st.session_state.streak = 0
        st.rerun()

    st.divider()

    if st.button("Reset Score"):
        st.session_state.score = 0
        st.session_state.attempts = 0
        st.session_state.streak = 0
        st.session_state.max_streak = 0
        if "last_result" in st.session_state:
            del st.session_state.last_result
        st.rerun()

# --- PREVIOUS RESULT DISPLAY ---
if "last_result" in st.session_state:
    res = st.session_state.last_result
    if res["correct"]:
        st.success(f"**Optimē!** Previous: {res['prompt']} → **{res['answer']}**\n\n*(Meaning: {res['translation']})*")
    else:
        st.error(f"**Errāstī.** Previous: {res['prompt']} → **{res['answer']}**\n\n*(Meaning: {res['translation']})*")

# --- SELECTION LOGIC ---
if "current_q" not in st.session_state:
    questions = []
    verbs_to_pull = available_verbs if verb_choice == "All" else [verb_choice]

    for verb_name in verbs_to_pull:
        verb_data = verbs_db[verb_name]

        # Process Indicatives
        if "indicative" in verb_data:
            for tense, voices in verb_data["indicative"].items():
                for voice, numbers in voices.items():
                    if voice == "passive" and not include_passive:
                        continue
                    for number, persons in numbers.items():
                        for person, form in persons.items():
                            translation = get_english_translation(verb_name, "indicative", tense, voice, person, number)
                            questions.append({
                                "prompt": f"{verb_name.upper()} — {voice.upper()} {tense.upper()} INDICATIVE — {person} {number}",
                                "answer": form,
                                "translation": translation
                            })

        # Process Imperatives
        if include_imp and "imperative" in verb_data:
            for tense, voices in verb_data["imperative"].items():
                for voice, numbers in voices.items():
                    if voice == "passive" and not include_passive:
                        continue
                    for number, persons in numbers.items():
                        for person, form in persons.items():
                            translation = get_english_translation(verb_name, "imperative", tense, voice, person, number)
                            questions.append({
                                "prompt": f"{verb_name.upper()} — {voice.upper()} {tense.upper()} IMPERATIVE — {person} {number}",
                                "answer": form,
                                "translation": translation
                            })

        # Process Infinitives
        if include_inf and "infinitives" in verb_data:
            for inf_type, form in verb_data["infinitives"].items():
                if "passive" in inf_type and not include_passive:
                    continue
                translation = get_english_translation(verb_name, "infinitives", inf_type)
                questions.append({
                    "prompt": f"{verb_name.upper()} — {inf_type.upper()} INFINITIVE",
                    "answer": form,
                    "translation": translation
                })

    if questions:
        st.session_state.current_q = random.choice(questions)

# --- DISPLAY & FORM ---
if "current_q" in st.session_state:
    q = st.session_state.current_q
    st.info(f"How do you say: **{q['prompt']}**?")

    with st.form(key='quiz_form', clear_on_submit=True):
        user_input = st.text_input("Your Answer:")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        is_correct = remove_macrons(user_input) == remove_macrons(q['answer'])

        # --- UPDATE SCORES & STREAKS ---
        st.session_state.attempts += 1
        
        if is_correct:
            st.session_state.score += 1
            st.session_state.streak += 1
            if st.session_state.streak > st.session_state.max_streak:
                st.session_state.max_streak = st.session_state.streak
        else:
            st.session_state.streak = 0

        st.session_state.last_result = {
            "prompt": q['prompt'],
            "answer": q['answer'],
            "translation": q['translation'],
            "correct": is_correct
        }

        del st.session_state.current_q
        st.rerun()
