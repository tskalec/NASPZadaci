
#provjerava da li ima negativnih elemenata u prvom retku te vraca najmanji
def checkForNegatives(tableau):
    pivotcolumn = None
    minimum = None
    for i in range(len(tableau[0])):
        if tableau[0][i] < 0 and (pivotcolumn is None or minimum > tableau[0][i]):
            minimum = tableau[0][i]
            pivotcolumn = i

    return pivotcolumn

#ocitava vektor rjesenja iz tablice simpleksa
def extractSolution(tableau):
    ansvector = []
    for i in range(len(tableau[0]) - 1):
        answer = True
        answerrow = None
        for j in range(len(tableau)):
            if tableau[j][i] == 1:
                answerrow = j
                continue
            if tableau[j][i] != 0:
                answer = False
                break

        if answer:
            ansvector.append(tableau[answerrow][len(tableau[0]) - 1])
        else:
            ansvector.append(0)

    return ansvector


def solve(tableau):
    for i in range(len(tableau[0])): # maksimizacija ciljne funkcije je minimizacija negativne ciljne funkcije
        tableau[0][i] *= -1

    pivotcolumn = checkForNegatives(tableau)
    while pivotcolumn is not None:  #ponavljaj tako dugo dok imamo negativne vrijednosti u prvom retku
        pivotrow = None
        minimum = None
        for i in range(1, len(tableau)): #pronalazak pivot elementa
            if tableau[i][pivotcolumn] < 0:
                continue

            candidate = tableau[i][len(tableau[i]) - 1] / tableau[i][pivotcolumn]
            if minimum is None or minimum > candidate:
                minimum = candidate
                pivotrow = i

        if pivotrow is None:  # provjera ako je problem neogranicen
            return None, None

        pivot = tableau[pivotrow][pivotcolumn]  #gauss-jordan eliminacija
        for i in range(len(tableau[pivotrow])):
            if i == pivotcolumn:
                tableau[pivotrow][i] = 1
            else:
                tableau[pivotrow][i] = tableau[pivotrow][i] / pivot

        for i in range(len(tableau)):
            if i == pivotrow:
                continue
            factor = tableau[i][pivotcolumn]
            for j in range(len(tableau[0])):
                if j == pivotcolumn:
                    tableau[i][j] = 0
                else:
                    tableau[i][j] = tableau[i][j] - factor * tableau[pivotrow][j]

        pivotcolumn = checkForNegatives(tableau)

    return extractSolution(tableau), tableau[0][len(tableau[0]) - 1]


if __name__ == '__main__':
    tableau = [[1, 5, 0, 0, 0],[5, 6, 1, 0, 30],[3, 2, 0, 1, 12]]

    solution,maximum = solve(tableau)
    print("Primjer")
    print("maksimizirati 1*x1 + 5*x2 uz ogranicenja:")
    print("5*x1 + 6*x2 <=30")
    print("3*x1 + 2*x2 <=12")

    if solution is None:
        print("problem je neogranicen")
    else:
        print(f"Maksimum funkcije je {maximum}")
        print(f"vektor rjesenja {solution}")

    print("----------------")
    print("veci primjer")
    tableau =[[6, -8, -7, -8, 2, -7, -8, -2, -4, -6, -6, 0, 0, 0, 0, 0, 0, 0],
            [5, 2, -6, -7, 7, 5, 2, 0, 7, 7, 9, -5, 1, 0, 0, 0, 0, 2],
            [7, -2, -0, -3, -3, -8, 0, 4, 4, -5, -2, 5, 0, 1, 0, 0, 0, 8],
            [-2, -5, -8, 1, 9, -4, 2, 6, -1, 5, 5, 1, 0, 0, 1, 0, 0, 8],
            [-8, -4, 0, 2, -5, -2, -1, 3, -2, -4, 4, 8, 0, 0, 0, 1, 0, 6],
            [6, -9, -8, -3, -8, -6, 0, -7, -6, -2, -3, 8, 0, 0, 0, 0, 1, 1]]
    solution, maximum = solve(tableau)
    print(f"Maksimum funkcije je {maximum}")
    print(f"vektor rjesenja {solution}")
