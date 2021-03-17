message = "One of Python's strengths is its diverse community."
print(message)
# single quotation in double quotatation will work.
# message = 'One of Python's strenghts is its diverse community.'
# print(message)
# single quotation in single quotation will not work.
# Parentheses are not needed with quotation marks in Python 2.
# 2.3
name = "Eric"
print(f"Hello {name}, would you like to learn Python today?")
# the f in the beginning is for formatting the string. More on this later.
# 2.4
nameOfPerson = "benjamin koot"
print(nameOfPerson.title())
print(nameOfPerson.upper())
print(nameOfPerson.lower())
# 2.5
quote = "Time is a game played beautifully by children."
author = "Heraclitus"
print(f"{author} said: {quote}")
# 2.6
famous_person = "Heraclitus"
message = "Much learning does not teach understanding."
print(famous_person + " once said: " + message)
# 2.7
person_name = "\t\njoshua koot"
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())