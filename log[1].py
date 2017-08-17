import random

bonne_reponse = 0
question_total = 0
vari_faux = "Taper oui si c'est vrai, tapez non si c'est faux"

def check(question, reponse):
    if question == reponse:
        print("Bonne réponse")
        print()
    else:
        print("Mauvaise réponse")
        print()

while True:
    regle = random.randrange(1, 9)
    if regle == 1:
        exposant=0
        puissance=1
        c=random.randrange(1, 11)
        question=0
        reponse=int(input("log" + str(c) + " " + str(puissance) + " = "))
        check(question, reponse)

    elif regle == 2:
        c=random.randrange(1, 11)

        question=1
        reponse=int(input("log" + str(c) + " " + str(c) + " = "))
        check(question, reponse)

    elif regle == 3:
        c=random.randrange(1, 11)
        n=random.randrange(-11, 11)

        question=n
        reponse=int(input("log" + str(c) + " " + str(c) + "^" + str(n) + " = "))
        check(question, reponse)

    elif regle == 4:
        print(vari_faux)
        sous_regle=random.randrange(1, 3)
        c=random.randrange(1, 11)
        m=random.randrange(1, 11)
        n=random.randrange(1, 11)
        if sous_regle == 1:
            question = "oui"
            reponse = str(input("log" + str(c) + " (" + str(m) + "*" + str(n) + ") = log" + str(c) + " " + str(m) + " + log" + str(c) + " " + str(n) + " ?"))
            check(question, reponse)
        else:
            question = "non"
            reponse = str(input("log" + str(c) + " (" + str(m) + "*" + str(n) + ") = log" + str(c) + " " + str(m) + " * log" + str(c) + " " + str(n) + " ?"))
            check(question, reponse)

    elif regle == 5:
        print(vari_faux)
        sous_regle=random.randrange(1, 3)
        c=random.randrange(1, 11)
        m=random.randrange(1, 11)
        n=random.randrange(1, 11)
        if sous_regle == 1:
            question = "oui"
            reponse = str(input("log" + str(c) + " (" + str(m) + "/" + str(n) + ") = log" + str(c) + " " + str(m) + " - log" + str(c) + " " + str(n) + " ?"))
            check(question, reponse)
        else:
            question = "non"
            reponse = str(input("log" + str(c) + "(" + str(m) + "/" + str(n) + ") = log" + str(c) + " " + str(m) + " / log" + str(c) + " " + str(n) + " ?"))
            check(question, reponse)

    elif regle == 6:
        print(vari_faux)
        sous_regle=random.randrange(1, 3)
        c=random.randrange(1, 11)
        m=random.randrange(1, 11)
        prod=random.randrange(-11, 11)
        while prod == 0:
            prod=random.randrange(-11, 11)
        if sous_regle == 1:
            question = "oui"
            reponse = str(input("log" + str(prod) + "/" + str(c) + " " + str(m) + " = " + str(prod*-1) + "log" + str(c) + " " + str(m) + " ?"))
            check(question, reponse)
        else:
            question = "non"
            reponse = str(input("log" + str(prod) + "/" + str(c) + " " + str(m) + " = log" + str(c) + " " + str(prod) + " - log" + str(c) + " " + str(m) + " ?"))
            check(question, reponse)

    elif regle == 7:
        print(vari_faux)
        sous_regle=random.randrange(1, 3)
        c=random.randrange(1, 11)
        m=random.randrange(1, 11)
        prod=random.randrange(-11, 11)
        if sous_regle == 1:
            question = "oui"
            reponse = str(input("log" + str(prod*-1) + "/" + str(c) + " " + str(m) + " = " + str(prod) + "log" + str(c) + " " + str(m) + " "))
            check(question, reponse)
        else:
            question = "non"
            reponse = str(input("log" + str(prod) + "/" + str(c) + " " + str(m) + " = log" + str(c) + " " + str(prod) + " - log" + str(c) + " " + str(m) + " "))
            check(question, reponse)

    elif regle == 8:
        print(vari_faux)
        sous_regle=random.randrange(1, 3)
        c=random.randrange(1, 11)
        m=random.randrange(1, 11)
        while c == m:
            m=random.randrange(1, 11)
        if sous_regle == 1:
            question = "oui"
            reponse = str(input("log" + str(c) + " " + str(m) + " = log " + str(m) + "/log " + str(c) + " ?"))
            check(question, reponse)
        else:
            question = "non"
            reponse = str(input("log" + str(c) + " " + str(m) + " = log " + str(c) + "/log " + str(m) + " ?"))
            check(question, reponse)
    else:
       