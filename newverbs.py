class Verb:
    def __init__(self, regular, word, translation):
        self.regular = regular
        self.word = word
        self.translation = translation

    def __str__(self):
        return f"{self.word} means {self.translation}"

    @property
    def regular(self):
        return self._regular
    
    @regular.setter
    def regular(self, regular):
        if not isinstance(regular, bool):
            raise ValueError("Need boolean value for regular")
        self._regular = regular

    @property
    def word(self):
        return self._word
    
    @word.setter
    def word(self, word):
        if not isinstance(word, str):
            raise ValueError("spanish word must be a str")
        self._word = word

    @property
    def translation(self):
        return self._translation
    
    @translation.setter
    def translation(self, translation):
        if not isinstance(translation, str):
            raise ValueError("translation must be a str")
        self._translation = translation


    @property
    def tense(self):
        return  {
            "present": getattr(self, "present_tense_endings", {}),
            "preterite": getattr(self, "preterite_tense_endings", {})
        }
    def conjugate(self, tense, form):
        root = self.word[:-2]
        verb_type = self.word[-2:]
        if tense == "present":
            if self.word[-3:] in ["ger", "gir"] and form == "yo":
                root = root[:-1] + "j"
            if self.word[-4:] == "guir" and form == "yo":
                root = root[:-1]
            if self.word[-3:] in ["cer", "cir"] and self.word[-4] in ["r", "n"] and form == "yo":
                root = root[:-1] + "z"
            if self.word[-3:] in ["cer", "cir"] and self.word[-4] in ["a", "e", "i", "o", "u"] and form == "yo":
                root = root[:-1] + "zc"
            if self.word[-3:] == "uir" and not self.word[-4] == "g" and form in ["yo", "tu", "usted", "ustedes"]:
                root = root + "y"
            # TODO
            # Some verbs that end in -iar and nearly all verbs 
            # that end in -uar take a written accent to the i or the u 
            # in all but the nosotros and vosotros forms.

        if tense == "preterite":
            if form == "yo" and verb_type == "ar":
                if root[-1] == "c":
                    root = root[:-1] + "qu"
                elif root[-1] == "g":
                    root = root[:-1] + "gu"
                elif root[-1] == "z":
                    root = root[:-1] + "c"
            if self.word[-3:] in ["aer", "eer", "oír", "oer"]:
                if form == "usted":
                    return root + "yó"
                if form == "ustedes":
                    return root + "yeron"
                if form in ["tu", "nosotros"] and self.word[-3:] == "uir":
                    return root + self.tense[tense][form]
                ending = self.tense[tense][form].replace("i", "í")
                return root + ending
        ending = self.tense[tense][form]
        return root + ending
    
    


class ArVerb(Verb):
    present_tense_endings = {
        "yo": "o",
        "tu": "as",
        "usted": "a",
        "nosotros": "amos",
        "ustedes": "an"
    }
    preterite_tense_endings = {
    "yo": "é",
    "tu": "aste",
    "usted": "ó",
    "nosotros": "amos",
    "ustedes": "aron",
    }

    def __init__(self, regular, word, translation):
        super().__init__(regular, word, translation)

class ErVerb(Verb):
    present_tense_endings = {
        "yo": "o",
        "tu": "es",
        "usted": "e",
        "nosotros": "emos",
        "ustedes": "en"
    }
    preterite_tense_endings = {
        "yo": "í",
        "tu": "iste",
        "usted": "ió",
        "nosotros": "imos",
        "ustedes": "ieron"
    }
    def __init__(self, regular, word, translation):
        super().__init__(regular, word, translation)

creer = ErVerb(True, "creer", "to believe")


if __name__ == "__main__":
    print(creer.conjugate("preterite", "yo"))
    print(creer.conjugate("preterite", "tu"))
    print(creer.conjugate("preterite", "usted"))
    print(creer.conjugate("preterite", "nosotros"))
    print(creer.conjugate("preterite", "ustedes"))
    
    