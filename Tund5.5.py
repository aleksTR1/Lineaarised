#1
def kool():
    opilased, puudumised = [], []
    for i in range(int(input())):
        opilased.append(input())
        puudumised.append(int(input()))
    for i in range(len(opilased)):
        print(opilased[i], puudumised[i])

#3
def linnad():
    linnad, elanikud = [], []
    for i in range(int(input())):
        linnad.append(input())
        elanikud.append(int(input()))
    for i in range(len(linnad)):
        print(linnad[i], elanikud[i])

#4
def pood():
    tooted, hinnad = [], []
    for i in range(int(input())):
        tooted.append(input())
        hinnad.append(float(input()))
    for i in range(len(tooted)):
        print(tooted[i], hinnad[i])

#6
def sisseastumine():
    abiturientide, ballid = [], []
    for i in range(int(input())):
        abiturientide.append(input())
        ballid.append(int(input()))
    for i in range(len(abiturientide)):
        print(abiturientide[i], ballid[i])


