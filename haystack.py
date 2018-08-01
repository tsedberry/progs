import random
import string

pun = "A MIDGET PSYCHIC ESCAPED FROM PRISON HE WAS A SMALL MEDIUM AT LARGE"

def generate_line(n):
    return "".join(random.choice(string.ascii_uppercase) for i in range(n))

def generate_haystack(letters,lines,pun,filename):
    lines = list(generate_line(letters) for i in range(lines))
    lines.append(pun.replace(" ","") #remove spaces
    random.shuffle(lines)
    with open(filename,"w") as fp:
        for line in lines:
            fp.write(line + '\n')
