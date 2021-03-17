print("Hello interpreter!")

message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course reader!" # the variable message has the new string assigned to it.
print(message) # will return error cause of typo

simple_message = "simple message"
print(simple_message)

simple_message = "even more simple"
print(simple_message)

'This is a string.'
"This is a string also."

print('I told my friend, "Python is my favorite language!"')
print("The language 'Python is named after Monty Python, not the snake.")
print("One of Python's strengths is its diverse and supportive community.")

name = "ada lovelace"
print(name.title()) # the title() method will make both 'ada' and 'lovelace' start with a capital letter

name = "adalovelace" # in this case the title()method will show only the first.
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

fist_name = "ada"
last_name = "lovelace"
full_name = fist_name.title() + " " + last_name.title()
print(full_name)
print("Hello, " + full_name.title() + "!")

print("Python")
print("\tPython") # the \t should be inside the string

print("Languages:\nPython\nC\nC++\nJava\nHaskell\nJavascript\nPHP")
print("Languages:\n\tPython\n\tC\n\tC++\n\tJava\n\tHaskell\n\tJavascript\n\tPHP")

favorite_language = 'python '
print(favorite_language)

favorite_language = ' python '
print(favorite_language.rstrip()) # strips the whitespace of the right side of the string
print(favorite_language.lstrip() )# strips the whitespace of the left side of the string
print(favorite_language.strip()) # strips all whitespace of the string