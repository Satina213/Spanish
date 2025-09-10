import sys
MILLION = 1000000
BILLION = 1000000000
base = {
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve",
    10: "diez",
    11: "once",
    12: "doce",
    13: "trece",
    14: "catorce",
    15: "quince",
    16: "dieciséis",
    17: "diecisiete",
    18: "dieciocho",
    19: "diecinueve",
    20: "veinte",
    21: "veintiuno",
    22: "veintidós",
    23: "veintitrés",
    24: "veinticuatro",
    25: "veinticinco",
    26: "veintiséis",
    27: "veintisiete",
    28: "veintiocho",
    29: "veintinueve",
    30: "treinta",
    40: "cuarenta",
    50: "cincuenta",
    60: "sesenta",
    70: "setenta",
    80: "ochenta",
    90: "noventa",
    100: "ciento",
    200: "doscientos",
    300: "trescientos",
    400: "cuatrocientos",
    500: "quinientos",
    600: "seiscientos",
    700: "setecientos",
    800: "ochocientos",
    900: "novecientos",
    1000: "mil",
    MILLION: "un millón",
    BILLION: "mil millones"
}

def nameSubHundred(number: int) -> str:
    if number == 0:
        return ""
    if number in base:
        return base[number]
    helper = number // 10
    tens = base[10 * helper]
    remainder = base[number - 10 * helper]
    if remainder:
        return tens + " y " + remainder
    else:
        return tens
    
def nameSubThousand(number: int) -> str:
    if number == 0:
        return ""
    if number in base:
        return base[number]
    if number < 100:
        return nameSubHundred(number)
    if number == 100:
        return "cien"
    helper = number // 100
    hundreds = base[100 * helper]
    remainder = number - helper * 100
    if remainder:
        return hundreds + " " + nameSubHundred(remainder)
    else:
        return hundreds

def nameSubMillion(number: int) -> str:
    if number == 0:
        return ""
    if number in base:
        return base[number]
    if number < 1000:
        return nameSubThousand(number)
    helper = (number // 1000)
    thousands = nameSubThousand(helper)
    remainder = number - helper * 1000
    if remainder:
        return thousands + " mil " + nameSubThousand(remainder)
    else:
        return thousands + " mil"
    
def nameSubBillion(number: int) ->(str):
    if number == 0:
        return ""
    if number in base:
        return base[number]
    if number < MILLION:
        return nameSubMillion(number)
    helper = (number // MILLION)
    millions = nameSubMillion(helper)
    remainder = number - helper * MILLION
    if remainder:
        return millions + " millones " + nameSubMillion(remainder)
    else:
        return millions + "millones"

def nameNumber(number: int) -> str:
    if number == 0:
        return "cero"
    if number == 100:
        return "cien"
    if number in base:
        return base[number]
    if number < 100:
        return(nameSubHundred(number))
    if number < 1000:
        return(nameSubThousand(number))
    if number < MILLION:
        return(nameSubMillion(number))
    if number < BILLION:
        return (nameSubBillion(number))
    
def main():
    # if len(sys.argv) == 2:
    #     if sys.argv[1] is int and sys.argv[1] > 0 and sys.argv[1] < BILLION:
    #         print(nameNumber(sys.argv[1]))
    # return 0
    print(nameNumber(525123))

if __name__ == "__main__":
    main()