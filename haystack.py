import random
import string

pun = "A MIDGET PSYCHIC ESCAPED FROM PRISON HE WAS A SMALL MEDIUM AT LARGE"

def generate_line(n):
    return "".join(random.choice(string.ascii_uppercase) for i in range(n))

def generate_haystack(letters,lines,pun,filename):
    lines = list(generate_line(letters) for i in range(lines))
    lines.append(pun.replace(" ","")) #remove spaces
    random.shuffle(lines)
    with open(filename,"w") as fp:
        for line in lines:
            fp.write(line + '\n')
    return None

#################possible solutions to consider
with open("haystack.txt") as fp:
    lines = fp.readlines()

english_letter_frequency = "etaoinsrhldcumfpgwybvkxjqz"
    
lines.sort(key=lambda line:line.count("E"),reverse=True)
lines.sort(key=lambda line:line.count("Z"))

def common(line):
    return line.count("E") + line.count("T") + line.count("A")

def rare(line):
    return line.count("Z") + line.count("Q") + line.count("J")

def freq(line):
    return line.count("E") + line.count("T") + line.count("A") - line.count("Z") - line.count("Q") - line.count("J")

def pvar(line):
    counter = Counter()
    for c in line:
        counter[c] += 1
    return statistics.pvariance(counter.values(),len(line)/26)

#works like a charm
score = dict() # dict(Z=1,Q=2,J=3,...,E=26)
for index,letter in enumerate(reversed(english_letter_frequency.upper())):
    score[letter] = index+1
def magic(line):
    return sum(score[c] for c in line)
lines.sort(key=magic,reverse=True)
