#Strings
#Q1
def askName():

    print("whats your name?")
    x = input()
    print("Hello", x)

    
    
#askName()

#Q2
def askNames():

    print("Hi, whats your name?")
    x = input()
    print("And you?")
    y = input()

    if (len(x) > len(y)):
        print (x , "have a longest name")
    else:
        print(y, "have a longest name")

#askNames()


#Q3

def vowelName():

    
    vowels= 'a','e','i','u','y','o'
    trans = input("whats your name? ")
    trans = trans.lower()
    t_list = trans.split()
    for word in t_list:
        if (word[0] in vowels):
            print("have a vowel name")
        else:
            print('dont have a vowel name')

#vowelName()

#Q4

def sumNambers():

    print("Hi, please give me a number")
    x = input()
    print("please give me more number")
    y = input()

    sum = int(x) + int(y)

    
    print("The sum of the tow numers you tell me is", sum)


#sumNambers()

#Q5

def withoutA():
    let = 'a','A'
    i = 0
    print("Please tell me sentence without any 'A'")

    trans = input()
    trans = trans.lower()
    t_list = trans.split()

    for word in t_list:
        if (word[i] in let):
            print("have A")
            break
       
        else:
            print("You are Win and wrote",len(trans), "letters")         
        

#withoutA()



#Q6



def fullName():
  
 
  myFullName =input("whats your fullname: ")

  words = myFullName.split()
  wordCount = len(words) 

  if(wordCount == 2 and myFullName[0].isupper() and (all(x.isalpha() or x.isspace() for x in myFullName))):

        print("Hii", myFullName)
  else:
      print("Invalid fullName")


#fullName():

#Q7

def wordCount():

  sentence =input("your sentence: ")

  words = sentence.split()
  wordCount = len(words) 

  print("You have ", wordCount , "words in your sentence")

#wordCount()

#8

def shortWord():

    word =input("your word: ")
    if (len(word) < 4):
       print("")
    else:
        print(word[0:2] + word[(len(word)-2):(len(word))] )

#shortWord()

#Q9

from datetime import date 
  
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year
  
    return age 
      
# Driver code  
#print(calculateAge(date(1997, 10, 19)), "years") 


#Q10

from datetime import date 
  
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
  
    return age 
      
# Driver code  
#print(calculateAge(date(1997, 10, 19)), "years") 

####################################################################################################################################
















