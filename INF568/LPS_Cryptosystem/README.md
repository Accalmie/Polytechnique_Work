## Implementation of the Lyubashevsky-Palacio-Segev encryption scheme :



### Files :


+ util.py
  - Contains several utility functions
  
+ lps_keygen.py
  - Contains the key generation functions
  
+ lps.py
  - Contains the encryption and decryption function
  
+ main.py
  - Main file to generate keys, encrypt and decrypt ciphers
 
 
 
 ### Usage :
 
##### For a demo
python main.py          (Will ask if a demo is wanted, if so, generates an arbitrary pair of keys, asks for a cipher, encrypts and decrypts it)
 
##### To generate a key : 
python main.py keygen [n] [q] [k]

##### To encrypt a string or a file: 
python main.py encrypt [m/filename]   (checks if the string is a filename and encrypts the file if it is)

##### To decrypt a file : 
python main.py decrypt [cipher_file]

##### To perform tests :
python main.py test [N]       (Will perform N encryption/decryption processes on an arbitrary file with current keys)