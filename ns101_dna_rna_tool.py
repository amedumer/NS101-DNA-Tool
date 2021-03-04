# -*- coding: utf-8 -*-
"""NS101 DNA/RNA Tool

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11p4MKDEWl9o9qcnfR0mSyuMcjD2mSto-

# **Welcome to the translation/transcription tool for NS101!**
*This tool is coded by Ahmet Ömer Kayabaşı, have fun using it!*
"""

import functools

db={"UUU":"Phe","UUC":"Phe","CUU":"Leu","UUA":"Leu","UUG":"Leu","CUU":"Leu","CUC":"Leu","CUA":"Leu","CUG":"Leu","AUU":"Ile","AUC":"Ile","AUA":"Ile","AUG":"Met","GUU":"Val","GUC":"Val","GUA":"Val","GUG":"Val","UCU":"Ser","UCC":"Ser","UCA":"Ser","UCG":"Ser","CCU":"Pro","CCC":"Pro","CCA":"Pro","CCG":"Pro","ACU":"Thr","ACC":"Thr","ACA":"Thr","ACG":"Thr","GCU":"Ala","GCC":"Ala","GCA":"Ala","GCG":"Ala","UAU":"Tyr","UAC":"Tyr","UAA":"Stop","UAG":"Stop","UGA":"Stop","CAU":"His","CAC":"His","CAG":"Gln","CAA":"Gln","AAU":"Asn","AAC":"Asn","AAA":"Lys","AAG":"Lys","GAU":"Asp","GAC":"Asp","GAA":"Glu","GAG":"Glu","UGU":"Cys","UGC":"Cys","UGG":"Trp","CGU":"Arg","CGC":"Arg","CGA":"Arg","CGG":"Arg","AGA":"Arg","AGG":"Arg","AGU":"Ser","AGC":"Ser","GGU":"Gly","GGC":"Gly","GGA":"Gly","GGG":"Gly"}

def dnarnaCheck(inp):

  if len(inp) % 3 != 0:
    print("Invalid input: {}".format("Length of DNA/RNA must be a factor of 3! "))
    return False

  if len(list(filter(lambda x: x not in "AGCTU", list(inp)))) != 0:
    print("Invalid input: {}".format("Invalid characthers detected in the input, please try again. "))
    return False

  return True

def menuCheck(inp):
  if len(inp) != 1:
    return False

  if len(list(filter(lambda x: x not in "1234", list(inp)))) != 0:
    return False

  return True

def transcription(chr, toRna):
    #from template to rna
    if chr == 'A':
      if toRna:
        return 'U'
      else:
        return 'T'

    elif chr == 'T':
      return 'A'

    elif chr == 'G':
      return 'C'

    elif chr == 'C':
      return 'G' 

    elif chr == 'U':
      return 'A' 

def TStoRNA():
  reminder()
  dna = input("Please give the template strand: ").upper()

  if " " in dna:
    dna = str(functools.reduce(lambda x,y: x + y, list(filter(lambda x: x != ' ',dna))))

  while not dnarnaCheck(dna):
    print("")
    dna = input("Please give the template strand: ").upper()

    if " " in dna:
      dna = str(functools.reduce(lambda x,y: x + y, list(filter(lambda x: x != ' ',dna))))
    
  dna = dna.upper()

  rnaList = list(transcription(chr,True) for chr in dna)
  rna = str(functools.reduce(lambda x,y: x + y, rnaList ))

  print("Template Strand is: ")
  printStr(dna)

  print("Resulting RNA after transcription is: ")
  printStr(rna)

  print("Resulting aminoacids accordding to translation are: ")
  aminoAcid(rna)


def CStoRNA():
  reminder()
  dna = input("Please give the coding strand: ").upper()

  if " " in dna:
    dna = str(functools.reduce(lambda x,y: x + y, list(filter(lambda x: x != ' ',dna))))

  while not dnarnaCheck(dna):
    print("")
    dna = input("Please give the coding strand: ").upper()

    if " " in dna:
      dna = str(functools.reduce(lambda x,y: x + y, list(filter(lambda x: x != ' ',dna))))
    
  dna = dna.upper()

  templateList = list(transcription(chr,False) for chr in dna)
  template = str(functools.reduce(lambda x,y: x + y, templateList ))

  rnaList = list(transcription(chr,True) for chr in template)
  rna = str(functools.reduce(lambda x,y: x + y, rnaList ))
  
  print("")
  print("Coding Strand is: ")
  printStr(dna)
  print("Template Strand is: ")
  printStr(template)
  print("Resulting RNA after transcription is: ")
  printStr(rna)

  print("Resulting aminoacids accordding to translation are: ")
  aminoAcid(rna)

def reminder():
    print("""
Reminder:

1 - Length of your strand must be a factor of 3.
2 - Your strand can only include letters A T G C
  
  """)

def aminoAcid(rna):
  antiCodons = list(rna[i:i+3] for i in range(0,len(rna), 3))
  resultStr = ""

  for antiCodon in antiCodons:
    resultStr += db[antiCodon] + " "
    
  print(resultStr + "\n")

  if not antiCodons[len(antiCodons) - 1] in ["UAG","UAA","UGA"]:
    print("Warning: Your RNA sequence doesnt end with a stop codon.")
  
  if not antiCodons[0] == "AUG":
    print("Warning: Your RNA sequence doesnt start with methionine.")


def printStr(dna):
    temp = list(dna[i:i+3] for i in range(0,len(dna), 3))

    print(" ".join(temp))
    print("")

def RNAtoCS():
  reminder()
  rna = input("Please give the RNA: ").upper()

  if " " in rna:
    rna = str(functools.reduce(lambda x,y: x + y, list(filter(lambda x: x != ' ',dna))))

  while not dnarnaCheck(rna):
    print("")
    rna = input("Please give the RNA: ").upper()

    if " " in rna:
      rna = str(functools.reduce(lambda x,y: x + y, list(filter(lambda x: x != ' ',dna))))
    
  rna = rna.upper()

  tsList = list(transcription(chr,False) for chr in rna)
  ts = str(functools.reduce(lambda x,y: x + y, tsList ))

  csList = list(transcription(chr,False) for chr in ts)
  cs = str(functools.reduce(lambda x,y: x + y, csList ))

  print("")
  print("Your RNA is: ")
  printStr(rna)

  print("Resulting Template Strand is: ")
  printStr(ts)

  print("Resulting Coding Strand is: ")
  printStr(cs) 

def menu():
  print("""
-----------------------------------------------------------
There are several options offered which you can find below.

1 - From: Coding Strand   To: RNA
2 - From: Template Strand To: RNA
3 - From: RNA             To: Coding Strand 
4 - Exit
  """)

  choice = input("Your choice: ")

  while not menuCheck(choice):
    choice = input("Given input was incorrect. Please try again: ")

  choice = int(choice)

  if choice == 4: return False

  if choice == 1: CStoRNA()
  
  elif choice == 2: TStoRNA()

  elif choice == 3: RNAtoCS()

  return True


print("Hi, and welcome transcription/translation machine!")

if __name__ == "__main__":
    while menu():
        continue

