#  -- Utilizzi il modulo "argparse" (https://docs.python.org/3/library/argparse.html) per prendere in input da riga di comando il file di testo
#  dell'esercizio 1 "input.txt" (passargli direttamente il path dell'esercizio 1) e un numero di riga di quel file e che quindi funzioni in questo modo:
#  "python exercise_2.py --file=<file_di_testo> --row_number=<numero_di_riga>".
#-- Stampi su schermo la riga "row_number" del file "file" presi in input dallo script.
#- Rendere lo script Python eseguibile, in modo che anzichè usare "python blabla.py" si possa usare "./blabla.py". 



#!/usr/bin/env python3.6


import argparse


"""parser = argparse.ArgumentParser(description="Print a given line of a given file.txt")
parser.add_argument("--file=",  help= "Insert file name")
parser.add_argument("--row_number", type=int, help= "The line to be printed")
args = parser.parse_args()"""

"""count_the_line = 0

with open(args.file) as file:
    for line in args.file :
         if count_the_line == args.row_number:
             print(line)

         count_the_line = count_the_line +1

args.file.close()

#file_path = "../../exercises/thesis_exercises/exercise_1" + """


def main():

    parser = argparse.ArgumentParser(description="Print a given line of a given file.txt")
    parser.add_argument("--file", "-f", type=str, help= "Insert file path")
    parser.add_argument("--row_number", type=int, help= "The line to be printed")
    args = parser.parse_args()
    count_the_line = 0
    
    with open(args.file) as file:
        for line in file :
            if count_the_line == args.row_number:
                print(line)
                

            count_the_line = count_the_line +1



if __name__ == "__main__":
    main()