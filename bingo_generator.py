import random
import math


def select_grid():
    grilleOk = False
    liste = []
    while not grilleOk:
        liste = []
        for i in range(15):
            liste.append(random.randint(1, 90))
            liste.sort()
        grilleOk = True
        ok = [0] * 9
        for i in range(len(liste)):
            if liste[i] == 90:
                ok[8] += 1
                if ok[8] >= 3: grilleOk = False
            else:
                ok[math.floor(liste[i] / 10)] += 1
                if ok[math.floor(liste[i] / 10)] >= 3: grilleOk = False
            if i > 0:
                if liste[i] == liste[i - 1]: grilleOk = False
        if 4 in liste or 54 in liste or 87 in liste:
            grilleOk = False
        if 0 in ok:
            grilleOk = False
    return liste


def create_grid():
    liste = select_grid()
    grille = []
    grilleOk = False
    while not grilleOk:
        grille = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(liste)):
            ligne = random.randint(0, 2)
            if liste[i] == 90:
                grille[8][ligne] = liste[i]
            else:
                grille[math.floor(liste[i] / 10)][ligne] = liste[i]
        grilleOk = True
        for i in range(3):
            somme = sum([1 if grille[j][i] != 0 else 0 for j in range(9)])
            if somme != 5: grilleOk = False
    for i in range(9):
        for a in range(2):
            for b in range(a + 1, 3):
                if grille[i][a] > grille[i][b] > 0:
                    (grille[i][a], grille[i][b]) = (grille[i][b], grille[i][a])
    print(grille)
    return grille


header = """<html>
<head>
	<title>Bingo de Sakti</title>
	<link rel="stylesheet" href="style.css" />
</head>
<body>
"""

f = open("bingo.html", "w")
f.write(header)

for g in range(600):
    grille = create_grid()
    f.write("<table><th colspan='9'>---- Le Bingo de Sakti - Grille n°" + str(g + 1) + " ----</th>")
    for i in range(3):
        f.write("<tr>")
        for j in range(9):
            if grille[j][i] != 0:
                f.write("<td><b>" + str(grille[j][i]) + "</b></td>")
            else:
                f.write("<td style='background-color:#CCC'></td>")
        f.write("</tr>")

    f.write("""</table>""")
    if (g+1)%2 == 0 : f.write("<br>")

f.write("""
</body>
</html>""")
f.close()
