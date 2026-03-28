try:
    f = open("text.txt", "r")
    s = f.read()
    f.close()
    print(s)
except:
    print('Não foi possivel abrir o arquivo')
