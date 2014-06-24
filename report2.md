#controlled_assessment

##Task 1


###Money converter

1. The system should be able to have exchange rates changed regulary by the user
1. The user must input an amount, select a currency to convert from and to, and get the correct output
1. The amount must be put to two decimal places E.G £1.09



###Pseudo code

```
It will ask for what money you want to convert from.
It asks for the numbers 1 to 4.
This means if the user inputs 1 its pounds, if the user inputs 2 its euros and so on.
After that it then asks what currency you want to convert to.
Once again it asks the user to input 1 to 4 numbers.
It then takes the numbers (Rates) and multiplys then together.
It then prints out the answer.
The answer is the value of the two numbers you just multiplyed.
If you enter you want to convert from pounds, to pounds it just prints the number you entered.
```
This is my plan to make task one work.



###Attemt 1 (FAILED)

This was the first code for the convert
```python
if choice == rates[0]:
   entry= input("You have selected Pounds. Now please enter a sum of money:")
   answer = (entry*rates[0])
   print(answer)
    
if choice == rates[1]:
   entry= input("You have selected Dollar. Now please enter a sum of money:")
   answer = (entry*rates[1])
   print(answer)
    
if choice == rates[2]:
   entry= input("You have selected Yen. Now please enter a sum of money:")
   answer = (entry*rates[2])
   print(answer)
    
if choice == rates[3]:
   entry= input("You have selected Euro. Now please enter a sum of money:")
   answer = (entry*rates[3])
   print(answer)
```


###Attemt 2 (PASSED)

```python
#http://stackoverflow.com/questions/20398017/showing-decimal-places-python-2-7-and-decimal-datatype#
#setup the decimal data type (including number of decimal places)
import decimal

#get the current value and type from the user
currencyAmount = decimal.Decimal(raw_input('please enter the amount: '))
currencyType = int(raw_input('please enter the type or if you want to change the rates (1 = pound, 2 = euro, 3 = dollar, 4 = yen): '))

#set the exchange rates (based on sterling)
euro = decimal.Decimal('1.2')
dollar = decimal.Decimal('1.6')
yen = decimal.Decimal('200')
#This will multiply the 2 numbers that you want to convert 

#convert the currency into pound sterling
if (currencyType == 2):
    currencyAmount = currencyAmount / euro
elif (currencyType == 3):
    currencyAmount = currencyAmount / dollar
elif (currencyType == 4):
    currencyAmount = currencyAmount / yen
#Tells the computer if a number 1 to 4 is picked it will run ethier pound, euro, yen or dollars 

#ask the user what currency they want it converted into
currencyConvert = int(raw_input('please enter the currency you would like to convert to (1 = pound, 2 = euro, 3 = dollar, 4 = yen): '))
#it then takes the numbers 1 to 4 and runs what the number is linked to.
#convert the currency into the new format (pound already done in previous steps)
if (currencyConvert == 2):
    currencyAmount = currencyAmount * euro
elif (currencyConvert == 3):
    currencyAmount = currencyAmount * dollar
elif (currencyConvert == 4):
    currencyAmount = currencyAmount * yen

#show the amount of money converted to user
print 'the result of the currency conversion was ',  currencyAmount.quantize(decimal.Decimal('0.00'))
```

Task 1 was one of the hardest tasks partly because of trying to convert to numbers.
It took a while but i finaly got it. After that it was easy.
Just put some words to print to the user to make it look pretty.

Task 1 PASSED



##Task 2


###Address book

1. A surname and first name
1. Two lines of the address and the post code
1. A telephone number
1. Date of birth
1. Email address

Search with:

1. By surname to retrieve and display the details for a contact
1. By the date of birth to retrieve and display all contacts with a birthday in a particular month


###Pseudo code
```
Welcome the user to the address book     
The address book will then ask the user to input two number to select if they want to add or search for an address
If the user clicks 1 they will be taken to the address adder
It will ask them to make an address based of their:
First name
Last name
Telephone
Email 
Address
Once this process is done it will add it to the address book to be search for at a later date
If the user pressed 2 then it will take them to the search engine
It will ask the user if they want to search by surname or by date of birth
If 1 is pressed it will ask the user to input a surname
The user will input a surname and the computer will find anyone in the address book with that surname
It will then print to the user all of the people with that surname
If 2 is pressed then it will search with the date of birth
The user must input the numbers 01 to 12
The numbers the user has input to the computer will then be used to search for the date of birth
The computer will then print all of the contacts with the same date
```


###Task 2 (PASSED)

```python
# surnames = {
#     "Jackson": ["Samantha Jackson", "2 Heather Row", "Basingstoke", "RG21 3SD", "01256 135434",	"23/04/1973", "sam.jackson@hotmail.com"]
#     "VickersJ": ["Jonathan",	"18 Saville Gardens", "Reading", "RG3 5FH",	"01196 678254",	"04/02/1965", "the_man@btinternet.com"]
#     "Morris": ["Sally", "The Old Lodge", "Hook", "RG23 5RD", "01256 728443", "19/02/1975", "smorris@fgh.co.uk"]
#     "Cobbly": ["Harry", "345 The High Street", "Guildford", "GU2 4KJ", "01458 288763", "30/03/1960", "harry.cobbly@somewhere.org.uk"]
#     "Khan": ["Jasmine", "36 Hever Avenue", "Edenbridge", "TN34 4FG", "01569 276524", "28/02/1980", "jas.khan@hotmail.com"]
#     "VickersH": ["Harriet", "45 Sage Gardens", "Brighton", "BN3 2FG", "01675 662554", "04/04/1968", "harriet.vickers@btinternet.com"]
#     }
#Loads up the address file to the code so it can find them
addressses = []
def getAddrs():
    with open('addressbook.csv')as book:
        data = book.read()
        for line in data.split('\r\n'):
            address = line.split(',')
            addressses.append(address)
#This welcomes the user and asks the user to select two choices
getAddrs()
print("Welcome to the Address Book!")
answer = None
while answer not in ["1", "2"]:
   answer = raw_input("Are You Adding An Address (Press 1) \nOr finding an address? (Press 2) ") 



 

#Creating a file into the address book and saving it for later
if answer == "1" : 
    print (" You have selected to create an entry.")

#Now it asks the user info on the person so it is easier to find them
    lastname = raw_input("What is the persons last name? ")
    firstname = raw_input("What is the persons first name? ")
    phone = raw_input("What is the persons phone number? ")
    email = raw_input("What is the persons email address? ")
    address = raw_input("What is the persons address? ")

    #This line tells the computer to open/create a file

    tempfile = open("datafile.txt","a")
    
    #adds the first name, last name, phone, email and address to the address book
    tempfile.write(firstname + " " + lastname + ", " + phone + ", " + email + ", " + address)
    tempfile.write("\n")
    tempfile.close()
    quit()

#If searching for a file already created

if answer == "2":
    choice = raw_input("you have selected to search for an entry. Would you like to search by surnames [Press 1] \n Or by month of birth [Press 2]")
    
#asks the user to input the lastname of someone. once done it then searchs the system for anyone with the last name
#after that it then gives you the list of people with that last name along with their info
if choice == "1":
    surname_search = raw_input("What surname are you searching for?: ")
    for address in addressses:
        if surname_search == address[0]:
            print address
            
#Pretty much the same as the choice 1 but you're looking for the birth month
if choice == "2":
    month_search = raw_input("What month are you searching for? \n(in numbers E.G 01=january)")
    for address in addressses:
        if len(address)>6:
            dd,mm,yy = address[6].split('/')
            if month_search == mm:
                print address
                
else:
   print("Incorrect entry, please restart the programme, and try again.")
   
It was a pain trying to transfer to contacts at first but once i found out to import the datafile it was fine
Up to a point were the search line is.
The search part of the code was one of the worst to overcome.
I think it was because i was over thinking it.
But now its fixed and task 2 is complete
```
Task 2 PASSED



##Task 3


###ISBN

1. The number entered must be correct length
1. Only contains the digits 0 to 9


###Pseudo code

```
Asks the user to input two numbers
If 2 pressed the programme is ended
If 1 is pressed the code goes on
It asks the to input a 10 digit number
If the digit number is not 10 it then loops to enter a 10 digit number
Once the user has input a 10 digit number the maths side of the code works out the number
The end result it the output to the user
```

###Task 3 (PASSED)
```python
#Tells the user to choose between starting or ending the programme
decision = str(input(""" What would you like to do?; 
1) Convert a 10 digit number to an ISBN number(1) 
2) Quit and end the programme(2)""")) 

#Ends the programme
if decision == "2": 
    quit()
    print("Good Bye!") 
    
#Asks the user to input a 10 digit number
elif decision == "1": 
    (ISBN)=raw_input("Enter a 10 digit number") 
    
#If the number isnt 10 it will loop round and ask the user to re-input the number
while len(ISBN)!= 10: 

#Informs the user the number that has been given to the computer isnt 10 digits
    print('you have not entered a 10 digit number!!!') 
    ISBN=int(input('Please enter a 10 digit number ')) 
    continue

#This is the math side of things. its pretty much just the ISBN.
else: 

    Di1=int(ISBN[0])*11
    Di2=int(ISBN[1])*10
    Di3=int(ISBN[2])*9
    Di4=int(ISBN[3])*8
    Di5=int(ISBN[4])*7
    Di6=int(ISBN[5])*6
    Di7=int(ISBN[6])*5
    Di8=int(ISBN[7])*4
    Di9=int(ISBN[8])*3
    Di10=int(ISBN[9])*2

sum=(Di1+Di2+Di3+Di4+Di5+Di6+Di7+Di8+Di9+Di10) 

num=sum%11
Di11=11-num 
if Di11==10: 
    Di11='X'
ISBNNumber=str(ISBN)+str(Di11) 
#Shows the user what number has been output by the computer thus being the ISBN number
print('The ISBN number is -->    ' + ISBNNumber) 

The hardest part of the code was the maths part but nothing else was that bad.
It was pretty easy.
```
Task 3 PASSED
