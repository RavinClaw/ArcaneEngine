import os, sys
import random, string, math, decimal
import csv, json

def InitializeNewAccount():
    _directory = ""
    _directory_2 = ""
    with open(_directory, "r") as file:
        accounts = json.load(file)
    
    with open(_directory_2, "r") as file:
        ...


def RESPONSE(text: str, status: str = ["OK" or "FAIL" or "ERROR"]):
    print("[ ARCANE ][ {0} ] {1}".format(status, text))
