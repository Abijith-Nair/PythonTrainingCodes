def cofvandc(text):
    v = "AEIOUaeiou"
    c = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    vc = 0
    cc = 0
    
    for char in text:
        if char in v:
            vc += 1
        elif char in c:
            cc += 1
    
    return vc, cc

inpstr = input("Enter a string: ")

v, c = cofvandc(inpstr)


print("Total characters:", len(inpstr))
print("Vowels:", v)
print("Consonants:", c)