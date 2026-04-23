#########################################################################
#                   Prof. Nuncio Perrella                               #
#                   Instituto Mauá de Tecnologia                        #
#                   Assemblador para Processador BIP                    #
#                   Modificado por: Leonardo Condrasisen                #
#########################################################################

# Modificacao 1: Adicionadas as instrucoes JMP, NOP, CMP, JNE, JL, JG ao dicionario
# Modificacao 2: Arquivo de saida adicional em .txt com o mesmo conteudo do .cdm
# Modificacao 3: Popup para nomear os arquivos de saida
# Modificacao 4: Cria uma pasta com o nome escolhido e salva todos os arquivos dentro dela,
#                incluindo copia do codigo fonte (_source.txt)

import tkinter as tk
from tkinter import simpledialog
import os

root = tk.Tk()
root.withdraw()

output_name = simpledialog.askstring("Assemblador BIP", "Nome dos arquivos de saida (sem extensao):", initialvalue="asmimt")

root.destroy()

output_name = output_name or "asmimt"

# Modificacao 4: cria pasta com o nome escolhido
os.makedirs(output_name, exist_ok=True)

output_cdm = os.path.join(output_name, output_name + ".cdm")
output_txt = os.path.join(output_name, output_name + ".txt")
output_src = os.path.join(output_name, output_name + "_source.txt")

file1 = open('code_imt.txt', 'r')
Lines = file1.readlines()

result     = open(output_cdm, 'w')
result_txt = open(output_txt, 'w')
result_src = open(output_src, 'w')  # Modificacao 4: copia do codigo fonte

result_src.writelines(Lines)  # Modificacao 4: escreve o conteudo original
result_src.close()

conversion = {"HLT":" : 0",
              "STO":" : 1",
              "LD":" : 2",
              "LDI":" : 3",
              "ADD":" : 4",
              "ADDI":" : 5",
              "SUB":" : 6",
              "SUBI":" : 7",
              "JMP":" : 8",
              "NOP":" : 9",
              "CMP":" : A",
              "JNE":" : B",
              "JL":" : C",
              "JG":" : D"}

count = 0
n = 0
# Strips the newline character
for line in Lines:
    try:
        split = line.strip().split(" ")
        output = str(hex(n)).upper()[2:] + conversion[split[0]] + split[1] + "\n"
        result.write(output)
        result_txt.write(output)  # Modificacao 2: espelha saida no .txt
        print(line.strip())
        n = n+1
    except:
        pass

result.close()
result_txt.close()