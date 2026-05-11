# latin_verbs.py

# === 1. PASTE YOUR EXACT verb_conjugations DICTIONARY HERE ===
verb_conjugations = {
    # 1st Conjugation
    "amāre": "1st", "laudāre": "1st", "vocāre": "1st", "portāre": "1st", "parāre": "1st",
    "spectāre": "1st", "superāre": "1st", "vulnerāre": "1st", "oppugnāre": "1st", "servāre": "1st",
    # 2nd Conjugation
    "monēre": "2nd", "vidēre": "2nd", "habēre": "2nd", "docēre": "2nd", "tenēre": "2nd",
    "terrēre": "2nd", "movēre": "2nd", "prohibēre": "2nd", "praebēre": "2nd", "miscēre": "2nd",
    # 3rd Conjugation
    "dūcere": "3rd", "mittere": "3rd", "pōnere": "3rd", "regere": "3rd", "trahere": "3rd",
    "dīcere": "3rd", "vincere": "3rd", "legere": "3rd", "scrībere": "3rd", "pellere": "3rd",
    # 3rd i-stem Conjugation
    "capere": "3rd i-stem", "rapere": "3rd i-stem", "iacere": "3rd i-stem", "accipere": "3rd i-stem", "excipere": "3rd i-stem",
    "dēcipere": "3rd i-stem", "recipere": "3rd i-stem", "ēripere": "3rd i-stem", "cōnspicere": "3rd i-stem", "dīripere": "3rd i-stem",
    # 4th Conjugation
    "audīre": "4th", "scīre": "4th", "invenīre": "4th", "pūnīre": "4th", "mūnīre": "4th",
    "custōdīre": "4th", "impedīre": "4th", "fīnīre": "4th", "aperīre": "4th", "reperīre": "4th"
}

# === 2. PASTE YOUR ENTIRE verbs_db DICTIONARY HERE ===
verbs_db = {
    # (Your massive dictionary goes here)
}

# === 3. NEW DICTIONARY FOR ENGLISH TRANSLATIONS ===
verb_english_forms = {
    # 1st Conjugation
    "amāre": {"base": "love", "s": "loves", "ing": "loving", "past": "loved", "pp": "loved"},
    "laudāre": {"base": "praise", "s": "praises", "ing": "praising", "past": "praised", "pp": "praised"},
    "vocāre": {"base": "call", "s": "calls", "ing": "calling", "past": "called", "pp": "called"},
    "portāre": {"base": "carry", "s": "carries", "ing": "carrying", "past": "carried", "pp": "carried"},
    "parāre": {"base": "prepare", "s": "prepares", "ing": "preparing", "past": "prepared", "pp": "prepared"},
    "spectāre": {"base": "watch", "s": "watches", "ing": "watching", "past": "watched", "pp": "watched"},
    "superāre": {"base": "overcome", "s": "overcomes", "ing": "overcoming", "past": "overcame", "pp": "overcome"},
    "vulnerāre": {"base": "wound", "s": "wounds", "ing": "wounding", "past": "wounded", "pp": "wounded"},
    "oppugnāre": {"base": "attack", "s": "attacks", "ing": "attacking", "past": "attacked", "pp": "attacked"},
    "servāre": {"base": "save", "s": "saves", "ing": "saving", "past": "saved", "pp": "saved"},
    
    # 2nd Conjugation
    "monēre": {"base": "warn", "s": "warns", "ing": "warning", "past": "warned", "pp": "warned"},
    "vidēre": {"base": "see", "s": "sees", "ing": "seeing", "past": "saw", "pp": "seen"},
    "habēre": {"base": "have", "s": "has", "ing": "having", "past": "had", "pp": "had"},
    "docēre": {"base": "teach", "s": "teaches", "ing": "teaching", "past": "taught", "pp": "taught"},
    "tenēre": {"base": "hold", "s": "holds", "ing": "holding", "past": "held", "pp": "held"},
    "terrēre": {"base": "frighten", "s": "frightens", "ing": "frightening", "past": "frightened", "pp": "frightened"},
    "movēre": {"base": "move", "s": "moves", "ing": "moving", "past": "moved", "pp": "moved"},
    "prohibēre": {"base": "prevent", "s": "prevents", "ing": "preventing", "past": "prevented", "pp": "prevented"},
    "praebēre": {"base": "provide", "s": "provides", "ing": "providing", "past": "provided", "pp": "provided"},
    "miscēre": {"base": "mix", "s": "mixes", "ing": "mixing", "past": "mixed", "pp": "mixed"},
    
    # 3rd Conjugation
    "dūcere": {"base": "lead", "s": "leads", "ing": "leading", "past": "led", "pp": "led"},
    "mittere": {"base": "send", "s": "sends", "ing": "sending", "past": "sent", "pp": "sent"},
    "pōnere": {"base": "put", "s": "puts", "ing": "putting", "past": "put", "pp": "put"},
    "regere": {"base": "rule", "s": "rules", "ing": "ruling", "past": "ruled", "pp": "ruled"},
    "trahere": {"base": "drag", "s": "drags", "ing": "dragging", "past": "dragged", "pp": "dragged"},
    "dīcere": {"base": "say", "s": "says", "ing": "saying", "past": "said", "pp": "said"},
    "vincere": {"base": "conquer", "s": "conquers", "ing": "conquering", "past": "conquered", "pp": "conquered"},
    "legere": {"base": "read", "s": "reads", "ing": "reading", "past": "read", "pp": "read"},
    "scrībere": {"base": "write", "s": "writes", "ing": "writing", "past": "wrote", "pp": "written"},
    "pellere": {"base": "drive", "s": "drives", "ing": "driving", "past": "drove", "pp": "driven"},
    
    # 3rd i-stem Conjugation
    "capere": {"base": "take", "s": "takes", "ing": "taking", "past": "took", "pp": "taken"},
    "rapere": {"base": "seize", "s": "seizes", "ing": "seizing", "past": "seized", "pp": "seized"},
    "iacere": {"base": "throw", "s": "throws", "ing": "throwing", "past": "threw", "pp": "thrown"},
    "accipere": {"base": "receive", "s": "receives", "ing": "receiving", "past": "received", "pp": "received"},
    "excipere": {"base": "catch", "s": "catches", "ing": "catching", "past": "caught", "pp": "caught"},
    "dēcipere": {"base": "deceive", "s": "deceives", "ing": "deceiving", "past": "deceived", "pp": "deceived"},
    "recipere": {"base": "take back", "s": "takes back", "ing": "taking back", "past": "took back", "pp": "taken back"},
    "ēripere": {"base": "snatch", "s": "snatches", "ing": "snatching", "past": "snatched", "pp": "snatched"},
    "cōnspicere": {"base": "spot", "s": "spots", "ing": "spotting", "past": "spotted", "pp": "spotted"},
    "dīripere": {"base": "plunder", "s": "plunders", "ing": "plundering", "past": "plundered", "pp": "plundered"},
    
    # 4th Conjugation
    "audīre": {"base": "hear", "s": "hears", "ing": "hearing", "past": "heard", "pp": "heard"},
    "scīre": {"base": "know", "s": "knows", "ing": "knowing", "past": "knew", "pp": "known"},
    "invenīre": {"base": "find", "s": "finds", "ing": "finding", "past": "found", "pp": "found"},
    "pūnīre": {"base": "punish", "s": "punishes", "ing": "punishing", "past": "punished", "pp": "punished"},
    "mūnīre": {"base": "fortify", "s": "fortifies", "ing": "fortifying", "past": "fortified", "pp": "fortified"},
    "custōdīre": {"base": "guard", "s": "guards", "ing": "guarding", "past": "guarded", "pp": "guarded"},
    "impedīre": {"base": "hinder", "s": "hinders", "ing": "hindering", "past": "hindered", "pp": "hindered"},
    "fīnīre": {"base": "finish", "s": "finishes", "ing": "finishing", "past": "finished", "pp": "finished"},
    "aperīre": {"base": "open", "s": "opens", "ing": "opening", "past": "opened", "pp": "opened"},
    "reperīre": {"base": "discover", "s": "discovers", "ing": "discovering", "past": "discovered", "pp": "discovered"}
}
