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
  for i1 in list1:
    for i2 in range(lnt):
      for i3 in range(lnt):
        for i4 in range(lnt):
          for i5 in range(lnt):
            for i6 in range(lnt):
              for i7 in range(lnt):
                for i8 in range(lnt):
                  fWrt.write(i1 + list1[i2] + list1[i3] + list1[i4] + list1[i5] + list1[i6] + list1[i7] + list1[i8])
def main():
  print("###Anagram generator program###")
  print("###Written by Mikael Brenner###")
  print("-------------------------------")
  print("  \n") 
  file1 = raw_input("Type the name of the container file(with extension):   ")
  selected = raw_input("Select your usage mode: \n 1-Letters \n 2-Numbers \n 3-Mixed \n 0-Exit \n")
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
    
  
  
  

    