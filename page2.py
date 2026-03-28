# irá dar erro e nao irá funcionar dessa forma.
f = open("text.txt", "r")
s = f.read()
f.close()
print(s)
except:
print('Não foi possivel abrir o arquivo')
