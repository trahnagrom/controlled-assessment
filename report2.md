#Controlled Assessment

##Task 1


###Currency Converter

####Design 

For this task I needed to split the code into three different parts. These parts were:

1) The system should be able to have exchange rates changed when necessary by the user.

2) The user must input the amount they want to convert, the currency they are converting from and the currency they are converting to. 

3) The output must be put to two decimal places (eg. £1.09)

I also need to make sure that the input is a number, and an error message must be displayed if the input is invalid. 

The program will ask for what abbreviated curremcy code for the currency you want to convert from.
They will be: GBP, EUR, USD, JPY
GBP being Pounds Sterling(£), EUR is Euros(€), USD is US Dollars($), JPY is Japanese Yen(¥).
After that it then asks what currency you want to convert to.
It will use the same system before, currency codes.
It will then multiply the input by the currency rate.
It then prints out the result.
The answer is the value of the two numbers you just multiplyed.

This is what I believe is necessary for the code to work successfully.

####Programming Techniques
List - I used this whilst setting the rates in my first attempt at the code.



####Psuedocode

```
BEGIN
INPUT currency to be converted, currency converting to (Pound Sterling/Euro/US Dollar/Japanese Yen)
ASSIGN to variables: c_type1, c_type2
INPUT numb1 as c_type1[key]
MATCH c_type1, c_type2 to key in dictionary
IF c_type1 != Pound Sterling and c_type2 != Pound Sterling:
    CONVERT c_type1 into Pound Sterling
    CONVERT Pound Sterling into c_type2
    RETURN int of c_type2
ELSE:
    IDENTIFY Pound Sterling as c_type1 or c_type2
    CHANGE this value to or from Pound Sterling
    RETURN int of c_type2

```

####Attempt 1 (FAILED)

This was the first code for the convert
```python
allowables = ["pounds", "dollars", "euro", "yen"]
rates = [1,2,3,4]
pounds = 'pounds'
dollars = 'dollars'
yen = 'yen'
euro = 'euro'
print("Welcome to the currency converter")

var1 = None
while var1 not in range(len(allowables)):
    print('Please type the currency code you wish to convert from')
    for index, currency in enumerate(allowables):
        print ('enter {0} for {1}'.format(index, currency))
    var1 = input("Please type what currency you wish to convert from ")
var1 = int(var1)

var2 = None
while var2 not in range(len(allowables)):
    print('Please type the currency code you wish to convert to')
    for index, currency in enumerate(allowables):
        print ('enter {0} for {1}'.format(index, currency))
    var2 = input("Please type the currency that you wish to convert to ")
var2 = int(var2)

var3 = float(input("Please type the amount of currency you wish to convert "))

ammount = var3/rates[var1] *rates[var2]
print(' your converted ammount is {0} {1}'.format(ammount,allowables[var2]))

#[GBP]


# if var1 == pounds and var2 == dollars:
#     sumusd1 = var3 * 1.64
#     print("You will recieve, ", sumusd)
# elif something != somethingelse: 
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == pounds and var2 == euro:
#     sumeuro = var3 * 1.22
#     print("You will recieve, ", sumeuro)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == pounds and var2 == yen:
#     sumyen = var3 * 171.53
#     print("You will recieve, ", sumyen)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# #[USD]
# if var1 == dollars and var2 == pounds:
#     sumpounds = var3 * 0.61
#     print("You will recieve, ", sumpounds)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == dollars and var2 == euro:
#     sumeuro = var3 * 0.74
#     print("You will recieve, ", sumeuro)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == dollars and var2 == yen:
#     sumyen = var3 * 104.16
#     print("You will recieve, ", sumyen)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# #[EURO]
# if var1 == euro and var2 == dollars:
#     sumusd2 = var3 * 1.64
#     print("You will recieve, ", sumusd)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == euro and var2 == pounds:
#     sumpounds = var3 * 0.82
#     print("You will recieve, ", sumpounds)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == euro and var2 == yen:
#     sumyen = var3 * 141.24
#     print("You will recieve, ", sumyen)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# #[YEN]
#     if var1 == yen and var2 == dollars:
#         sumusd3 = var3 * 0.0096
#     print("You will recieve, ", sumusd3)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == yen and var2 == euro:
#     sumeuro = var3 * 0.0071
#     print("You will recieve, ", sumeuro)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == yen and var2 == pounds:
#     sumpounds = var3 * 0.0058
#     print("You will recieve, ", sumpounds)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)

```

This code worked but only with GBP used as the currency being converted from, I have commented my first attempt at the code however I realised I could make it much shorter by not using different equations for the conversions between each currency and instead, using one master equation, into which the currencies may be substituted.

####Attempt 2 (PASSED)

```python
currencies= {
    "Pound Sterling": 1, 
    "Euro": 1.2, 
    "US Dollar": 1.6, 
    "Japanese Yen": 200
    }

short_hand = {
    "GBP": "Pound Sterling",
    "EUR": "Euro",
    "USD": "US Dollar",
    "JPY": "Japanese Yen"
    }
    
c_type1 = raw_input("What Currency are you converting from? GBP/EUR/USD/JPY: ")

if c_type1 == "GBP" or "EUR" or "USD" or "JPY":
    "You entered %s" %(c_type1)
else:
    print c_type1, "is not a valid input"
    c_type1 = raw_input("Please enter a valid currency to convert from- GBP/EUR/USD/JPY: ")
    
c_type2 = raw_input("What Currency are you converting to? GBP/EUR/USD/JPY: ")

if c_type2 != "GBP" or "EUR" or "USD" or "JPY":
    "You entered %s" %(c_type1)
else:
    print c_type2, "is not a valid input"
    c_type2 = raw_input("Please enter a valid currency to convert to- GBP/EUR/USD/JPY: ")

def rate(c_type1, c_type2):
    if c_type1 == "GBP":
        print "exchange rate is", currencies["Pound Sterling"]
    if c_type1 == "EUR":
        print "exchange rate is", currencies["Euro"]
    if c_type1 == "USD":
        print "exchange rate is", currencies["US Dollar"]
    if c_type1 == "JPY":
        print "exchange rate is", currencies["Japanese Yen"]
    if c_type2 == "GBP":
        print "to", currencies["Pound Sterling"]
    if c_type2 == "EUR":
        print "to", currencies["Euro"]
    if c_type2 == "USD":
        print "to", currencies["US Dollar"]
    if c_type2 == "JPY":
        print "to", currencies["Japanese Yen"]

rate(c_type1, c_type2)

numb1 = float(raw_input("How much %s do you wish to convert? " %c_type1))

def conversion(fromCurr, toCurr, value):
    if fromCurr == "GBP":
        answer = value * float(currencies[short_hand[toCurr]])
        return answer
    elif toCurr == "GBP":
        answer = value / float(currencies[short_hand[fromCurr]])
    else:
        answer = value / float(currencies[short_hand[fromCurr]])
        answer = value * float(currencies[short_hand[toCurr]]) 
        return answer

print "%2.f %s is %2.f %s" %(numb1, short_hand[c_type1], conversion(c_type1, c_type2, numb1), short_hand[c_type2])

```
For this code I set the curreenices and their rates, using Punds Sterling as the base value meaning it held the value of 1. I then set the shorthand or currency codes, for example: Pounds Sterling is GBP, US Dollars are USD and so on. I then had the program ask the user for the currency code for the currencies they are converting from and to, followed by the amount they wish to convert. It then displays the conversion rate and the amount of their chosen currency that they will recieve. 

Task 1 PASSED



##Task 2


###Address book

1. lastname
2. firstname
3. phone        
4. email
5. address
6. postcode

####Design

At the start of the program, the user will be displayed an option whether to create a new entry into the address book or to search the address book for an already present entry. If 'Option 1' is selected then the user will be asked to enter the necessary information. If instead, 'Option 2' is selected then the user will be aksed to inputnthe piece of information they want to search, such as entering the name or phone number that is being searched for within the database. Once the bit of information wanted has been searched then the program runs through the different categories until a match is found. It will display an error message for each category that does not have a match within it. 


###Pseudo code
```
BEGIN
INPUT 1 or 2 depending on job that is necessary
IF INPUT=1
INPUT numb1 as c_type1[key]
MATCH c_type1, c_type2 to key in dictionary
IF c_type1 != Pound Sterling and c_type2 != Pound Sterling:
    CONVERT c_type1 into Pound Sterling
    CONVERT Pound Sterling into c_type2
    RETURN int of c_type2
ELSE:
    IDENTIFY Pound Sterling as c_type1 or c_type2
    CHANGE this value to or from Pound Sterling
    RETURN int of c_type2

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
