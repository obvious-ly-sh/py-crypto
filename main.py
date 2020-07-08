from crypto import Crypto
cryptolib = Crypto()

message = "FBI, OPEN THE DOOR"
key = cryptolib.gen_key(32) # Stock the key which enable to encode and decode the string
salt = 6 # Create a salt which will ensure the string enryption

enc_message = cryptolib.encrypt(message, key, salt) # Encode the string with a salt
dec_message = cryptolib.decrypt(enc_message, key, salt) # Decode the string with the required salt