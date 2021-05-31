import string
f1name = input('Enter .srt file name.> ')
try :
    f1hand = open(f1name, "r")
except :
    print('Invalid file name entered.')
    quit()
lines = f1hand.readlines()
f1hand.close()
#
#
#
def isitint(i) :
    try :
        int(i)
        return True
    except ValueError :
        return False
#
#
#
flist = list()
#
#
#
def runall() :
    tcode = '-->'
    openi = '<i>'
    closei = '</i>'
    web = 'www.'
    rwordc = 'Subtitles'
    for line in lines[1:] :
        if tcode not in line.rstrip() :
            if web and rwordc in line : continue
            else :
                if line.startswith(openi) :
                    line = line[3:]
                if line.rstrip().endswith(closei) :
                    line = line[:-5]
                if not line == "\n" :
                    line = line.rstrip()
                    if len(line) < 7 :
                        if isitint(line.rstrip()) == False :
                            flist.append(line)
                    else :
                        flist.append(line)
#
#
#
def fwrite() :
    for line in flist :
        f2hand.write(line)
        f2hand.write("\n")
    f2hand.close()
#
#
#
dec = input('Enter 1 for listing all words\nEnter 2 for listing all letters\nEnter 3 for finding a specific word\nEnter 4 for finding a specific letter\nEnter 5 for counting all words\nEnter 6 for counting all characters (minus punctuation)\nEnter 7 for saving all parsed lines to file\nEnter 8 for listing most common words\nEnter 9 for listing most common characters\n> ')
try:
    deci = int(dec)
except:
    print("Only integers can be entered.")
    quit()
#
#
#
runall()
d = dict()
letr = dict()
wcount = 0
lcount = 0
for line in flist:
    line = line.lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.rstrip()
    words = line.split()
    for word in words:
        wcount += 1
        d[word] = d.get(word,0) + 1
        lrs = list(word)
        for lr in lrs:
            lcount += 1
            letr[lr] = letr.get(lr,0) + 1
dl = list(d.items())
dll = list()
for w,c in dl:
    dll.append( (c, w) )
dll.sort()
letrl = list(letr.items())
letrll = list()
for l,c in letrl:
    letrll.append( (c, l) )
letrll.sort()
#
#
#
def lall() :
    for c,w in dll:
        print(w + ": " + c)
#
#
#
def lallr() :
    for c,l in letrll:
        print(l + ": " + c)
#
#
#
def lsw(word) :
    word2 = word.translate(word.maketrans('', '', string.punctuation))
    for item in dll:
        if word2 in item :
            print(f"{word} is {item[0]} out of {wcount} total words in {f1name}")
            break
#
#
#
def lsl(lttr) :
    for item in letrll:
        if lttr in item :
            print(f"{word} is {item[0]} out of {lcount} total characters in {f1name}")
            break
#
#
#
def mcw(n) :
    wc = dict()
    for line in flist :
        words = line.split()
        for word in words :
            wc[word] = wc.get(word, 0) + 1
        wcl = list()
        for w, c in wc :
            wcl.append( (c, w) )
        wcl = sorted(wcl, reverse=True)
        wcla = list()
        for c, w in wcl :
            wcla.append( (w, c) )
        wcla = sorted(wcla)
        for w, c in wcla[:n] :
            print(w, "occurs", str(c), "times in", f1name)
#
#
#
def mcl(n) :
    lc = dict()
    for line in flist :
        words = line.split()
        for word in words :
            letters = word.split()
            for letter in letters :
                lc[letter] = lc.get(letter, 0) + 1
            lcl = list()
            for l, c in lc :
                lcl.append( (c, l) )
            lcl = sorted(lcl, reverse=True)
            lcla = list()
            for c, l in lcl :
                lcla.append( (l, c) )
            lcla = sorted(lcla)
            for l, c in lcla[:n] :
                print(l, "occurs", str(c), "times in", f1name)
#
#
#
if deci == 1 :
    lall()
elif deci == 2 :
    lallr()
elif deci == 3 :
    dec3 = input("Enter the word you're looking for.> ")
    dec3 = dec3.lower()
    lsw(dec3)
elif deci == 4 :
    dec4 = input("Enter the letter or number you're looking for.> ")
    dec4 = dec4.lower()
    lsl(dec4)
elif deci == 5 :
    print("There are", str(wcount), "words in", f1name + ".")
elif deci == 6 :
    print("There are", str(lcount), "characters, minus punctuation, in", f1name + ".")
elif deci == 7 :
    f2name = input("Enter your desired file name.> ")
    try :
        f2hand = open(f2name, "w")
    except :
        print('Invalid file name entered.')
        quit()
    fwrite()
    print("Parsed file has been saved to", f2name)
elif deci == 8 :
    count = input('Enter how many of the most common words you would like to see in order.> ')
    try :
        int(count)
    except :
        print('Only integers can be entered.')
        quit()
    mcw(count)
elif deci == 9 :
    count = input('Enter how many of the most common letters/numbers you would like to see in order.> ')
    try :
        int(count)
    except :
        print('Only integers can be entered.')
        quit()
    mcl(count)
else :
    print('Invalid selection. Please try again and choose an option from the list.')