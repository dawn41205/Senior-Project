import numpy as np

def select_label_with_thresholds(probabilities, id_to_label, thresholds):
    probs = [float(value) for value in probabilities]
    matched = []
    for index, label in id_to_label.items():
        if label in thresholds and probs[index] >= float(thresholds[label]):
            matched.append((probs[index] - float(thresholds[label]), probs[index], index))
    if matched:
        return max(matched)[2]
    return int(np.argmax(probs))
