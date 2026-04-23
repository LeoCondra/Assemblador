#########################################################################
#                   Prof. Nuncio Perrella                               #
#                   Instituto Mauá de Tecnologia                        #
#                   Assemblador para Processador BIP                    #
#                   Modificado por: Leonardo Condrasisen                #
#########################################################################

#Adicionadas as instrucoes JMP, NOP, CMP, JNE, JL, JG ao dicionario

file1 = open('code_imt.txt', 'r')
Lines = file1.readlines()

result = open('asmimt.cdm', 'w')

result_txt = open('asmimt.txt', 'w')

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
        result_txt.write(output)
        print(line.strip())
        n = n+1
    except:
        pass

result.close()
result_txt.close()