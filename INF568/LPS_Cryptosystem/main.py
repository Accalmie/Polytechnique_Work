import lps_keygen as keygen
import lps as lps
import util as u
import sys
import os.path


def cipher_to_file(c):

	with open('cipher', 'w+') as f:
		for i in range(len(c)):
			if i == len(c) - 1:
				f.write(str(c[i]))
			else:
				f.write(str(c[i]) + ' ')
		f.close()


def main():


	if len(sys.argv) == 1:
		print_usage()
		demo = raw_input("\nDo you want a basic demo ? [y/n] : ")

		if demo == 'y':
			print("This is a basic demo")
			print("Using default values for N and k")
			N = 16
			k = 800
			q = 1301
			print("Default N is : " + str(N))
			print("Default k is : " + str(k))
			print("Default q is : " + str(q))

			to_encrypt = raw_input("Enter a cipher to crypt !\n")

			print("Generating keys")
			keygen.keygen(N, q, k)
			print("Key generated")

			print("Encrypting message : " + to_encrypt)
			not_padded_m = u.string_to_binary(to_encrypt)

			m = pad(not_padded_m, k)

			A, n, k, q = lps.get_public_key()
			c = lps.encrypt(m, A, q, n, k)
			print('Encrypted !')

			print('Writing cipher to disk')
			cipher_to_file(c)	

			print("Now decrypting")
			S, n, k = lps.get_private_key()

			dec = lps.decrypt(c, S, q, n, k)

			clean_dec = clean(dec)

			final_dec = u.binary_to_string(clean_dec)
			print("Decrypted to : " + final_dec)
			print("Exiting")
			exit(0)
		else:
			print(":(")
			exit(0)

	else:
		if sys.argv[1] == 'decrypt':
			filename = sys.argv[2]
			if not os.path.isfile(filename):
				print("File doesn't exist")
				print("Exiting")
				exit(0)

			with open(filename, 'r') as f:
				line = f.readline()
				s = line.split(' ')
				f.close()
			c = map(int, s)

			print("Now decrypting cipher")
			S, n, k = lps.get_private_key()
			q = u.get_q_from_pub()

			dec = lps.decrypt(c, S, q, n, k)
			clean_dec = clean(dec)

			final_dec = u.binary_to_string(clean_dec)
			print("Decrypted to : " + final_dec)
			print("Exiting")
			exit(0)

		elif sys.argv[1] == 'encrypt':
			to_encrypt = sys.argv[2]

			print("Encrypting message : " + to_encrypt)
			not_padded_m = u.string_to_binary(to_encrypt)

			A, n, k, q = lps.get_public_key()
			m = pad(not_padded_m, k)

			c = lps.encrypt(m, A, q, n, k)
			print('Encrypted !')

			print('Writing cipher to disk')
			cipher_to_file(c)

			print("Done, now exiting ...")
			exit(0)
		elif sys.argv[1] == 'keygen':
			if len(sys.argv) != 5:
				print("USAGE : python main.py keygen [n] [q] [k]")
				exit(0)
			else:
				n = int(sys.argv[2])
				q = int(sys.argv[3])
				k = int(sys.argv[4])

				print("Generating keys")
				keygen.keygen(n, q, k)
				print("Key generated")


def print_usage():
	print("USAGE :")
	print("To generate a key : ")
	print("python main.py keygen [n] [q] [k]")
	print("To encrypt a string : ")
	print("python main.py encrypt [m]")
	print("To decrypt a file : ")
	print("python main.py decrypt [cipher_file]")


def clean(v):
	null_byte = [0,0,0,0,0,0,0,0]
	i = 0
	while i < len(v):
		byte = v[i:i+8]
		if byte == null_byte:
			return v[:i]
		i += 8

	return v


def pad(m, k):
	if len(m) > k:
		print("Cipher too long, need to generate a new keys")
		print("Exiting")
		exit(0)

	while(len(m) != k):
		m.append(0)

	return m

if __name__ == '__main__':
	main()