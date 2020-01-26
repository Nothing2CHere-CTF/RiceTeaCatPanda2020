# RiceTeaCatPanda (2020)
RiceTeaCatPanda - 2020

## Overview

**URL:** https://riceteacatpanda.wtf/  
**Organisers:** Rice Tea Cat Panda 
**Duration:** 112 hours  
**Team mates:** Team Competition  

```
Title                         Category            Points  Flag
----------------------------- ------------------- ------- ----------------------------------------------------------
Sticks and Stones              General Skills      50      rtcp{w0Rd5_HuRt_,_d0n'T_Bu11y_,_k1Dz}
print(f) to Pay Respects       Binary/Executable   100     rtcp{s0m3t1m35_0n1y_s0m3tImEz_sn^k3z_ar3_u5EfuL}
cat-chat                       Forensics           125     rtcp{th15_1z_a_c4t_ch4t_n0t_a_m3m3_ch4t}
catch-at (AKA cat-chat pt 2)   Forensics           66      rtcp{w0w_d15c0rd_h4s_s34rch_f34tur35}
Motivational Message           Forensics           200     rtcp{^ww3_1_b3l31v3_1n_y0u!}
FBI                            Cryptography        375     rtcp(happy-fiftieth-mlk-day-america-has-come-a-long-way)
IdleRPG                        Cryptography        800     rtcp{n0t_S0_1dl3_4ft3R_a1I}
*growls at the chicken*        Web                 1000    rtcp{ch1ck3n_4nd_th3_3gg}
Wrath of the Rice Goddess      Rice Goddess        4000    rtcp{pand4z_just_w4nt_cudd13z_fr0m_y0u!}
```

## Sticks and Stones

* **Category:** General Skills
* **Points:** 50

### Challenge

```
Sticks and Stones
-------------------------------------------

may break my bones but words could ~~never~~ hurt me

-------------------------------------------
```

File included: [worbz.txt](worbz.txt)

### Solution

worbz.txt contains a single 5 million character string with no line breaks or spaces.

Initial examination reveals numerous instances of the flag header (rtcp - nearly 135,000 of them).

On the challenge home page, we find this text: "flags should be submitted with the competition format: rtcp{random_text_here} (rtcp{} wrapping and underscores between words)", so if we delimit each instance of rtcp with a line break, and grep for "_", we get the following:
```
$ cat worbz.txt | sed 's/rtcp/\nrtcp/g' | grep _
rtcp{w0Rd5_HuRt_,_d0n'T_Bu11y_,_k1Dz}Rutelinae
```

**Flag**
```
rtcp{w0Rd5_HuRt_,_d0n'T_Bu11y_,_k1Dz}
```

---

## print(f) to Pay Respects

* **Category:** Binary/Executable
* **Points:** 100

### Challenge

```
print(f) to Pay Respects
-------------------------------------------

Lulu recently began to collect rice granules, she needs so many! (like over 9999) Jake says it might be a cure to Lulu's disease. Go help her get enough by throwing rice at the portal, print(f) to pay respects.

-------------------------------------------
Hints
-------------------------------------------
- Careful not to throw rice in the wrong direction, just thow it close by (not into) the portal - Jake can pick it up later.
```

File included: [Portal.zip](Portal.zip)

### Solution

The zip file contains the following files:
```
Portal.deps.json
Portal.dll
Portal.exe
Portal.pdb
Portal.runtimeconfig.json
```

I'm sure I solved this the wrong way, but this solution goes to show that it doesn't necessarily have to be a complicated solution to find flags...

In Windows, I ran strings on the exe file, with no result, but for good measure ran it on the dll file as well:
```
>strings Portal.dll | grep rtcp
rtcp{s0m3t1m35_0n1y_s0m3tImEz_sn^k3z_ar3_u5EfuL}
```
and that's all it took.

**Flag**
```
rtcp{s0m3t1m35_0n1y_s0m3tImEz_sn^k3z_ar3_u5EfuL}
```

---

## cat-chat

* **Category:** Forensics
* **Points:** 125

### Challenge

```
cat-chat
-------------------------------------------

nyameowmeow nyameow nyanya meow purr nyameowmeow nyameow nyanya meow purr nyameowmeow nyanyanyanya nyameow meow purr meow nyanyanyanya nya purr nyanyanyanya nya meownyameownya meownyameow purr nyanya nyanyanya purr meowmeownya meowmeowmeow nyanya meownya meowmeownya purr meowmeowmeow meownya purr nyanyanyanya nya nyameownya nya!!!!

-------------------------------------------
Hints
-------------------------------------------
- once you've figured this out, head to discord's #catchat channel.
```

### Solution

I went straight to the discord #catchat channel, and found lots of text similar to the above.  Copying it into a [text file](cipher_text.txt), I then ran some simple analysis on the data.
```
$ cat cipher_text.txt | sed 's/ /\n/g' | sort | uniq -c | sort -nr > uniq.txt
```

I found that there were a total of 42 unique words in the [text](uniq.txt) which ranged in usage frequency from once to nearly 3,000.  Percentage analysis of each frequency was very similar to [ETAION SHRDLU](https://en.wikipedia.org/wiki/Etaoin_shrdlu), so I substituted each word for a suitable character (a-z, 0-9, !@#$%^) and then ran a [Viginere cipher tool](https://www.guballa.de/vigenere-solver) on the substituted text.  This immediately confirmed my suspicion that this was a cryptography challenge.  I took only a little tweaking to come up with a better substitution (e.g. purr was " ", not a letter) and the majority of the text was easily readable.  It was only a matter of a short amount of time to derive the final [key](key.txt), and then the [plain text](plain_text.txt) of the chat was revealed.

The 31st line of the chat text was: "rtcp:th15_1z_a_c4t_ch4t_n0t_a_m3m3_ch4t"

(The challenge text reads: "wait wait what the heck is going on here!!!"

**Flag**
```
rtcp{th15_1z_a_c4t_ch4t_n0t_a_m3m3_ch4t}
```

---

## catch-at (AKA cat-chat part 2)

* **Category:** Forensics
* **Points:** 66

### Challenge

```
catch-at
-------------------------------------------

636274425917865984

-------------------------------------------
```

### Solution

To tell the truth, this took me far longer than it ought to have done.  I had been interested to see what the rest of the cat-chat [text](plain_text.txt) said, so I read through the whole lot.  Along the way I found this on the 98th line: "oh by the way, here's a little something: w0w_d15c0rd_h4s_s34rch_f34tur35"

Because I didn't understand what the catch-at clue was referring to (and at the point of writing this, still have no idea), I thought this was merely a suggestion for people new to discord...  So, I dutifully spend the next while searching the discord channel for all manner of things.  One of the things I naturally searched for was the clue "636274425917865984", but came up with nothing.

In fact, it was only because a team-mate prodded me, that I had a second thought about the "hint".  I knew it was in the flag format (although missing the rtcp{}), but after the nudge I decided just to type it in and "see if it worked"...  It did.  (Anyone who understands the clue can feel free to inform me ^_^)

**Flag**
```
rtcp{w0w_d15c0rd_h4s_s34rch_f34tur35}
```

---

## Motivational Message

* **Category:** Forensics
* **Points:** 200

### Challenge

```
Motivational Message
-------------------------------------------

My friend sent me this motivational message because the CTF organizers made this competition too hard, but there's nothing in the message but a complete mess. I think the CTF organizers tampered with it to make it seem like my friend doesn't believe in me anymore, but it's working like reverse psychology on me!!!!

-------------------------------------------
```

File included: [motivation!!!!!.txt](motivation!!!!!.txt)

### Solution

Examination of the txt file revealed it to be a binary file with a header I didn't recognise.  Scrolling through the rest of the file I didn't find anything to encourage me, until I came to the last line of the file: "GNP‰".  Immediately I realised this was a PNG file (with the IEND at the top) with all its data in reverse order.  Reversing the data of the file gave me a [picture](out.png)
```
$ < "motivation!!!!!.txt" xxd -p -c1 | tac | xxd -p -r > out.png
```

Running strings on the new file revealed nothing, but a quick steganography examination revealed the flag:
```
$ zsteg out.png
<snip>
rtcp{^ww3_1_b3l31v3_1n_y0u!}
</snip>
```

**Flag**
```
rtcp{^ww3_1_b3l31v3_1n_y0u!}
```

---

## FBI

* **Category:** Cryptography
* **Points:** 375

### Challenge

```
FBI
-------------------------------------------

Happy MLK day! (January 20th for y'alls non-American folk).

-------------------------------------------
Hints
-------------------------------------------
- What's does the challenge name have to do with its theme?
- Flag format is rtcp(...) not rtcp{}
- The text you use to solve this challenge may slightly vary by a few characters, spacing etc. If these exists, correct them to make it a valid string of english words separated by –s
```

File included: [MESSAGE.txt](MESSAGE.txt)

### Solution

Running a Google query for "fbi mlk" immediately brought me to a wikipedia entry for FBI–King suicide letter, and noting the capitalisation at the start of the [letter](Mlk-uncovered-letter.png) corresponded with the start of the [MESSAGE.txt](MESSAGE.txt), I assumed this to be a one-time pad cipher, using the letter as the key.  However, this is another challenge that took me far too long to solve, and that for a totally ridiculous reason: I opened the text file in Windows' Notepad.exe...

For future reference, and for anyone else who may one day read this: if doing CTFs, DO NOT USE NOTEPAD.EXE! (At the very least use Wordpad...)  Compare [this image](message_notepad.png) of the file opened in Notepad.exe to [this image](message_notepad++.png) of the same file opened in Notepad++.exe.  I spent the first two or three attempts at this challenge counting up to 650 individual characters (with and without spaces and/or punctuation).

Again, it was only through a team-mate's comment about column 1, column 2 and column 3 that I was able to solve this challenge.

The solution is fairly simple: the first column refers to the paragraph, the second column refers to the line in the paragraph, and the third column refers to the character position on the line (all counting from zero).
```
e.g. using the pad below as the key: "0 1 5, 0 1 0, 1 0 0, 1 0 6, 1 3 3, 1 0 2, 0 1 0" = "help me"

0
  0123456
0 ab cd
1 e fg hi
2 j k

1
  0123456
0 l mno p
1 q rs
2 tuvw
3 x y z
```

One minor variation which needed to be taken into account is that line zero is counted from the position of the first character, not from the left justification.  The exact cipher didn't make total sense, but using the advice given in the third hint, it was very simple to resolve the flag.

**Flag**
```
rtcp(happy-fiftieth-mlk-day-america-has-come-a-long-way)
```

---

## IdleRPG

* **Category:** Cryptography
* **Points:** 800

### Challenge

```
IdleRPG
-------------------------------------------

Adrian's a great guy. IdleRPG is too, if only I actually played it...

-------------------------------------------
Hints
-------------------------------------------

Y9xwh`iXm<Vy==0x957d3d19b4d2a__dZGmZ6=j?I%Q||0o112575172146646270--ASLyRE>;9zt,==0x2123efad3594b3__n>#M`=DmchH8||0o411076765515312077--t?V5{I{gMU|U==0x14a976197c2915__;+dC,.R/G~kw||0o245227303137024262---,8f`zTVPdNt==0x93dbfd1c5928f__xt\8X*]zyGL1||0o111733772161311037--%o]c"&z9?1b+==0x147f84671e56d__lV!*DK"1p*qq||0o12177410634362362--V9ik@"E]^\;|==0xf036125564a45__vDgZ*k.>imxm||0o170066044525444727--f!h3bI`YK|x5==0x723a8f0523b99__%z<9//w@S<'%||0o71072436024435551--sP]R0lq*[N:S==0x1b05a7c82fd37a__75=~hT~Q~fA?||0o330132371013751406--gbh(YZ>+"Gs~==0xdd2ea5ce253cf__,1yS%GL?*k;G||0o156456513470451560--Y?L5Ug:EI_A&==0x962f5786b2bc8__9\_65mO4<I:R||0o113057257032625565--^&QlEKy{o=SD==0xbb0e5e66a974a__;U^"Auqq,^K\||0o135416274632513432--3{RI(9`\~O~|==0x6c1cbf73e807b__hj6Nd(1Oro7e||0o66034576717500034--)=)MXYb~oA-m==0x267abd0c92e17__S7@`w(.e)h:%||0o23172572062226746--d1$dXWtmmZ[1==0x191edd987d99db__7tBUDZ$Fp0O3||0o310755663037314567--_nzHHj1KU#/Y==0xc3018045513b0__>}UA.s+SDkW%||0o141401400425211504--WfuvK}2)@XLd==0x4810904aed9ad__o!lr_oS1JuDJ||0o44020440453554572--%`53NS?<NyzQ==0x1ffa7a900063e4__:*+KK)"7*SkV||0o377647522000061605--!rI<c/~6Zc7$==0x1185db7ab832fc__R"%xF/*^#E6f||0o214135557256031310--,_rdR4O;uAo#==0x208c01f7ff8f55__iC5nt]G\.%#M||0o404300076777707357--&z=pJ5Fs(_^w==0x1204c1acf2a0cf__P:sPjc6,-XBh||0o220114065474520133--0d.rnoZ%t@:B==0x194749d970ca7__65fGWLm!z7,(||0o14507223545606164--OxCdv)/{2+/G==0xcc26fb68a1315__W7mtQfg>6/zy||0o146046766642411303--ZBrIi^,<%U)W==0x70d920ffd960__BSILih9EK-Rz||0o3415444077754401--G[@>aOM,CLcC==0x19ded68575f483__61U8qn0}5mIJ||0o316755320535372042--|1v<xMUqbcOq==0x2f81c8def09eb__:h6YYBB%^l9l||0o27601621573604672--kTx{=gbY#O26==0x4a21a24bfe0a7__S|]Re7U}^<s0||0o45041504457760136--L2E!4Z_~y_qh==0x2091f66c71e4ad__qJA|4AEE{aqC||0o404437315434362060--

- Adrian called it the "ideal solution"
```

### Solution

The first "hint", is actually the challenge.  The second hint was released later into the week which lead to a team-mate finding this [image](ideal.png), without which this would also have gone unsolved by me.

Using the solution given in the IdleRPG channel, I cleaned the data and retained only the hexadecimal and octal numbers, and then wrote this simple [python script](idlerpg_solution.py) which printed the flag.

**Flag**
```
rtcp{n0t_S0_1dl3_4ft3R_a1I}
```

---

## *growls at the chicken*

* **Category:** Web
* **Points:** 1000

### Challenge

```
*growls at the chicken*
-------------------------------------------

grrrrrrR<br>
big chicken, i hisS At you!!!

-------------------------------------------
Hints
-------------------------------------------

NQr2MIa1jsaifAVOn3zYeMynNJwd4oBiiem4fJHsA1WjzfyhUp1+seCW0GMijoDHb3w9BMKj7aw6hhtae5/Qw5xOqMioJU3vvEj0BEHO1wInPqlOeTRdZb8BcTsXP+Z/KBA2FjSZcpGHo7rOZ7NtR15y3eY4s/e/tgKUHvPe9MdmDe1kINtyRXgjghJO9e3uMEQmFe2Ai5moVnG7yIVfUd3QG6/Z+K4PSttbJtjWSLFO7zpmYpEOg3XBxsOw/w5scJQqJ7OLGiH22u4+JFXRlD/wPmDzk9uYlLWLcCuxnY0xuMlSfKIFJtVmF0ViO4o4X89ZwsQjjHuYYDaB3el7iA63BzBlsC54Q7Ekv70/GI0UA3R3zJkMaBV12Z6NAE/kAgEJu9ZRcVm6MAIZInLwMU4R1frM0Bks1jeTe72agmxnAIrR8XDeAxzovbvXFwoxNyxiA63fPJGPVoGZq4ecfGvJ23i/Cg+cynB35lc3f+4QifpjCn+MxWkKCzCVEJXdDah19yXKlIxbaR1zm+YHkS0YSUzjr7NJUXHfDCrwAUpXpikfi2f9tgcXEnuhszScE1PCbdt22rRz1pS7MNdRxjCZ5j+8BQNRBLi2BjLGW14X3zd4d6ieoHWH+4fmbqU9dFsUgKN5qL4Gs2LZbbQwkf3+VbIRQK9RaSO9Hj+4/T0=

Public
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmy27XroKLfED3q32/K7G +TnREe2ZkSgceDJH9X+Jf2I++kJHxNxe5HbQBdTHW/tLTWxwMEpric9zGFlt1f76 zdG2iocGw81BVznN/btVAYJBGbhJPYTeULSCv4WG+NTrss8NSl6WGS9NCOKEWTA/ JjR1z8fXik5foTK18sLJloRFGmxcKV6ZI0VFEi77U6PouOseaPBRYgVlPAjNM/pl AuJotPjFYtNTQWCgpj+Vgt3cxm9erBl8G9K9rIsK6snNA1yEZT774CMLCnyovkd5 i55/5mIjGOdmy+x3qCYC2J+Xmssx56OebPyO8cAou8XQf5E/PMxBZ+8X5zuqnHza 2oK9Lo4K2hYVGpCBmG8WhCstYVvfxeb0cXifPOZnpiC4DrQ3q5atx7sH1V4OaAze eJ+nWKTKVaT9NLKEC3ObUNtLLjoh3AZr/RFh9OsYf3rmRFflJkswlVpfMQF6MAR4 CrDITaTdL0M5RWzE2/1Mh98p2HvTJXz0bFbcIfAvd3rAYku0P3OyO3EZ7KrpGXZa 4Mdu10GKEllk9bwCmDFHK/HMVzZPFK9RvKNpMyWchLCLO2gRxIHySn3lF/MHlBkq 0+DH3YM5L0EW92Uzu/IkZJ4o3z7YnrMHdVVN14bGlBfspn+t7LT2xTx3sWYQLm6r xYeQDSkiY24IqAiQzwdPmi0CAwEAAQ==

Private 
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
```

### Solution

Without doubt, this was my favourite challenge of the event.

With the text in the hint clearly encrypted, and the public and private keys given as well, it was simply a question of what encryption method was used.  Thankfully, the capital letters in the challenge text pointed towards RSA.

Copying the private key into a [keyfile](private.key), adding header and footer, and cleaning it up, and then copying the encrypted data into another [file](encoded.txt), I decrypted the [binary version](bintext) to [plaintext](plaintext.txt).
```
$ base64 -d encoded.txt > bintext

$ openssl rsautl -decrypt -inkey private.key < bintext > plaintext.txt
```

The plaintext file was simply a [url](unknown-123-246-470-726.herokuapp.com), and visiting the url showed an animated gif image.  All manner of steganography analysis on the image revealed nothing.

Up to this point, this challenge had only involved crypto, but it was listed as a web challenge.  Robots.txt didn't work, and the [source code](view-source_unknown-123-246-470-726.herokuapp.com.html) didn't reveal much, except for a couple of hidden tags, and a script which entered a chat transcript into the browser console.  Since there didn't seem to be much else to go on, I focussed on the hidden tags which quickly resolved into a basic substitution cipher.

```
<p hidden>9 20 30 15 16 5 14 19 30 27 29 8 20 13 12 28</p>
<p hidden>"abcdefghijklmnopqrstuvwxyz[]. "</p>

0        1         2         3
123456789012345678901234567890
abcdefghijklmnopqrstuvwxyz[]. 

9 20 30 15 16 5 14 19 30 27 29 8 20 13 12 28
i t     o  p  e n  s     [  .  h t  m  l  ]
```

[unknown-123-246-470-726.herokuapp.com/it opens .html](unknown-123-246-470-726.herokuapp.com/it opens .html) didn't work (nor did /it%20opens%20.html, or without spaces), all errors redirected to the base url.  That left the chat transcript in the console.  The only thing mentioned there which opens (and shown opening in the gif) were the drawers.  "It opens" indicated singular, so I tried [unknown-123-246-470-726.herokuapp.com/drawer.html](unknown-123-246-470-726.herokuapp.com/drawer.html).  Nothing on the webpage was visibly different, but the url had changed!

Viewing the [source](view-source_unknown-123-246-470-726.herokuapp.com_drawer.html) showed another hidden tag containing the flag.

**Flag**
```
rtcp{ch1ck3n_4nd_th3_3gg}
```

---

## Wrath of the Rice Goddess

* **Category:** Rice Goddess
* **Points:** 4000

### Challenge

```
Wrath of the Rice Goddess
-------------------------------------------

So, uh, you see, when you wetuwnyed my uwu back to me, the wice goddess got a bit angwy - nyow she has a giant panda weady to sit on my uwu stowage... can you tawk to it? >w<

Quest: Talk to the giant panda on discord

-------------------------------------------
Hints
-------------------------------------------
- Data linearization and generalization tend to make a lot of things lead to Rome.
  ... or I think that's how the saying goes

- Python is more or less required for this. Try making a byte encoder!

- I would try sweet-talking the panda, maybe start with something like `I love rice, tea, cats, and pandas`

- Never, **EVER** trust the developer. (but do trust this hint)
```

File included: [dontbeconcerned.whatsoever](dontbeconcerned.whatsoever)
File included: [pandaspeak_encoder.py](pandaspeak_encoder.py)

### Solution

[dontbeconcerned.whatsoever](dontbeconcerned.whatsoever) appeared to be a reversed base64 string, but since re-reversing it and decoding it didn't produce any meaningful data, I left it.

The [python file](pandaspeak_encoder.py) showed the encoding process of an input string into 'panda speech', but it didn't mean much to me.

Visiting the rtcp discord channel again, I tried talking to the Giant Panda[BOT], but since repeating something seemed to generate different responses, I wasn't quite sure what to do next.  I tried running the pandaspeak_encoder, but it needed a key.  Using the dontbeconcerned.whatsoever file as the key didn't work, but using my previously reversed [base64 string](real_key.key) instead did!
```
$ < dontbeconcerned.whatsoever xxd -p -c1 | tac | xxd -p -r > real_key.key
```
I then realised that this script, too, produced different results when presented with the same input.  Since I had never reversed anything like this before, I wasn't too expectant of my success, but decided to give it a shot by breaking it down into smaller chunks.

Using pycharm to debug the encoder, I found that by stripping the first two and last two characters from the encoder result and removing the spaces, I could get back to the /response/ value on line 35.  Next I reverse line 32 by subtracting 97 from the ordinal of each character in my previous step and string encoded it, and found where it matched in the encoder sequence.

Using the class provided (which helpfully included an unnecessary decode method), I decoded that string, then decrypted it with the imported Fernet module.  Lo and behold, my [python script](pandaspeak_decoder.py) worked!

Now I was able to understand what the Giant Panda[BOT] was saying, but it responded differently whatever I said.  The third clue suggested saying 'I love rice, tea, cats, and pandas' to it, and I found that this was the first time it replied consistently with the same thing.  I took a stab, and repeated what it had told me, and after a brief sequence, it gave me the flag.

The sequence:
1. I love rice, tea, cats, and pandas
2. especially pandas
3. yeah do you want to tell me how much you love pandas?
4. i love them so much, i'd cuddle them all day
5. so? the rice goddess does that too.
6. darn!!! here's your flag: rtcp{pand4z_just_w4nt_cudd13z_fr0m_y0u!}

My chat transcript can be found [here](solution_chat.txt).

**Flag**
```
rtcp{pand4z_just_w4nt_cudd13z_fr0m_y0u!}
```

---
