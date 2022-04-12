# put your python code here
import sys

in_string = str(sys.stdin.readline()).strip()
in_string = in_string.lower()

clear_string = ""
for every_char in in_string:
    if every_char.isalpha():
        if every_char not in clear_string:
            clear_string = clear_string + every_char

# теперь сотрировка
encoded_string = clear_string.encode()
run_again = True
while run_again:
    run_again = False
    for i in range(len(encoded_string) - 1):
        if encoded_string[i] > encoded_string[i + 1]:
            #    #поменять местами
            replace_str = chr(encoded_string[i + 1]) + chr(encoded_string[i])
            replace_str = replace_str.encode()
            encoded_string = encoded_string[:i] + replace_str + encoded_string[i + 2:]
            #    #запустить цикл по новой, пока возможные перестаовки не закончатся
            run_again = True

print(encoded_string.decode())
