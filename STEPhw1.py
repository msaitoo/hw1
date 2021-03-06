dictionary = open('/usr/share/dict/words', 'r')
word = dictionary.readlines()
import time

'''
Generates the longest word from letters given.
'''
print ("Give letters separated by comma")
letter = raw_input()

ans = []                                #list of words made up of given letters
start = time.time()                     #start time
for w in word:
    w = w.rstrip("\n")                  #takes \n out
    sample = []                         #test list
    let = letter.split(',')             #string to list
    for i in range(len(w)):
        for x in range(len(let)):
            if w[0] == let[x].upper:    #takes in account for capitalised words
                sample.append(x)
                let.remove(let[x])
                break
            elif w[i] == let[x]:        #lower case words
                sample.append(x)
                let.remove(let[x])
                break
        if len(sample) != i+1:          #breaks if one letter doesn't match
            break
        if len(w) == len(sample):       #checks if the word is made up of let
            ans.append(w)
answer = max(ans, key=len)              #finds the longest word

end = time.time()                       #end time
took = end - start

print ('''
The longest word generated is [{}] with number of letters {}.
Took {} sec.'''.format(answer, len(answer), took))