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
 
##### To generate a key : 
python main.py keygen [n] [q] [k]

##### To encrypt a string : 
python main.py encrypt [m]

##### To decrypt a file : 
python main.py decrypt [cipher_file]
