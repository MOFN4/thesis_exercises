# 1)   -- Leggere in input il file "input.txt" 
#   e stampare su schermo la percentuale di numeri pari non multipli di 10 rispetto a tutti i numeri pari presenti nel file, evitando di leggere le stringhe.

# 2) -- Salvare tutti i numeri letti dal file dentro un Python dictionary che avrà tre keys: "even_not_10" contenente la lista di numeri pari non multipli di 10,
#  "even_10" contenente la lista con i restanti numeri pari e "odd" contenente la lista con i numeri dispari.

# 3) -- Rimuovere dalla lista "odd" del dictionary tutti i numeri multipli di 3.

# 4) -- Salvare il dictionary in un output file chiamato "results.txt".


#================= Fill the lists ===============================#

def listsFillerAndPrintPercent() :

      lines = []
      numbers = []
      num = []
      evenList = []
      evenListNOT_10 = []
      oddList = []
      evenCounter = 0 #counter of even numbers
      evenCounterNOT_10 = 0 # counter of even-multiple of 10 numbers 
      percent = 0

      exLists = []
      
      f = open("input.txt", "r")
      
      
      for line in f:
            lines.append(line.rstrip()[13:])

      #print(lines)

      f.close()
    
      for i in lines:
            numbers.append(i.split())
      #print(numbers)      
      for j in numbers:
            for k in j:
              num.append(int(k))   
      #print(num)       
      for element in num:
                 
                 if element%2 == 0 :
                     evenCounter = evenCounter +1
                     if element%10 != 0:
                         evenCounterNOT_10 = evenCounterNOT_10 +1
                         evenListNOT_10.append(element)
                     else :
                         evenList.append(element)
                 else:
                     oddList.append(element)

      #print(evenCounter)
      #print(evenCounterNOT_10)
      percent = (evenCounterNOT_10/evenCounter)*100
      print(round(percent),"%\n")    

      exLists.append(oddList)
      exLists.append(evenList)
      exLists.append(evenListNOT_10)

      return exLists

       


#===========Remove multiples of 3 ===========================#

def oddElementRemoval(oddList):

     oddity =list(set(oddList))
     oddity_sorted = []

     for x in oddity:
         if x%3 == 0 :
            oddity.remove(x)
     oddity_sorted = sorted(oddity)
     
     return oddity_sorted 
#=====================Write Dictionary in a file======================#
def FillDictionary(exDict, oddList,evenListNOT_10,evenList):

    exDict ["odd"]  =  sorted(list(set(oddList)))
    exDict ["even_not_10"] = sorted(list(set(evenListNOT_10)))
    exDict ["even_10"] = sorted(list(set(evenList)))

    return exDict

#===================Create Output File===============================#

def CreateOutFile(exDict):
    #r = open("results.txt", "w")
    with open('results.txt', 'w') as f:
         for k in exDict.keys():
           f.write("'{}':'{}'\n".format(k, exDict[k]))
    
    f.close()
           
    #r.close() 



#=================== Main ===========================#
def main():

    CompleteList = []
    oddDictList = []
    evenDictList = []
    evenDictListNOT10 = []
    myDict = {}
    


    CompleteList = listsFillerAndPrintPercent()
    oddDictList = oddElementRemoval(CompleteList[0])
    evenDictList = CompleteList[1]
    evenDictListNOT10 = CompleteList[2]
    myDict = FillDictionary(myDict,oddDictList,evenDictListNOT10,evenDictList)
    CreateOutFile(myDict)

    



if __name__ == "__main__":
           main()