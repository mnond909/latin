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
            "future": {
                "active": {"singular": {1: "amābō", 2: "amābis", 3: "amābit"},
                           "plural": {1: "amābimus", 2: "amābitis", 3: "amābunt"}},
                "passive": {"singular": {1: "amābor", 2: "amāberis", 3: "amābitur"},
                            "plural": {1: "amābimur", 2: "amābiminī", 3: "amābuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "amāvī", 2: "amāvistī", 3: "amāvit"},
                           "plural": {1: "amāvimus", 2: "amāvistis", 3: "amāvērunt"}},
                "passive": {"singular": {1: "amātus sum", 2: "amātus es", 3: "amātus est"},
                            "plural": {1: "amātī sumus", 2: "amātī estis", 3: "amātī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "amāverō", 2: "amāveris", 3: "amāverit"},
                           "plural": {1: "amāverimus", 2: "amāveritis", 3: "amāverint"}},
                "passive": {"singular": {1: "amātus erō", 2: "amātus eris", 3: "amātus erit"},
                            "plural": {1: "amātī erimus", 2: "amātī eritis", 3: "amātī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "amā"}, "plural": {2: "amāte"}},
                "passive": {"singular": {2: "amāre"}, "plural": {2: "amāminī"}}
            },
            "future": {
                "active": {"singular": {2: "amātō", 3: "amātō"}, "plural": {2: "amātōte", 3: "amantō"}},
                "passive": {"singular": {2: "amātor", 3: "amātor"}, "plural": {3: "amantor"}}
            }
        },
        "infinitives": {
            "present active": "amāre",
            "present passive": "amārī",
            "perfect active": "amāvisse",
            "perfect passive": "amātus esse",
            "future active": "amātūrus esse",
            "future passive": "amātum īrī"
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
            "future": {
                "active": {"singular": {1: "monēbō", 2: "monēbis", 3: "monēbit"},
                           "plural": {1: "monēbimus", 2: "monēbitis", 3: "monēbunt"}},
                "passive": {"singular": {1: "monēbor", 2: "monēberis", 3: "monēbitur"},
                            "plural": {1: "monēbimur", 2: "monēbiminī", 3: "monēbuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "monuī", 2: "monuistī", 3: "monuit"},
                           "plural": {1: "monuimus", 2: "monuistis", 3: "monuērunt"}},
                "passive": {"singular": {1: "monitus sum", 2: "monitus es", 3: "monitus est"},
                            "plural": {1: "monitī sumus", 2: "monitī estis", 3: "monitī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "monuerō", 2: "monueris", 3: "monuerit"},
                           "plural": {1: "monuerimus", 2: "monueritis", 3: "monuerint"}},
                "passive": {"singular": {1: "monitus erō", 2: "monitus eris", 3: "monitus erit"},
                            "plural": {1: "monitī erimus", 2: "monitī eritis", 3: "monitī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "monē"}, "plural": {2: "monēte"}},
                "passive": {"singular": {2: "monēre"}, "plural": {2: "monēminī"}}
            },
            "future": {
                "active": {"singular": {2: "monētō", 3: "monētō"}, "plural": {2: "monētōte", 3: "monentō"}},
                "passive": {"singular": {2: "monētor", 3: "monētor"}, "plural": {3: "monentor"}}
            }
        },
        "infinitives": {
            "present active": "monēre",
            "present passive": "monērī",
            "perfect active": "monuisse",
            "perfect passive": "monitus esse",
            "future active": "monitūrus esse",
            "future passive": "monitum īrī"
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

# --- SCORE TRACKER INITIALIZATION ---
if "score" not in st.session_state:
    st.session_state.score = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# --- SCORE DISPLAY ---
col1, col2 = st.columns(2)
col1.metric("Correct Answers ✅", st.session_state.score)
col2.metric("Total Attempts 📝", st.session_state.attempts)
st.divider()

with st.sidebar:
    st.header("Quiz Settings")
    verb_choice = st.selectbox("Select Verb:", ["All"] + list(verbs_db.keys()))
    include_passive = st.checkbox("Include Passive Voice?", value=True)
    include_inf = st.checkbox("Include Infinitives?", value=True)
    include_imp = st.checkbox("Include Imperatives?", value=True)

    if st.button("Skip / New Question"):
        if "current_q" in st.session_state:
            del st.session_state.current_q
        if "last_result" in st.session_state:
            del st.session_state.last_result
        st.rerun()
        
    st.divider()
    
    # Optional button to reset the score
    if st.button("Reset Score"):
        st.session_state.score = 0
        st.session_state.attempts = 0
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

        # Process Indicatives
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

        # Process Imperatives
        if include_imp and "imperative" in verb_data:
            for tense, voices in verb_data["imperative"].items():
                for voice, numbers in voices.items():
                    if voice == "passive" and not include_passive:
                        continue
                    for number, persons in numbers.items():
                        for person, form in persons.items():
                            questions.append({
                                "prompt": f"{verb_name.upper()} — {voice.upper()} {tense.upper()} IMPERATIVE — {person} {number}",
                                "answer": form
                            })

        # Process Infinitives
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

        # --- UPDATE SCORES ---
        st.session_state.attempts += 1
        if is_correct:
            st.session_state.score += 1

        # Save the context of the question we just finished
        st.session_state.last_result = {
            "prompt": q['prompt'],
            "answer": q['answer'],
            "correct": is_correct
        }

        # Move to next question immediately
        del st.session_state.current_q
        st.rerun()
