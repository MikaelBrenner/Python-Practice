#A program that creates anagrams with letters,numbers and custom words 
#provided by the user,exporting the to a selected by the user container file.
#Written by Mikael Brenner
#
#
#
letters=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","b","n","m"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
def anagrammer(list1,fWrt):
  lnt = len(list1)
  rng = range(lnt)
  for i1 in list1:
    for i2 in rng:
      for i3 in rng:
        for i4 in rng:
          for i5 in rng:
            for i6 in rng:
              for i7 in rng:
                for i8 in rng:
                  fWrt.write(i1 + list1[i2] + list1[i3] + list1[i4] + list1[i5] + list1[i6] + list1[i7] + list1[i8])
def main():
  print("###Anagram generator program###")
  print("###Written by Mikael Brenner###")
  print("-------------------------------")
  print("  \n") 
  file1 = input("Type the name of the container file(with extension):   ")
  selected = input("Select your usage mode: \n 1-Letters \n 2-Numbers \n 3-Mixed \n 0-Exit \n")
  print(" \n")
  with open(file1,"r+") as fOn:
    if selected == "1":
      anagrammer(letters,fOn)
    if selected == "2":
      anagrammer(numbers,fOn)
    if selected == "3":
      mixed = numbers + letters
      anagrammer(mixed,fOn)
    if selected == "0":
      pass
if __name__ == "__main__":
  main()
    
  
  
  

    
