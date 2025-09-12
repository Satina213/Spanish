import csv
import verbs

ar_verb_list = []
er_verb_list = []
ir_verb_list = []
def str_to_bool(s):
    return str(s).strip().lower() == "true"


with open("regularverbs.csv") as file:
    reader = csv.DictReader(file, skipinitialspace=True)
    for row in reader:
        if row["verbtype"] == "ar":
            ar_verb_list.append(verbs.ArVerb(row["word"], row["translation"], True))
        elif row["verbtype"] == "er":
            er_verb_list.append(verbs.ErVerb(row["word"], row["translation"], True))
        else:
            ir_verb_list.append(verbs.IrVerb(row["word"], row["translation"], True))

for item in ar_verb_list:
    print(item)
for item in er_verb_list:
    print(item)
for item in ir_verb_list:
    print(item)