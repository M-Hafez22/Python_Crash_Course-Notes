# filename = 'pi_digits.txt'
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    # pi_string += line.rstrip()
    pi_string += line.strip()

print(pi_string + '\n')
print(f" File Length: {len(pi_string)}")
