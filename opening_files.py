# USING PYTHON TO OPEN FILES

# THE open() FUNCTION IS USED TO OPEN FILES

# open() TAKES TWO ARGUMENTS ('FILENAME, MODE')

# FOR EXAMPLE: open(hello.txt, r) r means 'read'

# THE FILE OBJECT ALSO HAS A read() method

f = open('hello.py', 'r')
g = f.read()

# THE READ METHOD WILL RETURN THE CONTENTS OF f AS A STRING
# TO MAKE THE DATA MORE USEFUL, WE USE SPLITING TO CONVERT IT INTO A list

sample = 'john,plastic,joe'
split_list = sample.split(',')  # SPLITS AT EACH COMMA
print(split_list)

string_two = 'How much wood\ncan a woodchuck chuck\nif a woodchuck\ncan chuck wood?'
split_string_two = string_two.split('\n')  # SPLITS AT EACH \n
print(split_string_two)

# USING LOOPS TO split() DATA
cities = ['Boulder', 'Austin', 'San Francisco', 'Seattle', 'Vancouver']

# TO LOOP THROUGH THE LIST:
for city in cities:
   print(city)
