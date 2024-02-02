def is_anagram(string1, string2):
 
    string1 = string1.lower().replace(" ","")
    string2 = string2.lower().replace(" ","")

    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)

    return sorted_string1 == sorted_string2


string1 = "listen"
string2 = "silent"

if is_anagram(string1, string2):
    print("Output: True")
else:
    print("Output: False")
