def high(x):

# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

    def word_scoring(p):
        acc=0
        for c in p:
            #print(ord('a')) -- 97
            acc += ord(c)-96
        return acc
    
    def word_parsing(x):
        x=x+' ' #añadimos un espacio para parsear ultima palabra de la lista
        lista_palabras=[]
        i=0
        palabra='' 
        while i<= len(x)-1:
            if x[i]==' ':
                lista_palabras.append(palabra)
                palabra=''
            else:
                palabra=palabra+x[i]
            i+=1
        return lista_palabras
    
    lista_palabras=word_parsing(x)
    #print(lista_palabras)
    lista_scoring=[]
    for p in lista_palabras:
        lista_scoring.append(word_scoring(p))
    #print(lista_scoring)

    i_max=lista_scoring.index(max(lista_scoring))
    return lista_palabras[i_max]


    
print(high('what time are we climbing up the volcano'))
