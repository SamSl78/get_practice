import os

def main():

  directory = input("enter the directory that you want to save the file : ")
  filename = input("enter the filename : ")
  name = input("enter your name : ")
  address = input("enter your address : ")
  phone_number = input("enter your phone number : ")
  if os.path.isdir(directory):
    writeFile = open(os.path.join(directory,filename),'w')
    writeFile.write(name+','+address+','+phone_number+'\n')
    writeFile.close()

    print("file contents:")
    readFile = open(os.path.join(directory,filename),'r') 
    for line in readFile:
      print(line)
      readFile.close()

  else:
    print("Directory Not Found")

main()
