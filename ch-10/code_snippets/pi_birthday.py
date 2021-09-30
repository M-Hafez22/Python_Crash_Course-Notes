filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print(f"Your birthday ({birthday[:2]}/{birthday[2:4]}/19{birthday[4:]}) appears in the first million digits of pi!")
else:
    print("Sorry, Your birthday does not appear in the first million digits of pi.")
