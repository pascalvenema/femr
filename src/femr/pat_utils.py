import datetime

import meds


def get_patient_birthdate(patient: meds.Patient) -> datetime.datetime:
    for e in patient["events"]:
        for m in e["measurements"]:
            if (
                m["code"] == meds.birth_code or m["code"] == "SNOMED/184099003"
            ):  # Added SNOMED/184099003 for compatibility with EHRSHOT dataset
                return e["time"]
    raise ValueError("Couldn't find patient birthdate -- Patient has no events " + str(patient["events"][:5]))
