import util as u
import os.path





def get_public_key():
	if not os.path.isfile('pub_key.pub'):
		print("There are no public key available")
		return None

	with open('pub_key.pub', 'r') as f:
		lines = f.readlines()
		
		n = int(lines[1])
		k = int(lines[2])
		q = int(lines[3])

		lines = lines[4::]

		rows = []

		for i in range(len(lines) - 1):
			row = get_vector(lines[i])
			rows.append(row)

		A = u.transpose(rows)

		f.close()

	return A, n, k, q


def get_vector(line):
	vector = []
	s = line.split(' ')
	for n in s:
		vector.append(int(n))
	return vector


def get_private_key():
	if not os.path.isfile('priv_key.priv'):
		print("There are no private key available")
		return None

	with open('priv_key.priv', 'r') as f:
		lines = f.readlines()
		
		n = int(lines[1])
		k = int(lines[2])

		lines = lines[3::]

		S = []

		for i in range(len(lines) - 1):
			si = get_vector(lines[i])
			S.append(si)


		f.close()

	return S, n, k


def encrypt(m, A, q, n, k):
	r = u.random_bit_vector(n)
	tA = u.transpose(A)

	coeff = (q-1) / 2

	alpha = (u.matrix_vector(tA, r, q))

	beta = [0 for i in range(n)]

	for i in range(k):
		mi = coeff*m[i]
		beta.append(mi)

	c = []

	for i in range(len(alpha)):
		c.append(alpha[i] + beta[i])

	print("Encryption completed")
	return c


def decrypt(c, S, q, n, k):
	v = []
	w = []

	m = []

	for i in range(n):
		v.append(c[i])

	for i in range(k):
		w.append(c[n + i])

	for i in range(k):
		yi = u.scalar_product(v, S[i]) - w[i]

		if abs(yi) < q/4:
			mi = 0
		else:
			mi = 1

		m.append(mi)

	print("Decrypted")

	return m


def test_vector():
	a = '45 25 36 56 45'
	v = get_vector(a)
	print(v)

def test():
	test = 'coucou'

	m = u.string_to_binary(test)

	A, n, k, q = get_public_key()

	c = encrypt(m, A, q, n, k)

	print("Encrypted to : " + str(c))

	S, n, k = get_private_key()

	dec = decrypt(c, S, q, n, k)
	print(len(dec))
	final_dec = u.binary_to_string(dec)

	print("Decrypted to : " + final_dec)


if __name__ == '__main__':
	test_vector()
	test()



