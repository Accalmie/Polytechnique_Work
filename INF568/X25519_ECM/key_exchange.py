#from __future__ import unicode_literals

import ladder_rtc as l
import util as u
import struct

N = 2**255 - 19
A = 486662
youhou = 1249200067100348562666821505420423336230722882820348058174836965784280997377

def X25519(m, x):

	global N
	global A

	# decoded_m = u.decodeScalar25519(m)
	# decoded_x = u.decodeScalar25519(x)

	a24 = 121665
	print (N)
	print(A)

	x0 = l.ladder(N , a24, m, (x,0))

	alpha = x0[0] * (pow(x0[1], N-2, N)) % N
	#print(u.encodeUCoordinate(alpha, 255))
	print("ALPHA is : ")
	print(alpha)

	return alpha


def main():

	decoded_m = u.decodeScalar25519('a546e36bf0527c9d3b16154b82465edd62144c0ac1fc5a18506a2244ba449ac4')
	decoded_x = u.decodeUCoordinate('e6db6867583030db3594c1a424b15f7c726624ec26b3353b10a903a6d0ab1c4c', 255)

	decoded_output = u.decodeUCoordinate('c3da55379de9c6908e94ea4df28d084f32eccf03491c71f754b4075577a28552', 255)
	test_output = long(0xc3da55379de9c6908e94ea4df28d084f32eccf03491c71f754b4075577a28552)

	decoded_m_2 = u.decodeScalar25519('4b66e9d4d1b4673c5ad22691957d6af5c11b6421e0ea01d42ca4169e7918ba0d')
	decoded_x_2 = u.decodeUCoordinate('e5210f12786811d3f4b7959d0538ae2c31dbe7106fc03c3efc4cd549c715a493', 255)

	decoded_output_2 = u.decodeUCoordinate('95cbde9476e8907d7aade45cb4b873f88b595a68799fa152e6f8f7647aac7957', 255)

	#print(long(0xa546e36bf0527c9d3b16154b82465edd62144c0ac1fc5a18506a2244ba449ac4))

	print(decoded_x)	
	print("N is : " + str(N))

	raw_input()

	test = X25519(decoded_m, decoded_x)
	test2 = X25519(decoded_m_2, decoded_x_2)
	# test3 = X25519(m_test, u_test)

	print("We got : " + str(test))
	print(hex(test))
	print("We should have : " + str(decoded_output))
	print('Encoded gives : ' + u.encodeUCoordinate(test, 255))

	print("We got : " + str(test2))
	print("We should have : " + str(decoded_output_2))
	print('Encoded gives : ' + u.encodeUCoordinate(test, 255))

	# print("We got : " + str(test2))
	# print ('We got : ' + hex(test2))

	# print("We got : " + str(test3))
	# print ('We got : ' + hex(test3))

if __name__ == '__main__':
	main()