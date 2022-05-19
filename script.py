from tkinter import *

# Script Apprentissage Perceptron

def fonctionEchelon(x):
    if x >= 0:
        return 1
    else:
        return 0


def sum_wi_xi(p, x):
    n = len(p)
    s = 0
    for i in range(n):
        s = s + p[i] * x[i]
    return s


# Correction des poids wi

def dw_correction(nu, y_target, y, xi, p):
    poids_corrected = []
    n = len(xi)
    for i in range(n):
        poids_corrected.append(round(nu * (y_target - y) * xi[i] + p[i], 2))
    return poids_corrected


def perceptron_train(poids, x_train, y_train, nu):
    finProgramme = True
    n = len(y_train)
    while finProgramme:
        finProgramme = False
        for i in range(n):
            xi_wi = sum_wi_xi(poids, x_train[i])
            y = fonctionEchelon(xi_wi)
            if y != y_train[i]:
                finProgramme = True
                poids = dw_correction(nu, y_train[i], y, x_train[i], poids)
    return poids


def perceptron_eval(wi, xi):
    res = fonctionEchelon(sum_wi_xi(wi, xi))
    return [xi, wi, res]


# Apprentissage pour OU

nu = 0.03
poids = [0.02, 0.1, 0.05]
xi_train = [[1, 1, 0], [1, 0, 1], [1, 0, 0], [1, 1, 1]]
yi_train = [1, 1, 0, 1]

wi_trained_OU = perceptron_train(poids, xi_train, yi_train, nu)

# Evaluation pour OU

x_test = [1, 0, 1]
perceptron_eval(wi_trained_OU, x_test)

# Apprentissage pour ET

nu = 0.03
poids = [0.02, 0.1, 0.05]
xi_train = [[1, 1, 0], [1, 0, 1], [1, 0, 0], [1, 1, 1]]
yi_train = [0, 0, 0, 1]

wi_trained_ET = perceptron_train(poids, xi_train, yi_train, nu)

# Evaluation pour ET

x_test = [1, 0, 1]

perceptron_eval(wi_trained_ET, x_test)


def calcule_ET(X):
    res = perceptron_eval(wi_trained_ET, X)
    l4['text'] = 'X de test : ' + str(res[0])
    l5['text'] = 'WI fonction ET : ' + str(res[1])
    l6['text'] = 'Résultat final : ' + str(res[2])


def calcule_OU(X):
    res = perceptron_eval(wi_trained_OU, X)
    l4['text'] = 'X de test : ' + str(res[0])
    l5['text'] = 'WI fonction OU : ' + str(res[1])
    l6['text'] = 'Résultat final : ' + str(res[2])


# Interface graphique

gui = Tk()

l1 = Label(gui, text="X1 :")
l1.place(x=10, y=10)
e1 = Entry(gui, bd=5)
e1.place(x=70, y=10)

l2 = Label(gui, text="X2 :")
l2.place(x=10, y=50)
e2 = Entry(gui, bd=5)
e2.place(x=70, y=50)

l3 = Label(gui, text="Détails :")
l3.place(x=10, y=150)

l4 = Label(gui, text="Data test :")
l4.place(x=10, y=180)

l5 = Label(gui, text="Les Wi :")
l5.place(x=10, y=210)

l6 = Label(gui, text="Résultat:")
l6.place(x=10, y=240)

btn = Button(gui, text="Calcule ET", command=lambda: calcule_ET([1, int(e2.get()), int(e1.get())]))
btn.place(x=60, y=120)

btn = Button(gui, text="Calcule OU", command=lambda: calcule_OU([1, int(e2.get()), int(e1.get())]))
btn.place(x=160, y=120)

gui.geometry("300x330+150+150")
gui.mainloop()