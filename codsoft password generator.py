import string
import random

if __name__ == "__main__":
    a = string.ascii_lowercase
    # print(a)
    b = string.ascii_uppercase
    # print(b)
    c = string.digits
    # print(c)
    d = string.punctuation
    # print(d)
    plen = int(input("Enter password length\n")) #Todo1: Handle Gibberish
    s = []
    s.extend(list(a))
    s.extend(list(b))
    s.extend(list(c))
    s.extend(list(d))
    # print(s)
    # random.shuffle(s)
    # print(s)
    print("Your password is: ")
    print("".join(random.sample(s, plen)))
    # print("".join(s[0:plen]))

