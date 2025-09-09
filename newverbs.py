regular_ar_verbs = {
    "hablar": "to speak",
}

regular_ar_verb_endings = {
    "yo": "o",
    "tu": "as",
    "usted": "a",
    "nosotros": "amos",
    "ustedes": "an"
}

def conjugate_present_ar(verb, pov):
    root = verb[:-2]
    