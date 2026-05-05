import streamlit as st
import random

# --- DATA ---
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
verbs_db = {
    # === 1ST CONJUGATION ===
    "amāre": {
        "indicative": {
            "present": {"active": {"singular": {1: "amō", 2: "amās", 3: "amat"}, "plural": {1: "amāmus", 2: "amātis", 3: "amant"}}, "passive": {"singular": {1: "amor", 2: "amāris", 3: "amātur"}, "plural": {1: "amāmur", 2: "amāminī", 3: "amantur"}}},
            "imperfect": {"active": {"singular": {1: "amābam", 2: "amābās", 3: "amābat"}, "plural": {1: "amābāmus", 2: "amābātis", 3: "amābant"}}, "passive": {"singular": {1: "amābar", 2: "amābāris", 3: "amābātur"}, "plural": {1: "amābāmur", 2: "amābāminī", 3: "amābantur"}}},
            "future": {"active": {"singular": {1: "amābō", 2: "amābis", 3: "amābit"}, "plural": {1: "amābimus", 2: "amābitis", 3: "amābunt"}}, "passive": {"singular": {1: "amābor", 2: "amāberis", 3: "amābitur"}, "plural": {1: "amābimur", 2: "amābiminī", 3: "amābuntur"}}},
            "perfect": {"active": {"singular": {1: "amāvī", 2: "amāvistī", 3: "amāvit"}, "plural": {1: "amāvimus", 2: "amāvistis", 3: "amāvērunt"}}, "passive": {"singular": {1: "amātus sum", 2: "amātus es", 3: "amātus est"}, "plural": {1: "amātī sumus", 2: "amātī estis", 3: "amātī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "amāveram", 2: "amāverās", 3: "amāverat"}, "plural": {1: "amāverāmus", 2: "amāverātis", 3: "amāverant"}}, "passive": {"singular": {1: "amātus eram", 2: "amātus erās", 3: "amātus erat"}, "plural": {1: "amātī erāmus", 2: "amātī erātis", 3: "amātī erant"}}},
            "future perfect": {"active": {"singular": {1: "amāverō", 2: "amāveris", 3: "amāverit"}, "plural": {1: "amāverimus", 2: "amāveritis", 3: "amāverint"}}, "passive": {"singular": {1: "amātus erō", 2: "amātus eris", 3: "amātus erit"}, "plural": {1: "amātī erimus", 2: "amātī eritis", 3: "amātī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "amā"}, "plural": {2: "amāte"}}, "passive": {"singular": {2: "amāre"}, "plural": {2: "amāminī"}}},
            "future": {"active": {"singular": {2: "amātō", 3: "amātō"}, "plural": {2: "amātōte", 3: "amantō"}}, "passive": {"singular": {2: "amātor", 3: "amātor"}, "plural": {3: "amantor"}}}
        },
        "infinitives": {"present active": "amāre", "present passive": "amārī", "perfect active": "amāvisse", "perfect passive": "amātus esse", "future active": "amātūrus esse", "future passive": "amātum īrī"}
    },
    "laudāre": {
        "indicative": {
            "present": {"active": {"singular": {1: "laudō", 2: "laudās", 3: "laudat"}, "plural": {1: "laudāmus", 2: "laudātis", 3: "laudant"}}, "passive": {"singular": {1: "laudor", 2: "laudāris", 3: "laudātur"}, "plural": {1: "laudāmur", 2: "laudāminī", 3: "laudantur"}}},
            "imperfect": {"active": {"singular": {1: "laudābam", 2: "laudābās", 3: "laudābat"}, "plural": {1: "laudābāmus", 2: "laudābātis", 3: "laudābant"}}, "passive": {"singular": {1: "laudābar", 2: "laudābāris", 3: "laudābātur"}, "plural": {1: "laudābāmur", 2: "laudābāminī", 3: "laudābantur"}}},
            "future": {"active": {"singular": {1: "laudābō", 2: "laudābis", 3: "laudābit"}, "plural": {1: "laudābimus", 2: "laudābitis", 3: "laudābunt"}}, "passive": {"singular": {1: "laudābor", 2: "laudāberis", 3: "laudābitur"}, "plural": {1: "laudābimur", 2: "laudābiminī", 3: "laudābuntur"}}},
            "perfect": {"active": {"singular": {1: "laudāvī", 2: "laudāvistī", 3: "laudāvit"}, "plural": {1: "laudāvimus", 2: "laudāvistis", 3: "laudāvērunt"}}, "passive": {"singular": {1: "laudātus sum", 2: "laudātus es", 3: "laudātus est"}, "plural": {1: "laudātī sumus", 2: "laudātī estis", 3: "laudātī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "laudāveram", 2: "laudāverās", 3: "laudāverat"}, "plural": {1: "laudāverāmus", 2: "laudāverātis", 3: "laudāverant"}}, "passive": {"singular": {1: "laudātus eram", 2: "laudātus erās", 3: "laudātus erat"}, "plural": {1: "laudātī erāmus", 2: "laudātī erātis", 3: "laudātī erant"}}},
            "future perfect": {"active": {"singular": {1: "laudāverō", 2: "laudāveris", 3: "laudāverit"}, "plural": {1: "laudāverimus", 2: "laudāveritis", 3: "laudāverint"}}, "passive": {"singular": {1: "laudātus erō", 2: "laudātus eris", 3: "laudātus erit"}, "plural": {1: "laudātī erimus", 2: "laudātī eritis", 3: "laudātī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "laudā"}, "plural": {2: "laudāte"}}, "passive": {"singular": {2: "laudāre"}, "plural": {2: "laudāminī"}}},
            "future": {"active": {"singular": {2: "laudātō", 3: "laudātō"}, "plural": {2: "laudātōte", 3: "laudantō"}}, "passive": {"singular": {2: "laudātor", 3: "laudātor"}, "plural": {3: "laudantor"}}}
        },
        "infinitives": {"present active": "laudāre", "present passive": "laudārī", "perfect active": "laudāvisse", "perfect passive": "laudātus esse", "future active": "laudātūrus esse", "future passive": "laudātum īrī"}
    },
    "vocāre": {
        "indicative": {
            "present": {"active": {"singular": {1: "vocō", 2: "vocās", 3: "vocat"}, "plural": {1: "vocāmus", 2: "vocātis", 3: "vocant"}}, "passive": {"singular": {1: "vocor", 2: "vocāris", 3: "vocātur"}, "plural": {1: "vocāmur", 2: "vocāminī", 3: "vocantur"}}},
            "imperfect": {"active": {"singular": {1: "vocābam", 2: "vocābās", 3: "vocābat"}, "plural": {1: "vocābāmus", 2: "vocābātis", 3: "vocābant"}}, "passive": {"singular": {1: "vocābar", 2: "vocābāris", 3: "vocābātur"}, "plural": {1: "vocābāmur", 2: "vocābāminī", 3: "vocābantur"}}},
            "future": {"active": {"singular": {1: "vocābō", 2: "vocābis", 3: "vocābit"}, "plural": {1: "vocābimus", 2: "vocābitis", 3: "vocābunt"}}, "passive": {"singular": {1: "vocābor", 2: "vocāberis", 3: "vocābitur"}, "plural": {1: "vocābimur", 2: "vocābiminī", 3: "vocābuntur"}}},
            "perfect": {"active": {"singular": {1: "vocāvī", 2: "vocāvistī", 3: "vocāvit"}, "plural": {1: "vocāvimus", 2: "vocāvistis", 3: "vocāvērunt"}}, "passive": {"singular": {1: "vocātus sum", 2: "vocātus es", 3: "vocātus est"}, "plural": {1: "vocātī sumus", 2: "vocātī estis", 3: "vocātī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "vocāveram", 2: "vocāverās", 3: "vocāverat"}, "plural": {1: "vocāverāmus", 2: "vocāverātis", 3: "vocāverant"}}, "passive": {"singular": {1: "vocātus eram", 2: "vocātus erās", 3: "vocātus erat"}, "plural": {1: "vocātī erāmus", 2: "vocātī erātis", 3: "vocātī erant"}}},
            "future perfect": {"active": {"singular": {1: "vocāverō", 2: "vocāveris", 3: "vocāverit"}, "plural": {1: "vocāverimus", 2: "vocāveritis", 3: "vocāverint"}}, "passive": {"singular": {1: "vocātus erō", 2: "vocātus eris", 3: "vocātus erit"}, "plural": {1: "vocātī erimus", 2: "vocātī eritis", 3: "vocātī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "vocā"}, "plural": {2: "vocāte"}}, "passive": {"singular": {2: "vocāre"}, "plural": {2: "vocāminī"}}},
            "future": {"active": {"singular": {2: "vocātō", 3: "vocātō"}, "plural": {2: "vocātōte", 3: "vocantō"}}, "passive": {"singular": {2: "vocātor", 3: "vocātor"}, "plural": {3: "vocantor"}}}
        },
        "infinitives": {"present active": "vocāre", "present passive": "vocārī", "perfect active": "vocāvisse", "perfect passive": "vocātus esse", "future active": "vocātūrus esse", "future passive": "vocātum īrī"}
    },
    "portāre": {
        "indicative": {
            "present": {"active": {"singular": {1: "portō", 2: "portās", 3: "portat"}, "plural": {1: "portāmus", 2: "portātis", 3: "portant"}}, "passive": {"singular": {1: "portor", 2: "portāris", 3: "portātur"}, "plural": {1: "portāmur", 2: "portāminī", 3: "portantur"}}},
            "imperfect": {"active": {"singular": {1: "portābam", 2: "portābās", 3: "portābat"}, "plural": {1: "portābāmus", 2: "portābātis", 3: "portābant"}}, "passive": {"singular": {1: "portābar", 2: "portābāris", 3: "portābātur"}, "plural": {1: "portābāmur", 2: "portābāminī", 3: "portābantur"}}},
            "future": {"active": {"singular": {1: "portābō", 2: "portābis", 3: "portābit"}, "plural": {1: "portābimus", 2: "portābitis", 3: "portābunt"}}, "passive": {"singular": {1: "portābor", 2: "portāberis", 3: "portābitur"}, "plural": {1: "portābimur", 2: "portābiminī", 3: "portābuntur"}}},
            "perfect": {"active": {"singular": {1: "portāvī", 2: "portāvistī", 3: "portāvit"}, "plural": {1: "portāvimus", 2: "portāvistis", 3: "portāvērunt"}}, "passive": {"singular": {1: "portātus sum", 2: "portātus es", 3: "portātus est"}, "plural": {1: "portātī sumus", 2: "portātī estis", 3: "portātī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "portāveram", 2: "portāverās", 3: "portāverat"}, "plural": {1: "portāverāmus", 2: "portāverātis", 3: "portāverant"}}, "passive": {"singular": {1: "portātus eram", 2: "portātus erās", 3: "portātus erat"}, "plural": {1: "portātī erāmus", 2: "portātī erātis", 3: "portātī erant"}}},
            "future perfect": {"active": {"singular": {1: "portāverō", 2: "portāveris", 3: "portāverit"}, "plural": {1: "portāverimus", 2: "portāveritis", 3: "portāverint"}}, "passive": {"singular": {1: "portātus erō", 2: "portātus eris", 3: "portātus erit"}, "plural": {1: "portātī erimus", 2: "portātī eritis", 3: "portātī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "portā"}, "plural": {2: "portāte"}}, "passive": {"singular": {2: "portāre"}, "plural": {2: "portāminī"}}},
            "future": {"active": {"singular": {2: "portātō", 3: "portātō"}, "plural": {2: "portātōte", 3: "portantō"}}, "passive": {"singular": {2: "portātor", 3: "portātor"}, "plural": {3: "portantor"}}}
        },
        "infinitives": {"present active": "portāre", "present passive": "portārī", "perfect active": "portāvisse", "perfect passive": "portātus esse", "future active": "portātūrus esse", "future passive": "portātum īrī"}
    },
    "parāre": {
        "indicative": {
            "present": {"active": {"singular": {1: "parō", 2: "parās", 3: "parat"}, "plural": {1: "parāmus", 2: "parātis", 3: "parant"}}, "passive": {"singular": {1: "paror", 2: "parāris", 3: "parātur"}, "plural": {1: "parāmur", 2: "parāminī", 3: "parantur"}}},
            "imperfect": {"active": {"singular": {1: "parābam", 2: "parābās", 3: "parābat"}, "plural": {1: "parābāmus", 2: "parābātis", 3: "parābant"}}, "passive": {"singular": {1: "parābar", 2: "parābāris", 3: "parābātur"}, "plural": {1: "parābāmur", 2: "parābāminī", 3: "parābantur"}}},
            "future": {"active": {"singular": {1: "parābō", 2: "parābis", 3: "parābit"}, "plural": {1: "parābimus", 2: "parābitis", 3: "parābunt"}}, "passive": {"singular": {1: "parābor", 2: "parāberis", 3: "parābitur"}, "plural": {1: "parābimur", 2: "parābiminī", 3: "parābuntur"}}},
            "perfect": {"active": {"singular": {1: "parāvī", 2: "parāvistī", 3: "parāvit"}, "plural": {1: "parāvimus", 2: "parāvistis", 3: "parāvērunt"}}, "passive": {"singular": {1: "parātus sum", 2: "parātus es", 3: "parātus est"}, "plural": {1: "parātī sumus", 2: "parātī estis", 3: "parātī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "parāveram", 2: "parāverās", 3: "parāverat"}, "plural": {1: "parāverāmus", 2: "parāverātis", 3: "parāverant"}}, "passive": {"singular": {1: "parātus eram", 2: "parātus erās", 3: "parātus erat"}, "plural": {1: "parātī erāmus", 2: "parātī erātis", 3: "parātī erant"}}},
            "future perfect": {"active": {"singular": {1: "parāverō", 2: "parāveris", 3: "parāverit"}, "plural": {1: "parāverimus", 2: "parāveritis", 3: "parāverint"}}, "passive": {"singular": {1: "parātus erō", 2: "parātus eris", 3: "parātus erit"}, "plural": {1: "parātī erimus", 2: "parātī eritis", 3: "parātī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "parā"}, "plural": {2: "parāte"}}, "passive": {"singular": {2: "parāre"}, "plural": {2: "parāminī"}}},
            "future": {"active": {"singular": {2: "parātō", 3: "parātō"}, "plural": {2: "parātōte", 3: "parantō"}}, "passive": {"singular": {2: "parātor", 3: "parātor"}, "plural": {3: "parantor"}}}
        },
        "infinitives": {"present active": "parāre", "present passive": "parārī", "perfect active": "parāvisse", "perfect passive": "parātus esse", "future active": "parātūrus esse", "future passive": "parātum īrī"}
    },
    "spectāre": {
        "indicative": {
            "present": {"active": {"singular": {1: "spectō", 2: "spectās", 3: "spectat"}, "plural": {1: "spectāmus", 2: "spectātis", 3: "spectant"}}, "passive": {"singular": {1: "spector", 2: "spectāris", 3: "spectātur"}, "plural": {1: "spectāmur", 2: "spectāminī", 3: "spectantur"}}},
            "imperfect": {"active": {"singular": {1: "spectābam", 2: "spectābās", 3: "spectābat"}, "plural": {1: "spectābāmus", 2: "spectābātis", 3: "spectābant"}}, "passive": {"singular": {1: "spectābar", 2: "spectābāris", 3: "spectābātur"}, "plural": {1: "spectābāmur", 2: "spectābāminī", 3: "spectābantur"}}},
            "future": {"active": {"singular": {1: "spectābō", 2: "spectābis", 3: "spectābit"}, "plural": {1: "spectābimus", 2: "spectābitis", 3: "spectābunt"}}, "passive": {"singular": {1: "spectābor", 2: "spectāberis", 3: "spectābitur"}, "plural": {1: "spectābimur", 2: "spectābiminī", 3: "spectābuntur"}}},
            "perfect": {"active": {"singular": {1: "spectāvī", 2: "spectāvistī", 3: "spectāvit"}, "plural": {1: "spectāvimus", 2: "spectāvistis", 3: "spectāvērunt"}}, "passive": {"singular": {1: "spectātus sum", 2: "spectātus es", 3: "spectātus est"}, "plural": {1: "spectātī sumus", 2: "spectātī estis", 3: "spectātī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "spectāveram", 2: "spectāverās", 3: "spectāverat"}, "plural": {1: "spectāverāmus", 2: "spectāverātis", 3: "spectāverant"}}, "passive": {"singular": {1: "spectātus eram", 2: "spectātus erās", 3: "spectātus erat"}, "plural": {1: "spectātī erāmus", 2: "spectātī erātis", 3: "spectātī erant"}}},
            "future perfect": {"active": {"singular": {1: "spectāverō", 2: "spectāveris", 3: "spectāverit"}, "plural": {1: "spectāverimus", 2: "spectāveritis", 3: "spectāverint"}}, "passive": {"singular": {1: "spectātus erō", 2: "spectātus eris", 3: "spectātus erit"}, "plural": {1: "spectātī erimus", 2: "spectātī eritis", 3: "spectātī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "spectā"}, "plural": {2: "spectāte"}}, "passive": {"singular": {2: "spectāre"}, "plural": {2: "spectāminī"}}},
            "future": {"active": {"singular": {2: "spectātō", 3: "spectātō"}, "plural": {2: "spectātōte", 3: "spectantō"}}, "passive": {"singular": {2: "spectātor", 3: "spectātor"}, "plural": {3: "spectantor"}}}
        },
        "infinitives": {"present active": "spectāre", "present passive": "spectārī", "perfect active": "spectāvisse", "perfect passive": "spectātus esse", "future active": "spectātūrus esse", "future passive": "spectātum īrī"}
    },
    "superāre": {
        "indicative": {
            "present": {"active": {"singular": {1: "superō", 2: "superās", 3: "superat"}, "plural": {1: "superāmus", 2: "superātis", 3: "superant"}}, "passive": {"singular": {1: "superor", 2: "superāris", 3: "superātur"}, "plural": {1: "superāmur", 2: "superāminī", 3: "superantur"}}},
            "imperfect": {"active": {"singular": {1: "superābam", 2: "superābās", 3: "superābat"}, "plural": {1: "superābāmus", 2: "superābātis", 3: "superābant"}}, "passive": {"singular": {1: "superābar", 2: "superābāris", 3: "superābātur"}, "plural": {1: "superābāmur", 2: "superābāminī", 3: "superābantur"}}},
            "future": {"active": {"singular": {1: "superābō", 2: "superābis", 3: "superābit"}, "plural": {1: "superābimus", 2: "superābitis", 3: "superābunt"}}, "passive": {"singular": {1: "superābor", 2: "superāberis", 3: "superābitur"}, "plural": {1: "superābimur", 2: "superābiminī", 3: "superābuntur"}}},
            "perfect": {"active": {"singular": {1: "superāvī", 2: "superāvistī", 3: "superāvit"}, "plural": {1: "superāvimus", 2: "superāvistis", 3: "superāvērunt"}}, "passive": {"singular": {1: "superātus sum", 2: "superātus es", 3: "superātus est"}, "plural": {1: "superātī sumus", 2: "superātī estis", 3: "superātī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "superāveram", 2: "superāverās", 3: "superāverat"}, "plural": {1: "superāverāmus", 2: "superāverātis", 3: "superāverant"}}, "passive": {"singular": {1: "superātus eram", 2: "superātus erās", 3: "superātus erat"}, "plural": {1: "superātī erāmus", 2: "superātī erātis", 3: "superātī erant"}}},
            "future perfect": {"active": {"singular": {1: "superāverō", 2: "superāveris", 3: "superāverit"}, "plural": {1: "superāverimus", 2: "superāveritis", 3: "superāverint"}}, "passive": {"singular": {1: "superātus erō", 2: "superātus eris", 3: "superātus erit"}, "plural": {1: "superātī erimus", 2: "superātī eritis", 3: "superātī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "superā"}, "plural": {2: "superāte"}}, "passive": {"singular": {2: "superāre"}, "plural": {2: "superāminī"}}},
            "future": {"active": {"singular": {2: "superātō", 3: "superātō"}, "plural": {2: "superātōte", 3: "superantō"}}, "passive": {"singular": {2: "superātor", 3: "superātor"}, "plural": {3: "superantor"}}}
        },
        "infinitives": {"present active": "superāre", "present passive": "superārī", "perfect active": "superāvisse", "perfect passive": "superātus esse", "future active": "superātūrus esse", "future passive": "superātum īrī"}
    },
    "vulnerāre": {
        "indicative": {
            "present": {"active": {"singular": {1: "vulnerō", 2: "vulnerās", 3: "vulnerat"}, "plural": {1: "vulnerāmus", 2: "vulnerātis", 3: "vulnerant"}}, "passive": {"singular": {1: "vulneror", 2: "vulnerāris", 3: "vulnerātur"}, "plural": {1: "vulnerāmur", 2: "vulnerāminī", 3: "vulnerantur"}}},
            "imperfect": {"active": {"singular": {1: "vulnerābam", 2: "vulnerābās", 3: "vulnerābat"}, "plural": {1: "vulnerābāmus", 2: "vulnerābātis", 3: "vulnerābant"}}, "passive": {"singular": {1: "vulnerābar", 2: "vulnerābāris", 3: "vulnerābātur"}, "plural": {1: "vulnerābāmur", 2: "vulnerābāminī", 3: "vulnerābantur"}}},
            "future": {"active": {"singular": {1: "vulnerābō", 2: "vulnerābis", 3: "vulnerābit"}, "plural": {1: "vulnerābimus", 2: "vulnerābitis", 3: "vulnerābunt"}}, "passive": {"singular": {1: "vulnerābor", 2: "vulnerāberis", 3: "vulnerābitur"}, "plural": {1: "vulnerābimur", 2: "vulnerābiminī", 3: "vulnerābuntur"}}},
            "perfect": {"active": {"singular": {1: "vulnerāvī", 2: "vulnerāvistī", 3: "vulnerāvit"}, "plural": {1: "vulnerāvimus", 2: "vulnerāvistis", 3: "vulnerāvērunt"}}, "passive": {"singular": {1: "vulnerātus sum", 2: "vulnerātus es", 3: "vulnerātus est"}, "plural": {1: "vulnerātī sumus", 2: "vulnerātī estis", 3: "vulnerātī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "vulnerāveram", 2: "vulnerāverās", 3: "vulnerāverat"}, "plural": {1: "vulnerāverāmus", 2: "vulnerāverātis", 3: "vulnerāverant"}}, "passive": {"singular": {1: "vulnerātus eram", 2: "vulnerātus erās", 3: "vulnerātus erat"}, "plural": {1: "vulnerātī erāmus", 2: "vulnerātī erātis", 3: "vulnerātī erant"}}},
            "future perfect": {"active": {"singular": {1: "vulnerāverō", 2: "vulnerāveris", 3: "vulnerāverit"}, "plural": {1: "vulnerāverimus", 2: "vulnerāveritis", 3: "vulnerāverint"}}, "passive": {"singular": {1: "vulnerātus erō", 2: "vulnerātus eris", 3: "vulnerātus erit"}, "plural": {1: "vulnerātī erimus", 2: "vulnerātī eritis", 3: "vulnerātī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "vulnerā"}, "plural": {2: "vulnerāte"}}, "passive": {"singular": {2: "vulnerāre"}, "plural": {2: "vulnerāminī"}}},
            "future": {"active": {"singular": {2: "vulnerātō", 3: "vulnerātō"}, "plural": {2: "vulnerātōte", 3: "vulnerantō"}}, "passive": {"singular": {2: "vulnerātor", 3: "vulnerātor"}, "plural": {3: "vulnerantor"}}}
        },
        "infinitives": {"present active": "vulnerāre", "present passive": "vulnerārī", "perfect active": "vulnerāvisse", "perfect passive": "vulnerātus esse", "future active": "vulnerātūrus esse", "future passive": "vulnerātum īrī"}
    },
    "oppugnāre": {
        "indicative": {
            "present": {"active": {"singular": {1: "oppugnō", 2: "oppugnās", 3: "oppugnat"}, "plural": {1: "oppugnāmus", 2: "oppugnātis", 3: "oppugnant"}}, "passive": {"singular": {1: "oppugnor", 2: "oppugnāris", 3: "oppugnātur"}, "plural": {1: "oppugnāmur", 2: "oppugnāminī", 3: "oppugnantur"}}},
            "imperfect": {"active": {"singular": {1: "oppugnābam", 2: "oppugnābās", 3: "oppugnābat"}, "plural": {1: "oppugnābāmus", 2: "oppugnābātis", 3: "oppugnābant"}}, "passive": {"singular": {1: "oppugnābar", 2: "oppugnābāris", 3: "oppugnābātur"}, "plural": {1: "oppugnābāmur", 2: "oppugnābāminī", 3: "oppugnābantur"}}},
            "future": {"active": {"singular": {1: "oppugnābō", 2: "oppugnābis", 3: "oppugnābit"}, "plural": {1: "oppugnābimus", 2: "oppugnābitis", 3: "oppugnābunt"}}, "passive": {"singular": {1: "oppugnābor", 2: "oppugnāberis", 3: "oppugnābitur"}, "plural": {1: "oppugnābimur", 2: "oppugnābiminī", 3: "oppugnābuntur"}}},
            "perfect": {"active": {"singular": {1: "oppugnāvī", 2: "oppugnāvistī", 3: "oppugnāvit"}, "plural": {1: "oppugnāvimus", 2: "oppugnāvistis", 3: "oppugnāvērunt"}}, "passive": {"singular": {1: "oppugnātus sum", 2: "oppugnātus es", 3: "oppugnātus est"}, "plural": {1: "oppugnātī sumus", 2: "oppugnātī estis", 3: "oppugnātī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "oppugnāveram", 2: "oppugnāverās", 3: "oppugnāverat"}, "plural": {1: "oppugnāverāmus", 2: "oppugnāverātis", 3: "oppugnāverant"}}, "passive": {"singular": {1: "oppugnātus eram", 2: "oppugnātus erās", 3: "oppugnātus erat"}, "plural": {1: "oppugnātī erāmus", 2: "oppugnātī erātis", 3: "oppugnātī erant"}}},
            "future perfect": {"active": {"singular": {1: "oppugnāverō", 2: "oppugnāveris", 3: "oppugnāverit"}, "plural": {1: "oppugnāverimus", 2: "oppugnāveritis", 3: "oppugnāverint"}}, "passive": {"singular": {1: "oppugnātus erō", 2: "oppugnātus eris", 3: "oppugnātus erit"}, "plural": {1: "oppugnātī erimus", 2: "oppugnātī eritis", 3: "oppugnātī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "oppugnā"}, "plural": {2: "oppugnāte"}}, "passive": {"singular": {2: "oppugnāre"}, "plural": {2: "oppugnāminī"}}},
            "future": {"active": {"singular": {2: "oppugnātō", 3: "oppugnātō"}, "plural": {2: "oppugnātōte", 3: "oppugnantō"}}, "passive": {"singular": {2: "oppugnātor", 3: "oppugnātor"}, "plural": {3: "oppugnantor"}}}
        },
        "infinitives": {"present active": "oppugnāre", "present passive": "oppugnārī", "perfect active": "oppugnāvisse", "perfect passive": "oppugnātus esse", "future active": "oppugnātūrus esse", "future passive": "oppugnātum īrī"}
    },
    "servāre": {
        "indicative": {
            "present": {"active": {"singular": {1: "servō", 2: "servās", 3: "servat"}, "plural": {1: "servāmus", 2: "servātis", 3: "servant"}}, "passive": {"singular": {1: "servor", 2: "servāris", 3: "servātur"}, "plural": {1: "servāmur", 2: "servāminī", 3: "servantur"}}},
            "imperfect": {"active": {"singular": {1: "servābam", 2: "servābās", 3: "servābat"}, "plural": {1: "servābāmus", 2: "servābātis", 3: "servābant"}}, "passive": {"singular": {1: "servābar", 2: "servābāris", 3: "servābātur"}, "plural": {1: "servābāmur", 2: "servābāminī", 3: "servābantur"}}},
            "future": {"active": {"singular": {1: "servābō", 2: "servābis", 3: "servābit"}, "plural": {1: "servābimus", 2: "servābitis", 3: "servābunt"}}, "passive": {"singular": {1: "servābor", 2: "servāberis", 3: "servābitur"}, "plural": {1: "servābimur", 2: "servābiminī", 3: "servābuntur"}}},
            "perfect": {"active": {"singular": {1: "servāvī", 2: "servāvistī", 3: "servāvit"}, "plural": {1: "servāvimus", 2: "servāvistis", 3: "servāvērunt"}}, "passive": {"singular": {1: "servātus sum", 2: "servātus es", 3: "servātus est"}, "plural": {1: "servātī sumus", 2: "servātī estis", 3: "servātī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "servāveram", 2: "servāverās", 3: "servāverat"}, "plural": {1: "servāverāmus", 2: "servāverātis", 3: "servāverant"}}, "passive": {"singular": {1: "servātus eram", 2: "servātus erās", 3: "servātus erat"}, "plural": {1: "servātī erāmus", 2: "servātī erātis", 3: "servātī erant"}}},
            "future perfect": {"active": {"singular": {1: "servāverō", 2: "servāveris", 3: "servāverit"}, "plural": {1: "servāverimus", 2: "servāveritis", 3: "servāverint"}}, "passive": {"singular": {1: "servātus erō", 2: "servātus eris", 3: "servātus erit"}, "plural": {1: "servātī erimus", 2: "servātī eritis", 3: "servātī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "servā"}, "plural": {2: "servāte"}}, "passive": {"singular": {2: "servāre"}, "plural": {2: "servāminī"}}},
            "future": {"active": {"singular": {2: "servātō", 3: "servātō"}, "plural": {2: "servātōte", 3: "servantō"}}, "passive": {"singular": {2: "servātor", 3: "servātor"}, "plural": {3: "servantor"}}}
        },
        "infinitives": {"present active": "servāre", "present passive": "servārī", "perfect active": "servāvisse", "perfect passive": "servātus esse", "future active": "servātūrus esse", "future passive": "servātum īrī"}
    },

    # === 2ND CONJUGATION ===
    "monēre": {
        "indicative": {
            "present": {"active": {"singular": {1: "moneō", 2: "monēs", 3: "monet"}, "plural": {1: "monēmus", 2: "monētis", 3: "monent"}}, "passive": {"singular": {1: "moneor", 2: "monēris", 3: "monētur"}, "plural": {1: "monēmur", 2: "monēminī", 3: "monentur"}}},
            "imperfect": {"active": {"singular": {1: "monēbam", 2: "monēbās", 3: "monēbat"}, "plural": {1: "monēbāmus", 2: "monēbātis", 3: "monēbant"}}, "passive": {"singular": {1: "monēbar", 2: "monēbāris", 3: "monēbātur"}, "plural": {1: "monēbāmur", 2: "monēbāminī", 3: "monēbantur"}}},
            "future": {"active": {"singular": {1: "monēbō", 2: "monēbis", 3: "monēbit"}, "plural": {1: "monēbimus", 2: "monēbitis", 3: "monēbunt"}}, "passive": {"singular": {1: "monēbor", 2: "monēberis", 3: "monēbitur"}, "plural": {1: "monēbimur", 2: "monēbiminī", 3: "monēbuntur"}}},
            "perfect": {"active": {"singular": {1: "monuī", 2: "monuistī", 3: "monuit"}, "plural": {1: "monuimus", 2: "monuistis", 3: "monuērunt"}}, "passive": {"singular": {1: "monitus sum", 2: "monitus es", 3: "monitus est"}, "plural": {1: "monitī sumus", 2: "monitī estis", 3: "monitī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "monueram", 2: "monuerās", 3: "monuerat"}, "plural": {1: "monuerāmus", 2: "monuerātis", 3: "monuerant"}}, "passive": {"singular": {1: "monitus eram", 2: "monitus erās", 3: "monitus erat"}, "plural": {1: "monitī erāmus", 2: "monitī erātis", 3: "monitī erant"}}},
            "future perfect": {"active": {"singular": {1: "monuerō", 2: "monueris", 3: "monuerit"}, "plural": {1: "monuerimus", 2: "monueritis", 3: "monuerint"}}, "passive": {"singular": {1: "monitus erō", 2: "monitus eris", 3: "monitus erit"}, "plural": {1: "monitī erimus", 2: "monitī eritis", 3: "monitī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "monē"}, "plural": {2: "monēte"}}, "passive": {"singular": {2: "monēre"}, "plural": {2: "monēminī"}}},
            "future": {"active": {"singular": {2: "monētō", 3: "monētō"}, "plural": {2: "monētōte", 3: "monentō"}}, "passive": {"singular": {2: "monētor", 3: "monētor"}, "plural": {3: "monentor"}}}
        },
        "infinitives": {"present active": "monēre", "present passive": "monērī", "perfect active": "monuisse", "perfect passive": "monitus esse", "future active": "monitūrus esse", "future passive": "monitum īrī"}
    },
    "vidēre": {
        "indicative": {
            "present": {"active": {"singular": {1: "videō", 2: "vidēs", 3: "videt"}, "plural": {1: "vidēmus", 2: "vidētis", 3: "vident"}}, "passive": {"singular": {1: "videor", 2: "vidēris", 3: "vidētur"}, "plural": {1: "vidēmur", 2: "vidēminī", 3: "videntur"}}},
            "imperfect": {"active": {"singular": {1: "vidēbam", 2: "vidēbās", 3: "vidēbat"}, "plural": {1: "vidēbāmus", 2: "vidēbātis", 3: "vidēbant"}}, "passive": {"singular": {1: "vidēbar", 2: "vidēbāris", 3: "vidēbātur"}, "plural": {1: "vidēbāmur", 2: "vidēbāminī", 3: "vidēbantur"}}},
            "future": {"active": {"singular": {1: "vidēbō", 2: "vidēbis", 3: "vidēbit"}, "plural": {1: "vidēbimus", 2: "vidēbitis", 3: "vidēbunt"}}, "passive": {"singular": {1: "vidēbor", 2: "vidēberis", 3: "vidēbitur"}, "plural": {1: "vidēbimur", 2: "vidēbiminī", 3: "vidēbuntur"}}},
            "perfect": {"active": {"singular": {1: "vīdī", 2: "vīdistī", 3: "vīdit"}, "plural": {1: "vīdimus", 2: "vīdistis", 3: "vīdērunt"}}, "passive": {"singular": {1: "vīsus sum", 2: "vīsus es", 3: "vīsus est"}, "plural": {1: "vīsī sumus", 2: "vīsī estis", 3: "vīsī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "vīderam", 2: "vīderās", 3: "vīderat"}, "plural": {1: "vīderāmus", 2: "vīderātis", 3: "vīderant"}}, "passive": {"singular": {1: "vīsus eram", 2: "vīsus erās", 3: "vīsus erat"}, "plural": {1: "vīsī erāmus", 2: "vīsī erātis", 3: "vīsī erant"}}},
            "future perfect": {"active": {"singular": {1: "vīderō", 2: "vīderis", 3: "vīderit"}, "plural": {1: "vīderimus", 2: "vīderitis", 3: "vīderint"}}, "passive": {"singular": {1: "vīsus erō", 2: "vīsus eris", 3: "vīsus erit"}, "plural": {1: "vīsī erimus", 2: "vīsī eritis", 3: "vīsī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "vidē"}, "plural": {2: "vidēte"}}, "passive": {"singular": {2: "vidēre"}, "plural": {2: "vidēminī"}}},
            "future": {"active": {"singular": {2: "vidētō", 3: "vidētō"}, "plural": {2: "vidētōte", 3: "videntō"}}, "passive": {"singular": {2: "vidētor", 3: "vidētor"}, "plural": {3: "videntor"}}}
        },
        "infinitives": {"present active": "vidēre", "present passive": "vidērī", "perfect active": "vīdisse", "perfect passive": "vīsus esse", "future active": "vīsūrus esse", "future passive": "vīsum īrī"}
    },
    "habēre": {
        "indicative": {
            "present": {"active": {"singular": {1: "habeō", 2: "habēs", 3: "habet"}, "plural": {1: "habēmus", 2: "habētis", 3: "habent"}}, "passive": {"singular": {1: "habeor", 2: "habēris", 3: "habētur"}, "plural": {1: "habēmur", 2: "habēminī", 3: "habentur"}}},
            "imperfect": {"active": {"singular": {1: "habēbam", 2: "habēbās", 3: "habēbat"}, "plural": {1: "habēbāmus", 2: "habēbātis", 3: "habēbant"}}, "passive": {"singular": {1: "habēbar", 2: "habēbāris", 3: "habēbātur"}, "plural": {1: "habēbāmur", 2: "habēbāminī", 3: "habēbantur"}}},
            "future": {"active": {"singular": {1: "habēbō", 2: "habēbis", 3: "habēbit"}, "plural": {1: "habēbimus", 2: "habēbitis", 3: "habēbunt"}}, "passive": {"singular": {1: "habēbor", 2: "habēberis", 3: "habēbitur"}, "plural": {1: "habēbimur", 2: "habēbiminī", 3: "habēbuntur"}}},
            "perfect": {"active": {"singular": {1: "habuī", 2: "habuistī", 3: "habuit"}, "plural": {1: "habuimus", 2: "habuistis", 3: "habuērunt"}}, "passive": {"singular": {1: "habitus sum", 2: "habitus es", 3: "habitus est"}, "plural": {1: "habitī sumus", 2: "habitī estis", 3: "habitī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "habueram", 2: "habuerās", 3: "habuerat"}, "plural": {1: "habuerāmus", 2: "habuerātis", 3: "habuerant"}}, "passive": {"singular": {1: "habitus eram", 2: "habitus erās", 3: "habitus erat"}, "plural": {1: "habitī erāmus", 2: "habitī erātis", 3: "habitī erant"}}},
            "future perfect": {"active": {"singular": {1: "habuerō", 2: "habueris", 3: "habuerit"}, "plural": {1: "habuerimus", 2: "habueritis", 3: "habuerint"}}, "passive": {"singular": {1: "habitus erō", 2: "habitus eris", 3: "habitus erit"}, "plural": {1: "habitī erimus", 2: "habitī eritis", 3: "habitī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "habē"}, "plural": {2: "habēte"}}, "passive": {"singular": {2: "habēre"}, "plural": {2: "habēminī"}}},
            "future": {"active": {"singular": {2: "habētō", 3: "habētō"}, "plural": {2: "habētōte", 3: "habentō"}}, "passive": {"singular": {2: "habētor", 3: "habētor"}, "plural": {3: "habentor"}}}
        },
        "infinitives": {"present active": "habēre", "present passive": "habērī", "perfect active": "habuisse", "perfect passive": "habitus esse", "future active": "habitūrus esse", "future passive": "habitum īrī"}
    },
    "docēre": {
        "indicative": {
            "present": {"active": {"singular": {1: "doceō", 2: "docēs", 3: "docet"}, "plural": {1: "docēmus", 2: "docētis", 3: "docent"}}, "passive": {"singular": {1: "doceor", 2: "docēris", 3: "docētur"}, "plural": {1: "docēmur", 2: "docēminī", 3: "docentur"}}},
            "imperfect": {"active": {"singular": {1: "docēbam", 2: "docēbās", 3: "docēbat"}, "plural": {1: "docēbāmus", 2: "docēbātis", 3: "docēbant"}}, "passive": {"singular": {1: "docēbar", 2: "docēbāris", 3: "docēbātur"}, "plural": {1: "docēbāmur", 2: "docēbāminī", 3: "docēbantur"}}},
            "future": {"active": {"singular": {1: "docēbō", 2: "docēbis", 3: "docēbit"}, "plural": {1: "docēbimus", 2: "docēbitis", 3: "docēbunt"}}, "passive": {"singular": {1: "docēbor", 2: "docēberis", 3: "docēbitur"}, "plural": {1: "docēbimur", 2: "docēbiminī", 3: "docēbuntur"}}},
            "perfect": {"active": {"singular": {1: "docuī", 2: "docuistī", 3: "docuit"}, "plural": {1: "docuimus", 2: "docuistis", 3: "docuērunt"}}, "passive": {"singular": {1: "doctus sum", 2: "doctus es", 3: "doctus est"}, "plural": {1: "doctī sumus", 2: "doctī estis", 3: "doctī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "docueram", 2: "docuerās", 3: "docuerat"}, "plural": {1: "docuerāmus", 2: "docuerātis", 3: "docuerant"}}, "passive": {"singular": {1: "doctus eram", 2: "doctus erās", 3: "doctus erat"}, "plural": {1: "doctī erāmus", 2: "doctī erātis", 3: "doctī erant"}}},
            "future perfect": {"active": {"singular": {1: "docuerō", 2: "docueris", 3: "docuerit"}, "plural": {1: "docuerimus", 2: "docueritis", 3: "docuerint"}}, "passive": {"singular": {1: "doctus erō", 2: "doctus eris", 3: "doctus erit"}, "plural": {1: "doctī erimus", 2: "doctī eritis", 3: "doctī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "docē"}, "plural": {2: "docēte"}}, "passive": {"singular": {2: "docēre"}, "plural": {2: "docēminī"}}},
            "future": {"active": {"singular": {2: "docētō", 3: "docētō"}, "plural": {2: "docētōte", 3: "docentō"}}, "passive": {"singular": {2: "docētor", 3: "docētor"}, "plural": {3: "docentor"}}}
        },
        "infinitives": {"present active": "docēre", "present passive": "docērī", "perfect active": "docuisse", "perfect passive": "doctus esse", "future active": "doctūrus esse", "future passive": "doctum īrī"}
    },
    "tenēre": {
        "indicative": {
            "present": {"active": {"singular": {1: "teneō", 2: "tenēs", 3: "tenet"}, "plural": {1: "tenēmus", 2: "tenētis", 3: "tenent"}}, "passive": {"singular": {1: "teneor", 2: "tenēris", 3: "tenētur"}, "plural": {1: "tenēmur", 2: "tenēminī", 3: "tenentur"}}},
            "imperfect": {"active": {"singular": {1: "tenēbam", 2: "tenēbās", 3: "tenēbat"}, "plural": {1: "tenēbāmus", 2: "tenēbātis", 3: "tenēbant"}}, "passive": {"singular": {1: "tenēbar", 2: "tenēbāris", 3: "tenēbātur"}, "plural": {1: "tenēbāmur", 2: "tenēbāminī", 3: "tenēbantur"}}},
            "future": {"active": {"singular": {1: "tenēbō", 2: "tenēbis", 3: "tenēbit"}, "plural": {1: "tenēbimus", 2: "tenēbitis", 3: "tenēbunt"}}, "passive": {"singular": {1: "tenēbor", 2: "tenēberis", 3: "tenēbitur"}, "plural": {1: "tenēbimur", 2: "tenēbiminī", 3: "tenēbuntur"}}},
            "perfect": {"active": {"singular": {1: "tenuī", 2: "tenuistī", 3: "tenuit"}, "plural": {1: "tenuimus", 2: "tenuistis", 3: "tenuērunt"}}, "passive": {"singular": {1: "tentus sum", 2: "tentus es", 3: "tentus est"}, "plural": {1: "tentī sumus", 2: "tentī estis", 3: "tentī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "tenueram", 2: "tenuerās", 3: "tenuerat"}, "plural": {1: "tenuerāmus", 2: "tenuerātis", 3: "tenuerant"}}, "passive": {"singular": {1: "tentus eram", 2: "tentus erās", 3: "tentus erat"}, "plural": {1: "tentī erāmus", 2: "tentī erātis", 3: "tentī erant"}}},
            "future perfect": {"active": {"singular": {1: "tenuerō", 2: "tenueris", 3: "tenuerit"}, "plural": {1: "tenuerimus", 2: "tenueritis", 3: "tenuerint"}}, "passive": {"singular": {1: "tentus erō", 2: "tentus eris", 3: "tentus erit"}, "plural": {1: "tentī erimus", 2: "tentī eritis", 3: "tentī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "tenē"}, "plural": {2: "tenēte"}}, "passive": {"singular": {2: "tenēre"}, "plural": {2: "tenēminī"}}},
            "future": {"active": {"singular": {2: "tenētō", 3: "tenētō"}, "plural": {2: "tenētōte", 3: "tenentō"}}, "passive": {"singular": {2: "tenētor", 3: "tenētor"}, "plural": {3: "tenentor"}}}
        },
        "infinitives": {"present active": "tenēre", "present passive": "tenērī", "perfect active": "tenuisse", "perfect passive": "tentus esse", "future active": "tentūrus esse", "future passive": "tentum īrī"}
    },
    "terrēre": {
        "indicative": {
            "present": {"active": {"singular": {1: "terreō", 2: "terrēs", 3: "terret"}, "plural": {1: "terrēmus", 2: "terrētis", 3: "terrent"}}, "passive": {"singular": {1: "terreor", 2: "terrēris", 3: "terrētur"}, "plural": {1: "terrēmur", 2: "terrēminī", 3: "terrentur"}}},
            "imperfect": {"active": {"singular": {1: "terrēbam", 2: "terrēbās", 3: "terrēbat"}, "plural": {1: "terrēbāmus", 2: "terrēbātis", 3: "terrēbant"}}, "passive": {"singular": {1: "terrēbar", 2: "terrēbāris", 3: "terrēbātur"}, "plural": {1: "terrēbāmur", 2: "terrēbāminī", 3: "terrēbantur"}}},
            "future": {"active": {"singular": {1: "terrēbō", 2: "terrēbis", 3: "terrēbit"}, "plural": {1: "terrēbimus", 2: "terrēbitis", 3: "terrēbunt"}}, "passive": {"singular": {1: "terrēbor", 2: "terrēberis", 3: "terrēbitur"}, "plural": {1: "terrēbimur", 2: "terrēbiminī", 3: "terrēbuntur"}}},
            "perfect": {"active": {"singular": {1: "terruī", 2: "terruistī", 3: "terruit"}, "plural": {1: "terruimus", 2: "terruistis", 3: "terruērunt"}}, "passive": {"singular": {1: "territus sum", 2: "territus es", 3: "territus est"}, "plural": {1: "territī sumus", 2: "territī estis", 3: "territī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "terrueram", 2: "terruerās", 3: "terruerat"}, "plural": {1: "terruerāmus", 2: "terruerātis", 3: "terruerant"}}, "passive": {"singular": {1: "territus eram", 2: "territus erās", 3: "territus erat"}, "plural": {1: "territī erāmus", 2: "territī erātis", 3: "territī erant"}}},
            "future perfect": {"active": {"singular": {1: "terruerō", 2: "terrueris", 3: "terruerit"}, "plural": {1: "terruerimus", 2: "terrueritis", 3: "terruerint"}}, "passive": {"singular": {1: "territus erō", 2: "territus eris", 3: "territus erit"}, "plural": {1: "territī erimus", 2: "territī eritis", 3: "territī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "terrē"}, "plural": {2: "terrēte"}}, "passive": {"singular": {2: "terrēre"}, "plural": {2: "terrēminī"}}},
            "future": {"active": {"singular": {2: "terrētō", 3: "terrētō"}, "plural": {2: "terrētōte", 3: "terrentō"}}, "passive": {"singular": {2: "terrētor", 3: "terrētor"}, "plural": {3: "terrentor"}}}
        },
        "infinitives": {"present active": "terrēre", "present passive": "terrērī", "perfect active": "terruisse", "perfect passive": "territus esse", "future active": "territūrus esse", "future passive": "territum īrī"}
    },
    "movēre": {
        "indicative": {
            "present": {"active": {"singular": {1: "moveō", 2: "movēs", 3: "movet"}, "plural": {1: "movēmus", 2: "movētis", 3: "movent"}}, "passive": {"singular": {1: "moveor", 2: "movēris", 3: "movētur"}, "plural": {1: "movēmur", 2: "movēminī", 3: "moventur"}}},
            "imperfect": {"active": {"singular": {1: "movēbam", 2: "movēbās", 3: "movēbat"}, "plural": {1: "movēbāmus", 2: "movēbātis", 3: "movēbant"}}, "passive": {"singular": {1: "movēbar", 2: "movēbāris", 3: "movēbātur"}, "plural": {1: "movēbāmur", 2: "movēbāminī", 3: "movēbantur"}}},
            "future": {"active": {"singular": {1: "movēbō", 2: "movēbis", 3: "movēbit"}, "plural": {1: "movēbimus", 2: "movēbitis", 3: "movēbunt"}}, "passive": {"singular": {1: "movēbor", 2: "movēberis", 3: "movēbitur"}, "plural": {1: "movēbimur", 2: "movēbiminī", 3: "movēbuntur"}}},
            "perfect": {"active": {"singular": {1: "mōvī", 2: "mōvistī", 3: "mōvit"}, "plural": {1: "mōvimus", 2: "mōvistis", 3: "mōvērunt"}}, "passive": {"singular": {1: "mōtus sum", 2: "mōtus es", 3: "mōtus est"}, "plural": {1: "mōtī sumus", 2: "mōtī estis", 3: "mōtī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "mōveram", 2: "mōverās", 3: "mōverat"}, "plural": {1: "mōverāmus", 2: "mōverātis", 3: "mōverant"}}, "passive": {"singular": {1: "mōtus eram", 2: "mōtus erās", 3: "mōtus erat"}, "plural": {1: "mōtī erāmus", 2: "mōtī erātis", 3: "mōtī erant"}}},
            "future perfect": {"active": {"singular": {1: "mōverō", 2: "mōveris", 3: "mōverit"}, "plural": {1: "mōverimus", 2: "mōveritis", 3: "mōverint"}}, "passive": {"singular": {1: "mōtus erō", 2: "mōtus eris", 3: "mōtus erit"}, "plural": {1: "mōtī erimus", 2: "mōtī eritis", 3: "mōtī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "movē"}, "plural": {2: "movēte"}}, "passive": {"singular": {2: "movēre"}, "plural": {2: "movēminī"}}},
            "future": {"active": {"singular": {2: "movētō", 3: "movētō"}, "plural": {2: "movētōte", 3: "moventō"}}, "passive": {"singular": {2: "movētor", 3: "movētor"}, "plural": {3: "moventor"}}}
        },
        "infinitives": {"present active": "movēre", "present passive": "movērī", "perfect active": "mōvisse", "perfect passive": "mōtus esse", "future active": "mōtūrus esse", "future passive": "mōtum īrī"}
    },
    "prohibēre": {
        "indicative": {
            "present": {"active": {"singular": {1: "prohibeō", 2: "prohibēs", 3: "prohibet"}, "plural": {1: "prohibēmus", 2: "prohibētis", 3: "prohibent"}}, "passive": {"singular": {1: "prohibeor", 2: "prohibēris", 3: "prohibētur"}, "plural": {1: "prohibēmur", 2: "prohibēminī", 3: "prohibentur"}}},
            "imperfect": {"active": {"singular": {1: "prohibēbam", 2: "prohibēbās", 3: "prohibēbat"}, "plural": {1: "prohibēbāmus", 2: "prohibēbātis", 3: "prohibēbant"}}, "passive": {"singular": {1: "prohibēbar", 2: "prohibēbāris", 3: "prohibēbātur"}, "plural": {1: "prohibēbāmur", 2: "prohibēbāminī", 3: "prohibēbantur"}}},
            "future": {"active": {"singular": {1: "prohibēbō", 2: "prohibēbis", 3: "prohibēbit"}, "plural": {1: "prohibēbimus", 2: "prohibēbitis", 3: "prohibēbunt"}}, "passive": {"singular": {1: "prohibēbor", 2: "prohibēberis", 3: "prohibēbitur"}, "plural": {1: "prohibēbimur", 2: "prohibēbiminī", 3: "prohibēbuntur"}}},
            "perfect": {"active": {"singular": {1: "prohibuī", 2: "prohibuistī", 3: "prohibuit"}, "plural": {1: "prohibuimus", 2: "prohibuistis", 3: "prohibuērunt"}}, "passive": {"singular": {1: "prohibitus sum", 2: "prohibitus es", 3: "prohibitus est"}, "plural": {1: "prohibitī sumus", 2: "prohibitī estis", 3: "prohibitī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "prohibueram", 2: "prohibuerās", 3: "prohibuerat"}, "plural": {1: "prohibuerāmus", 2: "prohibuerātis", 3: "prohibuerant"}}, "passive": {"singular": {1: "prohibitus eram", 2: "prohibitus erās", 3: "prohibitus erat"}, "plural": {1: "prohibitī erāmus", 2: "prohibitī erātis", 3: "prohibitī erant"}}},
            "future perfect": {"active": {"singular": {1: "prohibuerō", 2: "prohibueris", 3: "prohibuerit"}, "plural": {1: "prohibuerimus", 2: "prohibueritis", 3: "prohibuerint"}}, "passive": {"singular": {1: "prohibitus erō", 2: "prohibitus eris", 3: "prohibitus erit"}, "plural": {1: "prohibitī erimus", 2: "prohibitī eritis", 3: "prohibitī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "prohibē"}, "plural": {2: "prohibēte"}}, "passive": {"singular": {2: "prohibēre"}, "plural": {2: "prohibēminī"}}},
            "future": {"active": {"singular": {2: "prohibētō", 3: "prohibētō"}, "plural": {2: "prohibētōte", 3: "prohibentō"}}, "passive": {"singular": {2: "prohibētor", 3: "prohibētor"}, "plural": {3: "prohibentor"}}}
        },
        "infinitives": {"present active": "prohibēre", "present passive": "prohibērī", "perfect active": "prohibuisse", "perfect passive": "prohibitus esse", "future active": "prohibitūrus esse", "future passive": "prohibitum īrī"}
    },
    "praebēre": {
        "indicative": {
            "present": {"active": {"singular": {1: "praebeō", 2: "praebēs", 3: "praebet"}, "plural": {1: "praebēmus", 2: "praebētis", 3: "praebent"}}, "passive": {"singular": {1: "praebeor", 2: "praebēris", 3: "praebētur"}, "plural": {1: "praebēmur", 2: "praebēminī", 3: "praebentur"}}},
            "imperfect": {"active": {"singular": {1: "praebēbam", 2: "praebēbās", 3: "praebēbat"}, "plural": {1: "praebēbāmus", 2: "praebēbātis", 3: "praebēbant"}}, "passive": {"singular": {1: "praebēbar", 2: "praebēbāris", 3: "praebēbātur"}, "plural": {1: "praebēbāmur", 2: "praebēbāminī", 3: "praebēbantur"}}},
            "future": {"active": {"singular": {1: "praebēbō", 2: "praebēbis", 3: "praebēbit"}, "plural": {1: "praebēbimus", 2: "praebēbitis", 3: "praebēbunt"}}, "passive": {"singular": {1: "praebēbor", 2: "praebēberis", 3: "praebēbitur"}, "plural": {1: "praebēbimur", 2: "praebēbiminī", 3: "praebēbuntur"}}},
            "perfect": {"active": {"singular": {1: "praebuī", 2: "praebuistī", 3: "praebuit"}, "plural": {1: "praebuimus", 2: "praebuistis", 3: "praebuērunt"}}, "passive": {"singular": {1: "praebitus sum", 2: "praebitus es", 3: "praebitus est"}, "plural": {1: "praebitī sumus", 2: "praebitī estis", 3: "praebitī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "praebueram", 2: "praebuerās", 3: "praebuerat"}, "plural": {1: "praebuerāmus", 2: "praebuerātis", 3: "praebuerant"}}, "passive": {"singular": {1: "praebitus eram", 2: "praebitus erās", 3: "praebitus erat"}, "plural": {1: "praebitī erāmus", 2: "praebitī erātis", 3: "praebitī erant"}}},
            "future perfect": {"active": {"singular": {1: "praebuerō", 2: "praebueris", 3: "praebuerit"}, "plural": {1: "praebuerimus", 2: "praebueritis", 3: "praebuerint"}}, "passive": {"singular": {1: "praebitus erō", 2: "praebitus eris", 3: "praebitus erit"}, "plural": {1: "praebitī erimus", 2: "praebitī eritis", 3: "praebitī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "praebē"}, "plural": {2: "praebēte"}}, "passive": {"singular": {2: "praebēre"}, "plural": {2: "praebēminī"}}},
            "future": {"active": {"singular": {2: "praebētō", 3: "praebētō"}, "plural": {2: "praebētōte", 3: "praebentō"}}, "passive": {"singular": {2: "praebētor", 3: "praebētor"}, "plural": {3: "praebentor"}}}
        },
        "infinitives": {"present active": "praebēre", "present passive": "praebērī", "perfect active": "praebuisse", "perfect passive": "praebitus esse", "future active": "praebitūrus esse", "future passive": "praebitum īrī"}
    },
    "miscēre": {
        "indicative": {
            "present": {"active": {"singular": {1: "misceō", 2: "miscēs", 3: "miscet"}, "plural": {1: "miscēmus", 2: "miscētis", 3: "miscent"}}, "passive": {"singular": {1: "misceor", 2: "miscēris", 3: "miscētur"}, "plural": {1: "miscēmur", 2: "miscēminī", 3: "miscentur"}}},
            "imperfect": {"active": {"singular": {1: "miscēbam", 2: "miscēbās", 3: "miscēbat"}, "plural": {1: "miscēbāmus", 2: "miscēbātis", 3: "miscēbant"}}, "passive": {"singular": {1: "miscēbar", 2: "miscēbāris", 3: "miscēbātur"}, "plural": {1: "miscēbāmur", 2: "miscēbāminī", 3: "miscēbantur"}}},
            "future": {"active": {"singular": {1: "miscēbō", 2: "miscēbis", 3: "miscēbit"}, "plural": {1: "miscēbimus", 2: "miscēbitis", 3: "miscēbunt"}}, "passive": {"singular": {1: "miscēbor", 2: "miscēberis", 3: "miscēbitur"}, "plural": {1: "miscēbimur", 2: "miscēbiminī", 3: "miscēbuntur"}}},
            "perfect": {"active": {"singular": {1: "miscuī", 2: "miscuistī", 3: "miscuit"}, "plural": {1: "miscuimus", 2: "miscuistis", 3: "miscuērunt"}}, "passive": {"singular": {1: "mixtus sum", 2: "mixtus es", 3: "mixtus est"}, "plural": {1: "mixtī sumus", 2: "mixtī estis", 3: "mixtī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "miscueram", 2: "miscuerās", 3: "miscuerat"}, "plural": {1: "miscuerāmus", 2: "miscuerātis", 3: "miscuerant"}}, "passive": {"singular": {1: "mixtus eram", 2: "mixtus erās", 3: "mixtus erat"}, "plural": {1: "mixtī erāmus", 2: "mixtī erātis", 3: "mixtī erant"}}},
            "future perfect": {"active": {"singular": {1: "miscuerō", 2: "miscueris", 3: "miscuerit"}, "plural": {1: "miscuerimus", 2: "miscueritis", 3: "miscuerint"}}, "passive": {"singular": {1: "mixtus erō", 2: "mixtus eris", 3: "mixtus erit"}, "plural": {1: "mixtī erimus", 2: "mixtī eritis", 3: "mixtī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "miscē"}, "plural": {2: "miscēte"}}, "passive": {"singular": {2: "miscēre"}, "plural": {2: "miscēminī"}}},
            "future": {"active": {"singular": {2: "miscētō", 3: "miscētō"}, "plural": {2: "miscētōte", 3: "miscentō"}}, "passive": {"singular": {2: "miscētor", 3: "miscētor"}, "plural": {3: "miscentor"}}}
        },
        "infinitives": {"present active": "miscēre", "present passive": "miscērī", "perfect active": "miscuisse", "perfect passive": "mixtus esse", "future active": "mixtūrus esse", "future passive": "mixtum īrī"}
    },

    # === 3RD CONJUGATION ===
    "dūcere": {
        "indicative": {
            "present": {"active": {"singular": {1: "dūcō", 2: "dūcis", 3: "dūcit"}, "plural": {1: "dūcimus", 2: "dūcitis", 3: "dūcunt"}}, "passive": {"singular": {1: "dūcor", 2: "dūceris", 3: "dūcitur"}, "plural": {1: "dūcimur", 2: "dūciminī", 3: "dūcuntur"}}},
            "imperfect": {"active": {"singular": {1: "dūcēbam", 2: "dūcēbās", 3: "dūcēbat"}, "plural": {1: "dūcēbāmus", 2: "dūcēbātis", 3: "dūcēbant"}}, "passive": {"singular": {1: "dūcēbar", 2: "dūcēbāris", 3: "dūcēbātur"}, "plural": {1: "dūcēbāmur", 2: "dūcēbāminī", 3: "dūcēbantur"}}},
            "future": {"active": {"singular": {1: "dūcam", 2: "dūcēs", 3: "dūcet"}, "plural": {1: "dūcēmus", 2: "dūcētis", 3: "dūcent"}}, "passive": {"singular": {1: "dūcar", 2: "dūcēris", 3: "dūcētur"}, "plural": {1: "dūcēmur", 2: "dūcēminī", 3: "dūcentur"}}},
            "perfect": {"active": {"singular": {1: "dūxī", 2: "dūxistī", 3: "dūxit"}, "plural": {1: "dūximus", 2: "dūxistis", 3: "dūxērunt"}}, "passive": {"singular": {1: "ductus sum", 2: "ductus es", 3: "ductus est"}, "plural": {1: "ductī sumus", 2: "ductī estis", 3: "ductī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "dūxeram", 2: "dūxerās", 3: "dūxerat"}, "plural": {1: "dūxerāmus", 2: "dūxerātis", 3: "dūxerant"}}, "passive": {"singular": {1: "ductus eram", 2: "ductus erās", 3: "ductus erat"}, "plural": {1: "ductī erāmus", 2: "ductī erātis", 3: "ductī erant"}}},
            "future perfect": {"active": {"singular": {1: "dūxerō", 2: "dūxeris", 3: "dūxerit"}, "plural": {1: "dūxerimus", 2: "dūxeritis", 3: "dūxerint"}}, "passive": {"singular": {1: "ductus erō", 2: "ductus eris", 3: "ductus erit"}, "plural": {1: "ductī erimus", 2: "ductī eritis", 3: "ductī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "dūc"}, "plural": {2: "dūcite"}}, "passive": {"singular": {2: "dūcere"}, "plural": {2: "dūciminī"}}},
            "future": {"active": {"singular": {2: "dūcitō", 3: "dūcitō"}, "plural": {2: "dūcitōte", 3: "dūcuntō"}}, "passive": {"singular": {2: "dūcitor", 3: "dūcitor"}, "plural": {3: "dūcuntor"}}}
        },
        "infinitives": {"present active": "dūcere", "present passive": "dūcī", "perfect active": "dūxisse", "perfect passive": "ductus esse", "future active": "ductūrus esse", "future passive": "ductum īrī"}
    },
    "mittere": {
        "indicative": {
            "present": {"active": {"singular": {1: "mittō", 2: "mittis", 3: "mittit"}, "plural": {1: "mittimus", 2: "mittitis", 3: "mittunt"}}, "passive": {"singular": {1: "mittor", 2: "mitteris", 3: "mittitur"}, "plural": {1: "mittimur", 2: "mittiminī", 3: "mittuntur"}}},
            "imperfect": {"active": {"singular": {1: "mittēbam", 2: "mittēbās", 3: "mittēbat"}, "plural": {1: "mittēbāmus", 2: "mittēbātis", 3: "mittēbant"}}, "passive": {"singular": {1: "mittēbar", 2: "mittēbāris", 3: "mittēbātur"}, "plural": {1: "mittēbāmur", 2: "mittēbāminī", 3: "mittēbantur"}}},
            "future": {"active": {"singular": {1: "mittam", 2: "mittēs", 3: "mittet"}, "plural": {1: "mittēmus", 2: "mittētis", 3: "mittent"}}, "passive": {"singular": {1: "mittar", 2: "mittēris", 3: "mittētur"}, "plural": {1: "mittēmur", 2: "mittēminī", 3: "mittentur"}}},
            "perfect": {"active": {"singular": {1: "mīsī", 2: "mīsistī", 3: "mīsit"}, "plural": {1: "mīsimus", 2: "mīsistis", 3: "mīsērunt"}}, "passive": {"singular": {1: "missus sum", 2: "missus es", 3: "missus est"}, "plural": {1: "missī sumus", 2: "missī estis", 3: "missī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "mīseram", 2: "mīserās", 3: "mīserat"}, "plural": {1: "mīserāmus", 2: "mīserātis", 3: "mīserant"}}, "passive": {"singular": {1: "missus eram", 2: "missus erās", 3: "missus erat"}, "plural": {1: "missī erāmus", 2: "missī erātis", 3: "missī erant"}}},
            "future perfect": {"active": {"singular": {1: "mīserō", 2: "mīseris", 3: "mīserit"}, "plural": {1: "mīserimus", 2: "mīseritis", 3: "mīserint"}}, "passive": {"singular": {1: "missus erō", 2: "missus eris", 3: "missus erit"}, "plural": {1: "missī erimus", 2: "missī eritis", 3: "missī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "mitte"}, "plural": {2: "mittite"}}, "passive": {"singular": {2: "mittere"}, "plural": {2: "mittiminī"}}},
            "future": {"active": {"singular": {2: "mittitō", 3: "mittitō"}, "plural": {2: "mittitōte", 3: "mittuntō"}}, "passive": {"singular": {2: "mittitor", 3: "mittitor"}, "plural": {3: "mittuntor"}}}
        },
        "infinitives": {"present active": "mittere", "present passive": "mittī", "perfect active": "mīsisse", "perfect passive": "missus esse", "future active": "missūrus esse", "future passive": "missum īrī"}
    },
    "pōnere": {
        "indicative": {
            "present": {"active": {"singular": {1: "pōnō", 2: "pōnis", 3: "pōnit"}, "plural": {1: "pōnimus", 2: "pōnitis", 3: "pōnunt"}}, "passive": {"singular": {1: "pōnor", 2: "pōneris", 3: "pōnitur"}, "plural": {1: "pōnimur", 2: "pōniminī", 3: "pōnuntur"}}},
            "imperfect": {"active": {"singular": {1: "pōnēbam", 2: "pōnēbās", 3: "pōnēbat"}, "plural": {1: "pōnēbāmus", 2: "pōnēbātis", 3: "pōnēbant"}}, "passive": {"singular": {1: "pōnēbar", 2: "pōnēbāris", 3: "pōnēbātur"}, "plural": {1: "pōnēbāmur", 2: "pōnēbāminī", 3: "pōnēbantur"}}},
            "future": {"active": {"singular": {1: "pōnam", 2: "pōnēs", 3: "pōnet"}, "plural": {1: "pōnēmus", 2: "pōnētis", 3: "pōnent"}}, "passive": {"singular": {1: "pōnar", 2: "pōnēris", 3: "pōnētur"}, "plural": {1: "pōnēmur", 2: "pōnēminī", 3: "pōnentur"}}},
            "perfect": {"active": {"singular": {1: "posuī", 2: "posuistī", 3: "posuit"}, "plural": {1: "posuimus", 2: "posuistis", 3: "posuērunt"}}, "passive": {"singular": {1: "positus sum", 2: "positus es", 3: "positus est"}, "plural": {1: "positī sumus", 2: "positī estis", 3: "positī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "posueram", 2: "posuerās", 3: "posuerat"}, "plural": {1: "posuerāmus", 2: "posuerātis", 3: "posuerant"}}, "passive": {"singular": {1: "positus eram", 2: "positus erās", 3: "positus erat"}, "plural": {1: "positī erāmus", 2: "positī erātis", 3: "positī erant"}}},
            "future perfect": {"active": {"singular": {1: "posuerō", 2: "posueris", 3: "posuerit"}, "plural": {1: "posuerimus", 2: "posueritis", 3: "posuerint"}}, "passive": {"singular": {1: "positus erō", 2: "positus eris", 3: "positus erit"}, "plural": {1: "positī erimus", 2: "positī eritis", 3: "positī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "pōne"}, "plural": {2: "pōnite"}}, "passive": {"singular": {2: "pōnere"}, "plural": {2: "pōniminī"}}},
            "future": {"active": {"singular": {2: "pōnitō", 3: "pōnitō"}, "plural": {2: "pōnitōte", 3: "pōnuntō"}}, "passive": {"singular": {2: "pōnitor", 3: "pōnitor"}, "plural": {3: "pōnuntor"}}}
        },
        "infinitives": {"present active": "pōnere", "present passive": "pōnī", "perfect active": "posuisse", "perfect passive": "positus esse", "future active": "positūrus esse", "future passive": "positum īrī"}
    },
    "regere": {
        "indicative": {
            "present": {"active": {"singular": {1: "regō", 2: "regis", 3: "regit"}, "plural": {1: "regimus", 2: "regitis", 3: "regunt"}}, "passive": {"singular": {1: "regor", 2: "regeris", 3: "regitur"}, "plural": {1: "regimur", 2: "regiminī", 3: "reguntur"}}},
            "imperfect": {"active": {"singular": {1: "regēbam", 2: "regēbās", 3: "regēbat"}, "plural": {1: "regēbāmus", 2: "regēbātis", 3: "regēbant"}}, "passive": {"singular": {1: "regēbar", 2: "regēbāris", 3: "regēbātur"}, "plural": {1: "regēbāmur", 2: "regēbāminī", 3: "regēbantur"}}},
            "future": {"active": {"singular": {1: "regam", 2: "regēs", 3: "reget"}, "plural": {1: "regēmus", 2: "regētis", 3: "regent"}}, "passive": {"singular": {1: "regar", 2: "regēris", 3: "regētur"}, "plural": {1: "regēmur", 2: "regēminī", 3: "regentur"}}},
            "perfect": {"active": {"singular": {1: "rēxī", 2: "rēxistī", 3: "rēxit"}, "plural": {1: "rēximus", 2: "rēxistis", 3: "rēxērunt"}}, "passive": {"singular": {1: "rēctus sum", 2: "rēctus es", 3: "rēctus est"}, "plural": {1: "rēctī sumus", 2: "rēctī estis", 3: "rēctī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "rēxeram", 2: "rēxerās", 3: "rēxerat"}, "plural": {1: "rēxerāmus", 2: "rēxerātis", 3: "rēxerant"}}, "passive": {"singular": {1: "rēctus eram", 2: "rēctus erās", 3: "rēctus erat"}, "plural": {1: "rēctī erāmus", 2: "rēctī erātis", 3: "rēctī erant"}}},
            "future perfect": {"active": {"singular": {1: "rēxerō", 2: "rēxeris", 3: "rēxerit"}, "plural": {1: "rēxerimus", 2: "rēxeritis", 3: "rēxerint"}}, "passive": {"singular": {1: "rēctus erō", 2: "rēctus eris", 3: "rēctus erit"}, "plural": {1: "rēctī erimus", 2: "rēctī eritis", 3: "rēctī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "rege"}, "plural": {2: "regite"}}, "passive": {"singular": {2: "regere"}, "plural": {2: "regiminī"}}},
            "future": {"active": {"singular": {2: "regitō", 3: "regitō"}, "plural": {2: "regitōte", 3: "reguntō"}}, "passive": {"singular": {2: "regitor", 3: "regitor"}, "plural": {3: "reguntor"}}}
        },
        "infinitives": {"present active": "regere", "present passive": "regī", "perfect active": "rēxisse", "perfect passive": "rēctus esse", "future active": "rēctūrus esse", "future passive": "rēctum īrī"}
    },
    "trahere": {
        "indicative": {
            "present": {"active": {"singular": {1: "trahō", 2: "trahis", 3: "trahit"}, "plural": {1: "trahimus", 2: "trahitis", 3: "trahunt"}}, "passive": {"singular": {1: "trahor", 2: "traheris", 3: "trahitur"}, "plural": {1: "trahimur", 2: "trahiminī", 3: "trahuntur"}}},
            "imperfect": {"active": {"singular": {1: "trahēbam", 2: "trahēbās", 3: "trahēbat"}, "plural": {1: "trahēbāmus", 2: "trahēbātis", 3: "trahēbant"}}, "passive": {"singular": {1: "trahēbar", 2: "trahēbāris", 3: "trahēbātur"}, "plural": {1: "trahēbāmur", 2: "trahēbāminī", 3: "trahēbantur"}}},
            "future": {"active": {"singular": {1: "traham", 2: "trahēs", 3: "trahet"}, "plural": {1: "trahēmus", 2: "trahētis", 3: "trahent"}}, "passive": {"singular": {1: "trahar", 2: "trahēris", 3: "trahētur"}, "plural": {1: "trahēmur", 2: "trahēminī", 3: "trahentur"}}},
            "perfect": {"active": {"singular": {1: "trāxī", 2: "trāxistī", 3: "trāxit"}, "plural": {1: "trāximus", 2: "trāxistis", 3: "trāxērunt"}}, "passive": {"singular": {1: "tractus sum", 2: "tractus es", 3: "tractus est"}, "plural": {1: "tractī sumus", 2: "tractī estis", 3: "tractī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "trāxeram", 2: "trāxerās", 3: "trāxerat"}, "plural": {1: "trāxerāmus", 2: "trāxerātis", 3: "trāxerant"}}, "passive": {"singular": {1: "tractus eram", 2: "tractus erās", 3: "tractus erat"}, "plural": {1: "tractī erāmus", 2: "tractī erātis", 3: "tractī erant"}}},
            "future perfect": {"active": {"singular": {1: "trāxerō", 2: "trāxeris", 3: "trāxerit"}, "plural": {1: "trāxerimus", 2: "trāxeritis", 3: "trāxerint"}}, "passive": {"singular": {1: "tractus erō", 2: "tractus eris", 3: "tractus erit"}, "plural": {1: "tractī erimus", 2: "tractī eritis", 3: "tractī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "trahe"}, "plural": {2: "trahite"}}, "passive": {"singular": {2: "trahere"}, "plural": {2: "trahiminī"}}},
            "future": {"active": {"singular": {2: "trahitō", 3: "trahitō"}, "plural": {2: "trahitōte", 3: "trahuntō"}}, "passive": {"singular": {2: "trahitor", 3: "trahitor"}, "plural": {3: "trahuntor"}}}
        },
        "infinitives": {"present active": "trahere", "present passive": "trahī", "perfect active": "trāxisse", "perfect passive": "tractus esse", "future active": "tractūrus esse", "future passive": "tractum īrī"}
    },
    "dīcere": {
        "indicative": {
            "present": {"active": {"singular": {1: "dīcō", 2: "dīcis", 3: "dīcit"}, "plural": {1: "dīcimus", 2: "dīcitis", 3: "dīcunt"}}, "passive": {"singular": {1: "dīcor", 2: "dīceris", 3: "dīcitur"}, "plural": {1: "dīcimur", 2: "dīciminī", 3: "dīcuntur"}}},
            "imperfect": {"active": {"singular": {1: "dīcēbam", 2: "dīcēbās", 3: "dīcēbat"}, "plural": {1: "dīcēbāmus", 2: "dīcēbātis", 3: "dīcēbant"}}, "passive": {"singular": {1: "dīcēbar", 2: "dīcēbāris", 3: "dīcēbātur"}, "plural": {1: "dīcēbāmur", 2: "dīcēbāminī", 3: "dīcēbantur"}}},
            "future": {"active": {"singular": {1: "dīcam", 2: "dīcēs", 3: "dīcet"}, "plural": {1: "dīcēmus", 2: "dīcētis", 3: "dīcent"}}, "passive": {"singular": {1: "dīcar", 2: "dīcēris", 3: "dīcētur"}, "plural": {1: "dīcēmur", 2: "dīcēminī", 3: "dīcentur"}}},
            "perfect": {"active": {"singular": {1: "dīxī", 2: "dīxistī", 3: "dīxit"}, "plural": {1: "dīximus", 2: "dīxistis", 3: "dīxērunt"}}, "passive": {"singular": {1: "dictus sum", 2: "dictus es", 3: "dictus est"}, "plural": {1: "dictī sumus", 2: "dictī estis", 3: "dictī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "dīxeram", 2: "dīxerās", 3: "dīxerat"}, "plural": {1: "dīxerāmus", 2: "dīxerātis", 3: "dīxerant"}}, "passive": {"singular": {1: "dictus eram", 2: "dictus erās", 3: "dictus erat"}, "plural": {1: "dictī erāmus", 2: "dictī erātis", 3: "dictī erant"}}},
            "future perfect": {"active": {"singular": {1: "dīxerō", 2: "dīxeris", 3: "dīxerit"}, "plural": {1: "dīxerimus", 2: "dīxeritis", 3: "dīxerint"}}, "passive": {"singular": {1: "dictus erō", 2: "dictus eris", 3: "dictus erit"}, "plural": {1: "dictī erimus", 2: "dictī eritis", 3: "dictī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "dīc"}, "plural": {2: "dīcite"}}, "passive": {"singular": {2: "dīcere"}, "plural": {2: "dīciminī"}}},
            "future": {"active": {"singular": {2: "dīcitō", 3: "dīcitō"}, "plural": {2: "dīcitōte", 3: "dīcuntō"}}, "passive": {"singular": {2: "dīcitor", 3: "dīcitor"}, "plural": {3: "dīcuntor"}}}
        },
        "infinitives": {"present active": "dīcere", "present passive": "dīcī", "perfect active": "dīxisse", "perfect passive": "dictus esse", "future active": "dictūrus esse", "future passive": "dictum īrī"}
    },
    "vincere": {
        "indicative": {
            "present": {"active": {"singular": {1: "vincō", 2: "vincis", 3: "vincit"}, "plural": {1: "vincimus", 2: "vincitis", 3: "vincunt"}}, "passive": {"singular": {1: "vincor", 2: "vinceris", 3: "vincitur"}, "plural": {1: "vincimur", 2: "vinciminī", 3: "vincuntur"}}},
            "imperfect": {"active": {"singular": {1: "vincēbam", 2: "vincēbās", 3: "vincēbat"}, "plural": {1: "vincēbāmus", 2: "vincēbātis", 3: "vincēbant"}}, "passive": {"singular": {1: "vincēbar", 2: "vincēbāris", 3: "vincēbātur"}, "plural": {1: "vincēbāmur", 2: "vincēbāminī", 3: "vincēbantur"}}},
            "future": {"active": {"singular": {1: "vincam", 2: "vincēs", 3: "vincet"}, "plural": {1: "vincēmus", 2: "vincētis", 3: "vincent"}}, "passive": {"singular": {1: "vincar", 2: "vincēris", 3: "vincētur"}, "plural": {1: "vincēmur", 2: "vincēminī", 3: "vincentur"}}},
            "perfect": {"active": {"singular": {1: "vīcī", 2: "vīcistī", 3: "vīcit"}, "plural": {1: "vīcimus", 2: "vīcistis", 3: "vīcērunt"}}, "passive": {"singular": {1: "victus sum", 2: "victus es", 3: "victus est"}, "plural": {1: "victī sumus", 2: "victī estis", 3: "victī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "vīceram", 2: "vīcerās", 3: "vīcerat"}, "plural": {1: "vīcerāmus", 2: "vīcerātis", 3: "vīcerant"}}, "passive": {"singular": {1: "victus eram", 2: "victus erās", 3: "victus erat"}, "plural": {1: "victī erāmus", 2: "victī erātis", 3: "victī erant"}}},
            "future perfect": {"active": {"singular": {1: "vīcerō", 2: "vīceris", 3: "vīcerit"}, "plural": {1: "vīcerimus", 2: "vīceritis", 3: "vīcerint"}}, "passive": {"singular": {1: "victus erō", 2: "victus eris", 3: "victus erit"}, "plural": {1: "victī erimus", 2: "victī eritis", 3: "victī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "vince"}, "plural": {2: "vincite"}}, "passive": {"singular": {2: "vincere"}, "plural": {2: "vinciminī"}}},
            "future": {"active": {"singular": {2: "vincitō", 3: "vincitō"}, "plural": {2: "vincitōte", 3: "vincuntō"}}, "passive": {"singular": {2: "vincitor", 3: "vincitor"}, "plural": {3: "vincuntor"}}}
        },
        "infinitives": {"present active": "vincere", "present passive": "vincī", "perfect active": "vīcisse", "perfect passive": "victus esse", "future active": "victūrus esse", "future passive": "victum īrī"}
    },
    "legere": {
        "indicative": {
            "present": {"active": {"singular": {1: "legō", 2: "legis", 3: "legit"}, "plural": {1: "legimus", 2: "legitis", 3: "legunt"}}, "passive": {"singular": {1: "legor", 2: "legeris", 3: "legitur"}, "plural": {1: "legimur", 2: "legiminī", 3: "leguntur"}}},
            "imperfect": {"active": {"singular": {1: "legēbam", 2: "legēbās", 3: "legēbat"}, "plural": {1: "legēbāmus", 2: "legēbātis", 3: "legēbant"}}, "passive": {"singular": {1: "legēbar", 2: "legēbāris", 3: "legēbātur"}, "plural": {1: "legēbāmur", 2: "legēbāminī", 3: "legēbantur"}}},
            "future": {"active": {"singular": {1: "legam", 2: "legēs", 3: "leget"}, "plural": {1: "legēmus", 2: "legētis", 3: "legent"}}, "passive": {"singular": {1: "legar", 2: "legēris", 3: "legētur"}, "plural": {1: "legēmur", 2: "legēminī", 3: "legentur"}}},
            "perfect": {"active": {"singular": {1: "lēgī", 2: "lēgistī", 3: "lēgit"}, "plural": {1: "lēgimus", 2: "lēgistis", 3: "lēgērunt"}}, "passive": {"singular": {1: "lēctus sum", 2: "lēctus es", 3: "lēctus est"}, "plural": {1: "lēctī sumus", 2: "lēctī estis", 3: "lēctī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "lēgeram", 2: "lēgerās", 3: "lēgerat"}, "plural": {1: "lēgerāmus", 2: "lēgerātis", 3: "lēgerant"}}, "passive": {"singular": {1: "lēctus eram", 2: "lēctus erās", 3: "lēctus erat"}, "plural": {1: "lēctī erāmus", 2: "lēctī erātis", 3: "lēctī erant"}}},
            "future perfect": {"active": {"singular": {1: "lēgerō", 2: "lēgeris", 3: "lēgerit"}, "plural": {1: "lēgerimus", 2: "lēgeritis", 3: "lēgerint"}}, "passive": {"singular": {1: "lēctus erō", 2: "lēctus eris", 3: "lēctus erit"}, "plural": {1: "lēctī erimus", 2: "lēctī eritis", 3: "lēctī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "lege"}, "plural": {2: "legite"}}, "passive": {"singular": {2: "legere"}, "plural": {2: "legiminī"}}},
            "future": {"active": {"singular": {2: "legitō", 3: "legitō"}, "plural": {2: "legitōte", 3: "leguntō"}}, "passive": {"singular": {2: "legitor", 3: "legitor"}, "plural": {3: "leguntor"}}}
        },
        "infinitives": {"present active": "legere", "present passive": "legī", "perfect active": "lēgisse", "perfect passive": "lēctus esse", "future active": "lēctūrus esse", "future passive": "lēctum īrī"}
    },
    "scrībere": {
        "indicative": {
            "present": {"active": {"singular": {1: "scrībō", 2: "scrībis", 3: "scrībit"}, "plural": {1: "scrībimus", 2: "scrībitis", 3: "scrībunt"}}, "passive": {"singular": {1: "scrībor", 2: "scrīberis", 3: "scrībitur"}, "plural": {1: "scrībimur", 2: "scrībiminī", 3: "scrībuntur"}}},
            "imperfect": {"active": {"singular": {1: "scrībēbam", 2: "scrībēbās", 3: "scrībēbat"}, "plural": {1: "scrībēbāmus", 2: "scrībēbātis", 3: "scrībēbant"}}, "passive": {"singular": {1: "scrībēbar", 2: "scrībēbāris", 3: "scrībēbātur"}, "plural": {1: "scrībēbāmur", 2: "scrībēbāminī", 3: "scrībēbantur"}}},
            "future": {"active": {"singular": {1: "scrībam", 2: "scrībēs", 3: "scrībet"}, "plural": {1: "scrībēmus", 2: "scrībētis", 3: "scrībent"}}, "passive": {"singular": {1: "scrībar", 2: "scrībēris", 3: "scrībētur"}, "plural": {1: "scrībēmur", 2: "scrībēminī", 3: "scrībentur"}}},
            "perfect": {"active": {"singular": {1: "scrīpsī", 2: "scrīpsistī", 3: "scrīpsit"}, "plural": {1: "scrīpsimus", 2: "scrīpsistis", 3: "scrīpsērunt"}}, "passive": {"singular": {1: "scrīptus sum", 2: "scrīptus es", 3: "scrīptus est"}, "plural": {1: "scrīptī sumus", 2: "scrīptī estis", 3: "scrīptī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "scrīpseram", 2: "scrīpserās", 3: "scrīpserat"}, "plural": {1: "scrīpserāmus", 2: "scrīpserātis", 3: "scrīpserant"}}, "passive": {"singular": {1: "scrīptus eram", 2: "scrīptus erās", 3: "scrīptus erat"}, "plural": {1: "scrīptī erāmus", 2: "scrīptī erātis", 3: "scrīptī erant"}}},
            "future perfect": {"active": {"singular": {1: "scrīpserō", 2: "scrīpseris", 3: "scrīpserit"}, "plural": {1: "scrīpserimus", 2: "scrīpseritis", 3: "scrīpserint"}}, "passive": {"singular": {1: "scrīptus erō", 2: "scrīptus eris", 3: "scrīptus erit"}, "plural": {1: "scrīptī erimus", 2: "scrīptī eritis", 3: "scrīptī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "scrībe"}, "plural": {2: "scrībite"}}, "passive": {"singular": {2: "scrībere"}, "plural": {2: "scrībiminī"}}},
            "future": {"active": {"singular": {2: "scrībitō", 3: "scrībitō"}, "plural": {2: "scrībitōte", 3: "scrībuntō"}}, "passive": {"singular": {2: "scrībitor", 3: "scrībitor"}, "plural": {3: "scrībuntor"}}}
        },
        "infinitives": {"present active": "scrībere", "present passive": "scrībī", "perfect active": "scrīpsisse", "perfect passive": "scrīptus esse", "future active": "scrīptūrus esse", "future passive": "scrīptum īrī"}
    },
    "pellere": {
        "indicative": {
            "present": {"active": {"singular": {1: "pellō", 2: "pellis", 3: "pellit"}, "plural": {1: "pellimus", 2: "pellitis", 3: "pellunt"}}, "passive": {"singular": {1: "pellor", 2: "pelleris", 3: "pellitur"}, "plural": {1: "pellimur", 2: "pelliminī", 3: "pelluntur"}}},
            "imperfect": {"active": {"singular": {1: "pellēbam", 2: "pellēbās", 3: "pellēbat"}, "plural": {1: "pellēbāmus", 2: "pellēbātis", 3: "pellēbant"}}, "passive": {"singular": {1: "pellēbar", 2: "pellēbāris", 3: "pellēbātur"}, "plural": {1: "pellēbāmur", 2: "pellēbāminī", 3: "pellēbantur"}}},
            "future": {"active": {"singular": {1: "pellam", 2: "pellēs", 3: "pellet"}, "plural": {1: "pellēmus", 2: "pellētis", 3: "pellent"}}, "passive": {"singular": {1: "pellar", 2: "pellēris", 3: "pellētur"}, "plural": {1: "pellēmur", 2: "pellēminī", 3: "pellentur"}}},
            "perfect": {"active": {"singular": {1: "pepulī", 2: "pepulistī", 3: "pepulit"}, "plural": {1: "pepulimus", 2: "pepulistis", 3: "pepulērunt"}}, "passive": {"singular": {1: "pulsus sum", 2: "pulsus es", 3: "pulsus est"}, "plural": {1: "pulsī sumus", 2: "pulsī estis", 3: "pulsī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "pepuleram", 2: "pepulerās", 3: "pepulerat"}, "plural": {1: "pepulerāmus", 2: "pepulerātis", 3: "pepulerant"}}, "passive": {"singular": {1: "pulsus eram", 2: "pulsus erās", 3: "pulsus erat"}, "plural": {1: "pulsī erāmus", 2: "pulsī erātis", 3: "pulsī erant"}}},
            "future perfect": {"active": {"singular": {1: "pepulerō", 2: "pepuleris", 3: "pepulerit"}, "plural": {1: "pepulerimus", 2: "pepuleritis", 3: "pepulerint"}}, "passive": {"singular": {1: "pulsus erō", 2: "pulsus eris", 3: "pulsus erit"}, "plural": {1: "pulsī erimus", 2: "pulsī eritis", 3: "pulsī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "pelle"}, "plural": {2: "pellite"}}, "passive": {"singular": {2: "pellere"}, "plural": {2: "pelliminī"}}},
            "future": {"active": {"singular": {2: "pellitō", 3: "pellitō"}, "plural": {2: "pellitōte", 3: "pelluntō"}}, "passive": {"singular": {2: "pellitor", 3: "pellitor"}, "plural": {3: "pelluntor"}}}
        },
        "infinitives": {"present active": "pellere", "present passive": "pellī", "perfect active": "pepulisse", "perfect passive": "pulsus esse", "future active": "pulsūrus esse", "future passive": "pulsum īrī"}
    },

    # === 3RD i-stem CONJUGATION ===
    "capere": {
        "indicative": {
            "present": {"active": {"singular": {1: "capiō", 2: "capis", 3: "capit"}, "plural": {1: "capimus", 2: "capitis", 3: "capiunt"}}, "passive": {"singular": {1: "capior", 2: "caperis", 3: "capitur"}, "plural": {1: "capimur", 2: "capiminī", 3: "capiuntur"}}},
            "imperfect": {"active": {"singular": {1: "capiēbam", 2: "capiēbās", 3: "capiēbat"}, "plural": {1: "capiēbāmus", 2: "capiēbātis", 3: "capiēbant"}}, "passive": {"singular": {1: "capiēbar", 2: "capiēbāris", 3: "capiēbātur"}, "plural": {1: "capiēbāmur", 2: "capiēbāminī", 3: "capiēbantur"}}},
            "future": {"active": {"singular": {1: "capiam", 2: "capiēs", 3: "capiet"}, "plural": {1: "capiēmus", 2: "capiētis", 3: "capient"}}, "passive": {"singular": {1: "capiar", 2: "capiēris", 3: "capiētur"}, "plural": {1: "capiēmur", 2: "capiēminī", 3: "capientur"}}},
            "perfect": {"active": {"singular": {1: "cēpī", 2: "cēpistī", 3: "cēpit"}, "plural": {1: "cēpimus", 2: "cēpistis", 3: "cēpērunt"}}, "passive": {"singular": {1: "captus sum", 2: "captus es", 3: "captus est"}, "plural": {1: "captī sumus", 2: "captī estis", 3: "captī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "cēperam", 2: "cēperās", 3: "cēperat"}, "plural": {1: "cēperāmus", 2: "cēperātis", 3: "cēperant"}}, "passive": {"singular": {1: "captus eram", 2: "captus erās", 3: "captus erat"}, "plural": {1: "captī erāmus", 2: "captī erātis", 3: "captī erant"}}},
            "future perfect": {"active": {"singular": {1: "cēperō", 2: "cēperis", 3: "cēperit"}, "plural": {1: "cēperimus", 2: "cēperitis", 3: "cēperint"}}, "passive": {"singular": {1: "captus erō", 2: "captus eris", 3: "captus erit"}, "plural": {1: "captī erimus", 2: "captī eritis", 3: "captī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "cape"}, "plural": {2: "capite"}}, "passive": {"singular": {2: "capere"}, "plural": {2: "capiminī"}}},
            "future": {"active": {"singular": {2: "capitō", 3: "capitō"}, "plural": {2: "capitōte", 3: "capiuntō"}}, "passive": {"singular": {2: "capitor", 3: "capitor"}, "plural": {3: "capiuntor"}}}
        },
        "infinitives": {"present active": "capere", "present passive": "capī", "perfect active": "cēpisse", "perfect passive": "captus esse", "future active": "captūrus esse", "future passive": "captum īrī"}
    },
    "rapere": {
        "indicative": {
            "present": {"active": {"singular": {1: "rapiō", 2: "rapis", 3: "rapit"}, "plural": {1: "rapimus", 2: "rapitis", 3: "rapiunt"}}, "passive": {"singular": {1: "rapior", 2: "raperis", 3: "rapitur"}, "plural": {1: "rapimur", 2: "rapiminī", 3: "rapiuntur"}}},
            "imperfect": {"active": {"singular": {1: "rapiēbam", 2: "rapiēbās", 3: "rapiēbat"}, "plural": {1: "rapiēbāmus", 2: "rapiēbātis", 3: "rapiēbant"}}, "passive": {"singular": {1: "rapiēbar", 2: "rapiēbāris", 3: "rapiēbātur"}, "plural": {1: "rapiēbāmur", 2: "rapiēbāminī", 3: "rapiēbantur"}}},
            "future": {"active": {"singular": {1: "rapiam", 2: "rapiēs", 3: "rapiet"}, "plural": {1: "rapiēmus", 2: "rapiētis", 3: "rapient"}}, "passive": {"singular": {1: "rapiar", 2: "rapiēris", 3: "rapiētur"}, "plural": {1: "rapiēmur", 2: "rapiēminī", 3: "rapientur"}}},
            "perfect": {"active": {"singular": {1: "rapuī", 2: "rapuistī", 3: "rapuit"}, "plural": {1: "rapuimus", 2: "rapuistis", 3: "rapuērunt"}}, "passive": {"singular": {1: "raptus sum", 2: "raptus es", 3: "raptus est"}, "plural": {1: "raptī sumus", 2: "raptī estis", 3: "raptī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "rapueram", 2: "rapuerās", 3: "rapuerat"}, "plural": {1: "rapuerāmus", 2: "rapuerātis", 3: "rapuerant"}}, "passive": {"singular": {1: "raptus eram", 2: "raptus erās", 3: "raptus erat"}, "plural": {1: "raptī erāmus", 2: "raptī erātis", 3: "raptī erant"}}},
            "future perfect": {"active": {"singular": {1: "rapuerō", 2: "rapueris", 3: "rapuerit"}, "plural": {1: "rapuerimus", 2: "rapueritis", 3: "rapuerint"}}, "passive": {"singular": {1: "raptus erō", 2: "raptus eris", 3: "raptus erit"}, "plural": {1: "raptī erimus", 2: "raptī eritis", 3: "raptī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "rape"}, "plural": {2: "rapite"}}, "passive": {"singular": {2: "rapere"}, "plural": {2: "rapiminī"}}},
            "future": {"active": {"singular": {2: "rapitō", 3: "rapitō"}, "plural": {2: "rapitōte", 3: "rapiuntō"}}, "passive": {"singular": {2: "rapitor", 3: "rapitor"}, "plural": {3: "rapiuntor"}}}
        },
        "infinitives": {"present active": "rapere", "present passive": "rapī", "perfect active": "rapuisse", "perfect passive": "raptus esse", "future active": "raptūrus esse", "future passive": "raptum īrī"}
    },
    "iacere": {
        "indicative": {
            "present": {"active": {"singular": {1: "iaciō", 2: "iacis", 3: "iacit"}, "plural": {1: "iacimus", 2: "iacitis", 3: "iaciunt"}}, "passive": {"singular": {1: "iacior", 2: "iaceris", 3: "iacitur"}, "plural": {1: "iacimur", 2: "iaciminī", 3: "iaciuntur"}}},
            "imperfect": {"active": {"singular": {1: "iaciēbam", 2: "iaciēbās", 3: "iaciēbat"}, "plural": {1: "iaciēbāmus", 2: "iaciēbātis", 3: "iaciēbant"}}, "passive": {"singular": {1: "iaciēbar", 2: "iaciēbāris", 3: "iaciēbātur"}, "plural": {1: "iaciēbāmur", 2: "iaciēbāminī", 3: "iaciēbantur"}}},
            "future": {"active": {"singular": {1: "iaciam", 2: "iaciēs", 3: "iaciet"}, "plural": {1: "iaciēmus", 2: "iaciētis", 3: "iacient"}}, "passive": {"singular": {1: "iaciar", 2: "iaciēris", 3: "iaciētur"}, "plural": {1: "iaciēmur", 2: "iaciēminī", 3: "iacientur"}}},
            "perfect": {"active": {"singular": {1: "iēcī", 2: "iēcistī", 3: "iēcit"}, "plural": {1: "iēcimus", 2: "iēcistis", 3: "iēcērunt"}}, "passive": {"singular": {1: "iactus sum", 2: "iactus es", 3: "iactus est"}, "plural": {1: "iactī sumus", 2: "iactī estis", 3: "iactī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "iēceram", 2: "iēcerās", 3: "iēcerat"}, "plural": {1: "iēcerāmus", 2: "iēcerātis", 3: "iēcerant"}}, "passive": {"singular": {1: "iactus eram", 2: "iactus erās", 3: "iactus erat"}, "plural": {1: "iactī erāmus", 2: "iactī erātis", 3: "iactī erant"}}},
            "future perfect": {"active": {"singular": {1: "iēcerō", 2: "iēceris", 3: "iēcerit"}, "plural": {1: "iēcerimus", 2: "iēceritis", 3: "iēcerint"}}, "passive": {"singular": {1: "iactus erō", 2: "iactus eris", 3: "iactus erit"}, "plural": {1: "iactī erimus", 2: "iactī eritis", 3: "iactī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "iace"}, "plural": {2: "iacite"}}, "passive": {"singular": {2: "iacere"}, "plural": {2: "iaciminī"}}},
            "future": {"active": {"singular": {2: "iacitō", 3: "iacitō"}, "plural": {2: "iacitōte", 3: "iaciuntō"}}, "passive": {"singular": {2: "iacitor", 3: "iacitor"}, "plural": {3: "iaciuntor"}}}
        },
        "infinitives": {"present active": "iacere", "present passive": "iacī", "perfect active": "iēcisse", "perfect passive": "iactus esse", "future active": "iactūrus esse", "future passive": "iactum īrī"}
    },
    "accipere": {
        "indicative": {
            "present": {"active": {"singular": {1: "accipiō", 2: "accipis", 3: "accipit"}, "plural": {1: "accipimus", 2: "accipitis", 3: "accipiunt"}}, "passive": {"singular": {1: "accipior", 2: "acciperis", 3: "accipitur"}, "plural": {1: "accipimur", 2: "accipiminī", 3: "accipiuntur"}}},
            "imperfect": {"active": {"singular": {1: "accipiēbam", 2: "accipiēbās", 3: "accipiēbat"}, "plural": {1: "accipiēbāmus", 2: "accipiēbātis", 3: "accipiēbant"}}, "passive": {"singular": {1: "accipiēbar", 2: "accipiēbāris", 3: "accipiēbātur"}, "plural": {1: "accipiēbāmur", 2: "accipiēbāminī", 3: "accipiēbantur"}}},
            "future": {"active": {"singular": {1: "accipiam", 2: "accipiēs", 3: "accipiet"}, "plural": {1: "accipiēmus", 2: "accipiētis", 3: "accipient"}}, "passive": {"singular": {1: "accipiar", 2: "accipiēris", 3: "accipiētur"}, "plural": {1: "accipiēmur", 2: "accipiēminī", 3: "accipientur"}}},
            "perfect": {"active": {"singular": {1: "accēpī", 2: "accēpistī", 3: "accēpit"}, "plural": {1: "accēpimus", 2: "accēpistis", 3: "accēpērunt"}}, "passive": {"singular": {1: "acceptus sum", 2: "acceptus es", 3: "acceptus est"}, "plural": {1: "acceptī sumus", 2: "acceptī estis", 3: "acceptī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "accēperam", 2: "accēperās", 3: "accēperat"}, "plural": {1: "accēperāmus", 2: "accēperātis", 3: "accēperant"}}, "passive": {"singular": {1: "acceptus eram", 2: "acceptus erās", 3: "acceptus erat"}, "plural": {1: "acceptī erāmus", 2: "acceptī erātis", 3: "acceptī erant"}}},
            "future perfect": {"active": {"singular": {1: "accēperō", 2: "accēperis", 3: "accēperit"}, "plural": {1: "accēperimus", 2: "accēperitis", 3: "accēperint"}}, "passive": {"singular": {1: "acceptus erō", 2: "acceptus eris", 3: "acceptus erit"}, "plural": {1: "acceptī erimus", 2: "acceptī eritis", 3: "acceptī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "accipe"}, "plural": {2: "accipite"}}, "passive": {"singular": {2: "accipere"}, "plural": {2: "accipiminī"}}},
            "future": {"active": {"singular": {2: "accipitō", 3: "accipitō"}, "plural": {2: "accipitōte", 3: "accipiuntō"}}, "passive": {"singular": {2: "accipitor", 3: "accipitor"}, "plural": {3: "accipiuntor"}}}
        },
        "infinitives": {"present active": "accipere", "present passive": "accipī", "perfect active": "accēpisse", "perfect passive": "acceptus esse", "future active": "acceptūrus esse", "future passive": "acceptum īrī"}
    },
    "excipere": {
        "indicative": {
            "present": {"active": {"singular": {1: "excipiō", 2: "excipis", 3: "excipit"}, "plural": {1: "excipimus", 2: "excipitis", 3: "excipiunt"}}, "passive": {"singular": {1: "excipior", 2: "exciperis", 3: "excipitur"}, "plural": {1: "excipimur", 2: "excipiminī", 3: "excipiuntur"}}},
            "imperfect": {"active": {"singular": {1: "excipiēbam", 2: "excipiēbās", 3: "excipiēbat"}, "plural": {1: "excipiēbāmus", 2: "excipiēbātis", 3: "excipiēbant"}}, "passive": {"singular": {1: "excipiēbar", 2: "excipiēbāris", 3: "excipiēbātur"}, "plural": {1: "excipiēbāmur", 2: "excipiēbāminī", 3: "excipiēbantur"}}},
            "future": {"active": {"singular": {1: "excipiam", 2: "excipiēs", 3: "excipiet"}, "plural": {1: "excipiēmus", 2: "excipiētis", 3: "excipient"}}, "passive": {"singular": {1: "excipiar", 2: "excipiēris", 3: "excipiētur"}, "plural": {1: "excipiēmur", 2: "excipiēminī", 3: "excipientur"}}},
            "perfect": {"active": {"singular": {1: "excēpī", 2: "excēpistī", 3: "excēpit"}, "plural": {1: "excēpimus", 2: "excēpistis", 3: "excēpērunt"}}, "passive": {"singular": {1: "exceptus sum", 2: "exceptus es", 3: "exceptus est"}, "plural": {1: "exceptī sumus", 2: "exceptī estis", 3: "exceptī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "excēperam", 2: "excēperās", 3: "excēperat"}, "plural": {1: "excēperāmus", 2: "excēperātis", 3: "excēperant"}}, "passive": {"singular": {1: "exceptus eram", 2: "exceptus erās", 3: "exceptus erat"}, "plural": {1: "exceptī erāmus", 2: "exceptī erātis", 3: "exceptī erant"}}},
            "future perfect": {"active": {"singular": {1: "excēperō", 2: "excēperis", 3: "excēperit"}, "plural": {1: "excēperimus", 2: "excēperitis", 3: "excēperint"}}, "passive": {"singular": {1: "exceptus erō", 2: "exceptus eris", 3: "exceptus erit"}, "plural": {1: "exceptī erimus", 2: "exceptī eritis", 3: "exceptī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "excipe"}, "plural": {2: "excipite"}}, "passive": {"singular": {2: "excipere"}, "plural": {2: "excipiminī"}}},
            "future": {"active": {"singular": {2: "excipitō", 3: "excipitō"}, "plural": {2: "excipitōte", 3: "excipiuntō"}}, "passive": {"singular": {2: "excipitor", 3: "excipitor"}, "plural": {3: "excipiuntor"}}}
        },
        "infinitives": {"present active": "excipere", "present passive": "excipī", "perfect active": "excēpisse", "perfect passive": "exceptus esse", "future active": "exceptūrus esse", "future passive": "exceptum īrī"}
    },
    "dēcipere": {
        "indicative": {
            "present": {"active": {"singular": {1: "dēcipiō", 2: "dēcipis", 3: "dēcipit"}, "plural": {1: "dēcipimus", 2: "dēcipitis", 3: "dēcipiunt"}}, "passive": {"singular": {1: "dēcipior", 2: "dēciperis", 3: "dēcipitur"}, "plural": {1: "dēcipimur", 2: "dēcipiminī", 3: "dēcipiuntur"}}},
            "imperfect": {"active": {"singular": {1: "dēcipiēbam", 2: "dēcipiēbās", 3: "dēcipiēbat"}, "plural": {1: "dēcipiēbāmus", 2: "dēcipiēbātis", 3: "dēcipiēbant"}}, "passive": {"singular": {1: "dēcipiēbar", 2: "dēcipiēbāris", 3: "dēcipiēbātur"}, "plural": {1: "dēcipiēbāmur", 2: "dēcipiēbāminī", 3: "dēcipiēbantur"}}},
            "future": {"active": {"singular": {1: "dēcipiam", 2: "dēcipiēs", 3: "dēcipiet"}, "plural": {1: "dēcipiēmus", 2: "dēcipiētis", 3: "dēcipient"}}, "passive": {"singular": {1: "dēcipiar", 2: "dēcipiēris", 3: "dēcipiētur"}, "plural": {1: "dēcipiēmur", 2: "dēcipiēminī", 3: "dēcipientur"}}},
            "perfect": {"active": {"singular": {1: "dēcēpī", 2: "dēcēpistī", 3: "dēcēpit"}, "plural": {1: "dēcēpimus", 2: "dēcēpistis", 3: "dēcēpērunt"}}, "passive": {"singular": {1: "dēceptus sum", 2: "dēceptus es", 3: "dēceptus est"}, "plural": {1: "dēceptī sumus", 2: "dēceptī estis", 3: "dēceptī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "dēcēperam", 2: "dēcēperās", 3: "dēcēperat"}, "plural": {1: "dēcēperāmus", 2: "dēcēperātis", 3: "dēcēperant"}}, "passive": {"singular": {1: "dēceptus eram", 2: "dēceptus erās", 3: "dēceptus erat"}, "plural": {1: "dēceptī erāmus", 2: "dēceptī erātis", 3: "dēceptī erant"}}},
            "future perfect": {"active": {"singular": {1: "dēcēperō", 2: "dēcēperis", 3: "dēcēperit"}, "plural": {1: "dēcēperimus", 2: "dēcēperitis", 3: "dēcēperint"}}, "passive": {"singular": {1: "dēceptus erō", 2: "dēceptus eris", 3: "dēceptus erit"}, "plural": {1: "dēceptī erimus", 2: "dēceptī eritis", 3: "dēceptī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "dēcipe"}, "plural": {2: "dēcipite"}}, "passive": {"singular": {2: "dēcipere"}, "plural": {2: "dēcipiminī"}}},
            "future": {"active": {"singular": {2: "dēcipitō", 3: "dēcipitō"}, "plural": {2: "dēcipitōte", 3: "dēcipiuntō"}}, "passive": {"singular": {2: "dēcipitor", 3: "dēcipitor"}, "plural": {3: "dēcipiuntor"}}}
        },
        "infinitives": {"present active": "dēcipere", "present passive": "dēcipī", "perfect active": "dēcēpisse", "perfect passive": "dēceptus esse", "future active": "dēceptūrus esse", "future passive": "dēceptum īrī"}
    },
    "recipere": {
        "indicative": {
            "present": {"active": {"singular": {1: "recipiō", 2: "recipis", 3: "recipit"}, "plural": {1: "recipimus", 2: "recipitis", 3: "recipiunt"}}, "passive": {"singular": {1: "recipior", 2: "reciperis", 3: "recipitur"}, "plural": {1: "recipimur", 2: "recipiminī", 3: "recipiuntur"}}},
            "imperfect": {"active": {"singular": {1: "recipiēbam", 2: "recipiēbās", 3: "recipiēbat"}, "plural": {1: "recipiēbāmus", 2: "recipiēbātis", 3: "recipiēbant"}}, "passive": {"singular": {1: "recipiēbar", 2: "recipiēbāris", 3: "recipiēbātur"}, "plural": {1: "recipiēbāmur", 2: "recipiēbāminī", 3: "recipiēbantur"}}},
            "future": {"active": {"singular": {1: "recipiam", 2: "recipiēs", 3: "recipiet"}, "plural": {1: "recipiēmus", 2: "recipiētis", 3: "recipient"}}, "passive": {"singular": {1: "recipiar", 2: "recipiēris", 3: "recipiētur"}, "plural": {1: "recipiēmur", 2: "recipiēminī", 3: "recipientur"}}},
            "perfect": {"active": {"singular": {1: "recēpī", 2: "recēpistī", 3: "recēpit"}, "plural": {1: "recēpimus", 2: "recēpistis", 3: "recēpērunt"}}, "passive": {"singular": {1: "receptus sum", 2: "receptus es", 3: "receptus est"}, "plural": {1: "receptī sumus", 2: "receptī estis", 3: "receptī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "recēperam", 2: "recēperās", 3: "recēperat"}, "plural": {1: "recēperāmus", 2: "recēperātis", 3: "recēperant"}}, "passive": {"singular": {1: "receptus eram", 2: "receptus erās", 3: "receptus erat"}, "plural": {1: "receptī erāmus", 2: "receptī erātis", 3: "receptī erant"}}},
            "future perfect": {"active": {"singular": {1: "recēperō", 2: "recēperis", 3: "recēperit"}, "plural": {1: "recēperimus", 2: "recēperitis", 3: "recēperint"}}, "passive": {"singular": {1: "receptus erō", 2: "receptus eris", 3: "receptus erit"}, "plural": {1: "receptī erimus", 2: "receptī eritis", 3: "receptī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "recipe"}, "plural": {2: "recipite"}}, "passive": {"singular": {2: "recipere"}, "plural": {2: "recipiminī"}}},
            "future": {"active": {"singular": {2: "recipitō", 3: "recipitō"}, "plural": {2: "recipitōte", 3: "recipiuntō"}}, "passive": {"singular": {2: "recipitor", 3: "recipitor"}, "plural": {3: "recipiuntor"}}}
        },
        "infinitives": {"present active": "recipere", "present passive": "recipī", "perfect active": "recēpisse", "perfect passive": "receptus esse", "future active": "receptūrus esse", "future passive": "receptum īrī"}
    },
    "ēripere": {
        "indicative": {
            "present": {"active": {"singular": {1: "ēripiō", 2: "ēripis", 3: "ēripit"}, "plural": {1: "ēripimus", 2: "ēripitis", 3: "ēripiunt"}}, "passive": {"singular": {1: "ēripior", 2: "ēriperis", 3: "ēripitur"}, "plural": {1: "ēripimur", 2: "ēripiminī", 3: "ēripiuntur"}}},
            "imperfect": {"active": {"singular": {1: "ēripiēbam", 2: "ēripiēbās", 3: "ēripiēbat"}, "plural": {1: "ēripiēbāmus", 2: "ēripiēbātis", 3: "ēripiēbant"}}, "passive": {"singular": {1: "ēripiēbar", 2: "ēripiēbāris", 3: "ēripiēbātur"}, "plural": {1: "ēripiēbāmur", 2: "ēripiēbāminī", 3: "ēripiēbantur"}}},
            "future": {"active": {"singular": {1: "ēripiam", 2: "ēripiēs", 3: "ēripiet"}, "plural": {1: "ēripiēmus", 2: "ēripiētis", 3: "ēripient"}}, "passive": {"singular": {1: "ēripiar", 2: "ēripiēris", 3: "ēripiētur"}, "plural": {1: "ēripiēmur", 2: "ēripiēminī", 3: "ēripientur"}}},
            "perfect": {"active": {"singular": {1: "ēripuī", 2: "ēripuistī", 3: "ēripuit"}, "plural": {1: "ēripuimus", 2: "ēripuistis", 3: "ēripuērunt"}}, "passive": {"singular": {1: "ēreptus sum", 2: "ēreptus es", 3: "ēreptus est"}, "plural": {1: "ēreptī sumus", 2: "ēreptī estis", 3: "ēreptī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "ēripueram", 2: "ēripuerās", 3: "ēripuerat"}, "plural": {1: "ēripuerāmus", 2: "ēripuerātis", 3: "ēripuerant"}}, "passive": {"singular": {1: "ēreptus eram", 2: "ēreptus erās", 3: "ēreptus erat"}, "plural": {1: "ēreptī erāmus", 2: "ēreptī erātis", 3: "ēreptī erant"}}},
            "future perfect": {"active": {"singular": {1: "ēripuerō", 2: "ēripueris", 3: "ēripuerit"}, "plural": {1: "ēripuerimus", 2: "ēripueritis", 3: "ēripuerint"}}, "passive": {"singular": {1: "ēreptus erō", 2: "ēreptus eris", 3: "ēreptus erit"}, "plural": {1: "ēreptī erimus", 2: "ēreptī eritis", 3: "ēreptī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "ēripe"}, "plural": {2: "ēripite"}}, "passive": {"singular": {2: "ēripere"}, "plural": {2: "ēripiminī"}}},
            "future": {"active": {"singular": {2: "ēripitō", 3: "ēripitō"}, "plural": {2: "ēripitōte", 3: "ēripiuntō"}}, "passive": {"singular": {2: "ēripitor", 3: "ēripitor"}, "plural": {3: "ēripiuntor"}}}
        },
        "infinitives": {"present active": "ēripere", "present passive": "ēripī", "perfect active": "ēripuisse", "perfect passive": "ēreptus esse", "future active": "ēreptūrus esse", "future passive": "ēreptum īrī"}
    },
    "cōnspicere": {
        "indicative": {
            "present": {"active": {"singular": {1: "cōnspiciō", 2: "cōnspicis", 3: "cōnspicit"}, "plural": {1: "cōnspicimus", 2: "cōnspicitis", 3: "cōnspiciunt"}}, "passive": {"singular": {1: "cōnspicior", 2: "cōnsPiceris", 3: "cōnspicitur"}, "plural": {1: "cōnspicimur", 2: "cōnspiciminī", 3: "cōnspiciuntur"}}},
            "imperfect": {"active": {"singular": {1: "cōnspiciēbam", 2: "cōnspiciēbās", 3: "cōnspiciēbat"}, "plural": {1: "cōnspiciēbāmus", 2: "cōnspiciēbātis", 3: "cōnspiciēbant"}}, "passive": {"singular": {1: "cōnspiciēbar", 2: "cōnspiciēbāris", 3: "cōnspiciēbātur"}, "plural": {1: "cōnspiciēbāmur", 2: "cōnspiciēbāminī", 3: "cōnspiciēbantur"}}},
            "future": {"active": {"singular": {1: "cōnspiciam", 2: "cōnspiciēs", 3: "cōnspiciet"}, "plural": {1: "cōnspiciēmus", 2: "cōnspiciētis", 3: "cōnspicient"}}, "passive": {"singular": {1: "cōnspiciar", 2: "cōnspiciēris", 3: "cōnspiciētur"}, "plural": {1: "cōnspiciēmur", 2: "cōnspiciēminī", 3: "cōnspicientur"}}},
            "perfect": {"active": {"singular": {1: "cōnspexī", 2: "cōnspexistī", 3: "cōnspexit"}, "plural": {1: "cōnspeximus", 2: "cōnspexistis", 3: "cōnspexērunt"}}, "passive": {"singular": {1: "cōnspectus sum", 2: "cōnspectus es", 3: "cōnspectus est"}, "plural": {1: "cōnspectī sumus", 2: "cōnspectī estis", 3: "cōnspectī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "cōnspexeram", 2: "cōnspexerās", 3: "cōnspexerat"}, "plural": {1: "cōnspexerāmus", 2: "cōnspexerātis", 3: "cōnspexerant"}}, "passive": {"singular": {1: "cōnspectus eram", 2: "cōnspectus erās", 3: "cōnspectus erat"}, "plural": {1: "cōnspectī erāmus", 2: "cōnspectī erātis", 3: "cōnspectī erant"}}},
            "future perfect": {"active": {"singular": {1: "cōnspexerō", 2: "cōnspexeris", 3: "cōnspexerit"}, "plural": {1: "cōnspexerimus", 2: "cōnspexeritis", 3: "cōnspexerint"}}, "passive": {"singular": {1: "cōnspectus erō", 2: "cōnspectus eris", 3: "cōnspectus erit"}, "plural": {1: "cōnspectī erimus", 2: "cōnspectī eritis", 3: "cōnspectī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "cōnspice"}, "plural": {2: "cōnspicite"}}, "passive": {"singular": {2: "cōnspicere"}, "plural": {2: "cōnspiciminī"}}},
            "future": {"active": {"singular": {2: "cōnspicitō", 3: "cōnspicitō"}, "plural": {2: "cōnspicitōte", 3: "cōnspiciuntō"}}, "passive": {"singular": {2: "cōnspicitor", 3: "cōnspicitor"}, "plural": {3: "cōnspiciuntor"}}}
        },
        "infinitives": {"present active": "cōnspicere", "present passive": "cōnspicī", "perfect active": "cōnspexisse", "perfect passive": "cōnspectus esse", "future active": "cōnspectūrus esse", "future passive": "cōnspectum īrī"}
    },
    "dīripere": {
        "indicative": {
            "present": {"active": {"singular": {1: "dīripiō", 2: "dīripis", 3: "dīripit"}, "plural": {1: "dīripimus", 2: "dīripitis", 3: "dīripiunt"}}, "passive": {"singular": {1: "dīripior", 2: "dīriperis", 3: "dīripitur"}, "plural": {1: "dīripimur", 2: "dīripiminī", 3: "dīripiuntur"}}},
            "imperfect": {"active": {"singular": {1: "dīripiēbam", 2: "dīripiēbās", 3: "dīripiēbat"}, "plural": {1: "dīripiēbāmus", 2: "dīripiēbātis", 3: "dīripiēbant"}}, "passive": {"singular": {1: "dīripiēbar", 2: "dīripiēbāris", 3: "dīripiēbātur"}, "plural": {1: "dīripiēbāmur", 2: "dīripiēbāminī", 3: "dīripiēbantur"}}},
            "future": {"active": {"singular": {1: "dīripiam", 2: "dīripiēs", 3: "dīripiet"}, "plural": {1: "dīripiēmus", 2: "dīripiētis", 3: "dīripient"}}, "passive": {"singular": {1: "dīripiar", 2: "dīripiēris", 3: "dīripiētur"}, "plural": {1: "dīripiēmur", 2: "dīripiēminī", 3: "dīripientur"}}},
            "perfect": {"active": {"singular": {1: "dīripuī", 2: "dīripuistī", 3: "dīripuit"}, "plural": {1: "dīripuimus", 2: "dīripuistis", 3: "dīripuērunt"}}, "passive": {"singular": {1: "dīreptus sum", 2: "dīreptus es", 3: "dīreptus est"}, "plural": {1: "dīreptī sumus", 2: "dīreptī estis", 3: "dīreptī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "dīripueram", 2: "dīripuerās", 3: "dīripuerat"}, "plural": {1: "dīripuerāmus", 2: "dīripuerātis", 3: "dīripuerant"}}, "passive": {"singular": {1: "dīreptus eram", 2: "dīreptus erās", 3: "dīreptus erat"}, "plural": {1: "dīreptī erāmus", 2: "dīreptī erātis", 3: "dīreptī erant"}}},
            "future perfect": {"active": {"singular": {1: "dīripuerō", 2: "dīripueris", 3: "dīripuerit"}, "plural": {1: "dīripuerimus", 2: "dīripueritis", 3: "dīripuerint"}}, "passive": {"singular": {1: "dīreptus erō", 2: "dīreptus eris", 3: "dīreptus erit"}, "plural": {1: "dīreptī erimus", 2: "dīreptī eritis", 3: "dīreptī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "dīripe"}, "plural": {2: "dīripite"}}, "passive": {"singular": {2: "dīripere"}, "plural": {2: "dīripiminī"}}},
            "future": {"active": {"singular": {2: "dīripitō", 3: "dīripitō"}, "plural": {2: "dīripitōte", 3: "dīripiuntō"}}, "passive": {"singular": {2: "dīripitor", 3: "dīripitor"}, "plural": {3: "dīripiuntor"}}}
        },
        "infinitives": {"present active": "dīripere", "present passive": "dīripī", "perfect active": "dīripuisse", "perfect passive": "dīreptus esse", "future active": "dīreptūrus esse", "future passive": "dīreptum īrī"}
    },

    # === 4TH CONJUGATION ===
    "audīre": {
        "indicative": {
            "present": {"active": {"singular": {1: "audiō", 2: "audīs", 3: "audit"}, "plural": {1: "audīmus", 2: "audītis", 3: "audiunt"}}, "passive": {"singular": {1: "audior", 2: "audīris", 3: "audītur"}, "plural": {1: "audīmur", 2: "audīminī", 3: "audiuntur"}}},
            "imperfect": {"active": {"singular": {1: "audiēbam", 2: "audiēbās", 3: "audiēbat"}, "plural": {1: "audiēbāmus", 2: "audiēbātis", 3: "audiēbant"}}, "passive": {"singular": {1: "audiēbar", 2: "audiēbāris", 3: "audiēbātur"}, "plural": {1: "audiēbāmur", 2: "audiēbāminī", 3: "audiēbantur"}}},
            "future": {"active": {"singular": {1: "audiam", 2: "audiēs", 3: "audiet"}, "plural": {1: "audiēmus", 2: "audiētis", 3: "audient"}}, "passive": {"singular": {1: "audiar", 2: "audiēris", 3: "audiētur"}, "plural": {1: "audiēmur", 2: "audiēminī", 3: "audientur"}}},
            "perfect": {"active": {"singular": {1: "audīvī", 2: "audīvistī", 3: "audīvit"}, "plural": {1: "audīvimus", 2: "audīvistis", 3: "audīvērunt"}}, "passive": {"singular": {1: "audītus sum", 2: "audītus es", 3: "audītus est"}, "plural": {1: "audītī sumus", 2: "audītī estis", 3: "audītī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "audīveram", 2: "audīverās", 3: "audīverat"}, "plural": {1: "audīverāmus", 2: "audīverātis", 3: "audīverant"}}, "passive": {"singular": {1: "audītus eram", 2: "audītus erās", 3: "audītus erat"}, "plural": {1: "audītī erāmus", 2: "audītī erātis", 3: "audītī erant"}}},
            "future perfect": {"active": {"singular": {1: "audīverō", 2: "audīveris", 3: "audīverit"}, "plural": {1: "audīverimus", 2: "audīveritis", 3: "audīverint"}}, "passive": {"singular": {1: "audītus erō", 2: "audītus eris", 3: "audītus erit"}, "plural": {1: "audītī erimus", 2: "audītī eritis", 3: "audītī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "audī"}, "plural": {2: "audīte"}}, "passive": {"singular": {2: "audīre"}, "plural": {2: "audīminī"}}},
            "future": {"active": {"singular": {2: "audītō", 3: "audītō"}, "plural": {2: "audītōte", 3: "audiuntō"}}, "passive": {"singular": {2: "audītor", 3: "audītor"}, "plural": {3: "audiuntor"}}}
        },
        "infinitives": {"present active": "audīre", "present passive": "audīrī", "perfect active": "audīvisse", "perfect passive": "audītus esse", "future active": "audītūrus esse", "future passive": "audītum īrī"}
    },
    "scīre": {
        "indicative": {
            "present": {"active": {"singular": {1: "sciō", 2: "scīs", 3: "scit"}, "plural": {1: "scīmus", 2: "scītis", 3: "sciunt"}}, "passive": {"singular": {1: "scior", 2: "scīris", 3: "scītur"}, "plural": {1: "scīmur", 2: "scīminī", 3: "sciuntur"}}},
            "imperfect": {"active": {"singular": {1: "sciēbam", 2: "sciēbās", 3: "sciēbat"}, "plural": {1: "sciēbāmus", 2: "sciēbātis", 3: "sciēbant"}}, "passive": {"singular": {1: "sciēbar", 2: "sciēbāris", 3: "sciēbātur"}, "plural": {1: "sciēbāmur", 2: "sciēbāminī", 3: "sciēbantur"}}},
            "future": {"active": {"singular": {1: "sciam", 2: "sciēs", 3: "sciet"}, "plural": {1: "sciēmus", 2: "sciētis", 3: "scient"}}, "passive": {"singular": {1: "sciar", 2: "sciēris", 3: "sciētur"}, "plural": {1: "sciēmur", 2: "sciēminī", 3: "scientur"}}},
            "perfect": {"active": {"singular": {1: "scīvī", 2: "scīvistī", 3: "scīvit"}, "plural": {1: "scīvimus", 2: "scīvistis", 3: "scīvērunt"}}, "passive": {"singular": {1: "scītus sum", 2: "scītus es", 3: "scītus est"}, "plural": {1: "scītī sumus", 2: "scītī estis", 3: "scītī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "scīveram", 2: "scīverās", 3: "scīverat"}, "plural": {1: "scīverāmus", 2: "scīverātis", 3: "scīverant"}}, "passive": {"singular": {1: "scītus eram", 2: "scītus erās", 3: "scītus erat"}, "plural": {1: "scītī erāmus", 2: "scītī erātis", 3: "scītī erant"}}},
            "future perfect": {"active": {"singular": {1: "scīverō", 2: "scīveris", 3: "scīverit"}, "plural": {1: "scīverimus", 2: "scīveritis", 3: "scīverint"}}, "passive": {"singular": {1: "scītus erō", 2: "scītus eris", 3: "scītus erit"}, "plural": {1: "scītī erimus", 2: "scītī eritis", 3: "scītī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "scī"}, "plural": {2: "scīte"}}, "passive": {"singular": {2: "scīre"}, "plural": {2: "scīminī"}}},
            "future": {"active": {"singular": {2: "scītō", 3: "scītō"}, "plural": {2: "scītōte", 3: "sciuntō"}}, "passive": {"singular": {2: "scītor", 3: "scītor"}, "plural": {3: "sciuntor"}}}
        },
        "infinitives": {"present active": "scīre", "present passive": "scīrī", "perfect active": "scīvisse", "perfect passive": "scītus esse", "future active": "scītūrus esse", "future passive": "scītum īrī"}
    },
    "invenīre": {
        "indicative": {
            "present": {"active": {"singular": {1: "inveniō", 2: "invenīs", 3: "invenit"}, "plural": {1: "invenīmus", 2: "invenītis", 3: "inveniunt"}}, "passive": {"singular": {1: "invenior", 2: "invenīris", 3: "invenītur"}, "plural": {1: "invenīmur", 2: "invenīminī", 3: "inveniuntur"}}},
            "imperfect": {"active": {"singular": {1: "inveniēbam", 2: "inveniēbās", 3: "inveniēbat"}, "plural": {1: "inveniēbāmus", 2: "inveniēbātis", 3: "inveniēbant"}}, "passive": {"singular": {1: "inveniēbar", 2: "inveniēbāris", 3: "inveniēbātur"}, "plural": {1: "inveniēbāmur", 2: "inveniēbāminī", 3: "inveniēbantur"}}},
            "future": {"active": {"singular": {1: "inveniam", 2: "inveniēs", 3: "inveniet"}, "plural": {1: "inveniēmus", 2: "inveniētis", 3: "invenient"}}, "passive": {"singular": {1: "inveniar", 2: "inveniēris", 3: "inveniētur"}, "plural": {1: "inveniēmur", 2: "inveniēminī", 3: "invenientur"}}},
            "perfect": {"active": {"singular": {1: "invēnī", 2: "invēnistī", 3: "invēnit"}, "plural": {1: "invēnimus", 2: "invēnistis", 3: "invēnērunt"}}, "passive": {"singular": {1: "inventus sum", 2: "inventus es", 3: "inventus est"}, "plural": {1: "inventī sumus", 2: "inventī estis", 3: "inventī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "invēneram", 2: "invēnerās", 3: "invēnerat"}, "plural": {1: "invēnerāmus", 2: "invēnerātis", 3: "invēnerant"}}, "passive": {"singular": {1: "inventus eram", 2: "inventus erās", 3: "inventus erat"}, "plural": {1: "inventī erāmus", 2: "inventī erātis", 3: "inventī erant"}}},
            "future perfect": {"active": {"singular": {1: "invēnerō", 2: "invēneris", 3: "invēnerit"}, "plural": {1: "invēnerimus", 2: "invēneritis", 3: "invēnerint"}}, "passive": {"singular": {1: "inventus erō", 2: "inventus eris", 3: "inventus erit"}, "plural": {1: "inventī erimus", 2: "inventī eritis", 3: "inventī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "invenī"}, "plural": {2: "invenīte"}}, "passive": {"singular": {2: "invenīre"}, "plural": {2: "invenīminī"}}},
            "future": {"active": {"singular": {2: "invenītō", 3: "invenītō"}, "plural": {2: "invenītōte", 3: "inveniuntō"}}, "passive": {"singular": {2: "invenītor", 3: "invenītor"}, "plural": {3: "inveniuntor"}}}
        },
        "infinitives": {"present active": "invenīre", "present passive": "invenīrī", "perfect active": "invēnisse", "perfect passive": "inventus esse", "future active": "inventūrus esse", "future passive": "inventum īrī"}
    },
    "pūnīre": {
        "indicative": {
            "present": {"active": {"singular": {1: "pūniō", 2: "pūnīs", 3: "pūnit"}, "plural": {1: "pūnīmus", 2: "pūnītis", 3: "pūniunt"}}, "passive": {"singular": {1: "pūnior", 2: "pūnīris", 3: "pūnītur"}, "plural": {1: "pūnīmur", 2: "pūnīminī", 3: "pūniuntur"}}},
            "imperfect": {"active": {"singular": {1: "pūniēbam", 2: "pūniēbās", 3: "pūniēbat"}, "plural": {1: "pūniēbāmus", 2: "pūniēbātis", 3: "pūniēbant"}}, "passive": {"singular": {1: "pūniēbar", 2: "pūniēbāris", 3: "pūniēbātur"}, "plural": {1: "pūniēbāmur", 2: "pūniēbāminī", 3: "pūniēbantur"}}},
            "future": {"active": {"singular": {1: "pūniam", 2: "pūniēs", 3: "pūniet"}, "plural": {1: "pūniēmus", 2: "pūniētis", 3: "pūnient"}}, "passive": {"singular": {1: "pūniar", 2: "pūniēris", 3: "pūniētur"}, "plural": {1: "pūniēmur", 2: "pūniēminī", 3: "pūnientur"}}},
            "perfect": {"active": {"singular": {1: "pūnīvī", 2: "pūnīvistī", 3: "pūnīvit"}, "plural": {1: "pūnīvimus", 2: "pūnīvistis", 3: "pūnīvērunt"}}, "passive": {"singular": {1: "pūnītus sum", 2: "pūnītus es", 3: "pūnītus est"}, "plural": {1: "pūnītī sumus", 2: "pūnītī estis", 3: "pūnītī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "pūnīveram", 2: "pūnīverās", 3: "pūnīverat"}, "plural": {1: "pūnīverāmus", 2: "pūnīverātis", 3: "pūnīverant"}}, "passive": {"singular": {1: "pūnītus eram", 2: "pūnītus erās", 3: "pūnītus erat"}, "plural": {1: "pūnītī erāmus", 2: "pūnītī erātis", 3: "pūnītī erant"}}},
            "future perfect": {"active": {"singular": {1: "pūnīverō", 2: "pūnīveris", 3: "pūnīverit"}, "plural": {1: "pūnīverimus", 2: "pūnīveritis", 3: "pūnīverint"}}, "passive": {"singular": {1: "pūnītus erō", 2: "pūnītus eris", 3: "pūnītus erit"}, "plural": {1: "pūnītī erimus", 2: "pūnītī eritis", 3: "pūnītī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "pūnī"}, "plural": {2: "pūnīte"}}, "passive": {"singular": {2: "pūnīre"}, "plural": {2: "pūnīminī"}}},
            "future": {"active": {"singular": {2: "pūnītō", 3: "pūnītō"}, "plural": {2: "pūnītōte", 3: "pūniuntō"}}, "passive": {"singular": {2: "pūnītor", 3: "pūnītor"}, "plural": {3: "pūniuntor"}}}
        },
        "infinitives": {"present active": "pūnīre", "present passive": "pūnīrī", "perfect active": "pūnīvisse", "perfect passive": "pūnītus esse", "future active": "pūnītūrus esse", "future passive": "pūnītum īrī"}
    },
    "mūnīre": {
        "indicative": {
            "present": {"active": {"singular": {1: "mūniō", 2: "mūnīs", 3: "mūnit"}, "plural": {1: "mūnīmus", 2: "mūnītis", 3: "mūniunt"}}, "passive": {"singular": {1: "mūnior", 2: "mūnīris", 3: "mūnītur"}, "plural": {1: "mūnīmur", 2: "mūnīminī", 3: "mūniuntur"}}},
            "imperfect": {"active": {"singular": {1: "mūniēbam", 2: "mūniēbās", 3: "mūniēbat"}, "plural": {1: "mūniēbāmus", 2: "mūniēbātis", 3: "mūniēbant"}}, "passive": {"singular": {1: "mūniēbar", 2: "mūniēbāris", 3: "mūniēbātur"}, "plural": {1: "mūniēbāmur", 2: "mūniēbāminī", 3: "mūniēbantur"}}},
            "future": {"active": {"singular": {1: "mūniam", 2: "mūniēs", 3: "mūniet"}, "plural": {1: "mūniēmus", 2: "mūniētis", 3: "mūnient"}}, "passive": {"singular": {1: "mūniar", 2: "mūniēris", 3: "mūniētur"}, "plural": {1: "mūniēmur", 2: "mūniēminī", 3: "mūnientur"}}},
            "perfect": {"active": {"singular": {1: "mūnīvī", 2: "mūnīvistī", 3: "mūnīvit"}, "plural": {1: "mūnīvimus", 2: "mūnīvistis", 3: "mūnīvērunt"}}, "passive": {"singular": {1: "mūnītus sum", 2: "mūnītus es", 3: "mūnītus est"}, "plural": {1: "mūnītī sumus", 2: "mūnītī estis", 3: "mūnītī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "mūnīveram", 2: "mūnīverās", 3: "mūnīverat"}, "plural": {1: "mūnīverāmus", 2: "mūnīverātis", 3: "mūnīverant"}}, "passive": {"singular": {1: "mūnītus eram", 2: "mūnītus erās", 3: "mūnītus erat"}, "plural": {1: "mūnītī erāmus", 2: "mūnītī erātis", 3: "mūnītī erant"}}},
            "future perfect": {"active": {"singular": {1: "mūnīverō", 2: "mūnīveris", 3: "mūnīverit"}, "plural": {1: "mūnīverimus", 2: "mūnīveritis", 3: "mūnīverint"}}, "passive": {"singular": {1: "mūnītus erō", 2: "mūnītus eris", 3: "mūnītus erit"}, "plural": {1: "mūnītī erimus", 2: "mūnītī eritis", 3: "mūnītī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "mūnī"}, "plural": {2: "mūnīte"}}, "passive": {"singular": {2: "mūnīre"}, "plural": {2: "mūnīminī"}}},
            "future": {"active": {"singular": {2: "mūnītō", 3: "mūnītō"}, "plural": {2: "mūnītōte", 3: "mūniuntō"}}, "passive": {"singular": {2: "mūnītor", 3: "mūnītor"}, "plural": {3: "mūniuntor"}}}
        },
        "infinitives": {"present active": "mūnīre", "present passive": "mūnīrī", "perfect active": "mūnīvisse", "perfect passive": "mūnītus esse", "future active": "mūnītūrus esse", "future passive": "mūnītum īrī"}
    },
    "custōdīre": {
        "indicative": {
            "present": {"active": {"singular": {1: "custōdiō", 2: "custōdīs", 3: "custōdit"}, "plural": {1: "custōdīmus", 2: "custōdītis", 3: "custōdiunt"}}, "passive": {"singular": {1: "custōdior", 2: "custōdīris", 3: "custōdītur"}, "plural": {1: "custōdīmur", 2: "custōdīminī", 3: "custōdiuntur"}}},
            "imperfect": {"active": {"singular": {1: "custōdiēbam", 2: "custōdiēbās", 3: "custōdiēbat"}, "plural": {1: "custōdiēbāmus", 2: "custōdiēbātis", 3: "custōdiēbant"}}, "passive": {"singular": {1: "custōdiēbar", 2: "custōdiēbāris", 3: "custōdiēbātur"}, "plural": {1: "custōdiēbāmur", 2: "custōdiēbāminī", 3: "custōdiēbantur"}}},
            "future": {"active": {"singular": {1: "custōdiam", 2: "custōdiēs", 3: "custōdiet"}, "plural": {1: "custōdiēmus", 2: "custōdiētis", 3: "custōdient"}}, "passive": {"singular": {1: "custōdiar", 2: "custōdiēris", 3: "custōdiētur"}, "plural": {1: "custōdiēmur", 2: "custōdiēminī", 3: "custōdientur"}}},
            "perfect": {"active": {"singular": {1: "custōdīvī", 2: "custōdīvistī", 3: "custōdīvit"}, "plural": {1: "custōdīvimus", 2: "custōdīvistis", 3: "custōdīvērunt"}}, "passive": {"singular": {1: "custōdītus sum", 2: "custōdītus es", 3: "custōdītus est"}, "plural": {1: "custōdītī sumus", 2: "custōdītī estis", 3: "custōdītī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "custōdīveram", 2: "custōdīverās", 3: "custōdīverat"}, "plural": {1: "custōdīverāmus", 2: "custōdīverātis", 3: "custōdīverant"}}, "passive": {"singular": {1: "custōdītus eram", 2: "custōdītus erās", 3: "custōdītus erat"}, "plural": {1: "custōdītī erāmus", 2: "custōdītī erātis", 3: "custōdītī erant"}}},
            "future perfect": {"active": {"singular": {1: "custōdīverō", 2: "custōdīveris", 3: "custōdīverit"}, "plural": {1: "custōdīverimus", 2: "custōdīveritis", 3: "custōdīverint"}}, "passive": {"singular": {1: "custōdītus erō", 2: "custōdītus eris", 3: "custōdītus erit"}, "plural": {1: "custōdītī erimus", 2: "custōdītī eritis", 3: "custōdītī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "custōdī"}, "plural": {2: "custōdīte"}}, "passive": {"singular": {2: "custōdīre"}, "plural": {2: "custōdīminī"}}},
            "future": {"active": {"singular": {2: "custōdītō", 3: "custōdītō"}, "plural": {2: "custōdītōte", 3: "custōdiuntō"}}, "passive": {"singular": {2: "custōdītor", 3: "custōdītor"}, "plural": {3: "custōdiuntor"}}}
        },
        "infinitives": {"present active": "custōdīre", "present passive": "custōdīrī", "perfect active": "custōdīvisse", "perfect passive": "custōdītus esse", "future active": "custōdītūrus esse", "future passive": "custōdītum īrī"}
    },
    "impedīre": {
        "indicative": {
            "present": {"active": {"singular": {1: "impediō", 2: "impedīs", 3: "impedit"}, "plural": {1: "impedīmus", 2: "impedītis", 3: "impediunt"}}, "passive": {"singular": {1: "impedior", 2: "impedīris", 3: "impedītur"}, "plural": {1: "impedīmur", 2: "impedīminī", 3: "impediuntur"}}},
            "imperfect": {"active": {"singular": {1: "impediēbam", 2: "impediēbās", 3: "impediēbat"}, "plural": {1: "impediēbāmus", 2: "impediēbātis", 3: "impediēbant"}}, "passive": {"singular": {1: "impediēbar", 2: "impediēbāris", 3: "impediēbātur"}, "plural": {1: "impediēbāmur", 2: "impediēbāminī", 3: "impediēbantur"}}},
            "future": {"active": {"singular": {1: "impediam", 2: "impediēs", 3: "impediet"}, "plural": {1: "impediēmus", 2: "impediētis", 3: "impedient"}}, "passive": {"singular": {1: "impediar", 2: "impediēris", 3: "impediētur"}, "plural": {1: "impediēmur", 2: "impediēminī", 3: "impedientur"}}},
            "perfect": {"active": {"singular": {1: "impedīvī", 2: "impedīvistī", 3: "impedīvit"}, "plural": {1: "impedīvimus", 2: "impedīvistis", 3: "impedīvērunt"}}, "passive": {"singular": {1: "impedītus sum", 2: "impedītus es", 3: "impedītus est"}, "plural": {1: "impedītī sumus", 2: "impedītī estis", 3: "impedītī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "impedīveram", 2: "impedīverās", 3: "impedīverat"}, "plural": {1: "impedīverāmus", 2: "impedīverātis", 3: "impedīverant"}}, "passive": {"singular": {1: "impedītus eram", 2: "impedītus erās", 3: "impedītus erat"}, "plural": {1: "impedītī erāmus", 2: "impedītī erātis", 3: "impedītī erant"}}},
            "future perfect": {"active": {"singular": {1: "impedīverō", 2: "impedīveris", 3: "impedīverit"}, "plural": {1: "impedīverimus", 2: "impedīveritis", 3: "impedīverint"}}, "passive": {"singular": {1: "impedītus erō", 2: "impedītus eris", 3: "impedītus erit"}, "plural": {1: "impedītī erimus", 2: "impedītī eritis", 3: "impedītī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "impedī"}, "plural": {2: "impedīte"}}, "passive": {"singular": {2: "impedīre"}, "plural": {2: "impedīminī"}}},
            "future": {"active": {"singular": {2: "impedītō", 3: "impedītō"}, "plural": {2: "impedītōte", 3: "impediuntō"}}, "passive": {"singular": {2: "impedītor", 3: "impedītor"}, "plural": {3: "impediuntor"}}}
        },
        "infinitives": {"present active": "impedīre", "present passive": "impedīrī", "perfect active": "impedīvisse", "perfect passive": "impedītus esse", "future active": "impedītūrus esse", "future passive": "impedītum īrī"}
    },
    "fīnīre": {
        "indicative": {
            "present": {"active": {"singular": {1: "fīniō", 2: "fīnīs", 3: "fīnit"}, "plural": {1: "fīnīmus", 2: "fīnītis", 3: "fīniunt"}}, "passive": {"singular": {1: "fīnior", 2: "fīnīris", 3: "fīnītur"}, "plural": {1: "fīnīmur", 2: "fīnīminī", 3: "fīniuntur"}}},
            "imperfect": {"active": {"singular": {1: "fīniēbam", 2: "fīniēbās", 3: "fīniēbat"}, "plural": {1: "fīniēbāmus", 2: "fīniēbātis", 3: "fīniēbant"}}, "passive": {"singular": {1: "fīniēbar", 2: "fīniēbāris", 3: "fīniēbātur"}, "plural": {1: "fīniēbāmur", 2: "fīniēbāminī", 3: "fīniēbantur"}}},
            "future": {"active": {"singular": {1: "fīniam", 2: "fīniēs", 3: "fīniet"}, "plural": {1: "fīniēmus", 2: "fīniētis", 3: "fīnient"}}, "passive": {"singular": {1: "fīniar", 2: "fīniēris", 3: "fīniētur"}, "plural": {1: "fīniēmur", 2: "fīniēminī", 3: "fīnientur"}}},
            "perfect": {"active": {"singular": {1: "fīnīvī", 2: "fīnīvistī", 3: "fīnīvit"}, "plural": {1: "fīnīvimus", 2: "fīnīvistis", 3: "fīnīvērunt"}}, "passive": {"singular": {1: "fīnītus sum", 2: "fīnītus es", 3: "fīnītus est"}, "plural": {1: "fīnītī sumus", 2: "fīnītī estis", 3: "fīnītī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "fīnīveram", 2: "fīnīverās", 3: "fīnīverat"}, "plural": {1: "fīnīverāmus", 2: "fīnīverātis", 3: "fīnīverant"}}, "passive": {"singular": {1: "fīnītus eram", 2: "fīnītus erās", 3: "fīnītus erat"}, "plural": {1: "fīnītī erāmus", 2: "fīnītī erātis", 3: "fīnītī erant"}}},
            "future perfect": {"active": {"singular": {1: "fīnīverō", 2: "fīnīveris", 3: "fīnīverit"}, "plural": {1: "fīnīverimus", 2: "fīnīveritis", 3: "fīnīverint"}}, "passive": {"singular": {1: "fīnītus erō", 2: "fīnītus eris", 3: "fīnītus erit"}, "plural": {1: "fīnītī erimus", 2: "fīnītī eritis", 3: "fīnītī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "fīnī"}, "plural": {2: "fīnīte"}}, "passive": {"singular": {2: "fīnīre"}, "plural": {2: "fīnīminī"}}},
            "future": {"active": {"singular": {2: "fīnītō", 3: "fīnītō"}, "plural": {2: "fīnītōte", 3: "fīniuntō"}}, "passive": {"singular": {2: "fīnītor", 3: "fīnītor"}, "plural": {3: "fīniuntor"}}}
        },
        "infinitives": {"present active": "fīnīre", "present passive": "fīnīrī", "perfect active": "fīnīvisse", "perfect passive": "fīnītus esse", "future active": "fīnītūrus esse", "future passive": "fīnītum īrī"}
    },
    "aperīre": {
        "indicative": {
            "present": {"active": {"singular": {1: "aperiō", 2: "aperīs", 3: "aperit"}, "plural": {1: "aperīmus", 2: "aperītis", 3: "aperiunt"}}, "passive": {"singular": {1: "aperior", 2: "aperīris", 3: "aperītur"}, "plural": {1: "aperīmur", 2: "aperīminī", 3: "aperiuntur"}}},
            "imperfect": {"active": {"singular": {1: "aperiēbam", 2: "aperiēbās", 3: "aperiēbat"}, "plural": {1: "aperiēbāmus", 2: "aperiēbātis", 3: "aperiēbant"}}, "passive": {"singular": {1: "aperiēbar", 2: "aperiēbāris", 3: "aperiēbātur"}, "plural": {1: "aperiēbāmur", 2: "aperiēbāminī", 3: "aperiēbantur"}}},
            "future": {"active": {"singular": {1: "aperiam", 2: "aperiēs", 3: "aperiet"}, "plural": {1: "aperiēmus", 2: "aperiētis", 3: "aperient"}}, "passive": {"singular": {1: "aperiar", 2: "aperiēris", 3: "aperiētur"}, "plural": {1: "aperiēmur", 2: "aperiēminī", 3: "aperientur"}}},
            "perfect": {"active": {"singular": {1: "aperuī", 2: "aperuistī", 3: "aperuit"}, "plural": {1: "aperuimus", 2: "aperuistis", 3: "aperuērunt"}}, "passive": {"singular": {1: "apertus sum", 2: "apertus es", 3: "apertus est"}, "plural": {1: "apertī sumus", 2: "apertī estis", 3: "apertī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "aperueram", 2: "aperuerās", 3: "aperuerat"}, "plural": {1: "aperuerāmus", 2: "aperuerātis", 3: "aperuerant"}}, "passive": {"singular": {1: "apertus eram", 2: "apertus erās", 3: "apertus erat"}, "plural": {1: "apertī erāmus", 2: "apertī erātis", 3: "apertī erant"}}},
            "future perfect": {"active": {"singular": {1: "aperuerō", 2: "aperueris", 3: "aperuerit"}, "plural": {1: "aperuerimus", 2: "aperueritis", 3: "aperuerint"}}, "passive": {"singular": {1: "apertus erō", 2: "apertus eris", 3: "apertus erit"}, "plural": {1: "apertī erimus", 2: "apertī eritis", 3: "apertī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "aperī"}, "plural": {2: "aperīte"}}, "passive": {"singular": {2: "aperīre"}, "plural": {2: "aperīminī"}}},
            "future": {"active": {"singular": {2: "aperītō", 3: "aperītō"}, "plural": {2: "aperītōte", 3: "aperiuntō"}}, "passive": {"singular": {2: "aperītor", 3: "aperītor"}, "plural": {3: "aperiuntor"}}}
        },
        "infinitives": {"present active": "aperīre", "present passive": "aperīrī", "perfect active": "aperuisse", "perfect passive": "apertus esse", "future active": "apertūrus esse", "future passive": "apertum īrī"}
    },
    "reperīre": {
        "indicative": {
            "present": {"active": {"singular": {1: "reperiō", 2: "reperīs", 3: "reperit"}, "plural": {1: "reperīmus", 2: "reperītis", 3: "reperiunt"}}, "passive": {"singular": {1: "reperior", 2: "reperīris", 3: "reperītur"}, "plural": {1: "reperīmur", 2: "reperīminī", 3: "reperiuntur"}}},
            "imperfect": {"active": {"singular": {1: "reperiēbam", 2: "reperiēbās", 3: "reperiēbat"}, "plural": {1: "reperiēbāmus", 2: "reperiēbātis", 3: "reperiēbant"}}, "passive": {"singular": {1: "reperiēbar", 2: "reperiēbāris", 3: "reperiēbātur"}, "plural": {1: "reperiēbāmur", 2: "reperiēbāminī", 3: "reperiēbantur"}}},
            "future": {"active": {"singular": {1: "reperiam", 2: "reperiēs", 3: "reperiet"}, "plural": {1: "reperiēmus", 2: "reperiētis", 3: "reperient"}}, "passive": {"singular": {1: "reperiar", 2: "reperiēris", 3: "reperiētur"}, "plural": {1: "reperiēmur", 2: "reperiēminī", 3: "reperientur"}}},
            "perfect": {"active": {"singular": {1: "repperī", 2: "repperistī", 3: "repperit"}, "plural": {1: "repperimus", 2: "repperistis", 3: "repperērunt"}}, "passive": {"singular": {1: "repertus sum", 2: "repertus es", 3: "repertus est"}, "plural": {1: "repertī sumus", 2: "repertī estis", 3: "repertī sunt"}}},
            "pluperfect": {"active": {"singular": {1: "reppereram", 2: "reppererās", 3: "reppererat"}, "plural": {1: "reppererāmus", 2: "reppererātis", 3: "reppererant"}}, "passive": {"singular": {1: "repertus eram", 2: "repertus erās", 3: "repertus erat"}, "plural": {1: "repertī erāmus", 2: "repertī erātis", 3: "repertī erant"}}},
            "future perfect": {"active": {"singular": {1: "reppererō", 2: "reppereris", 3: "reppererit"}, "plural": {1: "reppererimus", 2: "reppereritis", 3: "reppererint"}}, "passive": {"singular": {1: "repertus erō", 2: "repertus eris", 3: "repertus erit"}, "plural": {1: "repertī erimus", 2: "repertī eritis", 3: "repertī erunt"}}}
        },
        "imperative": {
            "present": {"active": {"singular": {2: "reperī"}, "plural": {2: "reperīte"}}, "passive": {"singular": {2: "reperīre"}, "plural": {2: "reperīminī"}}},
            "future": {"active": {"singular": {2: "reperītō", 3: "reperītō"}, "plural": {2: "reperītōte", 3: "reperiuntō"}}, "passive": {"singular": {2: "reperītor", 3: "reperītor"}, "plural": {3: "reperiuntor"}}}
        },
        "infinitives": {"present active": "reperīre", "present passive": "reperīrī", "perfect active": "repperisse", "perfect passive": "repertus esse", "future active": "repertūrus esse", "future passive": "repertum īrī"}
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
        st.success(f"**Optimē!** Previous: {res['prompt']} → **{res['answer']}**")
    else:
        st.error(f"**Errāstī.** Previous: {res['prompt']} → **{res['answer']}**")

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
            "correct": is_correct
        }

        del st.session_state.current_q
        st.rerun()
