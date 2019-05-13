import itertools
import time


# Read file and return an array of text
def read_file(filename):
	f = open(filename, 'r')
	rows = f.readlines()
	f.close()
	return rows


def replace(row, to_rep, rep_for):
	row = row.replace(to_rep, rep_for)

	return row


"""	Parse file replacing your desire words
	Write a new file and close it """
def parse_file(filename, new_filename, to_replace, replace_for):
	rows = read_file(filename)
	new_file = open(new_filename, 'w')

	i = 1
	start = time.time()
	for row in rows:
		for to_rep, rep_for in zip(to_replace, replace_for):
			if to_rep in row:
				row = replace(row, to_rep, rep_for)
				print('Modifying row: {}'.format(i))
		new_file.write(row)
		i += 1

	new_file.close()
	finished = time.time() - start
	print('Finished in {}'.format(finished))



filename = 'to_modify.txt'
new_filename = 'modified.txt'
to_replace = 'my', 'old', 'words'
replace_for = 'your', 'new', 'text'


parse_file(filename, new_filename, to_replace, replace_for)
