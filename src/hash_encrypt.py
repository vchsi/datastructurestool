import random
encrypted_keys = {}
def encrypt(encrypt_list):
	try:
		final = str(int((max(encrypt_list)**sum(encrypt_list)/len(encrypt_list))/random.randint(1,len(encrypt_list))))
	except OverflowError:
		final = str(int((max(encrypt_list)**sum(encrypt_list))*random.randint(1,max(encrypt_list))))
	except TypeError:
		print("List is not INTLIST")
		return
	except ValueError:
		print("something broke!")
		return
	encrypted_keys[final] = encrypt_list
	return final

def decrypt(anything):
	final = encrypted_keys[anything]
	print(final)
	del encrypted_keys[anything]
	return final


def ord_wordToNumber(sentence):
	new_list = []
	for i in range(len(sentence)):
		if(sentence[i] != ""):
			new_list.append(ord(sentence[i]))
	return new_list

def chr_numberListToWord(num_list):
	new_list = []
	for k in range(len(num_list)):
		new_list.append(chr(num_list[k]))
	return "".join(new_list)

def ordencryption(sentence):
	encrypt_list = []
	for i in range(len(sentence)):
		encrypt_list.append(str(ord(str(sentence[i]))))
	encrypted_keys["".join(encrypt_list)] = sentence
	return "".join(encrypt_list)

def orddecryption(sentence):
	returnval = encrypted_keys[sentence]
	return "".join(returnval)