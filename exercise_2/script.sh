#!/bin/bash


name_of_path="../exercise_1/input.txt"
counter=0


while read line; do

if grep -q " 7 " <<< "$line"; then
  
   python3.6 exercise_2.py --file=../exercise_1/input.txt --row_number=$counter
fi
let counter++
done < $name_of_path



#- Creare un nuovo script bash chiamato "script.sh" e renderlo eseguibile. Fargli fare le seguenti cose:
 # -- Creare una variabile con il nome e path del file di testo dell'esercizio 1.
  #-- Lanciare lo script Python "exercises_2.py" (come eseguibile) da dentro "script.sh", passando come argomento di "--file" di 
  #"exercises_2.py" la variabile definita al punto prima, e fare in modo che quest'ultimo stampi su schermo solamente 
  #le righe dell'input file che contengono il numero 7 (attenzione, solo 7, non altri numeri che hanno il digit 7 in mezzo).
   #Suggerimento: utilizzare un bash for loop (https://www.cyberciti.biz/faq/bash-for-loop/).
#- Pushare tutto sulla repository remota con un commit "Added exercise 2.".
  
# crea una variabile con path, dentro script.sh fai lanciare lo script python e all'interno dai come argomento di file la variabile
# Loop for che itera su tutte le righe e lancia lo script per ogni riga. Ma voglio che lo lanci solo se nella riga del file txt è 
# presente il numero 7   
# Fai un loop bash        


# controlla che la stringa " 7 " sia contenuta nella riga!!!