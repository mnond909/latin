import streamlit as st
import random

# --- DATA ---
verbs_db = {
    "amāre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "amō", 2: "amās", 3: "amat"},
                           "plural": {1: "amāmus", 2: "amātis", 3: "amant"}},
                "passive": {"singular": {1: "amor", 2: "amāris", 3: "amātur"},
                            "plural": {1: "amāmur", 2: "amāminī", 3: "amantur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "amābam", 2: "amābās", 3: "amābat"},
                           "plural": {1: "amābāmus", 2: "amābātis", 3: "amābānt"}},
                "passive": {"singular": {1: "amābar", 2: "amābāris", 3: "amābātur"},
                            "plural": {1: "amābāmur", 2: "amābāminī", 3: "amābantur"}}
            },
            "perfect": {
                "active": {"singular": {1: "amāvī", 2: "amāvistī", 3: "amāvit"},
                           "plural": {1: "amāvimus", 2: "amāvistis", 3: "amāvērunt"}},
                "passive": {"singular": {1: "amātus sum", 2: "amātus es", 3: "amātus est"},
                            "plural": {1: "amātī sumus", 2: "amātī estis", 3: "amātī sunt"}}
            }
        },
        "infinitives": {
            "present active": "amāre",
            "present passive": "amārī",
            "perfect active": "amāvisse",
            "perfect passive": "amātus esse",
            "future active": "amātūrus esse"
        }
    },
    "monēre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "moneō", 2: "monēs", 3: "monet"},
                           "plural": {1: "monēmus", 2: "monētis", 3: "monent"}},
                "passive": {"singular": {1: "moneor", 2: "monēris", 3: "monētur"},
                            "plural": {1: "monēmur", 2: "monēminī", 3: "monentur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "monēbam", 2: "monēbās", 3: "monēbat"},
                           "plural": {1: "monēbāmus", 2: "monēbātis", 3: "monēbant"}},
                "passive": {"singular": {1: "monēbar", 2: "monēbāris", 3: "monēbātur"},
                            "plural": {1: "monēbāmur", 2: "monēbāminī", 3: "monēbantur"}}
            },
            "perfect": {
                "active": {"singular": {1: "monuī", 2: "monuistī", 3: "monuit"},
                           "plural": {1: "monuimus", 2: "monuistis", 3: "monuērunt"}},
                "passive": {"singular": {1: "monitus sum", 2: "monitus es", 3: "monitus est"},
                            "plural": {1: "monitī sumus", 2: "monitī estis", 3: "monitī sunt"}}
            }
        },
        "infinitives": {
            "present active": "monēre",
            "present passive": "monērī",
            "perfect active": "monuisse",
            "perfect passive": "monitus esse",
            "future active": "monitūrus esse"
        }
    }
}


# --- HELPER FUNCTIONS ---
def remove_macrons(text):
    replacements = {'ā': 'a', 'ē': 'e', 'ī': 'i', 'ō': 'o', 'ū': 'u', 'Ā': 'A', 'Ē': 'E', 'Ī': 'I', 'Ō': 'O', 'Ū': 'U'}
    for macron, plain in replacements.items():
        text = text.replace(macron, plain)
    return text.lower().strip()


# --- STREAMLIT UI ---
st.set_page_config(page_title="Latin Verb Master", page_icon="🏛️")
st.title("🏛️ Latin Verb Master")

with st.sidebar:
    st.header("Quiz Settings")
    verb_choice = st.selectbox("Select Verb:", ["All"] + list(verbs_db.keys()))
    include_passive = st.checkbox("Include Passive Voice?", value=True)
    include_inf = st.checkbox("Include Infinitives?", value=True)

    if st.button("Skip / New Question"):
        if "current_q" in st.session_state:
            del st.session_state.current_q
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
    verbs_to_pull = list(verbs_db.keys()) if verb_choice == "All" else [verb_choice]

    for verb_name in verbs_to_pull:
        verb_data = verbs_db[verb_name]

        if "indicative" in verb_data:
            for tense, voices in verb_data["indicative"].items():
                for voice, numbers in voices.items():
                    if voice == "passive" and not include_passive:
                        continue
                    for number, persons in numbers.items():
                        for person, form in persons.items():
                            questions.append({
                                "prompt": f"{verb_name.upper()} — {voice.upper()} {tense.upper()} INDICATIVE — {person} {number}",
                                "answer": form
                            })

        if include_inf and "infinitives" in verb_data:
            for inf_type, form in verb_data["infinitives"].items():
                if "passive" in inf_type and not include_passive:
                    continue
                questions.append({
                    "prompt": f"{verb_name.upper()} — {inf_type.upper()} INFINITIVE",
                    "answer": form
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

        # Save the context of the question we just finished
        st.session_state.last_result = {
            "prompt": q['prompt'],
            "answer": q['answer'],
            "correct": is_correct
        }

        # Move to next question immediately
        del st.session_state.current_q
        st.rerun()