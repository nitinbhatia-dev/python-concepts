listoutput = []
def generate_permutations(inputstr, i=0):
    len_input = len(inputstr)

    if i == len(inputstr):   	 
        listoutput.append(inputstr)
    #'abcde'
    for j in range(i, len_input):

        print(inputstr)
        words = [c for c in inputstr]
        print ('words : ', words)
        print(i,j)

        # swap
        if (i + j) % 2 == 0:
            #print(i,j)
            words[i], words[j] = words[j], words[i]
            generate_permutations(words, i + 1)
   	 
        

generate_permutations("abcde")
tmp = ["".join(s) for s in listoutput]
print(list(set(tmp)))

