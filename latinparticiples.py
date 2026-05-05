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

forms_db = {
    # === 1ST CONJUGATION ===
    "amāre": {
        "Present Active Participle": {"form": "amāns", "meaning": "loving"},
        "Perfect Passive Participle": {"form": "amātus", "meaning": "having been loved"},
        "Future Active Participle": {"form": "amātūrus", "meaning": "about to love"},
        "Future Passive Participle (Gerundive)": {"form": "amandus", "meaning": "to be loved (must be loved)"},
        "Gerund (Genitive)": {"form": "amandī", "meaning": "of loving"},
        "Supine (Accusative)": {"form": "amātum", "meaning": "to love (purpose)"},
        "Supine (Ablative)": {"form": "amātū", "meaning": "to love (respect)"}
    },
    "laudāre": {
        "Present Active Participle": {"form": "laudāns", "meaning": "praising"},
        "Perfect Passive Participle": {"form": "laudātus", "meaning": "having been praised"},
        "Future Active Participle": {"form": "laudātūrus", "meaning": "about to praise"},
        "Future Passive Participle (Gerundive)": {"form": "laudandus", "meaning": "to be praised (must be praised)"},
        "Gerund (Genitive)": {"form": "laudandī", "meaning": "of praising"},
        "Supine (Accusative)": {"form": "laudātum", "meaning": "to praise (purpose)"},
        "Supine (Ablative)": {"form": "laudātū", "meaning": "to praise (respect)"}
    },
    "vocāre": {
        "Present Active Participle": {"form": "vocāns", "meaning": "calling"},
        "Perfect Passive Participle": {"form": "vocātus", "meaning": "having been called"},
        "Future Active Participle": {"form": "vocātūrus", "meaning": "about to call"},
        "Future Passive Participle (Gerundive)": {"form": "vocandus", "meaning": "to be called (must be called)"},
        "Gerund (Genitive)": {"form": "vocandī", "meaning": "of calling"},
        "Supine (Accusative)": {"form": "vocātum", "meaning": "to call (purpose)"},
        "Supine (Ablative)": {"form": "vocātū", "meaning": "to call (respect)"}
    },
    "portāre": {
        "Present Active Participle": {"form": "portāns", "meaning": "carrying"},
        "Perfect Passive Participle": {"form": "portātus", "meaning": "having been carried"},
        "Future Active Participle": {"form": "portātūrus", "meaning": "about to carry"},
        "Future Passive Participle (Gerundive)": {"form": "portandus", "meaning": "to be carried (must be carried)"},
        "Gerund (Genitive)": {"form": "portandī", "meaning": "of carrying"},
        "Supine (Accusative)": {"form": "portātum", "meaning": "to carry (purpose)"},
        "Supine (Ablative)": {"form": "portātū", "meaning": "to carry (respect)"}
    },
    "parāre": {
        "Present Active Participle": {"form": "parāns", "meaning": "preparing"},
        "Perfect Passive Participle": {"form": "parātus", "meaning": "having been prepared"},
        "Future Active Participle": {"form": "parātūrus", "meaning": "about to prepare"},
        "Future Passive Participle (Gerundive)": {"form": "parandus", "meaning": "to be prepared (must be prepared)"},
        "Gerund (Genitive)": {"form": "parandī", "meaning": "of preparing"},
        "Supine (Accusative)": {"form": "parātum", "meaning": "to prepare (purpose)"},
        "Supine (Ablative)": {"form": "parātū", "meaning": "to prepare (respect)"}
    },
    "spectāre": {
        "Present Active Participle": {"form": "spectāns", "meaning": "watching"},
        "Perfect Passive Participle": {"form": "spectātus", "meaning": "having been watched"},
        "Future Active Participle": {"form": "spectātūrus", "meaning": "about to watch"},
        "Future Passive Participle (Gerundive)": {"form": "spectandus", "meaning": "to be watched (must be watched)"},
        "Gerund (Genitive)": {"form": "spectandī", "meaning": "of watching"},
        "Supine (Accusative)": {"form": "spectātum", "meaning": "to watch (purpose)"},
        "Supine (Ablative)": {"form": "spectātū", "meaning": "to watch (respect)"}
    },
    "superāre": {
        "Present Active Participle": {"form": "superāns", "meaning": "overcoming"},
        "Perfect Passive Participle": {"form": "superātus", "meaning": "having been overcome"},
        "Future Active Participle": {"form": "superātūrus", "meaning": "about to overcome"},
        "Future Passive Participle (Gerundive)": {"form": "superandus", "meaning": "to be overcome (must be overcome)"},
        "Gerund (Genitive)": {"form": "superandī", "meaning": "of overcoming"},
        "Supine (Accusative)": {"form": "superātum", "meaning": "to overcome (purpose)"},
        "Supine (Ablative)": {"form": "superātū", "meaning": "to overcome (respect)"}
    },
    "vulnerāre": {
        "Present Active Participle": {"form": "vulnerāns", "meaning": "wounding"},
        "Perfect Passive Participle": {"form": "vulnerātus", "meaning": "having been wounded"},
        "Future Active Participle": {"form": "vulnerātūrus", "meaning": "about to wound"},
        "Future Passive Participle (Gerundive)": {"form": "vulnerandus", "meaning": "to be wounded (must be wounded)"},
        "Gerund (Genitive)": {"form": "vulnerandī", "meaning": "of wounding"},
        "Supine (Accusative)": {"form": "vulnerātum", "meaning": "to wound (purpose)"},
        "Supine (Ablative)": {"form": "vulnerātū", "meaning": "to wound (respect)"}
    },
    "oppugnāre": {
        "Present Active Participle": {"form": "oppugnāns", "meaning": "attacking"},
        "Perfect Passive Participle": {"form": "oppugnātus", "meaning": "having been attacked"},
        "Future Active Participle": {"form": "oppugnātūrus", "meaning": "about to attack"},
        "Future Passive Participle (Gerundive)": {"form": "oppugnandus", "meaning": "to be attacked (must be attacked)"},
        "Gerund (Genitive)": {"form": "oppugnandī", "meaning": "of attacking"},
        "Supine (Accusative)": {"form": "oppugnātum", "meaning": "to attack (purpose)"},
        "Supine (Ablative)": {"form": "oppugnātū", "meaning": "to attack (respect)"}
    },
    "servāre": {
        "Present Active Participle": {"form": "servāns", "meaning": "saving"},
        "Perfect Passive Participle": {"form": "servātus", "meaning": "having been saved"},
        "Future Active Participle": {"form": "servātūrus", "meaning": "about to save"},
        "Future Passive Participle (Gerundive)": {"form": "servandus", "meaning": "to be saved (must be saved)"},
        "Gerund (Genitive)": {"form": "servandī", "meaning": "of saving"},
        "Supine (Accusative)": {"form": "servātum", "meaning": "to save (purpose)"},
        "Supine (Ablative)": {"form": "servātū", "meaning": "to save (respect)"}
    },

    # === 2ND CONJUGATION ===
    "monēre": {
        "Present Active Participle": {"form": "monēns", "meaning": "warning"},
        "Perfect Passive Participle": {"form": "monitus", "meaning": "having been warned"},
        "Future Active Participle": {"form": "monitūrus", "meaning": "about to warn"},
        "Future Passive Participle (Gerundive)": {"form": "monendus", "meaning": "to be warned (must be warned)"},
        "Gerund (Genitive)": {"form": "monendī", "meaning": "of warning"},
        "Supine (Accusative)": {"form": "monitum", "meaning": "to warn (purpose)"},
        "Supine (Ablative)": {"form": "monitū", "meaning": "to warn (respect)"}
    },
    "vidēre": {
        "Present Active Participle": {"form": "vidēns", "meaning": "seeing"},
        "Perfect Passive Participle": {"form": "vīsus", "meaning": "having been seen"},
        "Future Active Participle": {"form": "vīsūrus", "meaning": "about to see"},
        "Future Passive Participle (Gerundive)": {"form": "videndus", "meaning": "to be seen (must be seen)"},
        "Gerund (Genitive)": {"form": "videndī", "meaning": "of seeing"},
        "Supine (Accusative)": {"form": "vīsum", "meaning": "to see (purpose)"},
        "Supine (Ablative)": {"form": "vīsū", "meaning": "to see (respect)"}
    },
    "habēre": {
        "Present Active Participle": {"form": "habēns", "meaning": "having"},
        "Perfect Passive Participle": {"form": "habitus", "meaning": "having been had"},
        "Future Active Participle": {"form": "habitūrus", "meaning": "about to have"},
        "Future Passive Participle (Gerundive)": {"form": "habendus", "meaning": "to be had (must be had)"},
        "Gerund (Genitive)": {"form": "habendī", "meaning": "of having"},
        "Supine (Accusative)": {"form": "habitum", "meaning": "to have (purpose)"},
        "Supine (Ablative)": {"form": "habitū", "meaning": "to have (respect)"}
    },
    "docēre": {
        "Present Active Participle": {"form": "docēns", "meaning": "teaching"},
        "Perfect Passive Participle": {"form": "doctus", "meaning": "having been taught"},
        "Future Active Participle": {"form": "doctūrus", "meaning": "about to teach"},
        "Future Passive Participle (Gerundive)": {"form": "docendus", "meaning": "to be taught (must be taught)"},
        "Gerund (Genitive)": {"form": "docendī", "meaning": "of teaching"},
        "Supine (Accusative)": {"form": "doctum", "meaning": "to teach (purpose)"},
        "Supine (Ablative)": {"form": "doctū", "meaning": "to teach (respect)"}
    },
    "tenēre": {
        "Present Active Participle": {"form": "tenēns", "meaning": "holding"},
        "Perfect Passive Participle": {"form": "tentus", "meaning": "having been held"},
        "Future Active Participle": {"form": "tentūrus", "meaning": "about to hold"},
        "Future Passive Participle (Gerundive)": {"form": "tenendus", "meaning": "to be held (must be held)"},
        "Gerund (Genitive)": {"form": "tenendī", "meaning": "of holding"},
        "Supine (Accusative)": {"form": "tentum", "meaning": "to hold (purpose)"},
        "Supine (Ablative)": {"form": "tentū", "meaning": "to hold (respect)"}
    },
    "terrēre": {
        "Present Active Participle": {"form": "terrēns", "meaning": "frightening"},
        "Perfect Passive Participle": {"form": "territus", "meaning": "having been frightened"},
        "Future Active Participle": {"form": "territūrus", "meaning": "about to frighten"},
        "Future Passive Participle (Gerundive)": {"form": "terrendus", "meaning": "to be frightened (must be frightened)"},
        "Gerund (Genitive)": {"form": "terrendī", "meaning": "of frightening"},
        "Supine (Accusative)": {"form": "territum", "meaning": "to frighten (purpose)"},
        "Supine (Ablative)": {"form": "territū", "meaning": "to frighten (respect)"}
    },
    "movēre": {
        "Present Active Participle": {"form": "movēns", "meaning": "moving"},
        "Perfect Passive Participle": {"form": "mōtus", "meaning": "having been moved"},
        "Future Active Participle": {"form": "mōtūrus", "meaning": "about to move"},
        "Future Passive Participle (Gerundive)": {"form": "movendus", "meaning": "to be moved (must be moved)"},
        "Gerund (Genitive)": {"form": "movendī", "meaning": "of moving"},
        "Supine (Accusative)": {"form": "mōtum", "meaning": "to move (purpose)"},
        "Supine (Ablative)": {"form": "mōtū", "meaning": "to move (respect)"}
    },
    "prohibēre": {
        "Present Active Participle": {"form": "prohibēns", "meaning": "preventing"},
        "Perfect Passive Participle": {"form": "prohibitus", "meaning": "having been prevented"},
        "Future Active Participle": {"form": "prohibitūrus", "meaning": "about to prevent"},
        "Future Passive Participle (Gerundive)": {"form": "prohibendus", "meaning": "to be prevented (must be prevented)"},
        "Gerund (Genitive)": {"form": "prohibendī", "meaning": "of preventing"},
        "Supine (Accusative)": {"form": "prohibitum", "meaning": "to prevent (purpose)"},
        "Supine (Ablative)": {"form": "prohibitū", "meaning": "to prevent (respect)"}
    },
    "praebēre": {
        "Present Active Participle": {"form": "praebēns", "meaning": "offering"},
        "Perfect Passive Participle": {"form": "praebitus", "meaning": "having been offered"},
        "Future Active Participle": {"form": "praebitūrus", "meaning": "about to offer"},
        "Future Passive Participle (Gerundive)": {"form": "praebendus", "meaning": "to be offered (must be offered)"},
        "Gerund (Genitive)": {"form": "praebendī", "meaning": "of offering"},
        "Supine (Accusative)": {"form": "praebitum", "meaning": "to offer (purpose)"},
        "Supine (Ablative)": {"form": "praebitū", "meaning": "to offer (respect)"}
    },
    "miscēre": {
        "Present Active Participle": {"form": "miscēns", "meaning": "mixing"},
        "Perfect Passive Participle": {"form": "mixtus", "meaning": "having been mixed"},
        "Future Active Participle": {"form": "mixtūrus", "meaning": "about to mix"},
        "Future Passive Participle (Gerundive)": {"form": "miscendus", "meaning": "to be mixed (must be mixed)"},
        "Gerund (Genitive)": {"form": "miscendī", "meaning": "of mixing"},
        "Supine (Accusative)": {"form": "mixtum", "meaning": "to mix (purpose)"},
        "Supine (Ablative)": {"form": "mixtū", "meaning": "to mix (respect)"}
    },

    # === 3RD CONJUGATION ===
    "dūcere": {
        "Present Active Participle": {"form": "dūcēns", "meaning": "leading"},
        "Perfect Passive Participle": {"form": "ductus", "meaning": "having been led"},
        "Future Active Participle": {"form": "ductūrus", "meaning": "about to lead"},
        "Future Passive Participle (Gerundive)": {"form": "dūcendus", "meaning": "to be led (must be led)"},
        "Gerund (Genitive)": {"form": "dūcendī", "meaning": "of leading"},
        "Supine (Accusative)": {"form": "ductum", "meaning": "to lead (purpose)"},
        "Supine (Ablative)": {"form": "ductū", "meaning": "to lead (respect)"}
    },
    "mittere": {
        "Present Active Participle": {"form": "mittēns", "meaning": "sending"},
        "Perfect Passive Participle": {"form": "missus", "meaning": "having been sent"},
        "Future Active Participle": {"form": "missūrus", "meaning": "about to send"},
        "Future Passive Participle (Gerundive)": {"form": "mittendus", "meaning": "to be sent (must be sent)"},
        "Gerund (Genitive)": {"form": "mittendī", "meaning": "of sending"},
        "Supine (Accusative)": {"form": "missum", "meaning": "to send (purpose)"},
        "Supine (Ablative)": {"form": "missū", "meaning": "to send (respect)"}
    },
    "pōnere": {
        "Present Active Participle": {"form": "pōnēns", "meaning": "placing / putting"},
        "Perfect Passive Participle": {"form": "positus", "meaning": "having been placed"},
        "Future Active Participle": {"form": "positūrus", "meaning": "about to place"},
        "Future Passive Participle (Gerundive)": {"form": "pōnendus", "meaning": "to be placed (must be placed)"},
        "Gerund (Genitive)": {"form": "pōnendī", "meaning": "of placing"},
        "Supine (Accusative)": {"form": "positum", "meaning": "to place (purpose)"},
        "Supine (Ablative)": {"form": "positū", "meaning": "to place (respect)"}
    },
    "regere": {
        "Present Active Participle": {"form": "regēns", "meaning": "ruling"},
        "Perfect Passive Participle": {"form": "rēctus", "meaning": "having been ruled"},
        "Future Active Participle": {"form": "rēctūrus", "meaning": "about to rule"},
        "Future Passive Participle (Gerundive)": {"form": "regendus", "meaning": "to be ruled (must be ruled)"},
        "Gerund (Genitive)": {"form": "regendī", "meaning": "of ruling"},
        "Supine (Accusative)": {"form": "rēctum", "meaning": "to rule (purpose)"},
        "Supine (Ablative)": {"form": "rēctū", "meaning": "to rule (respect)"}
    },
    "trahere": {
        "Present Active Participle": {"form": "trahēns", "meaning": "dragging"},
        "Perfect Passive Participle": {"form": "tractus", "meaning": "having been dragged"},
        "Future Active Participle": {"form": "tractūrus", "meaning": "about to drag"},
        "Future Passive Participle (Gerundive)": {"form": "trahendus", "meaning": "to be dragged (must be dragged)"},
        "Gerund (Genitive)": {"form": "trahendī", "meaning": "of dragging"},
        "Supine (Accusative)": {"form": "tractum", "meaning": "to drag (purpose)"},
        "Supine (Ablative)": {"form": "tractū", "meaning": "to drag (respect)"}
    },
    "dīcere": {
        "Present Active Participle": {"form": "dīcēns", "meaning": "saying"},
        "Perfect Passive Participle": {"form": "dictus", "meaning": "having been said"},
        "Future Active Participle": {"form": "dictūrus", "meaning": "about to say"},
        "Future Passive Participle (Gerundive)": {"form": "dīcendus", "meaning": "to be said (must be said)"},
        "Gerund (Genitive)": {"form": "dīcendī", "meaning": "of saying"},
        "Supine (Accusative)": {"form": "dictum", "meaning": "to say (purpose)"},
        "Supine (Ablative)": {"form": "dictū", "meaning": "to say (respect)"}
    },
    "vincere": {
        "Present Active Participle": {"form": "vincēns", "meaning": "conquering"},
        "Perfect Passive Participle": {"form": "victus", "meaning": "having been conquered"},
        "Future Active Participle": {"form": "victūrus", "meaning": "about to conquer"},
        "Future Passive Participle (Gerundive)": {"form": "vincendus", "meaning": "to be conquered (must be conquered)"},
        "Gerund (Genitive)": {"form": "vincendī", "meaning": "of conquering"},
        "Supine (Accusative)": {"form": "victum", "meaning": "to conquer (purpose)"},
        "Supine (Ablative)": {"form": "victū", "meaning": "to conquer (respect)"}
    },
    "legere": {
        "Present Active Participle": {"form": "legēns", "meaning": "reading"},
        "Perfect Passive Participle": {"form": "lēctus", "meaning": "having been read"},
        "Future Active Participle": {"form": "lēctūrus", "meaning": "about to read"},
        "Future Passive Participle (Gerundive)": {"form": "legendus", "meaning": "to be read (must be read)"},
        "Gerund (Genitive)": {"form": "legendī", "meaning": "of reading"},
        "Supine (Accusative)": {"form": "lēctum", "meaning": "to read (purpose)"},
        "Supine (Ablative)": {"form": "lēctū", "meaning": "to read (respect)"}
    },
    "scrībere": {
        "Present Active Participle": {"form": "scrībēns", "meaning": "writing"},
        "Perfect Passive Participle": {"form": "scrīptus", "meaning": "having been written"},
        "Future Active Participle": {"form": "scrīptūrus", "meaning": "about to write"},
        "Future Passive Participle (Gerundive)": {"form": "scrībendus", "meaning": "to be written (must be written)"},
        "Gerund (Genitive)": {"form": "scrībendī", "meaning": "of writing"},
        "Supine (Accusative)": {"form": "scrīptum", "meaning": "to write (purpose)"},
        "Supine (Ablative)": {"form": "scrīptū", "meaning": "to write (respect)"}
    },
    "pellere": {
        "Present Active Participle": {"form": "pellēns", "meaning": "driving"},
        "Perfect Passive Participle": {"form": "pulsus", "meaning": "having been driven"},
        "Future Active Participle": {"form": "pulsūrus", "meaning": "about to drive"},
        "Future Passive Participle (Gerundive)": {"form": "pellendus", "meaning": "to be driven (must be driven)"},
        "Gerund (Genitive)": {"form": "pellendī", "meaning": "of driving"},
        "Supine (Accusative)": {"form": "pulsum", "meaning": "to drive (purpose)"},
        "Supine (Ablative)": {"form": "pulsū", "meaning": "to drive (respect)"}
    },

    # === 3RD i-stem CONJUGATION ===
    "capere": {
        "Present Active Participle": {"form": "capiēns", "meaning": "taking / capturing"},
        "Perfect Passive Participle": {"form": "captus", "meaning": "having been taken"},
        "Future Active Participle": {"form": "captūrus", "meaning": "about to take"},
        "Future Passive Participle (Gerundive)": {"form": "capiendus", "meaning": "to be taken (must be taken)"},
        "Gerund (Genitive)": {"form": "capiendī", "meaning": "of taking"},
        "Supine (Accusative)": {"form": "captum", "meaning": "to take (purpose)"},
        "Supine (Ablative)": {"form": "captū", "meaning": "to take (respect)"}
    },
    "rapere": {
        "Present Active Participle": {"form": "rapiēns", "meaning": "seizing"},
        "Perfect Passive Participle": {"form": "raptus", "meaning": "having been seized"},
        "Future Active Participle": {"form": "raptūrus", "meaning": "about to seize"},
        "Future Passive Participle (Gerundive)": {"form": "rapiendus", "meaning": "to be seized (must be seized)"},
        "Gerund (Genitive)": {"form": "rapiendī", "meaning": "of seizing"},
        "Supine (Accusative)": {"form": "raptum", "meaning": "to seize (purpose)"},
        "Supine (Ablative)": {"form": "raptū", "meaning": "to seize (respect)"}
    },
    "iacere": {
        "Present Active Participle": {"form": "iaciēns", "meaning": "throwing"},
        "Perfect Passive Participle": {"form": "iactus", "meaning": "having been thrown"},
        "Future Active Participle": {"form": "iactūrus", "meaning": "about to throw"},
        "Future Passive Participle (Gerundive)": {"form": "iaciendus", "meaning": "to be thrown (must be thrown)"},
        "Gerund (Genitive)": {"form": "iaciendī", "meaning": "of throwing"},
        "Supine (Accusative)": {"form": "iactum", "meaning": "to throw (purpose)"},
        "Supine (Ablative)": {"form": "iactū", "meaning": "to throw (respect)"}
    },
    "accipere": {
        "Present Active Participle": {"form": "accipiēns", "meaning": "receiving"},
        "Perfect Passive Participle": {"form": "acceptus", "meaning": "having been received"},
        "Future Active Participle": {"form": "acceptūrus", "meaning": "about to receive"},
        "Future Passive Participle (Gerundive)": {"form": "accipiendus", "meaning": "to be received (must be received)"},
        "Gerund (Genitive)": {"form": "accipiendī", "meaning": "of receiving"},
        "Supine (Accusative)": {"form": "acceptum", "meaning": "to receive (purpose)"},
        "Supine (Ablative)": {"form": "acceptū", "meaning": "to receive (respect)"}
    },
    "excipere": {
        "Present Active Participle": {"form": "excipiēns", "meaning": "catching / receiving"},
        "Perfect Passive Participle": {"form": "exceptus", "meaning": "having been caught"},
        "Future Active Participle": {"form": "exceptūrus", "meaning": "about to catch"},
        "Future Passive Participle (Gerundive)": {"form": "excipiendus", "meaning": "to be caught (must be caught)"},
        "Gerund (Genitive)": {"form": "excipiendī", "meaning": "of catching"},
        "Supine (Accusative)": {"form": "exceptum", "meaning": "to catch (purpose)"},
        "Supine (Ablative)": {"form": "exceptū", "meaning": "to catch (respect)"}
    },
    "dēcipere": {
        "Present Active Participle": {"form": "dēcipiēns", "meaning": "deceiving"},
        "Perfect Passive Participle": {"form": "dēceptus", "meaning": "having been deceived"},
        "Future Active Participle": {"form": "dēceptūrus", "meaning": "about to deceive"},
        "Future Passive Participle (Gerundive)": {"form": "dēcipiendus", "meaning": "to be deceived (must be deceived)"},
        "Gerund (Genitive)": {"form": "dēcipiendī", "meaning": "of deceiving"},
        "Supine (Accusative)": {"form": "dēceptum", "meaning": "to deceive (purpose)"},
        "Supine (Ablative)": {"form": "dēceptū", "meaning": "to deceive (respect)"}
    },
    "recipere": {
        "Present Active Participle": {"form": "recipiēns", "meaning": "taking back"},
        "Perfect Passive Participle": {"form": "receptus", "meaning": "having been taken back"},
        "Future Active Participle": {"form": "receptūrus", "meaning": "about to take back"},
        "Future Passive Participle (Gerundive)": {"form": "recipiendus", "meaning": "to be taken back (must be taken back)"},
        "Gerund (Genitive)": {"form": "recipiendī", "meaning": "of taking back"},
        "Supine (Accusative)": {"form": "receptum", "meaning": "to take back (purpose)"},
        "Supine (Ablative)": {"form": "receptū", "meaning": "to take back (respect)"}
    },
    "ēripere": {
        "Present Active Participle": {"form": "ēripiēns", "meaning": "snatching away"},
        "Perfect Passive Participle": {"form": "ēreptus", "meaning": "having been snatched away"},
        "Future Active Participle": {"form": "ēreptūrus", "meaning": "about to snatch away"},
        "Future Passive Participle (Gerundive)": {"form": "ēripiendus", "meaning": "to be snatched away (must be snatched away)"},
        "Gerund (Genitive)": {"form": "ēripiendī", "meaning": "of snatching away"},
        "Supine (Accusative)": {"form": "ēreptum", "meaning": "to snatch away (purpose)"},
        "Supine (Ablative)": {"form": "ēreptū", "meaning": "to snatch away (respect)"}
    },
    "cōnspicere": {
        "Present Active Participle": {"form": "cōnspiciēns", "meaning": "catching sight of"},
        "Perfect Passive Participle": {"form": "cōnspectus", "meaning": "having been caught sight of"},
        "Future Active Participle": {"form": "cōnspectūrus", "meaning": "about to catch sight of"},
        "Future Passive Participle (Gerundive)": {"form": "cōnspiciendus", "meaning": "to be caught sight of (must be caught sight of)"},
        "Gerund (Genitive)": {"form": "cōnspiciendī", "meaning": "of catching sight of"},
        "Supine (Accusative)": {"form": "cōnspectum", "meaning": "to catch sight of (purpose)"},
        "Supine (Ablative)": {"form": "cōnspectū", "meaning": "to catch sight of (respect)"}
    },
    "dīripere": {
        "Present Active Participle": {"form": "dīripiēns", "meaning": "plundering"},
        "Perfect Passive Participle": {"form": "dīreptus", "meaning": "having been plundered"},
        "Future Active Participle": {"form": "dīreptūrus", "meaning": "about to plunder"},
        "Future Passive Participle (Gerundive)": {"form": "dīripiendus", "meaning": "to be plundered (must be plundered)"},
        "Gerund (Genitive)": {"form": "dīripiendī", "meaning": "of plundering"},
        "Supine (Accusative)": {"form": "dīreptum", "meaning": "to plunder (purpose)"},
        "Supine (Ablative)": {"form": "dīreptū", "meaning": "to plunder (respect)"}
    },

    # === 4TH CONJUGATION ===
    "audīre": {
        "Present Active Participle": {"form": "audiēns", "meaning": "hearing"},
        "Perfect Passive Participle": {"form": "audītus", "meaning": "having been heard"},
        "Future Active Participle": {"form": "audītūrus", "meaning": "about to hear"},
        "Future Passive Participle (Gerundive)": {"form": "audiendus", "meaning": "to be heard (must be heard)"},
        "Gerund (Genitive)": {"form": "audiendī", "meaning": "of hearing"},
        "Supine (Accusative)": {"form": "audītum", "meaning": "to hear (purpose)"},
        "Supine (Ablative)": {"form": "audītū", "meaning": "to hear (respect)"}
    },
    "scīre": {
        "Present Active Participle": {"form": "sciēns", "meaning": "knowing"},
        "Perfect Passive Participle": {"form": "scītus", "meaning": "having been known"},
        "Future Active Participle": {"form": "scītūrus", "meaning": "about to know"},
        "Future Passive Participle (Gerundive)": {"form": "sciendus", "meaning": "to be known (must be known)"},
        "Gerund (Genitive)": {"form": "sciendī", "meaning": "of knowing"},
        "Supine (Accusative)": {"form": "scītum", "meaning": "to know (purpose)"},
        "Supine (Ablative)": {"form": "scītū", "meaning": "to know (respect)"}
    },
    "invenīre": {
        "Present Active Participle": {"form": "inveniēns", "meaning": "finding"},
        "Perfect Passive Participle": {"form": "inventus", "meaning": "having been found"},
        "Future Active Participle": {"form": "inventūrus", "meaning": "about to find"},
        "Future Passive Participle (Gerundive)": {"form": "inveniendus", "meaning": "to be found (must be found)"},
        "Gerund (Genitive)": {"form": "inveniendī", "meaning": "of finding"},
        "Supine (Accusative)": {"form": "inventum", "meaning": "to find (purpose)"},
        "Supine (Ablative)": {"form": "inventū", "meaning": "to find (respect)"}
    },
    "pūnīre": {
        "Present Active Participle": {"form": "pūniēns", "meaning": "punishing"},
        "Perfect Passive Participle": {"form": "pūnītus", "meaning": "having been punished"},
        "Future Active Participle": {"form": "pūnītūrus", "meaning": "about to punish"},
        "Future Passive Participle (Gerundive)": {"form": "pūniendus", "meaning": "to be punished (must be punished)"},
        "Gerund (Genitive)": {"form": "pūniendī", "meaning": "of punishing"},
        "Supine (Accusative)": {"form": "pūnītum", "meaning": "to punish (purpose)"},
        "Supine (Ablative)": {"form": "pūnītū", "meaning": "to punish (respect)"}
    },
    "mūnīre": {
        "Present Active Participle": {"form": "mūniēns", "meaning": "fortifying"},
        "Perfect Passive Participle": {"form": "mūnītus", "meaning": "having been fortified"},
        "Future Active Participle": {"form": "mūnītūrus", "meaning": "about to fortify"},
        "Future Passive Participle (Gerundive)": {"form": "mūniendus", "meaning": "to be fortified (must be fortified)"},
        "Gerund (Genitive)": {"form": "mūniendī", "meaning": "of fortifying"},
        "Supine (Accusative)": {"form": "mūnītum", "meaning": "to fortify (purpose)"},
        "Supine (Ablative)": {"form": "mūnītū", "meaning": "to fortify (respect)"}
    },
    "custōdīre": {
        "Present Active Participle": {"form": "custōdiēns", "meaning": "guarding"},
        "Perfect Passive Participle": {"form": "custōdītus", "meaning": "having been guarded"},
        "Future Active Participle": {"form": "custōdītūrus", "meaning": "about to guard"},
        "Future Passive Participle (Gerundive)": {"form": "custōdiendus", "meaning": "to be guarded (must be guarded)"},
        "Gerund (Genitive)": {"form": "custōdiendī", "meaning": "of guarding"},
        "Supine (Accusative)": {"form": "custōdītum", "meaning": "to guard (purpose)"},
        "Supine (Ablative)": {"form": "custōdītū", "meaning": "to guard (respect)"}
    },
    "impedīre": {
        "Present Active Participle": {"form": "impediēns", "meaning": "hindering"},
        "Perfect Passive Participle": {"form": "impedītus", "meaning": "having been hindered"},
        "Future Active Participle": {"form": "impedītūrus", "meaning": "about to hinder"},
        "Future Passive Participle (Gerundive)": {"form": "impediendus", "meaning": "to be hindered (must be hindered)"},
        "Gerund (Genitive)": {"form": "impediendī", "meaning": "of hindering"},
        "Supine (Accusative)": {"form": "impedītum", "meaning": "to hinder (purpose)"},
        "Supine (Ablative)": {"form": "impedītū", "meaning": "to hinder (respect)"}
    },
    "fīnīre": {
        "Present Active Participle": {"form": "fīniēns", "meaning": "finishing"},
        "Perfect Passive Participle": {"form": "fīnītus", "meaning": "having been finished"},
        "Future Active Participle": {"form": "fīnītūrus", "meaning": "about to finish"},
        "Future Passive Participle (Gerundive)": {"form": "fīniendus", "meaning": "to be finished (must be finished)"},
        "Gerund (Genitive)": {"form": "fīniendī", "meaning": "of finishing"},
        "Supine (Accusative)": {"form": "fīnītum", "meaning": "to finish (purpose)"},
        "Supine (Ablative)": {"form": "fīnītū", "meaning": "to finish (respect)"}
    },
    "aperīre": {
        "Present Active Participle": {"form": "aperiēns", "meaning": "opening"},
        "Perfect Passive Participle": {"form": "apertus", "meaning": "having been opened"},
        "Future Active Participle": {"form": "apertūrus", "meaning": "about to open"},
        "Future Passive Participle (Gerundive)": {"form": "aperiendus", "meaning": "to be opened (must be opened)"},
        "Gerund (Genitive)": {"form": "aperiendī", "meaning": "of opening"},
        "Supine (Accusative)": {"form": "apertum", "meaning": "to open (purpose)"},
        "Supine (Ablative)": {"form": "apertū", "meaning": "to open (respect)"}
    },
    "reperīre": {
        "Present Active Participle": {"form": "reperiēns", "meaning": "discovering"},
        "Perfect Passive Participle": {"form": "repertus", "meaning": "having been discovered"},
        "Future Active Participle": {"form": "repertūrus", "meaning": "about to discover"},
        "Future Passive Participle (Gerundive)": {"form": "reperiendus", "meaning": "to be discovered (must be discovered)"},
        "Gerund (Genitive)": {"form": "reperiendī", "meaning": "of discovering"},
        "Supine (Accusative)": {"form": "repertum", "meaning": "to discover (purpose)"},
        "Supine (Ablative)": {"form": "repertū", "meaning": "to discover (respect)"}
    }
}

# --- HELPER FUNCTIONS ---
def remove_macrons(text):
    replacements = {'ā': 'a', 'ē': 'e', 'ī': 'i', 'ō': 'o', 'ū': 'u', 'Ā': 'A', 'Ē': 'E', 'Ī': 'I', 'Ō': 'O', 'Ū': 'U'}
    for macron, plain in replacements.items():
        text = text.replace(macron, plain)
    return text.lower().strip()


# --- STREAMLIT UI ---
st.set_page_config(page_title="Latin Participle Master", page_icon="🏛️")
st.title("🏛️ Latin Participle Master")

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
        available_verbs = list(forms_db.keys())
    else:
        available_verbs = [v for v, c in verb_conjugations.items() if c == conj_choice]
        
    verb_choice = st.selectbox("Select Verb:", ["All"] + available_verbs)
    
    # Form Type Selection
    form_types = st.multiselect(
        "Select Form Types to Practice:",
        [
            "Present Active Participle", 
            "Perfect Passive Participle", 
            "Future Active Participle", 
            "Future Passive Participle (Gerundive)", 
            "Gerund (Genitive)", 
            "Supine (Accusative)", 
            "Supine (Ablative)"
        ],
        default=[
            "Present Active Participle", 
            "Perfect Passive Participle", 
            "Future Active Participle", 
            "Future Passive Participle (Gerundive)"
        ]
    )

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
        st.success(f"**Optimē!** Previous: {res['prompt']} → **{res['answer']}** *(Meaning: {res['meaning']})*")
    else:
        st.error(f"**Errāstī.** Previous: {res['prompt']} → **{res['answer']}** *(Meaning: {res['meaning']})*")

# --- SELECTION LOGIC ---
if "current_q" not in st.session_state:
    questions = []
    verbs_to_pull = available_verbs if verb_choice == "All" else [verb_choice]

    for verb_name in verbs_to_pull:
        verb_data = forms_db.get(verb_name, {})
        for form_name in form_types:
            if form_name in verb_data:
                questions.append({
                    "prompt": f"{verb_name.upper()} — {form_name.upper()}",
                    "answer": verb_data[form_name]["form"],
                    "meaning": verb_data[form_name]["meaning"]
                })

    if questions:
        st.session_state.current_q = random.choice(questions)
    else:
        st.warning("Please select at least one form type to practice.")

# --- DISPLAY & FORM ---
if "current_q" in st.session_state:
    q = st.session_state.current_q
    st.info(f"How do you say: **{q['prompt']}**?")

    # Hint Expander
    with st.expander("Need a hint? Click here to see the English meaning."):
        st.write(f"The meaning of this form is: **{q['meaning']}**")

    with st.form(key='quiz_form', clear_on_submit=True):
        user_input = st.text_input("Your Answer (Nominative Singular Masculine for adjectives):")
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
            "meaning": q['meaning'],
            "correct": is_correct
        }

        del st.session_state.current_q
        st.rerun()
