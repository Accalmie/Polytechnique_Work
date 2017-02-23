import util as u
import ladder_rtc as ladder
import math
import random
import threading


param_array = (
	(15, 2000, 25),
	(20, 11000, 90),
	(25, 50000, 300),
	(30, 250000, 780),
	(35, 1000000, 1800),
	(40, 3000000, 5100)
	)


def get_proper_param(digit_length):

	for param in param_array:
		if digit_length <= param[0]:
			return param[1], param[2]

	return (3000000, 5100)


def launch_parallel_ECM_trial(N, A, bound, sieve, P, n_threads):

	for i in range(n_threads):
		ECM_thread = threading.Thread(target = ECMTrial, args = (N, A, bound, sieve, P))
		poison_thread.start()

def run_n_ECM_trial(ntrials, N, A, bound, sieve, P):
	for i in range (ntrials):

		if (i == ntrials/4):
			print("25 %% done")
		if (i == ntrials/2):
			print("50 %% done")
		if (i == 3*ntrials/4):
			print("75 %% done")

		primes = []
		used_A = []

		while(True):	

			sigma = random.randrange(6, N)

			U = pow(sigma, 2, N) - 5 % N
			v = 4*sigma % N
			xP = pow(U, 3, N)
			zP = pow(v, 3, N)

			A_prime = (pow((v - U) % N, 3, N) * (((3*U) % N + v) % N)) % N
			other_fac = ((4 * pow(U,3,N)) % N) * v % N
			A_prime = A_prime / other_fac % N
			A_prime = (A_prime - 2) % N

			if (A_prime not in used_A):
				used_A.append(A_prime)
				break


		#print("Launching trial : " + str(i) + " with A = " + str(A_prime))

		trial = ECMTrial(N, A_prime, B, sieve, (xP, zP))
		if trial == False:
			pass
		else:
			if N % trial == 0:
				print ("Found ! We got : " + str(trial))
				primes.append((trial, 1))
				N = N / trial
				break

	return primes



def ECMTrial(N, A, bound, sieve, P):
	
	 # Is always on the curve according to https://www.uam.es/personal_pdi/ciencias/fchamizo/asignaturas/cripto1011/lenstra.pdf 

	if u.gcd(N, 6) != 1:
		print ('Input is not valid, gcd(N,6) != 1')

	# Preparatory steps before Stage 1
	alpha = u.gcd(A**2 - 4, N)
	if  alpha != 1 and alpha != N:
		print("Returning alpha biatch")
		return alpha

	Q = P
	a24 = ((A + 2) / 4) % N

	#print("Calculating, for " + str(len(sieve)) + " primes")


	#Q = ladder.ladder(N, a24, m, Q)
	for l in sieve:
		k = long(math.floor(math.log(bound, l)))
		Q = ladder.ladder(N, a24, (l**k) % N, Q)

	beta = u.gcd(Q[1], N)
	if beta != 1:
		if beta == N:
			print("Found N again ...")
		else:
			print("Nope this time we found " + str(beta) + " when N is " + str(N))
			return beta

	return False



def factorization(N, file = None):

	original = N

	if (u.is_probable_prime(N, 100)):
		print("Don't fool me, N is already a prime !")
		return (N, 1)

	sieve_10000 = u.eratosthene(10000)

	easy_primes = u.trial_division(N, sieve_10000)

	for p in easy_primes:
		N = N / p[0]**p[1]

	B, ntrials = get_proper_param(len(list(str(N))))
	print("Calculating Sieve for B = " + str(B))
	sieve = u.eratosthene(B)
	print("Done calculating Sieve for B = " + str(B))

	# print("Calculating m")
	# m = 1
	# for l in sieve:
	# 	m *= l**(long(math.floor(math.log(B, l))))
	# print("Done calculating m")

	used_A = []	

	for i in range (ntrials):

		if (i == ntrials/4):
			print("25 %% done")
		if (i == ntrials/2):
			print("50 %% done")
		if (i == 3*ntrials/4):
			print("75 %% done")


		#print("Testing primality of " + str(N))
		if (N == 1):
			print("Done")
			return easy_primes
		if (u.is_probable_prime(N, 100)):
			print("Done")
			easy_primes.append((N, 1))
			return easy_primes

		while(True):	

			sigma = random.randrange(6, N)

			U = pow(sigma, 2, N) - 5 % N
			v = 4*sigma % N
			xP = pow(U, 3, N)
			zP = pow(v, 3, N)

			A_prime = (pow((v - U) % N, 3, N) * (((3*U) % N + v) % N)) % N
			other_fac = ((4 * pow(U,3,N)) % N) * v % N
			A_prime = A_prime / other_fac % N
			A_prime = (A_prime - 2) % N

			if (A_prime not in used_A):
				used_A.append(A_prime)
				break


		#print("Launching trial : " + str(i) + " with A = " + str(A_prime))

		trial = ECMTrial(N, A_prime, B, sieve, (xP, zP))
		if trial == False:
			pass
		else:
			if N % trial == 0:
				print ("Found ! We got : " + str(trial))
				easy_primes.append((trial, 1))
				N = N / trial

	attempts = ntrials - i

	#file.write("Found in " + str(attempts) + " using B = " + str(B) + '\n')
	if file != None:
		file.write(str(original) + " has prime factors : " + str(easy_primes) + '\n')

	return (easy_primes)



def main():

	n_threads = 10

	challenge_6 = 60790243792901123
	print(challenge_6 / (29* 1867))
	challenge_10 = 283145596067989314232986571
	challenge_13 = 34832770232311533733269410344933971
	challenge_15 = 282907299799502285459467329276894352404
	challenge_17 = 189088465618514846132633310971665950491283
	challenge_20 = 694971973667565209007002770691890212956824248678
	challenge_25 = 4686472189525581408610824687568930507712726168575666441611
	challenge_30 = 183569712182082210286964764249101420995753004898941099937028323369398
	challenge_35 = 577290253243046125669608560777808883939623680772930034353277250932238911551684
	challenge_40 = 242849535465934095419009251024475765684359393486121662520248120773699265836267786898014
	challenge_45 = 276985480746672227597830374069498870444044106732820554701712818217254007753909648248033821418288616
	challenge_50 = 34198088860465652305665540782362863803015679368703840950066382389623435114996979283423794624048455193733162408

	with open('results_new.txt', 'a') as f:
		a = random.randrange(1, 9999)
		f.write('\nRun id : ' + str(a) + '\n')

		thread_pool = []

		for i in range(n_threads):
			t = threading.Thread(target=factorization, args=(challenge_10, f))
			print("Starting thread " + str(i))
			t.daemon = True
			t.start()
			thread_pool.append(t)

		for t in thread_pool:
			t.join()

		# a_challenge_6 = factorization(challenge_6)
		# print(a_challenge_6)
		# print("ALL DONE : " + str(a_challenge_6))
		# f.write(str(challenge_6) + " has prime factors : " + str(a_challenge_6) + '\n')

		# a_challenge_10 = factorization(challenge_10)
		# print("ALL DONE : " + str(a_challenge_10))
		# f.write(str(challenge_10) + " has prime factors : " + str(a_challenge_10) + '\n')

		# a_challenge_13 = factorization(challenge_13)
		# print("ALL DONE : " + str(a_challenge_13))
		# f.write(str(challenge_13) + " has prime factors : " + str(a_challenge_13) + '\n')

		# a_challenge_15 = factorization(challenge_15)
		# print("ALL DONE : " + str(a_challenge_15))
		# f.write(str(challenge_15) + " has prime factors : " + str(a_challenge_15) + '\n')

		# a_challenge_17 = factorization(challenge_17)
		# print("ALL DONE : " + str(a_challenge_17))
		# f.write(str(challenge_17) + " has prime factors : " + str(a_challenge_17) + '\n')

		# a_challenge_6 = factorization(challenge_6)
		# a_challenge_6 = factorization(challenge_6)
		# a_challenge_6 = factorization(challenge_6)
		# a_challenge_6 = factorization(challenge_6)
		# a_challenge_6 = factorization(challenge_6)
		# a_challenge_6 = factorization(challenge_6)
		# a_challenge_6 = factorization(challenge_6)

		f.write('\n')

		
		
		
		
		


if __name__ == '__main__':
	main()
