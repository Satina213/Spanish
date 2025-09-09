ar_verbs = {
    "to speak": "hablar",
    "to cut": "cortar",
    "to work": "trabajar",
    "to dance": "bailar",
    "to study": "estudiar",
    "to walk": "caminar",
    "to cook": "cocinar",
}

er_verbs = {
    "to eat": "comer",
    "to drink": "beber",
    "to learn": "aprender",
    "to run": "correr",
    "to read": "to read",
    "to sell": "vender",
    "to comprehend": "comprender"
    
}

ir_verbs = {
    "to write": "escribir",
    "to live": "vivir",
    "to open": "abrir",
    "to receive": "recibir",
    "to decide": "decidir",
    "to share": "compartir",
}

ar_present_verb_endings = {
    "yo": "o",
    "tu": "as",
    "usted": "a",
    "nosotros": "amos",
    "ustedes": "an",
}
ar_preterite_verb_endings = {
    "yo": "é",
    "tu": "aste",
    "usted": "ó",
    "nosotros": "amos",
    "ustedes": "aron",
}

er_present_verb_endings = {
    "yo": "o",
    "tu": "es",
    "usted": "e",
    "nosotros": "emos",
    "ustedes": "en",  
}

er_preterite_verb_endings = {
    "yo": "í",
    "tu": "iste",
    "usted": "ió",
    "nosotros": "imos",
    "ustedes": "ieron",
}

ir_present_verb_endings = {
    "yo": "o",
    "tu": "es",
    "usted": "e",
    "nosotros": "imos",
    "ustedes": "en"
}

ir_preterite_verb_endings = {
    "yo": "í",
    "tu": "iste",
    "usted": "ió",
    "nosotros": "imos",
    "ustedes": "ieron",
}

endings = {
    "ar": {
        "present": ar_present_verb_endings,
        "preterite": ar_preterite_verb_endings,
        },
    "er": {
        "present": er_present_verb_endings,
        "preterite": er_preterite_verb_endings,
    },
    "ir": {
        "present": ir_present_verb_endings,
        "preterite": ir_preterite_verb_endings
    },
}
def get_word_ending(word):
    ending = word[-2:]
    return ending

def get_word_root(word):
    root = word[:-2]
    return root

def conjugate_present(pov, verb):
    ending = get_word_ending(verb)
    root = get_word_root(verb)
    conjugated_verb = root + endings[ending]["present"][pov]
    return(conjugated_verb)

def conjugate_preterite(pov, verb):
    ending=get_word_ending(verb)
    root = get_word_root(verb)
    if pov == "yo":
        if root[-1] == "c":
            root = root[:-1] + "qu"
        elif root[-1] == "g":
            root = root[:-1] + "gu"
        elif root[-1] == "z":
            root = root[:-1] + "c"
    conjugated_verb = root + endings[ending]["preterite"][pov]
    print(conjugated_verb)
    return conjugated_verb
    

def future_conjugate(pov, verb):
    return 0

