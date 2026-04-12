import streamlit as st
import random
from PIL import Image

# Use a default emoji if the local image is missing
st.set_page_config(page_title="Latin Pronoun Master", page_icon="🏛️")

# --- DATA ---
# Includes a robust list of pronouns categorized by type and gender.
# Multiple correct forms are provided as lists.
pronouns_db = {
    # --- PERSONAL PRONOUNS ---
    "ego (I / We)": {
        "type": "Personal", "gender": "N/A",
        "singular": {"nominative": "ego", "genitive": "meī", "dative": "mihi", "accusative": "mē", "ablative": "mē"},
        "plural": {"nominative": "nōs", "genitive": ["nostrum", "nostrī"], "dative": "nōbīs", "accusative": "nōs", "ablative": "nōbīs"}
    },
    "tū (You / You all)": {
        "type": "Personal", "gender": "N/A",
        "singular": {"nominative": "tū", "genitive": "tuī", "dative": "tibi", "accusative": "tē", "ablative": "tē"},
        "plural": {"nominative": "vōs", "genitive": ["vestrum", "vestrī"], "dative": "vōbīs", "accusative": "vōs", "ablative": "vōbīs"}
    },
    
    # --- REFLEXIVE PRONOUNS ---
    "suī (Himself/Herself/Itself/Themselves)": {
        "type": "Reflexive", "gender": "N/A",
        # Reflexive pronouns lack a nominative case and share forms across singular and plural.
        "singular": {"nominative": None, "genitive": "suī", "dative": "sibi", "accusative": "sē", "ablative": "sē"},
        "plural": {"nominative": None, "genitive": "suī", "dative": "sibi", "accusative": "sē", "ablative": "sē"}
    },

    # --- DEMONSTRATIVE PRONOUNS (is, ea, id) ---
    "is (He/This/That)": {
        "type": "Demonstrative", "gender": "Masculine",
        "singular": {"nominative": "is", "genitive": "eius", "dative": "eī", "accusative": "eum", "ablative": "eō"},
        "plural": {"nominative": ["eī", "iī"], "genitive": "eōrum", "dative": ["eīs", "iīs"], "accusative": "eōs", "ablative": ["eīs", "iīs"]}
    },
    "ea (She/This/That)": {
        "type": "Demonstrative", "gender": "Feminine",
        "singular": {"nominative": "ea", "genitive": "eius", "dative": "eī", "accusative": "eam", "ablative": "eā"},
        "plural": {"nominative": "eae", "genitive": "eārum", "dative": ["eīs", "iīs"], "accusative": "eās", "ablative": ["eīs", "iīs"]}
    },
    "id (It/This/That)": {
        "type": "Demonstrative", "gender": "Neuter",
        "singular": {"nominative": "id", "genitive": "eius", "dative": "eī", "accusative": "id", "ablative": "eō"},
        "plural": {"nominative": "ea", "genitive": "eōrum", "dative": ["eīs", "iīs"], "accusative": "ea", "ablative": ["eīs", "iīs"]}
    },

    # --- DEMONSTRATIVE PRONOUNS (hic, haec, hoc) ---
    "hic (This)": {
        "type": "Demonstrative", "gender": "Masculine",
        "singular": {"nominative": "hic", "genitive": "huius", "dative": "huic", "accusative": "hunc", "ablative": "hōc"},
        "plural": {"nominative": "hī", "genitive": "hōrum", "dative": "hīs", "accusative": "hōs", "ablative": "hīs"}
    },
    "haec (This)": {
        "type": "Demonstrative", "gender": "Feminine",
        "singular": {"nominative": "haec", "genitive": "huius", "dative": "huic", "accusative": "hanc", "ablative": "hāc"},
        "plural": {"nominative": "hae", "genitive": "hārum", "dative": "hīs", "accusative": "hās", "ablative": "hīs"}
    },
    "hoc (This)": {
        "type": "Demonstrative", "gender": "Neuter",
        "singular": {"nominative": "hoc", "genitive": "huius", "dative": "huic", "accusative": "hoc", "ablative": "hōc"},
        "plural": {"nominative": "haec", "genitive": "hōrum", "dative": "hīs", "accusative": "haec", "ablative": "hīs"}
    },

    # --- DEMONSTRATIVE PRONOUNS (ille, illa, illud) ---
    "ille (That)": {
        "type": "Demonstrative", "gender": "Masculine",
        "singular": {"nominative": "ille", "genitive": "illīus", "dative": "illī", "accusative": "illum", "ablative": "illō"},
        "plural": {"nominative": "illī", "genitive": "illōrum", "dative": "illīs", "accusative": "illōs", "ablative": "illīs"}
    },
    "illa (That)": {
        "type": "Demonstrative", "gender": "Feminine",
        "singular": {"nominative": "illa", "genitive": "illīus", "dative": "illī", "accusative": "illam", "ablative": "illā"},
        "plural": {"nominative": "illae", "genitive": "illārum", "dative": "illīs", "accusative": "illās", "ablative": "illīs"}
    },
    "illud (That)": {
        "type": "Demonstrative", "gender": "Neuter",
        "singular": {"nominative": "illud", "genitive": "illīus", "dative": "illī", "accusative": "illud", "ablative": "illō"},
        "plural": {"nominative": "illa", "genitive": "illōrum", "dative": "illīs", "accusative": "illa", "ablative": "illīs"}
    },

    # --- RELATIVE PRONOUNS (quī, quae, quod) ---
    "quī (Who/Which)": {
        "type": "Relative", "gender": "Masculine",
        "singular": {"nominative": "quī", "genitive": "cuius", "dative": "cui", "accusative": "quem", "ablative": "quō"},
        "plural": {"nominative": "quī", "genitive": "quōrum", "dative": "quibus", "accusative": "quōs", "ablative": "quibus"}
    },
    "quae (Who/Which)": {
        "type": "Relative", "gender": "Feminine",
        "singular": {"nominative": "quae", "genitive": "cuius", "dative": "cui", "accusative": "quam", "ablative": "quā"},
        "plural": {"nominative": "quae", "genitive": "quārum", "dative": "quibus", "accusative": "quās", "ablative": "quibus"}
    },
    "quod (Who/Which)": {
        "type": "Relative", "gender": "Neuter",
        "singular": {"nominative": "quod", "genitive": "cuius", "dative": "cui", "accusative": "quod", "ablative": "quō"},
        "plural": {"nominative": "quae", "genitive": "quōrum", "dative": "quibus", "accusative": "quae", "ablative": "quibus"}
    }
}

# --- HELPER FUNCTIONS ---
def remove_macrons(text):
    if not isinstance(text, str):
        return ""
    replacements = {'ā': 'a', 'ē': 'e', 'ī': 'i', 'ō': 'o', 'ū': 'u', 'Ā': 'A', 'Ē': 'E', 'Ī': 'I', 'Ō': 'O', 'Ū': 'U'}
    for macron, plain in replacements.items():
        text = text.replace(macron, plain)
    return text.lower().strip()

def check_answer(user_input, correct_answer):
    user_clean = remove_macrons(user_input)
    # Handle multiple valid answers (e.g., nostrum vs nostri)
    if isinstance(correct_answer, list):
        clean_correct_list = [remove_macrons(ans) for ans in correct_answer]
        return user_clean in clean_correct_list
    else:
        return user_clean == remove_macrons(correct_answer)

def get_display_answer(answer_data):
    if isinstance(answer_data, list):
        return " / ".join(answer_data)
    return answer_data

# --- STREAMLIT UI ---
st.title("🏛️ Latin Pronoun Master")

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
accuracy = (st.session_state.score / st.session_state.attempts) * 100 if st.session_state.attempts > 0 else 0.0

# --- SCORE DISPLAY ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Correct ✅", st.session_state.score)
col2.metric("Attempts 📝", st.session_state.attempts)
col3.metric("Accuracy 🎯", f"{accuracy:.1f}%")
col4.metric("Streak 🔥", f"{st.session_state.streak} (Max: {st.session_state.max_streak})")
st.divider()

with st.sidebar:
    st.header("Quiz Settings")
    
    # Filters adapted for pronouns
    selected_type = st.selectbox("Select Pronoun Type:", ["All", "Personal", "Reflexive", "Demonstrative", "Relative"])
    selected_gender = st.selectbox("Select Gender:", ["All", "Masculine", "Feminine", "Neuter", "N/A (1st/2nd Person & Reflexive)"])

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
    display_correct = get_display_answer(res['answer'])
    if res["correct"]:
        st.success(f"**Optimē!** Previous: {res['prompt']} → **{display_correct}**")
    else:
        st.error(f"**Errāstī.** Previous: {res['prompt']} → **{display_correct}**")

# --- SELECTION LOGIC ---
if "current_q" not in st.session_state:
    questions = []
    
    # Map the dropdown UI selection to the internal data tags
    gender_map = {"Masculine": "Masculine", "Feminine": "Feminine", "Neuter": "Neuter", "N/A (1st/2nd Person & Reflexive)": "N/A"}

    for pronoun, data in pronouns_db.items():
        # Apply filters
        if selected_type != "All" and data["type"] != selected_type:
            continue
        if selected_gender != "All" and data["gender"] != gender_map[selected_gender]:
            continue
            
        for number in ["singular", "plural"]:
            for case, form in data[number].items():
                # Skip cases that don't exist (like nominative reflexive)
                if form is None:
                    continue
                
                meta_info = f"({data['type']}, {data['gender']})"
                prompt_text = f"{pronoun.upper()} {meta_info} — {number.upper()} {case.upper()}"
                
                questions.append({
                    "prompt": prompt_text,
                    "answer": form
                })

    if questions:
        st.session_state.current_q = random.choice(questions)
    else:
        st.warning("No pronouns match your current filter criteria. Please adjust your settings.")

# --- DISPLAY & FORM ---
if "current_q" in st.session_state:
    q = st.session_state.current_q
    st.info(f"How do you decline: **{q['prompt']}**?")

    with st.form(key='quiz_form', clear_on_submit=True):
        user_input = st.text_input("Your Answer (if multiple exist, type just one):")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        is_correct = check_answer(user_input, q['answer'])

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
            "correct": is_correct
        }

        del st.session_state.current_q
        st.rerun()
