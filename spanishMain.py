import random
import sqlite3
from WordLists import body_parts, colors, food, kitchen_items, common_phrases, people

word_categories = {
    "body parts": body_parts,
    "colors": colors,
    "food": food,
    "kitchen": kitchen_items,
    "phrases": common_phrases,
    "people": people
}

def get_question(wordList):
    random_key = random.choice(list(wordList))
    while True:
        print("What is the word for " + wordList[random_key])
        response = input().lower()
        if response == random_key:
            print("Great Job!!\n")
            random_key = random.choice(list(wordList))
        elif response == "quit":
            print("exiting...")
            return
        elif response == "hint":
            if len(random_key) >= 5:
                print(random_key[:3])
            elif len(random_key) > 2:
                print(random_key[:2])
            else: print(random_key[:1])
        else:
            print("Not quite, try again")

def get_verb():
    verb_categories = [Verbs.ar_verbs, Verbs.er_verbs, Verbs.ir_verbs]
    verb_category = random.choice(verb_categories)
    english_verb = random.choice(list(verb_category))
    spanish_verb  = verb_category[english_verb]
    # print(english_verb, spanish_verb)
    return(english_verb, spanish_verb)

def get_subject():
    subject = random.choice(list(people))
    info = people[subject]
    return(subject, info["translation"], info["pov"])


    # return(subject, pov)
def build_sentence(english_subject, spanish_subject, pov, english_verb, spanish_verb):
    print("build a sentence with these words")
    print(english_subject, english_verb)
    
    guesses = 0
    while guesses < 4:
        response = input()
        # print(spanish_subject + " " + Verbs.conjugate(pov, spanish_verb))
        if response == spanish_subject + " " + Verbs.conjugate_present(pov, spanish_verb):
            print("YAAAAY")
            guesses = 4
        else:
            print("not quite")
        guesses = guesses + 1


def get_category():
    loop = True
    while loop:
        for category in word_categories:
            print(category, end="     ")
        print("")
        choice = input()
        if choice in word_categories:
            loop = False
            return word_categories[choice]
        else:
            print("Please choose a valid category")

def main():
    from verbs import Verb
    conn = sqlite3.connect("spanishverbs.db")
    c = conn.cursor()
    c.execute(f"""SELECT DISTINCT infinitive FROM verbs;""")
    dbVerb = c.fetchall()
    dbVerb = [item[0] for item in dbVerb]
    c.execute("""CREATE TABLE IF NOT EXISTS 'present_tense'(
              infinitive TEXT,
              form_1s TEXT,
              form_2s TEXT,
              form_3s TEXT,
              form_1p TEXT,
              form_3p TEXT,
              id INTEGER PRIMARY KEY AUTOINCREMENT);""")
    # print(dbVerb)
    for verb in dbVerb:
        c.execute("""SELECT form_1s, form_2s, form_3s, form_1p, form_3p
                  FROM verbs WHERE mood_english = 'Indicative' AND
                  infinitive = ?;""", (verb,))
        form_1s, form_2s, form_3s, form_1p, form_3p = c.fetchone()
        c.execute("""INSERT INTO present_tense (infinitive, form_1s, form_2s, form_3s, form_1p, form_3p)
                  VALUES (?, ?, ?, ?, ?, ?)""",(verb, form_1s, form_2s, form_3s, form_1p, form_3p))
    conn.commit()
    conn.close()
    
    # abandonar = Verb.create("abandonar", "to abandon")
    # myVerb = abandonar.conjugate("present", "yo")
    # print(myVerb == dbVerb)


if __name__ == "__main__":
    main()