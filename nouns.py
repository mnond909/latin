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
    # ==========================================
    # --- 1ST DECLENSION (10 Fem, 10 Masc) ---
    # ==========================================
    
    # 1st Declension - Feminine (10)
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
    "fēmina": {
        "declension": "1st", "gender": "Feminine",
        "singular": {"nominative": "fēmina", "genitive": "fēminae", "dative": "fēminae", "accusative": "fēminam", "ablative": "fēminā", "vocative": "fēmina"},
        "plural": {"nominative": "fēminae", "genitive": "fēminārum", "dative": "fēminīs", "accusative": "fēminās", "ablative": "fēminīs", "vocative": "fēminae"}
    },
    "īnsula": {
        "declension": "1st", "gender": "Feminine",
        "singular": {"nominative": "īnsula", "genitive": "īnsulae", "dative": "īnsulae", "accusative": "īnsulam", "ablative": "īnsulā", "vocative": "īnsula"},
        "plural": {"nominative": "īnsulae", "genitive": "īnsulārum", "dative": "īnsulīs", "accusative": "īnsulās", "ablative": "īnsulīs", "vocative": "īnsulae"}
    },
    "silva": {
        "declension": "1st", "gender": "Feminine",
        "singular": {"nominative": "silva", "genitive": "silvae", "dative": "silvae", "accusative": "silvam", "ablative": "silvā", "vocative": "silva"},
        "plural": {"nominative": "silvae", "genitive": "silvārum", "dative": "silvīs", "accusative": "silvās", "ablative": "silvīs", "vocative": "silvae"}
    },
    "via": {
        "declension": "1st", "gender": "Feminine",
        "singular": {"nominative": "via", "genitive": "viae", "dative": "viae", "accusative": "viam", "ablative": "viā", "vocative": "via"},
        "plural": {"nominative": "viae", "genitive": "viārum", "dative": "viīs", "accusative": "viās", "ablative": "viīs", "vocative": "viae"}
    },
    "aqua": {
        "declension": "1st", "gender": "Feminine",
        "singular": {"nominative": "aqua", "genitive": "aquae", "dative": "aquae", "accusative": "aquam", "ablative": "aquā", "vocative": "aqua"},
        "plural": {"nominative": "aquae", "genitive": "aquārum", "dative": "aquīs", "accusative": "aquās", "ablative": "aquīs", "vocative": "aquae"}
    },
    "vīta": {
        "declension": "1st", "gender": "Feminine",
        "singular": {"nominative": "vīta", "genitive": "vītae", "dative": "vītae", "accusative": "vītam", "ablative": "vītā", "vocative": "vīta"},
        "plural": {"nominative": "vītae", "genitive": "vītārum", "dative": "vītīs", "accusative": "vītās", "ablative": "vītīs", "vocative": "vītae"}
    },
    "umbra": {
        "declension": "1st", "gender": "Feminine",
        "singular": {"nominative": "umbra", "genitive": "umbrae", "dative": "umbrae", "accusative": "umbram", "ablative": "umbrā", "vocative": "umbra"},
        "plural": {"nominative": "umbrae", "genitive": "umbrārum", "dative": "umbrīs", "accusative": "umbrās", "ablative": "umbrīs", "vocative": "umbrae"}
    },
    "rēgīna": {
        "declension": "1st", "gender": "Feminine",
        "singular": {"nominative": "rēgīna", "genitive": "rēgīnae", "dative": "rēgīnae", "accusative": "rēgīnam", "ablative": "rēgīnā", "vocative": "rēgīna"},
        "plural": {"nominative": "rēgīnae", "genitive": "rēgīnārum", "dative": "rēgīnīs", "accusative": "rēgīnās", "ablative": "rēgīnīs", "vocative": "rēgīnae"}
    },

    # 1st Declension - Masculine (10)
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
    "poēta": {
        "declension": "1st", "gender": "Masculine",
        "singular": {"nominative": "poēta", "genitive": "poētae", "dative": "poētae", "accusative": "poētam", "ablative": "poētā", "vocative": "poēta"},
        "plural": {"nominative": "poētae", "genitive": "poētārum", "dative": "poētīs", "accusative": "poētās", "ablative": "poētīs", "vocative": "poētae"}
    },
    "pīrāta": {
        "declension": "1st", "gender": "Masculine",
        "singular": {"nominative": "pīrāta", "genitive": "pīrātae", "dative": "pīrātae", "accusative": "pīrātam", "ablative": "pīrātā", "vocative": "pīrāta"},
        "plural": {"nominative": "pīrātae", "genitive": "pīrātārum", "dative": "pīrātīs", "accusative": "pīrātās", "ablative": "pīrātīs", "vocative": "pīrātae"}
    },
    "incola": {
        "declension": "1st", "gender": "Masculine",
        "singular": {"nominative": "incola", "genitive": "incolae", "dative": "incolae", "accusative": "incolam", "ablative": "incolā", "vocative": "incola"},
        "plural": {"nominative": "incolae", "genitive": "incolārum", "dative": "incolīs", "accusative": "incolās", "ablative": "incolīs", "vocative": "incolae"}
    },
    "scrība": {
        "declension": "1st", "gender": "Masculine",
        "singular": {"nominative": "scrība", "genitive": "scrībae", "dative": "scrībae", "accusative": "scrībam", "ablative": "scrībās", "vocative": "scrība"},
        "plural": {"nominative": "scrībae", "genitive": "scrībārum", "dative": "scrībīs", "accusative": "scrībās", "ablative": "scrībīs", "vocative": "scrībae"}
    },
    "aurīga": {
        "declension": "1st", "gender": "Masculine",
        "singular": {"nominative": "aurīga", "genitive": "aurīgae", "dative": "aurīgae", "accusative": "aurīgam", "ablative": "aurīgā", "vocative": "aurīga"},
        "plural": {"nominative": "aurīgae", "genitive": "aurīgārum", "dative": "aurīgīs", "accusative": "aurīgās", "ablative": "aurīgīs", "vocative": "aurīgae"}
    },
    "athlēta": {
        "declension": "1st", "gender": "Masculine",
        "singular": {"nominative": "athlēta", "genitive": "athlētae", "dative": "athlētae", "accusative": "athlētam", "ablative": "athlētā", "vocative": "athlēta"},
        "plural": {"nominative": "athlētae", "genitive": "athlētārum", "dative": "athlētīs", "accusative": "athlētās", "ablative": "athlētīs", "vocative": "athlētae"}
    },
    "convīva": {
        "declension": "1st", "gender": "Masculine",
        "singular": {"nominative": "convīva", "genitive": "convīvae", "dative": "convīvae", "accusative": "convīvam", "ablative": "convīvā", "vocative": "convīva"},
        "plural": {"nominative": "convīvae", "genitive": "convīvārum", "dative": "convīvīs", "accusative": "convīvās", "ablative": "convīvīs", "vocative": "convīvae"}
    },
    "parricīda": {
        "declension": "1st", "gender": "Masculine",
        "singular": {"nominative": "parricīda", "genitive": "parricīdae", "dative": "parricīdae", "accusative": "parricīdam", "ablative": "parricīdā", "vocative": "parricīda"},
        "plural": {"nominative": "parricīdae", "genitive": "parricīdārum", "dative": "parricīdīs", "accusative": "parricīdās", "ablative": "parricīdīs", "vocative": "parricīdae"}
    },

    # ==========================================
    # --- 2ND DECLENSION (10 Masc, 10 Neut) ---
    # ==========================================
    
    # 2nd Declension - Masculine (10)
    "servus": {
        "declension": "2nd", "gender": "Masculine",
        "singular": {"nominative": "servus", "genitive": "servī", "dative": "servō", "accusative": "servum", "ablative": "servō", "vocative": "serve"},
        "plural": {"nominative": "servī", "genitive": "servōrum", "dative": "servīs", "accusative": "servōs", "ablative": "servīs", "vocative": "servī"}
    },
    "amīcus": {
        "declension": "2nd", "gender": "Masculine",
        "singular": {"nominative": "amīcus", "genitive": "amīcī", "dative": "amīcō", "accusative": "amīcum", "ablative": "amīcō", "vocative": "amīce"},
        "plural": {"nominative": "amīcī", "genitive": "amīcōrum", "dative": "amīcīs", "accusative": "amīcōs", "ablative": "amīcīs", "vocative": "amīcī"}
    },
    "puer": {
        "declension": "2nd", "gender": "Masculine",
        "singular": {"nominative": "puer", "genitive": "puerī", "dative": "puerō", "accusative": "puerum", "ablative": "puerō", "vocative": "puer"},
        "plural": {"nominative": "puerī", "genitive": "puerōrum", "dative": "puerīs", "accusative": "puerōs", "ablative": "puerīs", "vocative": "puerī"}
    },
    "ager": {
        "declension": "2nd", "gender": "Masculine",
        "singular": {"nominative": "ager", "genitive": "agrī", "dative": "agrō", "accusative": "agrum", "ablative": "agrō", "vocative": "ager"},
        "plural": {"nominative": "agrī", "genitive": "agrōrum", "dative": "agrīs", "accusative": "agrōs", "ablative": "agrīs", "vocative": "agrī"}
    },
    "vir": {
        "declension": "2nd", "gender": "Masculine",
        "singular": {"nominative": "vir", "genitive": "virī", "dative": "virō", "accusative": "virum", "ablative": "virō", "vocative": "vir"},
        "plural": {"nominative": "virī", "genitive": "virōrum", "dative": "virīs", "accusative": "virōs", "ablative": "virīs", "vocative": "virī"}
    },
    "equus": {
        "declension": "2nd", "gender": "Masculine",
        "singular": {"nominative": "equus", "genitive": "equī", "dative": "equō", "accusative": "equum", "ablative": "equō", "vocative": "eque"},
        "plural": {"nominative": "equī", "genitive": "equōrum", "dative": "equīs", "accusative": "equōs", "ablative": "equīs", "vocative": "equī"}
    },
    "gladius": {
        "declension": "2nd", "gender": "Masculine",
        "singular": {"nominative": "gladius", "genitive": "gladiī", "dative": "gladiō", "accusative": "gladium", "ablative": "gladiō", "vocative": "gladie"},
        "plural": {"nominative": "gladiī", "genitive": "gladiōrum", "dative": "gladiīs", "accusative": "gladiōs", "ablative": "gladiīs", "vocative": "gladiī"}
    },
    "dominus": {
        "declension": "2nd", "gender": "Masculine",
        "singular": {"nominative": "dominus", "genitive": "dominī", "dative": "dominō", "accusative": "dominum", "ablative": "dominō", "vocative": "domine"},
        "plural": {"nominative": "dominī", "genitive": "dominōrum", "dative": "dominīs", "accusative": "dominōs", "ablative": "dominīs", "vocative": "dominī"}
    },
    "annus": {
        "declension": "2nd", "gender": "Masculine",
        "singular": {"nominative": "annus", "genitive": "annī", "dative": "annō", "accusative": "annum", "ablative": "annō", "vocative": "anne"},
        "plural": {"nominative": "annī", "genitive": "annōrum", "dative": "annīs", "accusative": "annōs", "ablative": "annīs", "vocative": "annī"}
    },
    "mūrus": {
        "declension": "2nd", "gender": "Masculine",
        "singular": {"nominative": "mūrus", "genitive": "mūrī", "dative": "mūrō", "accusative": "mūrum", "ablative": "mūrō", "vocative": "mūre"},
        "plural": {"nominative": "mūrī", "genitive": "mūrōrum", "dative": "mūrīs", "accusative": "mūrōs", "ablative": "mūrīs", "vocative": "mūrī"}
    },

    # 2nd Declension - Neuter (10)
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
    "verbum": {
        "declension": "2nd", "gender": "Neuter",
        "singular": {"nominative": "verbum", "genitive": "verbī", "dative": "verbō", "accusative": "verbum", "ablative": "verbō", "vocative": "verbum"},
        "plural": {"nominative": "verba", "genitive": "verbōrum", "dative": "verbīs", "accusative": "verba", "ablative": "verbīs", "vocative": "verba"}
    },
    "oppidum": {
        "declension": "2nd", "gender": "Neuter",
        "singular": {"nominative": "oppidum", "genitive": "oppidī", "dative": "oppidō", "accusative": "oppidum", "ablative": "oppidō", "vocative": "oppidum"},
        "plural": {"nominative": "oppida", "genitive": "oppidōrum", "dative": "oppidīs", "accusative": "oppida", "ablative": "oppidīs", "vocative": "oppida"}
    },
    "caelum": {
        "declension": "2nd", "gender": "Neuter",
        "singular": {"nominative": "caelum", "genitive": "caelī", "dative": "caelō", "accusative": "caelum", "ablative": "caelō", "vocative": "caelum"},
        "plural": {"nominative": "caela", "genitive": "caelōrum", "dative": "caelīs", "accusative": "caela", "ablative": "caelīs", "vocative": "caela"}
    },
    "templum": {
        "declension": "2nd", "gender": "Neuter",
        "singular": {"nominative": "templum", "genitive": "templī", "dative": "templō", "accusative": "templum", "ablative": "templō", "vocative": "templum"},
        "plural": {"nominative": "templa", "genitive": "templōrum", "dative": "templīs", "accusative": "templa", "ablative": "templīs", "vocative": "templa"}
    },
    "rēgnum": {
        "declension": "2nd", "gender": "Neuter",
        "singular": {"nominative": "rēgnum", "genitive": "rēgnī", "dative": "rēgnō", "accusative": "rēgnum", "ablative": "rēgnō", "vocative": "rēgnum"},
        "plural": {"nominative": "rēgna", "genitive": "rēgnōrum", "dative": "rēgnīs", "accusative": "rēgna", "ablative": "rēgnīs", "vocative": "rēgna"}
    },
    "perīculum": {
        "declension": "2nd", "gender": "Neuter",
        "singular": {"nominative": "perīculum", "genitive": "perīculī", "dative": "perīculō", "accusative": "perīculum", "ablative": "perīculō", "vocative": "perīculum"},
        "plural": {"nominative": "perīcula", "genitive": "perīculōrum", "dative": "perīculīs", "accusative": "perīcula", "ablative": "perīculīs", "vocative": "perīcula"}
    },
    "cōnsilium": {
        "declension": "2nd", "gender": "Neuter",
        "singular": {"nominative": "cōnsilium", "genitive": "cōnsiliī", "dative": "cōnsiliō", "accusative": "cōnsilium", "ablative": "cōnsiliō", "vocative": "cōnsilium"},
        "plural": {"nominative": "cōnsilia", "genitive": "cōnsiliōrum", "dative": "cōnsiliīs", "accusative": "cōnsilia", "ablative": "cōnsiliīs", "vocative": "cōnsilia"}
    },
    "saxum": {
        "declension": "2nd", "gender": "Neuter",
        "singular": {"nominative": "saxum", "genitive": "saxī", "dative": "saxō", "accusative": "saxum", "ablative": "saxō", "vocative": "saxum"},
        "plural": {"nominative": "saxa", "genitive": "saxōrum", "dative": "saxīs", "accusative": "saxa", "ablative": "saxīs", "vocative": "saxa"}
    },

    # ==========================================
    # --- 3RD DECLENSION (10 Masc, 10 Fem, 10 Neut) ---
    # ==========================================
    
    # 3rd Declension - Masculine (10)
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
    "frāter": {
        "declension": "3rd", "gender": "Masculine",
        "singular": {"nominative": "frāter", "genitive": "frātris", "dative": "frātrī", "accusative": "frātrem", "ablative": "frātre", "vocative": "frāter"},
        "plural": {"nominative": "frātrēs", "genitive": "frātrum", "dative": "frātribus", "accusative": "frātrēs", "ablative": "frātribus", "vocative": "frātrēs"}
    },
    "mīles": {
        "declension": "3rd", "gender": "Masculine",
        "singular": {"nominative": "mīles", "genitive": "mīlitis", "dative": "mīlitī", "accusative": "mīlitem", "ablative": "mīlite", "vocative": "mīles"},
        "plural": {"nominative": "mīlitēs", "genitive": "mīlitum", "dative": "mīlitibus", "accusative": "mīlitēs", "ablative": "mīlitibus", "vocative": "mīlitēs"}
    },
    "cōnsul": {
        "declension": "3rd", "gender": "Masculine",
        "singular": {"nominative": "cōnsul", "genitive": "cōnsulis", "dative": "cōnsulī", "accusative": "cōnsulem", "ablative": "cōnsule", "vocative": "cōnsul"},
        "plural": {"nominative": "cōnsulēs", "genitive": "cōnsulum", "dative": "cōnsulibus", "accusative": "cōnsulēs", "ablative": "cōnsulibus", "vocative": "cōnsulēs"}
    },
    "pēs": {
        "declension": "3rd", "gender": "Masculine",
        "singular": {"nominative": "pēs", "genitive": "pedis", "dative": "pedī", "accusative": "pedem", "ablative": "pede", "vocative": "pēs"},
        "plural": {"nominative": "pedēs", "genitive": "pedum", "dative": "pedibus", "accusative": "pedēs", "ablative": "pedibus", "vocative": "pedēs"}
    },
    "dux": {
        "declension": "3rd", "gender": "Masculine",
        "singular": {"nominative": "dux", "genitive": "ducis", "dative": "ducī", "accusative": "ducem", "ablative": "duce", "vocative": "dux"},
        "plural": {"nominative": "ducēs", "genitive": "ducum", "dative": "ducibus", "accusative": "ducēs", "ablative": "ducibus", "vocative": "ducēs"}
    },
    "comes": {
        "declension": "3rd", "gender": "Masculine",
        "singular": {"nominative": "comes", "genitive": "comitis", "dative": "comitī", "accusative": "comitem", "ablative": "comite", "vocative": "comes"},
        "plural": {"nominative": "comitēs", "genitive": "comitum", "dative": "comitibus", "accusative": "comitēs", "ablative": "comitibus", "vocative": "comitēs"}
    },
    "hospes": {
        "declension": "3rd", "gender": "Masculine",
        "singular": {"nominative": "hospes", "genitive": "hospitis", "dative": "hospitī", "accusative": "hospitem", "ablative": "hospite", "vocative": "hospes"},
        "plural": {"nominative": "hospitēs", "genitive": "hospitum", "dative": "hospitibus", "accusative": "hospitēs", "ablative": "hospitibus", "vocative": "hospitēs"}
    },
    "senex": {
        "declension": "3rd", "gender": "Masculine",
        "singular": {"nominative": "senex", "genitive": "senis", "dative": "senī", "accusative": "senem", "ablative": "sene", "vocative": "senex"},
        "plural": {"nominative": "senēs", "genitive": "senum", "dative": "senibus", "accusative": "senēs", "ablative": "senibus", "vocative": "senēs"}
    },

    # 3rd Declension - Feminine (10)
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
    "soror": {
        "declension": "3rd", "gender": "Feminine",
        "singular": {"nominative": "soror", "genitive": "sorōris", "dative": "sorōrī", "accusative": "sorōrem", "ablative": "sorōre", "vocative": "soror"},
        "plural": {"nominative": "sorōrēs", "genitive": "sorōrum", "dative": "sorōribus", "accusative": "sorōrēs", "ablative": "sorōribus", "vocative": "sorōrēs"}
    },
    "virtūs": {
        "declension": "3rd", "gender": "Feminine",
        "singular": {"nominative": "virtūs", "genitive": "virtūtis", "dative": "virtūtī", "accusative": "virtūtem", "ablative": "virtūte", "vocative": "virtūs"},
        "plural": {"nominative": "virtūtēs", "genitive": "virtūtum", "dative": "virtūtibus", "accusative": "virtūtēs", "ablative": "virtūtibus", "vocative": "virtūtēs"}
    },
    "vōx": {
        "declension": "3rd", "gender": "Feminine",
        "singular": {"nominative": "vōx", "genitive": "vōcis", "dative": "vōcī", "accusative": "vōcem", "ablative": "vōce", "vocative": "vōx"},
        "plural": {"nominative": "vōcēs", "genitive": "vōcum", "dative": "vōcibus", "accusative": "vōcēs", "ablative": "vōcibus", "vocative": "vōcēs"}
    },
    "pāx": {
        "declension": "3rd", "gender": "Feminine",
        "singular": {"nominative": "pāx", "genitive": "pācis", "dative": "pācī", "accusative": "pācem", "ablative": "pāce", "vocative": "pāx"},
        "plural": {"nominative": "pācēs", "genitive": "pācum", "dative": "pācibus", "accusative": "pācēs", "ablative": "pācibus", "vocative": "pācēs"}
    },
    "lūx": {
        "declension": "3rd", "gender": "Feminine",
        "singular": {"nominative": "lūx", "genitive": "lūcis", "dative": "lūcī", "accusative": "lūcem", "ablative": "lūce", "vocative": "lūx"},
        "plural": {"nominative": "lūcēs", "genitive": "lūcum", "dative": "lūcibus", "accusative": "lūcēs", "ablative": "lūcibus", "vocative": "lūcēs"}
    },
    "nātiō": {
        "declension": "3rd", "gender": "Feminine",
        "singular": {"nominative": "nātiō", "genitive": "nātiōnis", "dative": "nātiōnī", "accusative": "nātiōnem", "ablative": "nātiōne", "vocative": "nātiō"},
        "plural": {"nominative": "nātiōnēs", "genitive": "nātiōnum", "dative": "nātiōnibus", "accusative": "nātiōnēs", "ablative": "nātiōnibus", "vocative": "nātiōnēs"}
    },
    "cīvitās": {
        "declension": "3rd", "gender": "Feminine",
        "singular": {"nominative": "cīvitās", "genitive": "cīvitātis", "dative": "cīvitātī", "accusative": "cīvitātem", "ablative": "cīvitāte", "vocative": "cīvitās"},
        "plural": {"nominative": "cīvitātēs", "genitive": "cīvitātum", "dative": "cīvitātibus", "accusative": "cīvitātēs", "ablative": "cīvitātibus", "vocative": "cīvitātēs"}
    },
    "vēritās": {
        "declension": "3rd", "gender": "Feminine",
        "singular": {"nominative": "vēritās", "genitive": "vēritātis", "dative": "vēritātī", "accusative": "vēritātem", "ablative": "vēritāte", "vocative": "vēritās"},
        "plural": {"nominative": "vēritātēs", "genitive": "vēritātum", "dative": "vēritātibus", "accusative": "vēritātēs", "ablative": "vēritātibus", "vocative": "vēritātēs"}
    },

    # 3rd Declension - Neuter (10)
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
    "flūmen": {
        "declension": "3rd", "gender": "Neuter",
        "singular": {"nominative": "flūmen", "genitive": "flūminis", "dative": "flūminī", "accusative": "flūmen", "ablative": "flūmine", "vocative": "flūmen"},
        "plural": {"nominative": "flūmina", "genitive": "flūminum", "dative": "flūminibus", "accusative": "flūmina", "ablative": "flūminibus", "vocative": "flūmina"}
    },
    "tempus": {
        "declension": "3rd", "gender": "Neuter",
        "singular": {"nominative": "tempus", "genitive": "temporis", "dative": "temporī", "accusative": "tempus", "ablative": "tempore", "vocative": "tempus"},
        "plural": {"nominative": "tempora", "genitive": "temporum", "dative": "temporibus", "accusative": "tempora", "ablative": "temporibus", "vocative": "tempora"}
    },
    "iter": {
        "declension": "3rd", "gender": "Neuter",
        "singular": {"nominative": "iter", "genitive": "itineris", "dative": "itinerī", "accusative": "iter", "ablative": "itinere", "vocative": "iter"},
        "plural": {"nominative": "itinera", "genitive": "itinerum", "dative": "itineribus", "accusative": "itinera", "ablative": "itineribus", "vocative": "itinera"}
    },
    "caput": {
        "declension": "3rd", "gender": "Neuter",
        "singular": {"nominative": "caput", "genitive": "capitis", "dative": "capitī", "accusative": "caput", "ablative": "capite", "vocative": "caput"},
        "plural": {"nominative": "capita", "genitive": "capitum", "dative": "capitibus", "accusative": "capita", "ablative": "capitibus", "vocative": "capita"}
    },
    "iūs": {
        "declension": "3rd", "gender": "Neuter",
        "singular": {"nominative": "iūs", "genitive": "iūris", "dative": "iūrī", "accusative": "iūs", "ablative": "iūre", "vocative": "iūs"},
        "plural": {"nominative": "iūra", "genitive": "iūrum", "dative": "iūribus", "accusative": "iūra", "ablative": "iūribus", "vocative": "iūra"}
    },
    "vulnus": {
        "declension": "3rd", "gender": "Neuter",
        "singular": {"nominative": "vulnus", "genitive": "vulneris", "dative": "vulnerī", "accusative": "vulnus", "ablative": "vulnere", "vocative": "vulnus"},
        "plural": {"nominative": "vulnera", "genitive": "vulnerum", "dative": "vulneribus", "accusative": "vulnera", "ablative": "vulneribus", "vocative": "vulnera"}
    },
    "opus": {
        "declension": "3rd", "gender": "Neuter",
        "singular": {"nominative": "opus", "genitive": "operis", "dative": "operī", "accusative": "opus", "ablative": "opere", "vocative": "opus"},
        "plural": {"nominative": "opera", "genitive": "operum", "dative": "operibus", "accusative": "opera", "ablative": "operibus", "vocative": "opera"}
    },
    "ōmen": {
        "declension": "3rd", "gender": "Neuter",
        "singular": {"nominative": "ōmen", "genitive": "ōminis", "dative": "ōminī", "accusative": "ōmen", "ablative": "ōmine", "vocative": "ōmen"},
        "plural": {"nominative": "ōmina", "genitive": "ōminum", "dative": "ōminibus", "accusative": "ōmina", "ablative": "ōminibus", "vocative": "ōmina"}
    },

    # ==========================================
    # --- 4TH DECLENSION (10 Masc, 10 Fem, 4 Neut) ---
    # ==========================================
    
    # 4th Declension - Masculine (10)
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
    "senātus": {
        "declension": "4th", "gender": "Masculine",
        "singular": {"nominative": "senātus", "genitive": "senātūs", "dative": "senātuī", "accusative": "senātum", "ablative": "senātū", "vocative": "senātus"},
        "plural": {"nominative": "senātūs", "genitive": "senātuum", "dative": "senātibus", "accusative": "senātūs", "ablative": "senātibus", "vocative": "senātūs"}
    },
    "passus": {
        "declension": "4th", "gender": "Masculine",
        "singular": {"nominative": "passus", "genitive": "passūs", "dative": "passuī", "accusative": "passum", "ablative": "passū", "vocative": "passus"},
        "plural": {"nominative": "passūs", "genitive": "passuum", "dative": "passibus", "accusative": "passūs", "ablative": "passibus", "vocative": "passūs"}
    },
    "cāsus": {
        "declension": "4th", "gender": "Masculine",
        "singular": {"nominative": "cāsus", "genitive": "cāsūs", "dative": "cāsuī", "accusative": "cāsum", "ablative": "cāsū", "vocative": "cāsus"},
        "plural": {"nominative": "cāsūs", "genitive": "cāsuum", "dative": "cāsibus", "accusative": "cāsūs", "ablative": "cāsibus", "vocative": "cāsūs"}
    },
    "impetus": {
        "declension": "4th", "gender": "Masculine",
        "singular": {"nominative": "impetus", "genitive": "impetūs", "dative": "impetuī", "accusative": "impetum", "ablative": "impetū", "vocative": "impetus"},
        "plural": {"nominative": "impetūs", "genitive": "impetuum", "dative": "impetibus", "accusative": "impetūs", "ablative": "impetibus", "vocative": "impetūs"}
    },
    "gradus": {
        "declension": "4th", "gender": "Masculine",
        "singular": {"nominative": "gradus", "genitive": "gradūs", "dative": "graduī", "accusative": "gradum", "ablative": "gradū", "vocative": "gradus"},
        "plural": {"nominative": "gradūs", "genitive": "graduum", "dative": "gradibus", "accusative": "gradūs", "ablative": "gradibus", "vocative": "gradūs"}
    },
    "currus": {
        "declension": "4th", "gender": "Masculine",
        "singular": {"nominative": "currus", "genitive": "currūs", "dative": "curruī", "accusative": "currum", "ablative": "currū", "vocative": "currus"},
        "plural": {"nominative": "currūs", "genitive": "curruum", "dative": "curribus", "accusative": "currūs", "ablative": "curribus", "vocative": "currūs"}
    },
    "vultus": {
        "declension": "4th", "gender": "Masculine",
        "singular": {"nominative": "vultus", "genitive": "vultūs", "dative": "vultuī", "accusative": "vultum", "ablative": "vultū", "vocative": "vultus"},
        "plural": {"nominative": "vultūs", "genitive": "vultuum", "dative": "vultibus", "accusative": "vultūs", "ablative": "vultibus", "vocative": "vultūs"}
    },
    "mōtus": {
        "declension": "4th", "gender": "Masculine",
        "singular": {"nominative": "mōtus", "genitive": "mōtūs", "dative": "mōtuī", "accusative": "mōtum", "ablative": "mōtū", "vocative": "mōtus"},
        "plural": {"nominative": "mōtūs", "genitive": "mōtuum", "dative": "mōtibus", "accusative": "mōtūs", "ablative": "mōtibus", "vocative": "mōtūs"}
    },

    # 4th Declension - Feminine (10)
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
    "porticus": {
        "declension": "4th", "gender": "Feminine",
        "singular": {"nominative": "porticus", "genitive": "porticūs", "dative": "porticuī", "accusative": "porticum", "ablative": "porticū", "vocative": "porticus"},
        "plural": {"nominative": "porticūs", "genitive": "porticuum", "dative": "porticibus", "accusative": "porticūs", "ablative": "porticibus", "vocative": "porticūs"}
    },
    "tribus": {
        "declension": "4th", "gender": "Feminine",
        "singular": {"nominative": "tribus", "genitive": "tribūs", "dative": "tribuī", "accusative": "tribum", "ablative": "tribū", "vocative": "tribus"},
        "plural": {"nominative": "tribūs", "genitive": "tribuum", "dative": "tribubus", "accusative": "tribūs", "ablative": "tribubus", "vocative": "tribūs"}
    },
    "socrus": {
        "declension": "4th", "gender": "Feminine",
        "singular": {"nominative": "socrus", "genitive": "socrūs", "dative": "socruī", "accusative": "socrum", "ablative": "socrū", "vocative": "socrus"},
        "plural": {"nominative": "socrūs", "genitive": "socruum", "dative": "socribus", "accusative": "socrūs", "ablative": "socribus", "vocative": "socrūs"}
    },
    "nurus": {
        "declension": "4th", "gender": "Feminine",
        "singular": {"nominative": "nurus", "genitive": "nurūs", "dative": "nuruī", "accusative": "nurum", "ablative": "nurū", "vocative": "nurus"},
        "plural": {"nominative": "nurūs", "genitive": "nuruum", "dative": "nuribus", "accusative": "nurūs", "ablative": "nuribus", "vocative": "nurūs"}
    },
    "ānus": {
        "declension": "4th", "gender": "Feminine",
        "singular": {"nominative": "ānus", "genitive": "ānūs", "dative": "ānuī", "accusative": "ānum", "ablative": "ānū", "vocative": "ānus"},
        "plural": {"nominative": "ānūs", "genitive": "ānuum", "dative": "ānibus", "accusative": "ānūs", "ablative": "ānibus", "vocative": "ānūs"}
    },
    "quercus": {
        "declension": "4th", "gender": "Feminine",
        "singular": {"nominative": "quercus", "genitive": "quercūs", "dative": "quercuī", "accusative": "quercum", "ablative": "quercū", "vocative": "quercus"},
        "plural": {"nominative": "quercūs", "genitive": "quercuum", "dative": "quercibus", "accusative": "quercūs", "ablative": "quercibus", "vocative": "quercūs"}
    },
    "fīcus": {
        "declension": "4th", "gender": "Feminine",
        "singular": {"nominative": "fīcus", "genitive": "fīcūs", "dative": "fīcuī", "accusative": "fīcum", "ablative": "fīcū", "vocative": "fīcus"},
        "plural": {"nominative": "fīcūs", "genitive": "fīcuum", "dative": "fīcibus", "accusative": "fīcūs", "ablative": "fīcibus", "vocative": "fīcūs"}
    },
    "pīnus": {
        "declension": "4th", "gender": "Feminine",
        "singular": {"nominative": "pīnus", "genitive": "pīnūs", "dative": "pīnuī", "accusative": "pīnum", "ablative": "pīnū", "vocative": "pīnus"},
        "plural": {"nominative": "pīnūs", "genitive": "pīnuum", "dative": "pīnibus", "accusative": "pīnūs", "ablative": "pīnibus", "vocative": "pīnūs"}
    },

    # 4th Declension - Neuter (ALL 4 THAT EXIST)
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
    "verū": {
        "declension": "4th", "gender": "Neuter",
        "singular": {"nominative": "verū", "genitive": "verūs", "dative": "verū", "accusative": "verū", "ablative": "verū", "vocative": "verū"},
        "plural": {"nominative": "verua", "genitive": "veruum", "dative": "veribus", "accusative": "verua", "ablative": "veribus", "vocative": "verua"}
    },
    "pecū": {
        "declension": "4th", "gender": "Neuter",
        "singular": {"nominative": "pecū", "genitive": "pecūs", "dative": "pecū", "accusative": "pecū", "ablative": "pecū", "vocative": "pecū"},
        "plural": {"nominative": "pecua", "genitive": "pecuum", "dative": "pecubus", "accusative": "pecua", "ablative": "pecubus", "vocative": "pecua"}
    },

    # ==========================================
    # --- 5TH DECLENSION (10 Fem, 2 Masc) ---
    # ==========================================
    
    # 5th Declension - Feminine (10)
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
    "aciēs": {
        "declension": "5th", "gender": "Feminine",
        "singular": {"nominative": "aciēs", "genitive": "aciēī", "dative": "aciēī", "accusative": "aciem", "ablative": "aciē", "vocative": "aciēs"},
        "plural": {"nominative": "aciēs", "genitive": "aciērum", "dative": "aciēbus", "accusative": "aciēs", "ablative": "aciēbus", "vocative": "aciēs"}
    },
    "faciēs": {
        "declension": "5th", "gender": "Feminine",
        "singular": {"nominative": "faciēs", "genitive": "faciēī", "dative": "faciēī", "accusative": "faciem", "ablative": "faciē", "vocative": "faciēs"},
        "plural": {"nominative": "faciēs", "genitive": "faciērum", "dative": "faciēbus", "accusative": "faciēs", "ablative": "faciēbus", "vocative": "faciēs"}
    },
    "fidēs": {
        "declension": "5th", "gender": "Feminine",
        "singular": {"nominative": "fidēs", "genitive": "fideī", "dative": "fideī", "accusative": "fidem", "ablative": "fidē", "vocative": "fidēs"},
        "plural": {"nominative": "fidēs", "genitive": "fidērum", "dative": "fidēbus", "accusative": "fidēs", "ablative": "fidēbus", "vocative": "fidēs"}
    },
    "speciēs": {
        "declension": "5th", "gender": "Feminine",
        "singular": {"nominative": "speciēs", "genitive": "speciēī", "dative": "speciēī", "accusative": "speciem", "ablative": "speciē", "vocative": "speciēs"},
        "plural": {"nominative": "speciēs", "genitive": "speciērum", "dative": "speciēbus", "accusative": "speciēs", "ablative": "speciēbus", "vocative": "speciēs"}
    },
    "perniciēs": {
        "declension": "5th", "gender": "Feminine",
        "singular": {"nominative": "perniciēs", "genitive": "perniciēī", "dative": "perniciēī", "accusative": "perniciem", "ablative": "perniciē", "vocative": "perniciēs"},
        "plural": {"nominative": "perniciēs", "genitive": "perniciērum", "dative": "perniciēbus", "accusative": "perniciēs", "ablative": "perniciēbus", "vocative": "perniciēs"}
    },
    "glaciēs": {
        "declension": "5th", "gender": "Feminine",
        "singular": {"nominative": "glaciēs", "genitive": "glaciēī", "dative": "glaciēī", "accusative": "glaciem", "ablative": "glaciē", "vocative": "glaciēs"},
        "plural": {"nominative": "glaciēs", "genitive": "glaciērum", "dative": "glaciēbus", "accusative": "glaciēs", "ablative": "glaciēbus", "vocative": "glaciēs"}
    },
    "effigiēs": {
        "declension": "5th", "gender": "Feminine",
        "singular": {"nominative": "effigiēs", "genitive": "effigiēī", "dative": "effigiēī", "accusative": "effigiem", "ablative": "effigiē", "vocative": "effigiēs"},
        "plural": {"nominative": "effigiēs", "genitive": "effigiērum", "dative": "effigiēbus", "accusative": "effigiēs", "ablative": "effigiēbus", "vocative": "effigiēs"}
    },
    "seriēs": {
        "declension": "5th", "gender": "Feminine",
        "singular": {"nominative": "seriēs", "genitive": "seriēī", "dative": "seriēī", "accusative": "seriem", "ablative": "seriē", "vocative": "seriēs"},
        "plural": {"nominative": "seriēs", "genitive": "seriērum", "dative": "seriēbus", "accusative": "seriēs", "ablative": "seriēbus", "vocative": "seriēs"}
    },

    # 5th Declension - Masculine (ALL 2 THAT EXIST)
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
