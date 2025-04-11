#1
def kool():
    opilased, puudumised = [], []
    for i in range(int(input())):
        opilased.append(input())
        puudumised.append(int(input()))
    for o, p in zip(opilased, puudumised):
        print(o, p)

#3
def linnad():
    linnad, elanikud = [], []
    for i in range(int(input())):
        linnad.append(input())
        elanikud.append(int(input()))
    for l, e in zip(linnad, elanikud):
        print(l, e)

#4
def pood():
    tooted, hinnad = [], []
    for i in range(int(input())):
        tooted.append(input())
        hinnad.append(float(input()))
    for t, h in zip(tooted, hinnad):
        print(t, h)

#6
def sisseastumine():
    abiturientide, ballid = [], []
    for i in range(int(input())):
        abiturientide.append(input())
        ballid.append(int(input()))
    for a, b in zip(abiturientide, ballid):
        print(a, b)


