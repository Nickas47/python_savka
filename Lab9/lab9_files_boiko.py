import os
import shutil


if os.path.exists('C:/lab9/Boiko'):
    save_path = 'C:/lab9/Boiko/'
    name = os.path.join(save_path,"v4.txt")
    handle = open(name, "w")
    handle.write("Вася бігав по гриби.Бігав Вася від ведмедя.Не втік!")
    handle.close()
else:
    os.makedirs('C:/lab9/Boiko')
    
save_path = 'C:/lab9/Boiko/'
nam = os.path.join(save_path,"41.txt")
with open(name) as inp, open(nam, "w+") as out:
    a = inp.readline()
    for el in a.replace('.','\n'):
        out.write(el)
handle.close

i = input("Введіть нову букву: ")

save_path = 'C:/lab9/Boiko/'
na = os.path.join(save_path,"42.txt")
with open(nam) as inp, open(na, "w+",encoding="utf-8") as out:
    for el in inp :
        n=el.find(i)
        if (n!=-1):
          out.write(el)
handle.close

