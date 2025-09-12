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
        "yo": "ó",
        "tu": "iste",
        "usted": "ió",
        "nosotros": "imos",
        "ustedes": "ieron"
    }
    def __init__(self, regular, word, translation):
        super().__init__(regular, word, translation)

hablar = ArVerb(True, "hablar", "to speak")


if __name__ == "__main__":
    print(hablar.conjugate("present", "yo"))
    print(hablar.conjugate("present", "tu"))
    print(hablar.conjugate("present", "usted"))
    print(hablar.conjugate("preterite", "yo"))
    print(hablar.conjugate("preterite", "tu"))
    print(hablar.conjugate("preterite", "usted"))