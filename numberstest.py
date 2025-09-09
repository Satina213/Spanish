import pytest
import spanish_numbers


def test_ten():
    assert spanish_numbers.nameNumber(1) == "uno"
    assert spanish_numbers.nameNumber(2) == "dos"
    assert spanish_numbers.nameNumber(3) == "tres"
    assert spanish_numbers.nameNumber(4) == "cuatro"
    assert spanish_numbers.nameNumber(5) == "cinco"
    assert spanish_numbers.nameNumber(6) == "seis"
    assert spanish_numbers.nameNumber(7) == "siete"
    assert spanish_numbers.nameNumber(8) == "ocho"
    assert spanish_numbers.nameNumber(9) == "nueve"
    assert spanish_numbers.nameNumber(10) == "diez"

def test_teen():
    assert spanish_numbers.nameNumber(11) == "once"
    assert spanish_numbers.nameNumber(12) == "doce"
    assert spanish_numbers.nameNumber(13) == "trece"
    assert spanish_numbers.nameNumber(14) == "catorce"
    assert spanish_numbers.nameNumber(15) == "quince"
    assert spanish_numbers.nameNumber(16) == "dieciséis"
    assert spanish_numbers.nameNumber(17) == "diecisiete"
    assert spanish_numbers.nameNumber(18) == "dieciocho"
    assert spanish_numbers.nameNumber(19) == "diecinueve"

def test_twenties():
    assert spanish_numbers.nameNumber(20) == "veinte"
    assert spanish_numbers.nameNumber(21) == "veintiuno"
    assert spanish_numbers.nameNumber(22) == "veintidós"
    assert spanish_numbers.nameNumber(23) == "veintitrés"
    assert spanish_numbers.nameNumber(24) == "veinticuatro"
    assert spanish_numbers.nameNumber(25) == "veinticinco"
    assert spanish_numbers.nameNumber(26) == "veintiséis"
    assert spanish_numbers.nameNumber(27) == "veintisiete"
    assert spanish_numbers.nameNumber(28) == "veintiocho"
    assert spanish_numbers.nameNumber(29) == "veintinueve"

def test_sub_hundred():
    assert spanish_numbers.nameNumber(30) == "treinta"
    assert spanish_numbers.nameNumber(31) == "treinta y uno"
    assert spanish_numbers.nameNumber(32) == "treinta y dos"
    assert spanish_numbers.nameNumber(33) == "treinta y tres"
    assert spanish_numbers.nameNumber(40) == "cuarenta"
    assert spanish_numbers.nameNumber(41) == "cuarenta y uno"
    assert spanish_numbers.nameNumber(42) == "cuarenta y dos"
    assert spanish_numbers.nameNumber(50) == "cincuenta"
    assert spanish_numbers.nameNumber(60) == "sesenta"
    assert spanish_numbers.nameNumber(70) == "setenta"
    assert spanish_numbers.nameNumber(80) == "ochenta"
    assert spanish_numbers.nameNumber(90) == "noventa"
    
def test_hundreds():
    assert spanish_numbers.nameNumber(100) == "cien"
    assert spanish_numbers.nameNumber(101) == "ciento uno"
    assert spanish_numbers.nameNumber(102) == "ciento dos"
    assert spanish_numbers.nameNumber(103) == "ciento tres"
    assert spanish_numbers.nameNumber(110) == "ciento diez"
    assert spanish_numbers.nameNumber(199) == "ciento noventa y nueve"

def test_multiple_hundreds():
    assert spanish_numbers.nameNumber(200) == "doscientos"
    assert spanish_numbers.nameNumber(201) == "doscientos uno"
    assert spanish_numbers.nameNumber(202) == "doscientos dos"
    assert spanish_numbers.nameNumber(203) == "doscientos tres"
    assert spanish_numbers.nameNumber(251) == "doscientos cincuenta y uno"
    assert spanish_numbers.nameNumber(252) == "doscientos cincuenta y dos"
    assert spanish_numbers.nameNumber(300) == "trescientos"
    assert spanish_numbers.nameNumber(400) == "cuatrocientos"
    assert spanish_numbers.nameNumber(500) == "quinientos"
    assert spanish_numbers.nameNumber(600) == "seiscientos"
    assert spanish_numbers.nameNumber(700) == "setecientos"
    assert spanish_numbers.nameNumber(800) == "ochocientos"
    assert spanish_numbers.nameNumber(900) == "novecientos"

def test_thousands():
    assert spanish_numbers.nameNumber(1000) == "mil"
    assert spanish_numbers.nameNumber(2000) == "dos mil"
    assert spanish_numbers.nameNumber(3000) == "tres mil"
    assert spanish_numbers.nameNumber(3333) == "tres mil trescientos treinta y tres"

def test_million():
    assert spanish_numbers.nameNumber(1000000) == "un millón"

def test_billion():
    assert spanish_numbers.nameNumber(1000000000) == "mil millones"