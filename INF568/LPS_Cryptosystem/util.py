import binascii
import random
import os.path

def matrix_vector(A, s, q):
	n = len(A)
	m = len(A[0])
	
	modulus = q ** m

	total_sum = 0

	for i in range(n):
		if s[i] == 1:
			total_sum += (sum_vector_base_q(A[i], q)) % modulus

	t = []

	for i in range(m):
		ti = total_sum // q**(m - 1 - i)

		if ti > ((q - 1) / 2):
			ti -= (q - 1)
		if ti < -((q-1)/2):
			ti += (q-1)

		t.append(ti)
		total_sum = total_sum % q**(m - 1 - i)

	return list(reversed(t))


def sum_vector_base_q(v, q):
	s = 0
	for i in range(len(v)):
		s += v[i] * (q**i)

	return q

def random_bit_vector(n):
	S = []
	for i in range(n):
		S.append(random.randint(0,1))

	return S

def transpose(A):
	return [list(x) for x in zip(*A)]

def scalar_product(x,y):
	s = 0
	for i in range(len(x)):
		s += x[i] * y[i]

	return s

def string_to_binary(s):
	binary = ''
	b = bytearray(s)
	for byte in b:
		bits = bin(byte)[2::]
		while len(bits) != 8:
			bits = '0' + bits
		binary += bits

	#print(len(binary))
	return map(int, list(binary))


def binary_to_string(b):
	i = 0
	s = ''
	#print(len(b))
	while i < len(b):
		byte = '0b'
		for j in range(8):
			byte += str(b[i+j])
		i += 8
		s += chr(int(byte, 2))
	
	return s

def get_q_from_pub():
	if not os.path.isfile('pub_key.pub'):
		print("There are no public key available")
		return None

	with open('pub_key.pub', 'r') as f:
		lines = f.readlines()

		q = int(lines[3])

	return q

def test():
	a = string_to_binary('Super Secret Message')
	print(a)	
	print(len(a))
	d = binary_to_string(a)

	print(d)

if __name__ == '__main__':
	test()