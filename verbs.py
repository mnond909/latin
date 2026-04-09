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
                           "plural": {1: "amābāmus", 2: "amābātis", 3: "amābant"}},
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
    },
    "laudāre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "laudō", 2: "laudās", 3: "laudat"},
                           "plural": {1: "laudāmus", 2: "laudātis", 3: "laudant"}},
                "passive": {"singular": {1: "laudor", 2: "laudāris", 3: "laudātur"},
                            "plural": {1: "laudāmur", 2: "laudāminī", 3: "laudantur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "laudābam", 2: "laudābās", 3: "laudābat"},
                           "plural": {1: "laudābāmus", 2: "laudābātis", 3: "laudābant"}},
                "passive": {"singular": {1: "laudābar", 2: "laudābāris", 3: "laudābātur"},
                            "plural": {1: "laudābāmur", 2: "laudābāminī", 3: "laudābantur"}}
            },
            "future": {
                "active": {"singular": {1: "laudābō", 2: "laudābis", 3: "laudābit"},
                           "plural": {1: "laudābimus", 2: "laudābitis", 3: "laudābunt"}},
                "passive": {"singular": {1: "laudābor", 2: "laudāberis", 3: "laudābitur"},
                            "plural": {1: "laudābimur", 2: "laudābiminī", 3: "laudābuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "laudāvī", 2: "laudāvistī", 3: "laudāvit"},
                           "plural": {1: "laudāvimus", 2: "laudāvistis", 3: "laudāvērunt"}},
                "passive": {"singular": {1: "laudātus sum", 2: "laudātus es", 3: "laudātus est"},
                            "plural": {1: "laudātī sumus", 2: "laudātī estis", 3: "laudātī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "laudāverō", 2: "laudāveris", 3: "laudāverit"},
                           "plural": {1: "laudāverimus", 2: "laudāveritis", 3: "laudāverint"}},
                "passive": {"singular": {1: "laudātus erō", 2: "laudātus eris", 3: "laudātus erit"},
                            "plural": {1: "laudātī erimus", 2: "laudātī eritis", 3: "laudātī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "laudā"}, "plural": {2: "laudāte"}},
                "passive": {"singular": {2: "laudāre"}, "plural": {2: "laudāminī"}}
            },
            "future": {
                "active": {"singular": {2: "laudātō", 3: "laudātō"}, "plural": {2: "laudātōte", 3: "laudantō"}},
                "passive": {"singular": {2: "laudātor", 3: "laudātor"}, "plural": {3: "laudantor"}}
            }
        },
        "infinitives": {
            "present active": "laudāre",
            "present passive": "laudārī",
            "perfect active": "laudāvisse",
            "perfect passive": "laudātus esse",
            "future active": "laudātūrus esse",
            "future passive": "laudātum īrī"
        }
    },
    "vidēre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "videō", 2: "vidēs", 3: "videt"},
                           "plural": {1: "vidēmus", 2: "vidētis", 3: "vident"}},
                "passive": {"singular": {1: "videor", 2: "vidēris", 3: "vidētur"},
                            "plural": {1: "vidēmur", 2: "vidēminī", 3: "videntur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "vidēbam", 2: "vidēbās", 3: "vidēbat"},
                           "plural": {1: "vidēbāmus", 2: "vidēbātis", 3: "vidēbant"}},
                "passive": {"singular": {1: "vidēbar", 2: "vidēbāris", 3: "vidēbātur"},
                            "plural": {1: "vidēbāmur", 2: "vidēbāminī", 3: "vidēbantur"}}
            },
            "future": {
                "active": {"singular": {1: "vidēbō", 2: "vidēbis", 3: "vidēbit"},
                           "plural": {1: "vidēbimus", 2: "vidēbitis", 3: "vidēbunt"}},
                "passive": {"singular": {1: "vidēbor", 2: "vidēberis", 3: "vidēbitur"},
                            "plural": {1: "vidēbimur", 2: "vidēbiminī", 3: "vidēbuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "vīdī", 2: "vīdistī", 3: "vīdit"},
                           "plural": {1: "vīdimus", 2: "vīdistis", 3: "vīdērunt"}},
                "passive": {"singular": {1: "vīsus sum", 2: "vīsus es", 3: "vīsus est"},
                            "plural": {1: "vīsī sumus", 2: "vīsī estis", 3: "vīsī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "vīderō", 2: "vīderis", 3: "vīderit"},
                           "plural": {1: "vīderimus", 2: "vīderitis", 3: "vīderint"}},
                "passive": {"singular": {1: "vīsus erō", 2: "vīsus eris", 3: "vīsus erit"},
                            "plural": {1: "vīsī erimus", 2: "vīsī eritis", 3: "vīsī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "vidē"}, "plural": {2: "vidēte"}},
                "passive": {"singular": {2: "vidēre"}, "plural": {2: "vidēminī"}}
            },
            "future": {
                "active": {"singular": {2: "vidētō", 3: "vidētō"}, "plural": {2: "vidētōte", 3: "videntō"}},
                "passive": {"singular": {2: "vidētor", 3: "vidētor"}, "plural": {3: "videntor"}}
            }
        },
        "infinitives": {
            "present active": "vidēre",
            "present passive": "vidērī",
            "perfect active": "vīdisse",
            "perfect passive": "vīsus esse",
            "future active": "vīsūrus esse",
            "future passive": "vīsum īrī"
        }
    },
    "vocāre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "vocō", 2: "vocās", 3: "vocat"},
                           "plural": {1: "vocāmus", 2: "vocātis", 3: "vocant"}},
                "passive": {"singular": {1: "vocor", 2: "vocāris", 3: "vocātur"},
                            "plural": {1: "vocāmur", 2: "vocāminī", 3: "vocantur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "vocābam", 2: "vocābās", 3: "vocābat"},
                           "plural": {1: "vocābāmus", 2: "vocābātis", 3: "vocābant"}},
                "passive": {"singular": {1: "vocābar", 2: "vocābāris", 3: "vocābātur"},
                            "plural": {1: "vocābāmur", 2: "vocābāminī", 3: "vocābantur"}}
            },
            "future": {
                "active": {"singular": {1: "vocābō", 2: "vocābis", 3: "vocābit"},
                           "plural": {1: "vocābimus", 2: "vocābitis", 3: "vocābunt"}},
                "passive": {"singular": {1: "vocābor", 2: "vocāberis", 3: "vocābitur"},
                            "plural": {1: "vocābimur", 2: "vocābiminī", 3: "vocābuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "vocāvī", 2: "vocāvistī", 3: "vocāvit"},
                           "plural": {1: "vocāvimus", 2: "vocāvistis", 3: "vocāvērunt"}},
                "passive": {"singular": {1: "vocātus sum", 2: "vocātus es", 3: "vocātus est"},
                            "plural": {1: "vocātī sumus", 2: "vocātī estis", 3: "vocātī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "vocāverō", 2: "vocāveris", 3: "vocāverit"},
                           "plural": {1: "vocāverimus", 2: "vocāveritis", 3: "vocāverint"}},
                "passive": {"singular": {1: "vocātus erō", 2: "vocātus eris", 3: "vocātus erit"},
                            "plural": {1: "vocātī erimus", 2: "vocātī eritis", 3: "vocātī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "vocā"}, "plural": {2: "vocāte"}},
                "passive": {"singular": {2: "vocāre"}, "plural": {2: "vocāminī"}}
            },
            "future": {
                "active": {"singular": {2: "vocātō", 3: "vocātō"}, "plural": {2: "vocātōte", 3: "vocantō"}},
                "passive": {"singular": {2: "vocātor", 3: "vocātor"}, "plural": {3: "vocantor"}}
            }
        },
        "infinitives": {
            "present active": "vocāre",
            "present passive": "vocārī",
            "perfect active": "vocāvisse",
            "perfect passive": "vocātus esse",
            "future active": "vocātūrus esse",
            "future passive": "vocātum īrī"
        }
    },
    "portāre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "portō", 2: "portās", 3: "portat"},
                           "plural": {1: "portāmus", 2: "portātis", 3: "portant"}},
                "passive": {"singular": {1: "portor", 2: "portāris", 3: "portātur"},
                            "plural": {1: "portāmur", 2: "portāminī", 3: "portantur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "portābam", 2: "portābās", 3: "portābat"},
                           "plural": {1: "portābāmus", 2: "portābātis", 3: "portābant"}},
                "passive": {"singular": {1: "portābar", 2: "portābāris", 3: "portābātur"},
                            "plural": {1: "portābāmur", 2: "portābāminī", 3: "portābantur"}}
            },
            "future": {
                "active": {"singular": {1: "portābō", 2: "portābis", 3: "portābit"},
                           "plural": {1: "portābimus", 2: "portābitis", 3: "portābunt"}},
                "passive": {"singular": {1: "portābor", 2: "portāberis", 3: "portābitur"},
                            "plural": {1: "portābimur", 2: "portābiminī", 3: "portābuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "portāvī", 2: "portāvistī", 3: "portāvit"},
                           "plural": {1: "portāvimus", 2: "portāvistis", 3: "portāvērunt"}},
                "passive": {"singular": {1: "portātus sum", 2: "portātus es", 3: "portātus est"},
                            "plural": {1: "portātī sumus", 2: "portātī estis", 3: "portātī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "portāverō", 2: "portāveris", 3: "portāverit"},
                           "plural": {1: "portāverimus", 2: "portāveritis", 3: "portāverint"}},
                "passive": {"singular": {1: "portātus erō", 2: "portātus eris", 3: "portātus erit"},
                            "plural": {1: "portātī erimus", 2: "portātī eritis", 3: "portātī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "portā"}, "plural": {2: "portāte"}},
                "passive": {"singular": {2: "portāre"}, "plural": {2: "portāminī"}}
            },
            "future": {
                "active": {"singular": {2: "portātō", 3: "portātō"}, "plural": {2: "portātōte", 3: "portantō"}},
                "passive": {"singular": {2: "portātor", 3: "portātor"}, "plural": {3: "portantor"}}
            }
        },
        "infinitives": {
            "present active": "portāre",
            "present passive": "portārī",
            "perfect active": "portāvisse",
            "perfect passive": "portātus esse",
            "future active": "portātūrus esse",
            "future passive": "portātum īrī"
        }
    },
    "parāre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "parō", 2: "parās", 3: "parat"},
                           "plural": {1: "parāmus", 2: "parātis", 3: "parant"}},
                "passive": {"singular": {1: "paror", 2: "parāris", 3: "parātur"},
                            "plural": {1: "parāmur", 2: "parāminī", 3: "parantur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "parābam", 2: "parābās", 3: "parābat"},
                           "plural": {1: "parābāmus", 2: "parābātis", 3: "parābant"}},
                "passive": {"singular": {1: "parābar", 2: "parābāris", 3: "parābātur"},
                            "plural": {1: "parābāmur", 2: "parābāminī", 3: "parābantur"}}
            },
            "future": {
                "active": {"singular": {1: "parābō", 2: "parābis", 3: "parābit"},
                           "plural": {1: "parābimus", 2: "parābitis", 3: "parābunt"}},
                "passive": {"singular": {1: "parābor", 2: "parāberis", 3: "parābitur"},
                            "plural": {1: "parābimur", 2: "parābiminī", 3: "parābuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "parāvī", 2: "parāvistī", 3: "parāvit"},
                           "plural": {1: "parāvimus", 2: "parāvistis", 3: "parāvērunt"}},
                "passive": {"singular": {1: "parātus sum", 2: "parātus es", 3: "parātus est"},
                            "plural": {1: "parātī sumus", 2: "parātī estis", 3: "parātī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "parāverō", 2: "parāveris", 3: "parāverit"},
                           "plural": {1: "parāverimus", 2: "parāveritis", 3: "parāverint"}},
                "passive": {"singular": {1: "parātus erō", 2: "parātus eris", 3: "parātus erit"},
                            "plural": {1: "parātī erimus", 2: "parātī eritis", 3: "parātī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "parā"}, "plural": {2: "parāte"}},
                "passive": {"singular": {2: "parāre"}, "plural": {2: "parāminī"}}
            },
            "future": {
                "active": {"singular": {2: "parātō", 3: "parātō"}, "plural": {2: "parātōte", 3: "parantō"}},
                "passive": {"singular": {2: "parātor", 3: "parātor"}, "plural": {3: "parantor"}}
            }
        },
        "infinitives": {
            "present active": "parāre",
            "present passive": "parārī",
            "perfect active": "parāvisse",
            "perfect passive": "parātus esse",
            "future active": "parātūrus esse",
            "future passive": "parātum īrī"
        }
    },
    "spectāre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "spectō", 2: "spectās", 3: "spectat"},
                           "plural": {1: "spectāmus", 2: "spectātis", 3: "spectant"}},
                "passive": {"singular": {1: "spector", 2: "spectāris", 3: "spectātur"},
                            "plural": {1: "spectāmur", 2: "spectāminī", 3: "spectantur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "spectābam", 2: "spectābās", 3: "spectābat"},
                           "plural": {1: "spectābāmus", 2: "spectābātis", 3: "spectābant"}},
                "passive": {"singular": {1: "spectābar", 2: "spectābāris", 3: "spectābātur"},
                            "plural": {1: "spectābāmur", 2: "spectābāminī", 3: "spectābantur"}}
            },
            "future": {
                "active": {"singular": {1: "spectābō", 2: "spectābis", 3: "spectābit"},
                           "plural": {1: "spectābimus", 2: "spectābitis", 3: "spectābunt"}},
                "passive": {"singular": {1: "spectābor", 2: "spectāberis", 3: "spectābitur"},
                            "plural": {1: "spectābimur", 2: "spectābiminī", 3: "spectābuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "spectāvī", 2: "spectāvistī", 3: "spectāvit"},
                           "plural": {1: "spectāvimus", 2: "spectāvistis", 3: "spectāvērunt"}},
                "passive": {"singular": {1: "spectātus sum", 2: "spectātus es", 3: "spectātus est"},
                            "plural": {1: "spectātī sumus", 2: "spectātī estis", 3: "spectātī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "spectāverō", 2: "spectāveris", 3: "spectāverit"},
                           "plural": {1: "spectāverimus", 2: "spectāveritis", 3: "spectāverint"}},
                "passive": {"singular": {1: "spectātus erō", 2: "spectātus eris", 3: "spectātus erit"},
                            "plural": {1: "spectātī erimus", 2: "spectātī eritis", 3: "spectātī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "spectā"}, "plural": {2: "spectāte"}},
                "passive": {"singular": {2: "spectāre"}, "plural": {2: "spectāminī"}}
            },
            "future": {
                "active": {"singular": {2: "spectātō", 3: "spectātō"}, "plural": {2: "spectātōte", 3: "spectantō"}},
                "passive": {"singular": {2: "spectātor", 3: "spectātor"}, "plural": {3: "spectantor"}}
            }
        },
        "infinitives": {
            "present active": "spectāre",
            "present passive": "spectārī",
            "perfect active": "spectāvisse",
            "perfect passive": "spectātus esse",
            "future active": "spectātūrus esse",
            "future passive": "spectātum īrī"
        }
    },
    "superāre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "superō", 2: "superās", 3: "superat"},
                           "plural": {1: "superāmus", 2: "superātis", 3: "superant"}},
                "passive": {"singular": {1: "superor", 2: "superāris", 3: "superātur"},
                            "plural": {1: "superāmur", 2: "superāminī", 3: "superantur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "superābam", 2: "superābās", 3: "superābat"},
                           "plural": {1: "superābāmus", 2: "superābātis", 3: "superābant"}},
                "passive": {"singular": {1: "superābar", 2: "superābāris", 3: "superābātur"},
                            "plural": {1: "superābāmur", 2: "superābāminī", 3: "superābantur"}}
            },
            "future": {
                "active": {"singular": {1: "superābō", 2: "superābis", 3: "superābit"},
                           "plural": {1: "superābimus", 2: "superābitis", 3: "superābunt"}},
                "passive": {"singular": {1: "superābor", 2: "superāberis", 3: "superābitur"},
                            "plural": {1: "superābimur", 2: "superābiminī", 3: "superābuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "superāvī", 2: "superāvistī", 3: "superāvit"},
                           "plural": {1: "superāvimus", 2: "superāvistis", 3: "superāvērunt"}},
                "passive": {"singular": {1: "superātus sum", 2: "superātus es", 3: "superātus est"},
                            "plural": {1: "superātī sumus", 2: "superātī estis", 3: "superātī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "superāverō", 2: "superāveris", 3: "superāverit"},
                           "plural": {1: "superāverimus", 2: "superāveritis", 3: "superāverint"}},
                "passive": {"singular": {1: "superātus erō", 2: "superātus eris", 3: "superātus erit"},
                            "plural": {1: "superātī erimus", 2: "superātī eritis", 3: "superātī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "superā"}, "plural": {2: "superāte"}},
                "passive": {"singular": {2: "superāre"}, "plural": {2: "superāminī"}}
            },
            "future": {
                "active": {"singular": {2: "superātō", 3: "superātō"}, "plural": {2: "superātōte", 3: "superantō"}},
                "passive": {"singular": {2: "superātor", 3: "superātor"}, "plural": {3: "superantor"}}
            }
        },
        "infinitives": {
            "present active": "superāre",
            "present passive": "superārī",
            "perfect active": "superāvisse",
            "perfect passive": "superātus esse",
            "future active": "superātūrus esse",
            "future passive": "superātum īrī"
        }
    },
    "vulnerāre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "vulnerō", 2: "vulnerās", 3: "vulnerat"},
                           "plural": {1: "vulnerāmus", 2: "vulnerātis", 3: "vulnerant"}},
                "passive": {"singular": {1: "vulneror", 2: "vulnerāris", 3: "vulnerātur"},
                            "plural": {1: "vulnerāmur", 2: "vulnerāminī", 3: "vulnerantur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "vulnerābam", 2: "vulnerābās", 3: "vulnerābat"},
                           "plural": {1: "vulnerābāmus", 2: "vulnerābātis", 3: "vulnerābant"}},
                "passive": {"singular": {1: "vulnerābar", 2: "vulnerābāris", 3: "vulnerābātur"},
                            "plural": {1: "vulnerābāmur", 2: "vulnerābāminī", 3: "vulnerābantur"}}
            },
            "future": {
                "active": {"singular": {1: "vulnerābō", 2: "vulnerābis", 3: "vulnerābit"},
                           "plural": {1: "vulnerābimus", 2: "vulnerābitis", 3: "vulnerābunt"}},
                "passive": {"singular": {1: "vulnerābor", 2: "vulnerāberis", 3: "vulnerābitur"},
                            "plural": {1: "vulnerābimur", 2: "vulnerābiminī", 3: "vulnerābuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "vulnerāvī", 2: "vulnerāvistī", 3: "vulnerāvit"},
                           "plural": {1: "vulnerāvimus", 2: "vulnerāvistis", 3: "vulnerāvērunt"}},
                "passive": {"singular": {1: "vulnerātus sum", 2: "vulnerātus es", 3: "vulnerātus est"},
                            "plural": {1: "vulnerātī sumus", 2: "vulnerātī estis", 3: "vulnerātī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "vulnerāverō", 2: "vulnerāveris", 3: "vulnerāverit"},
                           "plural": {1: "vulnerāverimus", 2: "vulnerāveritis", 3: "vulnerāverint"}},
                "passive": {"singular": {1: "vulnerātus erō", 2: "vulnerātus eris", 3: "vulnerātus erit"},
                            "plural": {1: "vulnerātī erimus", 2: "vulnerātī eritis", 3: "vulnerātī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "vulnerā"}, "plural": {2: "vulnerāte"}},
                "passive": {"singular": {2: "vulnerāre"}, "plural": {2: "vulnerāminī"}}
            },
            "future": {
                "active": {"singular": {2: "vulnerātō", 3: "vulnerātō"}, "plural": {2: "vulnerātōte", 3: "vulnerantō"}},
                "passive": {"singular": {2: "vulnerātor", 3: "vulnerātor"}, "plural": {3: "vulnerantor"}}
            }
        },
        "infinitives": {
            "present active": "vulnerāre",
            "present passive": "vulnerārī",
            "perfect active": "vulnerāvisse",
            "perfect passive": "vulnerātus esse",
            "future active": "vulnerātūrus esse",
            "future passive": "vulnerātum īrī"
        }
    },
    "oppugnāre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "oppugnō", 2: "oppugnās", 3: "oppugnat"},
                           "plural": {1: "oppugnāmus", 2: "oppugnātis", 3: "oppugnant"}},
                "passive": {"singular": {1: "oppugnor", 2: "oppugnāris", 3: "oppugnātur"},
                            "plural": {1: "oppugnāmur", 2: "oppugnāminī", 3: "oppugnantur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "oppugnābam", 2: "oppugnābās", 3: "oppugnābat"},
                           "plural": {1: "oppugnābāmus", 2: "oppugnābātis", 3: "oppugnābant"}},
                "passive": {"singular": {1: "oppugnābar", 2: "oppugnābāris", 3: "oppugnābātur"},
                            "plural": {1: "oppugnābāmur", 2: "oppugnābāminī", 3: "oppugnābantur"}}
            },
            "future": {
                "active": {"singular": {1: "oppugnābō", 2: "oppugnābis", 3: "oppugnābit"},
                           "plural": {1: "oppugnābimus", 2: "oppugnābitis", 3: "oppugnābunt"}},
                "passive": {"singular": {1: "oppugnābor", 2: "oppugnāberis", 3: "oppugnābitur"},
                            "plural": {1: "oppugnābimur", 2: "oppugnābiminī", 3: "oppugnābuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "oppugnāvī", 2: "oppugnāvistī", 3: "oppugnāvit"},
                           "plural": {1: "oppugnāvimus", 2: "oppugnāvistis", 3: "oppugnāvērunt"}},
                "passive": {"singular": {1: "oppugnātus sum", 2: "oppugnātus es", 3: "oppugnātus est"},
                            "plural": {1: "oppugnātī sumus", 2: "oppugnātī estis", 3: "oppugnātī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "oppugnāverō", 2: "oppugnāveris", 3: "oppugnāverit"},
                           "plural": {1: "oppugnāverimus", 2: "oppugnāveritis", 3: "oppugnāverint"}},
                "passive": {"singular": {1: "oppugnātus erō", 2: "oppugnātus eris", 3: "oppugnātus erit"},
                            "plural": {1: "oppugnātī erimus", 2: "oppugnātī eritis", 3: "oppugnātī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "oppugnā"}, "plural": {2: "oppugnāte"}},
                "passive": {"singular": {2: "oppugnāre"}, "plural": {2: "oppugnāminī"}}
            },
            "future": {
                "active": {"singular": {2: "oppugnātō", 3: "oppugnātō"}, "plural": {2: "oppugnātōte", 3: "oppugnantō"}},
                "passive": {"singular": {2: "oppugnātor", 3: "oppugnātor"}, "plural": {3: "oppugnantor"}}
            }
        },
        "infinitives": {
            "present active": "oppugnāre",
            "present passive": "oppugnārī",
            "perfect active": "oppugnāvisse",
            "perfect passive": "oppugnātus esse",
            "future active": "oppugnātūrus esse",
            "future passive": "oppugnātum īrī"
        }
    },
    "servāre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "servō", 2: "servās", 3: "servat"},
                           "plural": {1: "servāmus", 2: "servātis", 3: "servant"}},
                "passive": {"singular": {1: "servor", 2: "servāris", 3: "servātur"},
                            "plural": {1: "servāmur", 2: "servāminī", 3: "servantur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "servābam", 2: "servābās", 3: "servābat"},
                           "plural": {1: "servābāmus", 2: "servābātis", 3: "servābant"}},
                "passive": {"singular": {1: "servābar", 2: "servābāris", 3: "servābātur"},
                            "plural": {1: "servābāmur", 2: "servābāminī", 3: "servābantur"}}
            },
            "future": {
                "active": {"singular": {1: "servābō", 2: "servābis", 3: "servābit"},
                           "plural": {1: "servābimus", 2: "servābitis", 3: "servābunt"}},
                "passive": {"singular": {1: "servābor", 2: "servāberis", 3: "servābitur"},
                            "plural": {1: "servābimur", 2: "servābiminī", 3: "servābuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "servāvī", 2: "servāvistī", 3: "servāvit"},
                           "plural": {1: "servāvimus", 2: "servāvistis", 3: "servāvērunt"}},
                "passive": {"singular": {1: "servātus sum", 2: "servātus es", 3: "servātus est"},
                            "plural": {1: "servātī sumus", 2: "servātī estis", 3: "servātī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "servāverō", 2: "servāveris", 3: "servāverit"},
                           "plural": {1: "servāverimus", 2: "servāveritis", 3: "servāverint"}},
                "passive": {"singular": {1: "servātus erō", 2: "servātus eris", 3: "servātus erit"},
                            "plural": {1: "servātī erimus", 2: "servātī eritis", 3: "servātī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "servā"}, "plural": {2: "servāte"}},
                "passive": {"singular": {2: "servāre"}, "plural": {2: "servāminī"}}
            },
            "future": {
                "active": {"singular": {2: "servātō", 3: "servātō"}, "plural": {2: "servātōte", 3: "servantō"}},
                "passive": {"singular": {2: "servātor", 3: "servātor"}, "plural": {3: "servantor"}}
            }
        },
        "infinitives": {
            "present active": "servāre",
            "present passive": "servārī",
            "perfect active": "servāvisse",
            "perfect passive": "servātus esse",
            "future active": "servātūrus esse",
            "future passive": "servātum īrī"
        }
    },
    "habēre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "habeō", 2: "habēs", 3: "habet"},
                           "plural": {1: "habēmus", 2: "habētis", 3: "habent"}},
                "passive": {"singular": {1: "habeor", 2: "habēris", 3: "habētur"},
                            "plural": {1: "habēmur", 2: "habēminī", 3: "habentur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "habēbam", 2: "habēbās", 3: "habēbat"},
                           "plural": {1: "habēbāmus", 2: "habēbātis", 3: "habēbant"}},
                "passive": {"singular": {1: "habēbar", 2: "habēbāris", 3: "habēbātur"},
                            "plural": {1: "habēbāmur", 2: "habēbāminī", 3: "habēbantur"}}
            },
            "future": {
                "active": {"singular": {1: "habēbō", 2: "habēbis", 3: "habēbit"},
                           "plural": {1: "habēbimus", 2: "habēbitis", 3: "habēbunt"}},
                "passive": {"singular": {1: "habēbor", 2: "habēberis", 3: "habēbitur"},
                            "plural": {1: "habēbimur", 2: "habēbiminī", 3: "habēbuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "habuī", 2: "habuistī", 3: "habuit"},
                           "plural": {1: "habuimus", 2: "habuistis", 3: "habuērunt"}},
                "passive": {"singular": {1: "habitus sum", 2: "habitus es", 3: "habitus est"},
                            "plural": {1: "habitī sumus", 2: "habitī estis", 3: "habitī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "habuerō", 2: "habueris", 3: "habuerit"},
                           "plural": {1: "habuerimus", 2: "habueritis", 3: "habuerint"}},
                "passive": {"singular": {1: "habitus erō", 2: "habitus eris", 3: "habitus erit"},
                            "plural": {1: "habitī erimus", 2: "habitī eritis", 3: "habitī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "habē"}, "plural": {2: "habēte"}},
                "passive": {"singular": {2: "habēre"}, "plural": {2: "habēminī"}}
            },
            "future": {
                "active": {"singular": {2: "habētō", 3: "habētō"}, "plural": {2: "habētōte", 3: "habentō"}},
                "passive": {"singular": {2: "habētor", 3: "habētor"}, "plural": {3: "habentor"}}
            }
        },
        "infinitives": {
            "present active": "habēre",
            "present passive": "habērī",
            "perfect active": "habuisse",
            "perfect passive": "habitus esse",
            "future active": "habitūrus esse",
            "future passive": "habitum īrī"
        }
    },
    "docēre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "doceō", 2: "docēs", 3: "docet"},
                           "plural": {1: "docēmus", 2: "docētis", 3: "docent"}},
                "passive": {"singular": {1: "doceor", 2: "docēris", 3: "docētur"},
                            "plural": {1: "docēmur", 2: "docēminī", 3: "docentur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "docēbam", 2: "docēbās", 3: "docēbat"},
                           "plural": {1: "docēbāmus", 2: "docēbātis", 3: "docēbant"}},
                "passive": {"singular": {1: "docēbar", 2: "docēbāris", 3: "docēbātur"},
                            "plural": {1: "docēbāmur", 2: "docēbāminī", 3: "docēbantur"}}
            },
            "future": {
                "active": {"singular": {1: "docēbō", 2: "docēbis", 3: "docēbit"},
                           "plural": {1: "docēbimus", 2: "docēbitis", 3: "docēbunt"}},
                "passive": {"singular": {1: "docēbor", 2: "docēberis", 3: "docēbitur"},
                            "plural": {1: "docēbimur", 2: "docēbiminī", 3: "docēbuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "docuī", 2: "docuistī", 3: "docuit"},
                           "plural": {1: "docuimus", 2: "docuistis", 3: "docuērunt"}},
                "passive": {"singular": {1: "doctus sum", 2: "doctus es", 3: "doctus est"},
                            "plural": {1: "doctī sumus", 2: "doctī estis", 3: "doctī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "docuerō", 2: "docueris", 3: "docuerit"},
                           "plural": {1: "docuerimus", 2: "docueritis", 3: "docuerint"}},
                "passive": {"singular": {1: "doctus erō", 2: "doctus eris", 3: "doctus erit"},
                            "plural": {1: "doctī erimus", 2: "doctī eritis", 3: "doctī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "docē"}, "plural": {2: "docēte"}},
                "passive": {"singular": {2: "docēre"}, "plural": {2: "docēminī"}}
            },
            "future": {
                "active": {"singular": {2: "docētō", 3: "docētō"}, "plural": {2: "docētōte", 3: "docentō"}},
                "passive": {"singular": {2: "docētor", 3: "docētor"}, "plural": {3: "docentor"}}
            }
        },
        "infinitives": {
            "present active": "docēre",
            "present passive": "docērī",
            "perfect active": "docuisse",
            "perfect passive": "doctus esse",
            "future active": "doctūrus esse",
            "future passive": "doctum īrī"
        }
    },
    "tenēre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "teneō", 2: "tenēs", 3: "tenet"},
                           "plural": {1: "tenēmus", 2: "tenētis", 3: "tenent"}},
                "passive": {"singular": {1: "teneor", 2: "tenēris", 3: "tenētur"},
                            "plural": {1: "tenēmur", 2: "tenēminī", 3: "tenentur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "tenēbam", 2: "tenēbās", 3: "tenēbat"},
                           "plural": {1: "tenēbāmus", 2: "tenēbātis", 3: "tenēbant"}},
                "passive": {"singular": {1: "tenēbar", 2: "tenēbāris", 3: "tenēbātur"},
                            "plural": {1: "tenēbāmur", 2: "tenēbāminī", 3: "tenēbantur"}}
            },
            "future": {
                "active": {"singular": {1: "tenēbō", 2: "tenēbis", 3: "tenēbit"},
                           "plural": {1: "tenēbimus", 2: "tenēbitis", 3: "tenēbunt"}},
                "passive": {"singular": {1: "tenēbor", 2: "tenēberis", 3: "tenēbitur"},
                            "plural": {1: "tenēbimur", 2: "tenēbiminī", 3: "tenēbuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "tenuī", 2: "tenuistī", 3: "tenuit"},
                           "plural": {1: "tenuimus", 2: "tenuistis", 3: "tenuērunt"}},
                "passive": {"singular": {1: "tentus sum", 2: "tentus es", 3: "tentus est"},
                            "plural": {1: "tentī sumus", 2: "tentī estis", 3: "tentī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "tenuerō", 2: "tenueris", 3: "tenuerit"},
                           "plural": {1: "tenuerimus", 2: "tenueritis", 3: "tenuerint"}},
                "passive": {"singular": {1: "tentus erō", 2: "tentus eris", 3: "tentus erit"},
                            "plural": {1: "tentī erimus", 2: "tentī eritis", 3: "tentī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "tenē"}, "plural": {2: "tenēte"}},
                "passive": {"singular": {2: "tenēre"}, "plural": {2: "tenēminī"}}
            },
            "future": {
                "active": {"singular": {2: "tenētō", 3: "tenētō"}, "plural": {2: "tenētōte", 3: "tenentō"}},
                "passive": {"singular": {2: "tenētor", 3: "tenētor"}, "plural": {3: "tenentor"}}
            }
        },
        "infinitives": {
            "present active": "tenēre",
            "present passive": "tenērī",
            "perfect active": "tenuisse",
            "perfect passive": "tentus esse",
            "future active": "tentūrus esse",
            "future passive": "tentum īrī"
        }
    },
    "terrēre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "terreō", 2: "terrēs", 3: "terret"},
                           "plural": {1: "terrēmus", 2: "terrētis", 3: "terrent"}},
                "passive": {"singular": {1: "terreor", 2: "terrēris", 3: "terrētur"},
                            "plural": {1: "terrēmur", 2: "terrēminī", 3: "terrentur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "terrēbam", 2: "terrēbās", 3: "terrēbat"},
                           "plural": {1: "terrēbāmus", 2: "terrēbātis", 3: "terrēbant"}},
                "passive": {"singular": {1: "terrēbar", 2: "terrēbāris", 3: "terrēbātur"},
                            "plural": {1: "terrēbāmur", 2: "terrēbāminī", 3: "terrēbantur"}}
            },
            "future": {
                "active": {"singular": {1: "terrēbō", 2: "terrēbis", 3: "terrēbit"},
                           "plural": {1: "terrēbimus", 2: "terrēbitis", 3: "terrēbunt"}},
                "passive": {"singular": {1: "terrēbor", 2: "terrēberis", 3: "terrēbitur"},
                            "plural": {1: "terrēbimur", 2: "terrēbiminī", 3: "terrēbuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "terruī", 2: "terruistī", 3: "terruit"},
                           "plural": {1: "terruimus", 2: "terruistis", 3: "terruērunt"}},
                "passive": {"singular": {1: "territus sum", 2: "territus es", 3: "territus est"},
                            "plural": {1: "territī sumus", 2: "territī estis", 3: "territī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "terruerō", 2: "terrueris", 3: "terruerit"},
                           "plural": {1: "terruerimus", 2: "terrueritis", 3: "terruerint"}},
                "passive": {"singular": {1: "territus erō", 2: "territus eris", 3: "territus erit"},
                            "plural": {1: "territī erimus", 2: "territī eritis", 3: "territī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "terrē"}, "plural": {2: "terrēte"}},
                "passive": {"singular": {2: "terrēre"}, "plural": {2: "terrēminī"}}
            },
            "future": {
                "active": {"singular": {2: "terrētō", 3: "terrētō"}, "plural": {2: "terrētōte", 3: "terrentō"}},
                "passive": {"singular": {2: "terrētor", 3: "terrētor"}, "plural": {3: "terrentor"}}
            }
        },
        "infinitives": {
            "present active": "terrēre",
            "present passive": "terrērī",
            "perfect active": "terruisse",
            "perfect passive": "territus esse",
            "future active": "territūrus esse",
            "future passive": "territum īrī"
        }
    },
    "movēre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "moveō", 2: "movēs", 3: "movet"},
                           "plural": {1: "movēmus", 2: "movētis", 3: "movent"}},
                "passive": {"singular": {1: "moveor", 2: "movēris", 3: "movētur"},
                            "plural": {1: "movēmur", 2: "movēminī", 3: "moventur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "movēbam", 2: "movēbās", 3: "movēbat"},
                           "plural": {1: "movēbāmus", 2: "movēbātis", 3: "movēbant"}},
                "passive": {"singular": {1: "movēbar", 2: "movēbāris", 3: "movēbātur"},
                            "plural": {1: "movēbāmur", 2: "movēbāminī", 3: "movēbantur"}}
            },
            "future": {
                "active": {"singular": {1: "movēbō", 2: "movēbis", 3: "movēbit"},
                           "plural": {1: "movēbimus", 2: "movēbitis", 3: "movēbunt"}},
                "passive": {"singular": {1: "movēbor", 2: "movēberis", 3: "movēbitur"},
                            "plural": {1: "movēbimur", 2: "movēbiminī", 3: "movēbuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "mōvī", 2: "mōvistī", 3: "mōvit"},
                           "plural": {1: "mōvimus", 2: "mōvistis", 3: "mōvērunt"}},
                "passive": {"singular": {1: "mōtus sum", 2: "mōtus es", 3: "mōtus est"},
                            "plural": {1: "mōtī sumus", 2: "mōtī estis", 3: "mōtī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "mōverō", 2: "mōveris", 3: "mōverit"},
                           "plural": {1: "mōverimus", 2: "mōveritis", 3: "mōverint"}},
                "passive": {"singular": {1: "mōtus erō", 2: "mōtus eris", 3: "mōtus erit"},
                            "plural": {1: "mōtī erimus", 2: "mōtī eritis", 3: "mōtī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "movē"}, "plural": {2: "movēte"}},
                "passive": {"singular": {2: "movēre"}, "plural": {2: "movēminī"}}
            },
            "future": {
                "active": {"singular": {2: "movētō", 3: "movētō"}, "plural": {2: "movētōte", 3: "moventō"}},
                "passive": {"singular": {2: "movētor", 3: "movētor"}, "plural": {3: "moventor"}}
            }
        },
        "infinitives": {
            "present active": "movēre",
            "present passive": "movērī",
            "perfect active": "mōvisse",
            "perfect passive": "mōtus esse",
            "future active": "mōtūrus esse",
            "future passive": "mōtum īrī"
        }
    },
    "prohibēre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "prohibeō", 2: "prohibēs", 3: "prohibet"},
                           "plural": {1: "prohibēmus", 2: "prohibētis", 3: "prohibent"}},
                "passive": {"singular": {1: "prohibeor", 2: "prohibēris", 3: "prohibētur"},
                            "plural": {1: "prohibēmur", 2: "prohibēminī", 3: "prohibentur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "prohibēbam", 2: "prohibēbās", 3: "prohibēbat"},
                           "plural": {1: "prohibēbāmus", 2: "prohibēbātis", 3: "prohibēbant"}},
                "passive": {"singular": {1: "prohibēbar", 2: "prohibēbāris", 3: "prohibēbātur"},
                            "plural": {1: "prohibēbāmur", 2: "prohibēbāminī", 3: "prohibēbantur"}}
            },
            "future": {
                "active": {"singular": {1: "prohibēbō", 2: "prohibēbis", 3: "prohibēbit"},
                           "plural": {1: "prohibēbimus", 2: "prohibēbitis", 3: "prohibēbunt"}},
                "passive": {"singular": {1: "prohibēbor", 2: "prohibēberis", 3: "prohibēbitur"},
                            "plural": {1: "prohibēbimur", 2: "prohibēbiminī", 3: "prohibēbuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "prohibuī", 2: "prohibuistī", 3: "prohibuit"},
                           "plural": {1: "prohibuimus", 2: "prohibuistis", 3: "prohibuērunt"}},
                "passive": {"singular": {1: "prohibitus sum", 2: "prohibitus es", 3: "prohibitus est"},
                            "plural": {1: "prohibitī sumus", 2: "prohibitī estis", 3: "prohibitī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "prohibuerō", 2: "prohibueris", 3: "prohibuerit"},
                           "plural": {1: "prohibuerimus", 2: "prohibueritis", 3: "prohibuerint"}},
                "passive": {"singular": {1: "prohibitus erō", 2: "prohibitus eris", 3: "prohibitus erit"},
                            "plural": {1: "prohibitī erimus", 2: "prohibitī eritis", 3: "prohibitī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "prohibē"}, "plural": {2: "prohibēte"}},
                "passive": {"singular": {2: "prohibēre"}, "plural": {2: "prohibēminī"}}
            },
            "future": {
                "active": {"singular": {2: "prohibētō", 3: "prohibētō"}, "plural": {2: "prohibētōte", 3: "prohibentō"}},
                "passive": {"singular": {2: "prohibētor", 3: "prohibētor"}, "plural": {3: "prohibentor"}}
            }
        },
        "infinitives": {
            "present active": "prohibēre",
            "present passive": "prohibērī",
            "perfect active": "prohibuisse",
            "perfect passive": "prohibitus esse",
            "future active": "prohibitūrus esse",
            "future passive": "prohibitum īrī"
        }
    },
    "praebēre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "praebeō", 2: "praebēs", 3: "praebet"},
                           "plural": {1: "praebēmus", 2: "praebētis", 3: "praebent"}},
                "passive": {"singular": {1: "praebeor", 2: "praebēris", 3: "praebētur"},
                            "plural": {1: "praebēmur", 2: "praebēminī", 3: "praebentur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "praebēbam", 2: "praebēbās", 3: "praebēbat"},
                           "plural": {1: "praebēbāmus", 2: "praebēbātis", 3: "praebēbant"}},
                "passive": {"singular": {1: "praebēbar", 2: "praebēbāris", 3: "praebēbātur"},
                            "plural": {1: "praebēbāmur", 2: "praebēbāminī", 3: "praebēbantur"}}
            },
            "future": {
                "active": {"singular": {1: "praebēbō", 2: "praebēbis", 3: "praebēbit"},
                           "plural": {1: "praebēbimus", 2: "praebēbitis", 3: "praebēbunt"}},
                "passive": {"singular": {1: "praebēbor", 2: "praebēberis", 3: "praebēbitur"},
                            "plural": {1: "praebēbimur", 2: "praebēbiminī", 3: "praebēbuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "praebuī", 2: "praebuistī", 3: "praebuit"},
                           "plural": {1: "praebuimus", 2: "praebuistis", 3: "praebuērunt"}},
                "passive": {"singular": {1: "praebitus sum", 2: "praebitus es", 3: "praebitus est"},
                            "plural": {1: "praebitī sumus", 2: "praebitī estis", 3: "praebitī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "praebuerō", 2: "praebueris", 3: "praebuerit"},
                           "plural": {1: "praebuerimus", 2: "praebueritis", 3: "praebuerint"}},
                "passive": {"singular": {1: "praebitus erō", 2: "praebitus eris", 3: "praebitus erit"},
                            "plural": {1: "praebitī erimus", 2: "praebitī eritis", 3: "praebitī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "praebē"}, "plural": {2: "praebēte"}},
                "passive": {"singular": {2: "praebēre"}, "plural": {2: "praebēminī"}}
            },
            "future": {
                "active": {"singular": {2: "praebētō", 3: "praebētō"}, "plural": {2: "praebētōte", 3: "praebentō"}},
                "passive": {"singular": {2: "praebētor", 3: "praebētor"}, "plural": {3: "praebentor"}}
            }
        },
        "infinitives": {
            "present active": "praebēre",
            "present passive": "praebērī",
            "perfect active": "praebuisse",
            "perfect passive": "praebitus esse",
            "future active": "praebitūrus esse",
            "future passive": "praebitum īrī"
        }
    },
    "miscēre": {
        "indicative": {
            "present": {
                "active": {"singular": {1: "misceō", 2: "miscēs", 3: "miscet"},
                           "plural": {1: "miscēmus", 2: "miscētis", 3: "miscent"}},
                "passive": {"singular": {1: "misceor", 2: "miscēris", 3: "miscētur"},
                            "plural": {1: "miscēmur", 2: "miscēminī", 3: "miscentur"}}
            },
            "imperfect": {
                "active": {"singular": {1: "miscēbam", 2: "miscēbās", 3: "miscēbat"},
                           "plural": {1: "miscēbāmus", 2: "miscēbātis", 3: "miscēbant"}},
                "passive": {"singular": {1: "miscēbar", 2: "miscēbāris", 3: "miscēbātur"},
                            "plural": {1: "miscēbāmur", 2: "miscēbāminī", 3: "miscēbantur"}}
            },
            "future": {
                "active": {"singular": {1: "miscēbō", 2: "miscēbis", 3: "miscēbit"},
                           "plural": {1: "miscēbimus", 2: "miscēbitis", 3: "miscēbunt"}},
                "passive": {"singular": {1: "miscēbor", 2: "miscēberis", 3: "miscēbitur"},
                            "plural": {1: "miscēbimur", 2: "miscēbiminī", 3: "miscēbuntur"}}
            },
            "perfect": {
                "active": {"singular": {1: "miscuī", 2: "miscuistī", 3: "miscuit"},
                           "plural": {1: "miscuimus", 2: "miscuistis", 3: "miscuērunt"}},
                "passive": {"singular": {1: "mixtus sum", 2: "mixtus es", 3: "mixtus est"},
                            "plural": {1: "mixtī sumus", 2: "mixtī estis", 3: "mixtī sunt"}}
            },
            "future perfect": {
                "active": {"singular": {1: "miscuerō", 2: "miscueris", 3: "miscuerit"},
                           "plural": {1: "miscuerimus", 2: "miscueritis", 3: "miscuerint"}},
                "passive": {"singular": {1: "mixtus erō", 2: "mixtus eris", 3: "mixtus erit"},
                            "plural": {1: "mixtī erimus", 2: "mixtī eritis", 3: "mixtī erunt"}}
            }
        },
        "imperative": {
            "present": {
                "active": {"singular": {2: "miscē"}, "plural": {2: "miscēte"}},
                "passive": {"singular": {2: "miscēre"}, "plural": {2: "miscēminī"}}
            },
            "future": {
                "active": {"singular": {2: "miscētō", 3: "miscētō"}, "plural": {2: "miscētōte", 3: "miscentō"}},
                "passive": {"singular": {2: "miscētor", 3: "miscētor"}, "plural": {3: "miscentor"}}
            }
        },
        "infinitives": {
            "present active": "miscēre",
            "present passive": "miscērī",
            "perfect active": "miscuisse",
            "perfect passive": "mixtus esse",
            "future active": "mixtūrus esse",
            "future passive": "mixtum īrī"
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
        
