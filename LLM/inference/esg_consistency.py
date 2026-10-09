NA_VALUES = {"", "N/A", None}


def is_na(value):
    return value in NA_VALUES


def apply_consistency_gates(pred_obj, na_value=""):
    """Apply ontology-level consistency rules to one prediction object."""
    if pred_obj.get("promise_status") == "No":
        pred_obj["verification_timeline"] = na_value
        pred_obj["evidence_status"] = na_value
        pred_obj["evidence_quality"] = na_value
        return pred_obj

    if is_na(pred_obj.get("evidence_status")):
        pred_obj["promise_status"] = "No"
        pred_obj["verification_timeline"] = na_value
        pred_obj["evidence_status"] = na_value
        pred_obj["evidence_quality"] = na_value
        return pred_obj

    if pred_obj.get("evidence_status") != "Yes":
        pred_obj["evidence_quality"] = na_value

    return pred_obj
