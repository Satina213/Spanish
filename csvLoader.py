import csv
import newverbs

verb_list = []
def str_to_bool(s):
    return str(s).strip().lower() == "true"


with open("spanishwords.csv") as file:
    reader = csv.DictReader(file, skipinitialspace=True)
    for row in reader:
        verb_list.append(newverbs.Verb(str_to_bool(row["regular_word"]), row["spanish_word"], row["translation"]))

for item in verb_list:
    print(item)