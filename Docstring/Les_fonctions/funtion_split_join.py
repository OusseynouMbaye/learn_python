#split and joint :a revoir
a = "bonjour, je moi, je vais".split(", ")
print(a)
a = "-".join("bonjour , je moi , je vais".split(","))
print(a)
print("*********************")
b ="-".join(["1","2","4"])
print(b)
print("*********************")
# la methode zfill
'''est juste utile sur les chaines de caracteres
'''
c = "9".zfill(2)
print(c)
print("*********************")
'''est juste utile sur les chaines de caracteres
'''
for i in range(20):
    print(str(i).zfill(2))