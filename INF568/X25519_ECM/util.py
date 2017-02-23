import random

N = 2**255 - 19

def SWAP(b, x):
	# print(b)
	# print(x[0])
	# print(x[1])
	mask = pow(2, 255 +1) - 1
	v = (0 - b) & (x[0] ^ x[1])
	x2 = x[0] ^ v
	z2 = x[1] ^ v
	return (x2, z2)

def decodeLittleEndian(b, bits):
       return sum([b[i] << 8*i for i in range((bits+7)/8)])

def decodeUCoordinate(u, bits):
    u_list = [ord(b) for b in u]
    # Ignore any unused bits.
    if bits % 8:
       u_list[-1] &= (1<<(bits%8))-1
    return decodeLittleEndian(u_list, bits)

def encodeUCoordinate(u, bits):
    return ''.join([chr((u >> 8*i) & 0xff) for i in range((bits+7)/8)])

def decodeScalar25519(k):
    k_list = [ord(b) for b in k]
    k_list[0] &= 248
    k_list[31] &= 127
    k_list[31] |= 64
    return decodeLittleEndian(k_list, 255)

def gcd(a, b):
	while b != 0:
		t = b
		b = a % b
		a = t
	return a

#Following funtion is taken from Internet, my implementation was waaaaaaaaaaaay too slow
# It uses an array of bool instead of an array of number to reduce memory space
def eratosthene(N):
    if N < 2:
        return []
    N += 1
    tableau = [False,False] + [True]*(N-2)
    tableau[2::2] = [False]*((N-2)//2 + N%2) # sup. des nb pairs
    premiers = [2] # initialisation de la tableau des nb 1ers (2 est 1er)
    racine = int(N**0.5)
    racine = racine + [1,0][racine%2] # pour que racine soit impair
    for i in xrange(3, racine+1, 2):
        if tableau[i]:
            # on enregistre le nouveau nb 1er
            premiers.append(i)
            tableau[i::i] = [False]*((N-i)//i + int((N-i)%i>0)) 
    for i in xrange(racine, N, 2):
        if tableau[i]:
            premiers.append(i)
    return premiers

# def eratosthene(N):
# 	primes = []
# 	L = range(N)
# 	L.remove(0)
# 	L.remove(1)
# 	while L != []:
# 		p = L.pop(0)
# 		#print("Doing first prime " + str(p))
# 		primes.append(p)
# 		to_remove = p*2
# 		while to_remove < N:
# 			try:
# 				L.remove(to_remove)
# 			except ValueError:
# 				pass
# 			to_remove += p
# 	return primes

def is_probable_prime(m, ntrials):
	""" Returns true if m passes n trials of the Miller-Rabin primality test """
	d = m - 1
	s = 0
	while d % 2 == 0:
		d /= 2
		s += 1
	

	for i in range(ntrials):
		a = random.randrange(2, m - 1)
		if (miller_witness(a, m, s, d)):
			return False

	return True


def miller_witness(a, m, s, d):

	x = pow(a, d, m)

	if x == 1 or x == m - 1:
		return False
	for i in range(s):
		x = pow(x, 2, m)
		if x == m - 1:
			return False
	return True


def trial_division(N, sieve):
	"""Find the prime factors of N < 10000"""
	factors = []
	for p in sieve:
		if (N % p == 0):
			power = 1
			N = N / p
			while (N % p == 0):
				power += 1
				N = N / p
			print("Prime factor " + str(p) + " with power " + str(power))
			factors.append((p, power))
	return factors

if __name__ == '__main__':
	print (eratosthene(100))
	sieve = eratosthene(100)

	factors = trial_division(11076, sieve)

	print(is_probable_prime(23, 10))
	print(is_probable_prime(93, 10))
	print(is_probable_prime(27, 10))
	print(is_probable_prime(99, 10))
