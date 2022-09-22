### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["William Shakespeare", "George Orwell", "J Rowling", "Virginia Woolf", "Ernest Hemingway", "Ernest Hemingway", "William Faulkner",]

# Now let's add a new author to the end with the .append() method. Type your code below.

my_authors.append("H.G. Wells")
# Example: my_authors.append("H.G. Wells")


# Now let's remove an element in the list

my_authors.remove("William Shakespeare")
# Example: my_authors.remove("H.G. Wells")


# Now access an element by it's index. (Remember it indexes start at 0.)

my_authors[0]
# Example: my_authors[2]


# Now slice the list.

my_authors[0:3]
# Example: my_authors[1:4]


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

my_tuple = ("George Orwell", "Virginia Woolf", "Ernest Hemingway", "William Faulkner")
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###

# Create a set with your authors.

author_set = {"George Orwell", "Virginia Woolf", "Ernest Hemingway", "William Faulkner"}
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


# Add a new author to your set.

author_set.add("William Shakespeare")
# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.

print(author_set.add("William Shakespeare"))
# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

for author in my_authors:
    print(author)


for author in author_set:
    print(author)

for author in my_tuple:
    print(author)



