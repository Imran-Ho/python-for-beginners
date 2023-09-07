from datetime import date   # This code imports date of date and time.
import getpass              # this is for importing user name.

name = ''                   # declaration of name.
fahrenheit = ''             # declaration of fahrenheit.

# input section

print('Type your name below here to see the message')  # print the statement
name = input('type your Name: ')                     # input name
fahrenheit = input('input a degree: ')                # input any degree.

# Processing section

fahrenheit = float(fahrenheit)                      #
name_upperCase = name.upper()                        # turn the name into upper case.
name_lowerCase = name.lower()                        # turn the name into lower case.
name_title = name.title()                            # turn the name title into upper case.
length_of_name = str(len(name))                      # shows the length of the name string.
first_letter_of_name = name[0]                       # shows the first letter of name.
last_letter_of_name = name[-1]                       # shows the last letter of name.
name_length_slice = name[1:len(name)]                # shows the all letters except first one.
f_string_function = f"Hello {name_title}, Your name is {length_of_name} characters long!"   # shows how many characters contain in a string.
concatination_name = "Hello " + name_title + ", Your name is " + length_of_name + " characters long!"     # concatinate the statement.
name_multiplication = name * 10         # it shows 10 times output of name.
fahrenheit_integer = int(fahrenheit)
celsius_integer = (fahrenheit_integer - 32) * 5 / 9
celsius_float = (fahrenheit_integer - 32) * 5 / 9


# Output section
print(date.today())
print(getpass.getuser())

print(name)
print(type(name))
print(name_upperCase)
print(name_lowerCase)
print(name_title)
print(length_of_name)
print(first_letter_of_name)
print(last_letter_of_name)
print(name_length_slice)
print(f_string_function)
print(concatination_name)
print(name_multiplication)
print(celsius_float)
print(type(celsius_float))
print(celsius_integer)
print(type(celsius_integer))








