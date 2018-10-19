import os
import shutil

if os.path.exists('C:/lab9/Boiko'):
    save_path = 'C:/lab9/Boiko/'
    name = os.path.join(save_path,'v4.txt')
    file = open(name, 'w')
    file.write("Вася бігав по гриби. Бігав Вася від ведмедя. Не втік!!!")
    file.close
else:
    os.makedirs('C:/lab9/Boiko')

file = open(name, "w+")
line = file.readline()
file.write((line.replace('.','\n')))
file.close

        

 
    
