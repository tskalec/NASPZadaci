numbers = set([x for x in range(1, 10)])

backtrace = 0

def get_initial_constraints(sudoku):
	constraints = {}

	for i in range(9):
		for j in range(9):
			if sudoku[i][j] != -1:
				continue

			possible = numbers.copy()

			for k in range(9):
				if sudoku[i][k] in possible:
					possible.remove(sudoku[i][k])
				if sudoku[k][j] in possible:
					possible.remove(sudoku[k][j])

			for k in range(i//3 * 3, i//3 * 3 + 3):
				for l in range(j//3 * 3, j//3 * 3 + 3):
					if sudoku[k][l] in possible:
						possible.remove(sudoku[k][l])

			constraints[(i, j)] = possible

	return constraints

def update_constraints(constraints, sudoku, i, j):
	constraints2 = constraints.copy()

	for k in range(9):
		if (i, k) in constraints2:
			if sudoku[i][j] in constraints2[(i, k)]:
				constraints2[(i, k)].remove(sudoku[i][j])
		if (k, j) in constraints2:
			if sudoku[i][j] in constraints2[(k, j)]:
				constraints2[(k, j)].remove(sudoku[i][j])

	for k in range(i//3 * 3, i//3 * 3 + 3):
		for l in range(j//3 * 3, j//3 * 3 + 3):
			if (k, l) in constraints2:
				if sudoku[i][j] in constraints2[(k, l)]:
					constraints2[(k, l)].remove(sudoku[i][j])

	return constraints2

def solve_recursive(sudoku, constraints):
	global backtrace
	backtrace += 1

	sudoku = sudoku.copy()
	constraints = constraints.copy()

	sorted_c = sorted(constraints.items(), key=lambda x: len(x[1]))

	for c in sorted_c:
		if sudoku[c[0][0]][c[0][1]] != -1:
			continue

		for possible in c[1].copy():
			sudoku[c[0][0]][c[0][1]] = possible
			new_constraints = update_constraints(constraints, sudoku, c[0][0], c[0][1])
			if solve_recursive(sudoku, new_constraints):
				return sudoku
			else:
				sudoku[c[0][0]][c[0][1]] = -1

		return None

	return sudoku

def solve(sudoku):
	return solve_recursive(sudoku, get_initial_constraints(sudoku))

def main():
	global backtrace

	sudoku = [
		[-1,4,-1,-1,3,-1,5,-1,-1],
		[6,-1,-1,1,5,-1,8,-1,-1],
		[3,-1,-1,-1,-1,-1,-1,1,-1],
		[2,-1,-1,9,4,-1,-1,-1,-1],
		[4,-1,-1,3,-1,-1,9,2,-1],
		[5,-1,-1,-1,-1,-1,-1,-1,-1],
		[-1,-1,-1,-1,9,-1,-1,4,-1],
		[-1,-1,-1,-1,-1,-1,3,-1,-1],
		[7,5,-1,-1,8,-1,-1,-1,-1]
	]

	unsolvable = [
		[2, -1, -1, 9, -1, -1, -1, -1 ,-1],
		[-1, -1, -1, -1, -1, -1, -1, 6, -1],
		[-1, -1, -1, -1, -1, 1, -1, -1, -1],
		[5, -1, 2, 6, -1, -1, 4, -1, 7],
		[-1, -1, -1, -1, -1, 4, 1, -1, -1],
		[-1, -1, -1, -1, 9, 8, -1, 2, 3],
		[-1, -1, -1, -1, -1, 3, -1, 8, -1],
		[-1, -1, 5, -1, 1, -1, -1, -1, -1],
		[-1, -1, 7, -1, -1, -1, -1, -1, -1]
	]

	print(solve(unsolvable))
	print(backtrace)

	backtrace = 0
	print(solve(sudoku))
	print(backtrace)

if __name__ == "__main__":
	main()
