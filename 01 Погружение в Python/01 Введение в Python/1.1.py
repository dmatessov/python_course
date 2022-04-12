import sys

string1 = str(sys.stdin.readline()).strip()
string2 = str(sys.stdin.readline()).strip()
string1 = string1.lower()
string2 = string2.lower()

done_chars = ""
for every_char in string2:
    if every_char.isalpha():
        if not every_char in done_chars:
            counter = ""
            cur_position = 1
            for current_char in string1:
                if current_char == every_char:
                    counter = counter + (str(cur_position) if counter == "" else (" " + str(cur_position)))
                cur_position = cur_position + 1
            done_chars = done_chars + every_char
            print(every_char, counter if counter != "" else "None")
