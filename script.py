
# exercise-01 Vowel or Consonant
letter = input("Enter a letter in the alphabet: ")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("The letter is a vowel")
else:
    print("The letter is a consonant")


# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase:
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered

length_of_phrase = input("Please enter a word or phrase: ")
while length_of_phrase != "quit":
    print("What you entered is", len(length_of_phrase), "characters long")
    length_of_phrase = input("Please enter a word or phrase: ")


# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years:
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx
# Hint:  Use the int() function to convert the string returned from input() into an integer

pups_age = int(input("Input your pups age in human years: "))
if pups_age <= 2:
    pups_age = pups_age * 10
else:
    pups_age = 20 + (pups_age - 2) * 7
print("Your pup's age in dog years is", pups_age)


# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

triangle = int(input("Enter the lengths of three sides of a triangle (at the same time): "))
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a == b == c:
    print("A triangle with sides of", a, b, c, "is an equalateral triangle")
elif a != b != c:
    print("A triangle with sides of", a, b, c, "is a scalene triangle")
else:
    print("A triangle with sides of", a, b, c, "is an isosceles triangle")


# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.
# Hint: The next number is found by adding the two numbers before it

a = 0
b = 1
print("term: 0 / number: 0")
print("term: 1 / number: 1")
for i in range(2, 50):
    c = a + b
    print("term:", i, "/ number:", c)
    a = b
    b = c

# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then promptshtt the user to enter the day of the month:
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.


