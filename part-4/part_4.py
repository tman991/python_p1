### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a 
# function.

title = input('Enter book title')
author = input('Enter autro name')
year = input('Enter year made')
rating = input('Enter book rating')
pages = input('Enter book pages')

my_book = {
    "title": "Harry Potter",
    "author": "J.K. Rowling",
    "year": "2008",
    "rating": "4.32",
    "pages": "374"
}

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out 
# your old function so you don't get an error, or copy/paste and give it a new name.

y = int(year)
r = float(rating)
p = int(pages)



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type 
# properly.

# Code here



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

def menu():
    print("[1] Option 1")
    print("[2] Option 2")
    print("[0] Exit the program.")

    menu()
    option = int(input("Enter your option: "))

while option != 0: 
    if option == 1:
        #do option 1 stuff
        print("Option 1 has been called")
    elif option == 2:
        #do option 2 stuff
        print("Option 2 has been called")
    else: 
        print("Invalid option.")





