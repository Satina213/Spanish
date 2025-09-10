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

    

hablar = Verb(True, "hablar", "to speak")

print(hablar)