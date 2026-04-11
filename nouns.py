import streamlit as st
import random
from PIL import Image # Add this line

# Load your custom icon
icon_image = Image.open("spqr.png")

# Change page_icon to use your image
st.set_page_config(page_title="Latin Noun Master", page_icon=icon_image)
# --- DATA ---
# Includes at least 2 nouns for each declension-gender pair
nouns_db = {
    # --- 1ST DECLENSION ---
    "puella": {
        "declension": "1st", "gender": "Feminine",
        "singular": {"nominative": "puella", "genitive": "puellae", "dative": "puellae", "accusative": "puellam", "ablative": "puellā", "vocative": "puella"},
        "plural": {"nominative": "puellae", "genitive": "puellārum", "dative": "puellīs", "accusative": "puellās", "ablative": "puellīs", "vocative": "puellae"}
    },
    "rosa": {
        "declension": "1st", "gender": "Feminine",
        "singular": {"nominative": "rosa", "genitive": "rosae", "dative": "rosae", "accusative": "rosam", "ablative": "rosā", "vocative": "rosa"},
        "plural": {"nominative": "rosae", "genitive": "rosārum", "dative": "rosīs", "accusative": "rosās", "ablative": "rosīs", "vocative": "rosae"}
    },
    "nauta": {
        "declension": "1st", "gender": "Masculine",
        "singular": {"nominative": "nauta", "genitive": "nautae", "dative": "nautae", "accusative": "nautam", "ablative": "nautā", "vocative": "nauta"},
        "plural": {"nominative": "nautae", "genitive": "nautārum", "dative": "nautīs", "accusative": "nautās", "ablative": "nautīs", "vocative": "nautae"}
    },
    "agricola": {
        "declension": "1st", "gender": "Masculine",
        "singular": {"nominative": "agricola", "genitive": "agricolae", "dative": "agricolae", "accusative": "agricolam", "ablative": "agricolā", "vocative": "agricola"},
        "plural": {"nominative": "agricolae", "genitive": "agricolārum", "dative": "agricolīs", "accusative": "agricolās", "ablative": "agricolīs", "vocative": "agricolae"}
    },

    # --- 2ND DECLENSION ---
    "servus": {
        "declension": "2nd", "gender": "Masculine",
        "singular": {"nominative": "servus", "genitive": "servī", "dative": "servō", "accusative": "servum", "ablative": "servō", "vocative": "serve"},
        "plural": {"nominative": "servī", "genitive": "servōrum", "dative": "servīs", "accusative": "servōs", "ablative": "servīs", "vocative": "servī"}
    },
    "puer": {
        "declension": "2nd", "gender": "Masculine",
        "singular": {"nominative": "puer", "genitive": "puerī", "dative": "puerō", "accusative": "puerum", "ablative": "puerō", "vocative": "puer"},
        "plural": {"nominative": "puerī", "genitive": "puerōrum", "dative": "puerīs", "accusative": "puerōs", "ablative": "puerīs", "vocative": "puerī"}
    },
    "bellum": {
        "declension": "2nd", "gender": "Neuter",
        "singular": {"nominative": "bellum", "genitive": "bellī", "dative": "bellō", "accusative": "bellum", "ablative": "bellō", "vocative": "bellum"},
        "plural": {"nominative": "bella", "genitive": "bellōrum", "dative": "bellīs", "accusative": "bella", "ablative": "bellīs", "vocative": "bella"}
    },
    "dōnum": {
        "declension": "2nd", "gender": "Neuter",
        "singular": {"nominative": "dōnum", "genitive": "dōnī", "dative": "dōnō", "accusative": "dōnum", "ablative": "dōnō", "vocative": "dōnum"},
        "plural": {"nominative": "dōna", "genitive": "dōnōrum", "dative": "dōnīs", "accusative": "dōna", "ablative": "dōnīs", "vocative": "dōna"}
    },

    # --- 3RD DECLENSION ---
    "rēx": {
        "declension": "3rd", "gender": "Masculine",
        "singular": {"nominative": "rēx", "genitive": "rēgis", "dative": "rēgī", "accusative": "rēgem", "ablative": "rēge", "vocative": "rēx"},
        "plural": {"nominative": "rēgēs", "genitive": "rēgum", "dative": "rēgibus", "accusative": "rēgēs", "ablative": "rēgibus", "vocative": "rēgēs"}
    },
    "pater": {
        "declension": "3rd", "gender": "Masculine",
        "singular": {"nominative": "pater", "genitive": "patris", "dative": "patrī", "accusative": "patrem", "ablative": "patre", "vocative": "pater"},
        "plural": {"nominative": "patrēs", "genitive": "patrum", "dative": "patribus", "accusative": "patrēs", "ablative": "patribus", "vocative": "patrēs"}
    },
    "lēx": {
        "declension": "3rd", "gender": "Feminine",
        "singular": {"nominative": "lēx", "genitive": "lēgis", "dative": "lēgī", "accusative": "lēgem", "ablative": "lēge", "vocative": "lēx"},
        "plural": {"nominative": "lēgēs", "genitive": "lēgum", "dative": "lēgibus", "accusative": "lēgēs", "ablative": "lēgibus", "vocative": "lēgēs"}
    },
    "māter": {
        "declension": "3rd", "gender": "Feminine",
        "singular": {"nominative": "māter", "genitive": "mātris", "dative": "mātrī", "accusative": "mātrem", "ablative": "mātre", "vocative": "māter"},
        "plural": {"nominative": "mātrēs", "genitive": "mātrum", "dative": "mātribus", "accusative": "mātrēs", "ablative": "mātribus", "vocative": "mātrēs"}
    },
    "corpus": {
        "declension": "3rd", "gender": "Neuter",
        "singular": {"nominative": "corpus", "genitive": "corporis", "dative": "corporī", "accusative": "corpus", "ablative": "corpore", "vocative": "corpus"},
        "plural": {"nominative": "corpora", "genitive": "corporum", "dative": "corporibus", "accusative": "corpora", "ablative": "corporibus", "vocative": "corpora"}
    },
    "nōmen": {
        "declension": "3rd", "gender": "Neuter",
        "singular": {"nominative": "nōmen", "genitive": "nōminis", "dative": "nōminī", "accusative": "nōmen", "ablative": "nōmine", "vocative": "nōmen"},
        "plural": {"nominative": "nōmina", "genitive": "nōminum", "dative": "nōminibus", "accusative": "nōmina", "ablative": "nōminibus", "vocative": "nōmina"}
    },

    # --- 4TH DECLENSION ---
    "portus": {
        "declension": "4th", "gender": "Masculine",
        "singular": {"nominative": "portus", "genitive": "portūs", "dative": "portuī", "accusative": "portum", "ablative": "portū", "vocative": "portus"},
        "plural": {"nominative": "portūs", "genitive": "portuum", "dative": "portibus", "accusative": "portūs", "ablative": "portibus", "vocative": "portūs"}
    },
    "exercitus": {
        "declension": "4th", "gender": "Masculine",
        "singular": {"nominative": "exercitus", "genitive": "exercitūs", "dative": "exercituī", "accusative": "exercitum", "ablative": "exercitū", "vocative": "exercitus"},
        "plural": {"nominative": "exercitūs", "genitive": "exercituum", "dative": "exercitibus", "accusative": "exercitūs", "ablative": "exercitibus", "vocative": "exercitūs"}
    },
    "manus": {
        "declension": "4th", "gender": "Feminine",
        "singular": {"nominative": "manus", "genitive": "manūs", "dative": "manuī", "accusative": "manum", "ablative": "manū", "vocative": "manus"},
        "plural": {"nominative": "manūs", "genitive": "manuum", "dative": "manibus", "accusative": "manūs", "ablative": "manibus", "vocative": "manūs"}
    },
    "acus": {
        "declension": "4th", "gender": "Feminine",
        "singular": {"nominative": "acus", "genitive": "acūs", "dative": "acuī", "accusative": "acum", "ablative": "acū", "vocative": "acus"},
        "plural": {"nominative": "acūs", "genitive": "acuum", "dative": "acubus", "accusative": "acūs", "ablative": "acubus", "vocative": "acūs"}
    },
    "cornū": {
        "declension": "4th", "gender": "Neuter",
        "singular": {"nominative": "cornū", "genitive": "cornūs", "dative": "cornū", "accusative": "cornū", "ablative": "cornū", "vocative": "cornū"},
        "plural": {"nominative": "cornua", "genitive": "cornuum", "dative": "cornibus", "accusative": "cornua", "ablative": "cornibus", "vocative": "cornua"}
    },
    "genū": {
        "declension": "4th", "gender": "Neuter",
        "singular": {"nominative": "genū", "genitive": "genūs", "dative": "genū", "accusative": "genū", "ablative": "genū", "vocative": "genū"},
        "plural": {"nominative": "genua", "genitive": "genuum", "dative": "genibus", "accusative": "genua", "ablative": "genibus", "vocative": "genua"}
    },

    # --- 5TH DECLENSION ---
    "rēs": {
        "declension": "5th", "gender": "Feminine",
        "singular": {"nominative": "rēs", "genitive": "reī", "dative": "reī", "accusative": "rem", "ablative": "rē", "vocative": "rēs"},
        "plural": {"nominative": "rēs", "genitive": "rērum", "dative": "rēbus", "accusative": "rēs", "ablative": "rēbus", "vocative": "rēs"}
    },
    "spēs": {
        "declension": "5th", "gender": "Feminine",
        "singular": {"nominative": "spēs", "genitive": "speī", "dative": "speī", "accusative": "spem", "ablative": "spē", "vocative": "spēs"},
        "plural": {"nominative": "spēs", "genitive": "spērum", "dative": "spēbus", "accusative": "spēs", "ablative": "spēbus", "vocative": "spēs"}
    },
    "diēs": {
        "declension": "5th", "gender": "Masculine",
        "singular": {"nominative": "diēs", "genitive": "diēī", "dative": "diēī", "accusative": "diem", "ablative": "diē", "vocative": "diēs"},
        "plural": {"nominative": "diēs", "genitive": "diērum", "dative": "diēbus", "accusative": "diēs", "ablative": "diēbus", "vocative": "diēs"}
    },
    "merīdiēs": {
        "declension": "5th", "gender": "Masculine",
        "singular": {"nominative": "merīdiēs", "genitive": "merīdiēī", "dative": "merīdiēī", "accusative": "merīdiem", "ablative": "merīdiē", "vocative": "merīdiēs"},
        "plural": {"nominative": "merīdiēs", "genitive": "merīdiērum", "dative": "merīdiēbus", "accusative": "merīdiēs", "ablative": "merīdiēbus", "vocative": "merīdiēs"}
    }
}


# --- HELPER FUNCTIONS ---
def remove_macrons(text):
    replacements = {'ā': 'a', 'ē': 'e', 'ī': 'i', 'ō': 'o', 'ū': 'u', 'Ā': 'A', 'Ē': 'E', 'Ī': 'I', 'Ō': 'O', 'Ū': 'U'}
    for macron, plain in replacements.items():
        text = text.replace(macron, plain)
    return text.lower().strip()


# --- STREAMLIT UI ---
st.set_page_config(page_title="Latin Noun Master", page_icon="🏛️")
st.title("🏛️ Latin Noun Master")

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
    
    # Filters
    selected_declension = st.selectbox("Select Declension:", ["All", "1st", "2nd", "3rd", "4th", "5th"])
    selected_gender = st.selectbox("Select Gender:", ["All", "Masculine", "Feminine", "Neuter"])
    include_vocative = st.checkbox("Include Vocative Case?", value=False)

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
        st.success(f"**Optimē!** Previous: {res['prompt']} → **{res['answer']}**")
    else:
        st.error(f"**Errāstī.** Previous: {res['prompt']} → **{res['answer']}**")

# --- SELECTION LOGIC ---
if "current_q" not in st.session_state:
    questions = []
    
    for noun, data in nouns_db.items():
        # Apply filters
        if selected_declension != "All" and data["declension"] != selected_declension:
            continue
        if selected_gender != "All" and data["gender"] != selected_gender:
            continue
            
        for number in ["singular", "plural"]:
            for case, form in data[number].items():
                if case == "vocative" and not include_vocative:
                    continue
                
                # Build a readable prompt with Nominative AND Genitive Singular
                genitive_singular = data["singular"]["genitive"]
                meta_info = f"({data['declension']}, {data['gender'][0]})" # e.g. (1st, F)
                prompt_text = f"{noun.upper()}, {genitive_singular.upper()} {meta_info} — {number.upper()} {case.upper()}"
                
                questions.append({
                    "prompt": prompt_text,
                    "answer": form
                })

    if questions:
        st.session_state.current_q = random.choice(questions)
    else:
        st.warning("No nouns match your current filter criteria. Please adjust your settings.")

# --- DISPLAY & FORM ---
if "current_q" in st.session_state:
    q = st.session_state.current_q
    st.info(f"How do you decline: **{q['prompt']}**?")

    with st.form(key='quiz_form', clear_on_submit=True):
        user_input = st.text_input("Your Answer:")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        is_correct = remove_macrons(user_input) == remove_macrons(q['answer'])

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
