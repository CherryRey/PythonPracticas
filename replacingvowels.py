test_string = ""


def disemvowel(string_):
    vowel = ["a","e","i","o","u"]
    
    for i in string_:
        if i.lower() is vowel:
            string_ = string_.replace(i,"")
        return string_

print(disemvowel("hellomyworld"))
 