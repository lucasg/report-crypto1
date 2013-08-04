from string import ascii_lowercase
from random import shuffle

# convert a string to a char list
strToList = lambda s: [ c for c in s] 

def create_key():
	alphabet = strToList(ascii_lowercase)
	substitution = strToList(ascii_lowercase)
	shuffle( substitution ) #mutable operation !	

	key = { ch : sub for ch,sub in zip( alphabet, substitution )  }
	inv_key = { sub : ch for ch,sub in zip( alphabet, substitution )  }
	return key,inv_key

def encrypt(key,message):
	return "".join([ key[ch] for ch in message ])


if __name__ == "__main__":
	# Key creation
	key,inv_key = create_key()
	print "Substitution function :"
	print "\t"+"|".join( key.keys() )
	print "\t"+"|".join( [ key[k] for k in key.keys()] )
	print	

	#Encryption
	message = "attackatdawn"
	ciphertext = encrypt(key,message)
	print "Encryption of :", message ,"=>", ciphertext
	print 

	#Decryption
	#the encryption and decryption mechanism are identical (symetric encryption)
	print "Decryption of :",ciphertext  ,"=>", encrypt(inv_key,ciphertext)
	print 