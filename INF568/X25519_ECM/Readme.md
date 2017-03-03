# Assignment for the advanced cryptology course in Polytechnique

## Files :

+ ladder_rtc : Implementation of the Montgomery Ladder
  Usage :
 - function ladder(N, a24, m, P) performs [m]P on the curve defined with a24 = (A + 2)/4 % N (modulus N)
  
+ key_exchange : Implementation of X25519 function
  Usage :
  - function X25519(m , x) m the scalar and x the first coordinate
  
+ ECM : Implementation of ECM factorization
  Usage : 
  - function factorization(N, file) tries to factor N (first using the primes up to 10000) and then with a proper number of run of ECM trial
  - function ECMTrial(N, A, bound, sieve, P) N the modulus, A the parameter of the curve, the bound, the sieve of limit B and a point P
  - function get_proper_param(digit_length) returns proper number of trials and the bound for the length of the digit
          
- util : Set of util functions used in the files listed above



Results are in the txt files, computation is too long so the main in ECM use threads
