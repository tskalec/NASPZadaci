def solve(M, N, problem):
    problem2 = [[0 for i in range(M)] for j in range(N)]

    problem2[0][0] = problem[0]
    for i in range(1, M):
        problem2[0][i] = problem[0][i-1] + problem[0][i]

    for i in range(1, N):
        problem2[i][0] = problem[i-1][0] + problem[i][0]

    for i in range(1, N):
        for j in range(1, M):
            problem2[i][j] = min(problem2[i][j-1], problem2[i-1][j]) + problem[i][j]

    solution = problem2[N-1][M-1]

    moves = []

    x = M - 1
    y = N - 1
    moves.append((y, x))
    while x > 0 and y > 0:
        left = problem2[y][x-1]
        top = problem2[y-1][x]
        if left <= top:
            moves.append((y, x-1))
            x -= 1
        else:
            moves.append((y-1, x))
            y -= 1

    while x > 0:
        x -= 1
        moves.append((y, x))

    while y > 0:
        y -= 1
        moves.append((y, x))

    moves.reverse()

    return moves, solution

def test(moves, solution, problem):
    sum = 0

    for move in moves:
        sum += problem[move[0]][move[1]]

    return sum == solution

def main():
    problem = [[100, 200, 1000, 0], [200, 100, 600, 0], [300, 1600, 100, 0]]
    moves, min_flowers = solve(4, 3, problem)

    print(moves, min_flowers)
    print(test(moves, min_flowers, problem))

if __name__ == "__main__":
    main()

