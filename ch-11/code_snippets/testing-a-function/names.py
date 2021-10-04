from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")

exit_words = ['q', 'quit', 'exit', 'end' ] 

while True:
    first = input("\nPlease give me a first name: ")
    if first in exit_words:
        break
    last = input("Please give me a last name: ")
    if last in exit_words:
        break
    formatted_name = get_formatted_name(first, last)
    print("Neatly formatted name:\n\n\t" + formatted_name)