import os
from constants import *


def function2(from_folder=OUTPUT_FOLDER, to_folder=REPORTS_FOLDER):

    print("\n----- Second function")
    print(f"From folder value in function 2: {from_folder}")
    print(f"To folder value in function 2: {to_folder}")

    print("Filenames in from folder")
    for filename in os.listdir(from_folder):
        print(filename)
    print("Filenames in to folder")
    for filename in os.listdir(to_folder):
        print(filename)

def function1(folder=OUTPUT_FOLDER):
    print("\n----- First function")
    print(f"folder value in function 1: {folder}")
    print(f"Constant value : {OUTPUT_FOLDER}")
    for filename in os.listdir(folder):
        print(filename)
    function2()
