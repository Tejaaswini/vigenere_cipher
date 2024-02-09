### This is an attempt to crack a variation of the vigenère cipher using kasiski method
#### Steps followed:
1. since we do not know the key or the key length, we perfom kasiski examination
2. Kasiski Examination is a process used to determine how long the Vigenère key used to encrypt a ciphertext was
3. After this is determined, frequency analysis is used to break each of the subkeys
4. brute force thru the possible keys to find the plain text