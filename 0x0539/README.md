#0x0539 notes

## Look at it
I am given the string  `D7B9{9B7D_D7B9_DD77BB99}` and can tell this some sort of readable cipher text. The ciphertext 
uses numbers so I rule out ROT13 or Substitution ciphers.

The flag submission box gives us a hint that the flag will be in the format FLAG{...} so using that we can instantly
decode the FLAG as D789 and working off of that crudely decode the flag by hand
```
D - F
7 - L
B - A
9 - G

9B7D_D7B9_DD77BB99
GALF_FLAG_FFLLAAGG
```
Wrapping the decoded in FLAG{} gives us 
> FLAG{GALF_FLAG_FFLLAAGG}

## Here be dragons
The flag gives me a clue that it will be an HTML comment ` <!-- FLAG{} --> `
So I quickly look through the source code of the page scanning for green lines and find it
> <\!-\- FLAG{5L4Y3R_0F_DR4G0NS} -\->

## Excessive Alert
The title gives me a clue that I could possibly use XSS in order to make a js alert pop-up
which is a popular way to solve these challenges. I saw a search box which could be used
to submit my payload. I didn't know any payloads off the top of my head but quickly reviewed them
here, [payloads](https://owasp.org/www-community/xss-filter-evasion-cheatsheet).
There's a search box which can be used to submit a payload 
[search box](./search.png)
And I settle on a simple payload which is an alert box which echoes "Hello"
` <SCRIPT>javascript:alert('Hello!')</SCRIPT> `

And this yields my flag
[flag](xss.png)

> FLAG{w3ll_th4ts_4_b1t_3XeSS1ve!}
