import string
import hashlib

translator = str.maketrans('','', string.punctuation)


with open('titanic_srt.txt', 'r') as file:
	# read each line
	for line in file:
		#read each word which is split by a space
		for word in line.split():
			# turn each word into lowercase
			lower = word.lower()
			# remove all punctuation
			lower_no_punc = lower.translate(translator)
			# wrap in flag 
			encased = 'tjctf{' + lower_no_punc + '}'
			no_punc_encoded = hashlib.md5(encased.encode())
			hashed = no_punc_encoded.hexdigest()
			# print(hashed)
			if hashed == '9326ea0931baf5786cde7f280f965ebb':
				print('[*] Hash found!')
				print(encased)
				print(hashed)
				break
			else:
				continue