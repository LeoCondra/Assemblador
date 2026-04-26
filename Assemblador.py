#########################################################################
#                   Prof. Nuncio Perrella                               #
#                   Instituto Mauá de Tecnologia                        #
#                   Sistemas Digitais e Arquitetura de Computadores     #
#                   Assemblador para Processador BIP                    #
#                                                                       #
#                   João Carlos de Oliveira Serrano  - RA: 23.10205-5  #
#                   Gabriel Tembra Gomes de Oliveira - RA: 22.10051-2  #
#                   Gustavo Fernandes Arantes Maluta - RA: 23.10050-8  #
#                   Leonardo Condrasisen             - RA: 23.01270-6  #
#########################################################################

# Modificação 1: Adicionadas as instruções JMP, NOP, CMP, JNE, JL, JG ao dicionário
# Modificação 2: Arquivo de saída adicional em .txt com o mesmo conteúdo do .cdm
# Modificação 3: Popup para nomear os arquivos de saída
# Modificação 4: Cria uma pasta com o nome escolhido e salva todos os arquivos dentro dela,
#                incluindo cópia do código fonte (_source.txt)

import tkinter as tk
from tkinter import simpledialog
import os

root = tk.Tk()
root.withdraw()

output_name = simpledialog.askstring("Assemblador BIP", "Nome dos arquivos de saída (sem extensão):", initialvalue="asmimt")

root.destroy()

output_name = output_name or "asmimt"

# Modificação 4: cria pasta com o nome escolhido
os.makedirs(output_name, exist_ok=True)

output_cdm = os.path.join(output_name, output_name + ".cdm")
output_txt = os.path.join(output_name, output_name + ".txt")
output_src = os.path.join(output_name, output_name + "_source.txt")

file1 = open('code_imt.txt', 'r')
Lines = file1.readlines()

result     = open(output_cdm, 'w')
result_txt = open(output_txt, 'w')
result_src = open(output_src, 'w')  # Modificação 4: cópia do código fonte

result_src.writelines(Lines)  # Modificação 4: escreve o conteúdo original
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
        result_txt.write(output)  # Modificação 2: espelha saída no .txt
        print(line.strip())
        n = n+1
    except:
        pass

result.close()
result_txt.close()
