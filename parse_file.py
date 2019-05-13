

def read_file(filename):
	f = open(filename, 'r')
	rows = f.readlines()
	f.close()
	return rows


def parse_file():
	filename = 'filename.txt'
	new_file = 'new_file.txt'
	rows = read_file(filename)
	new_file = open(new_file, 'w')
	to_replace = 'Fizz'
	replace_for = 'Buzz'

	i = 1
	for row in rows:
		if to_replace in row:
			row = row.replace(to_replace, replace_for)
		new_file.write(row)
		print('Modifying row: {}'.format(i))
		i += 1

	new_file.close()


parse_file()
