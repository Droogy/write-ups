Titanic - TJCTF
===

### Challenge
> I wrapped tjctf{} around the lowercase version of a word said in the 1997 film "Titanic" and created an MD5 hash of it: 9326ea0931baf5786cde7f280f965ebb

So I obviously chose Python 3 as my language to solve this challenge, which is made perfectly for reading text files, the only problem was getting the right text files in the first place. So in my mind the pseudo-code for my program went something like this:

1. Read and open a text file.
2. Read each word from each line of the text file.
3. Wrap each word in tjctf{}
4. Make the wrapped string lowercase.
5. Hash the lowercase string.
6. If the md5 hash matches the hash provided in the challenge then stop the program and print the un-hashed version of the wrapped string which matches the hash provided for us.

This was the first version of my script scripter (heh) 
```python3
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
```
Now this code actually worked well but I made a critical mistake. While I learned a bit about the string module, which is really useful for cases like these where we need to read a text file, I didn't allow for the possibility of contracted words (e.g., don't, can't, shouldn't). I didn't consider this at first and wasted some time running this script on about 6 different versions of the Titanic script as seen in this github repo. 

I reached out to the challenge author to audit my code real quick which he said was technically sound but pointed out my mistake for stripping all punctuation and he also pointed out another mistake I had made in using the screenplay for the movie as opposed to an actual transcription of the movie, because actors are often subject to improvising lines which may not be in the script. D'oh!

I thought for a moment about how the hell to get a transcription of a movie and (duh) realized I just needed subtitles. In the following version of my script I did away with the string module in favor of the re module which I felt was better suited for stripping away certain punctuation.
I also cleaned up the srt file a bit using find-and-replace via Sublime 3 in order to strip away certain `<b>` tags littered throughout the file.

```python3
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
			# print(wrapped)
			# print(hashed)
			if hashed == '9326ea0931baf5786cde7f280f965ebb':
				print('[*] Hash found!')
				print(wrapped)
				print(hashed)
				break
```
Run the code and bingo!
```
[*] Hash found!
tjctf{marlborough's}
9326ea0931baf5786cde7f280f965ebb
```