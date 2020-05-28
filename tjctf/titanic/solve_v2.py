# hash a string into md5
import re
import hashlib

with open('titanic_srt.txt', 'r') as file:
	# read each line
	for line in file:
		# read each word split by space
		for word in line.split():
			lower = word.lower()
			# ezpz regex
			stripped = re.sub(r'[^\w\d\s\']+' , '', lower)
			# dont forget to wrap the word in tjctf{} !!
			wrapped = 'tjctf{' + lower + '}'
			encoded = hashlib.md5(wrapped.encode())
			hashed = encoded.hexdigest()
			#print(wrapped)
			#print(hashed)
			if hashed == '9326ea0931baf5786cde7f280f965ebb':
				print('[*] Hash found!')
				print(wrapped)
				print(hashed)
				break