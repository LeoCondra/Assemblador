#########################################################################
#                   Prof. Nuncio Perrella                               #
#                   Instituto Mauá de Tecnologia                        #
#                   Assemblador para Processador BIP                    #
#                                                                       #
#########################################################################


file1 = open('code_imt.txt', 'r')
Lines = file1.readlines()

result = open('asmimt.cdm', 'w')

conversion = {"HLT":" : 00",
              "STO":" : 1",
              "LD":" : 2",
              "LDI":" : 3",
              "ADD":" : 4",
              "ADDI":" : 5",
              "SUB":" : 6",
              "SUBI":" : 7"}

count = 0
n = 0
# Strips the newline character
for line in Lines:
    try:
        split = line.strip().split(" ")
        result.write(str(hex(n)).upper()[2:] + conversion[split[0]] + split[1] + "\n")
        print(line.strip())
        n = n+1
    except:
        pass
result.close()
