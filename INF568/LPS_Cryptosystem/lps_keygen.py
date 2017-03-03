import util as u
import math
import random

def keygen(n, q, k):
	check = 10 * n
	check *= (math.log(n))**2

	if (q <= check):
		print("Invalid input parameters for key generation")
		print("q = " + str(q))
		print("check = " + str(check))
		print("Exiting")
		exit(0)

	A = random_matrix(q, n)

	#print("Random matrix generated")

	S = []
	T = []

	for i in range(1, k+1):
		si = u.random_bit_vector(n)
		S.append(si)

		ti = u.matrix_vector(A, si, q)
		T.append(ti)

		#print("Iteration " + str(i))

	for i in range(len(T)):
		A.append(T[i])

	create_pub_key_file(A, n, k, q)
	create_priv_key_file(S, n, k)

	print("Keys successfully generated")
	return


def get_row(A, i):
	row = []

	for j in range(len(A)):
		row.append(A[j][i])

	return row


def create_pub_key_file(A, n, k, q):
	with open('pub_key.pub', 'w+') as f:
		f.write('---- BEGIN LPS PUBLIC KEY ----\n')
		f.write(str(n) + '\n')
		f.write(str(k) + '\n')
		f.write(str(q) + '\n')

		for j in range(len(A[0])):
			row = get_row(A, j)
			write_row(row, f)

		f.write('---- END LPS PUBLIC KEY ----')
		f.close()
	
	print("Public key written")
	return


def write_row(row, f):
	for i in range(len(row)):
		if i == len(row) - 1:
			f.write(str(row[i]) + '\n')
		else:
			f.write(str(row[i]) + ' ')
	return


def create_priv_key_file(S, n, k):
	with open('priv_key.priv', 'w+') as f:
		f.write('---- BEGIN LPS PRIVATE KEY ----\n')
		f.write(str(n) + '\n')
		f.write(str(k) + '\n')

		for i in range(len(S)):
			write_row(S[i], f)

		f.write('---- END LPS PRIVATE KEY ----')
		f.close()
	print("Private key written")
	return




def random_matrix(q, n):
	A = [[0 for i in range(n)] for j in range(n)]

	sup = (q - 1) / 2
	inf = (-q + 1) / 2

	for i in range(n):
		for j in range(n):
			A[i][j] = random.randint(inf, sup)

	return A



def test():
	n = 10
	q = 863
	k = 47

	keygen(n, q, k)


if __name__ == '__main__':
	test()


