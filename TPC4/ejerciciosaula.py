import re

def ejer1(archivos):
    for filename in file_names:
        if re.fullmatch(r"\.*[\w-]+(\.[a-z]+)+", filename):
            print(filename + ": Válido")
        else:
            print(filename + ": Inválido")
def ejer12(archivos):
    dic = dict()
    for filename in file_names:
        if re.fullmatch(r"\.*[\w-]+(\.[a-z]+)+", filename):
            if(re.sub(r"*\.$"," ",filename) not in dic.keys()):
                dic[re.sub(r"\.[a.z]$",filename)] = []
            else:
                dic[re.sub(r"\.[a.z]$")].append(filename)
    print(dic)
            
file_names = [
  "document.txt", # válido
  "file name.docx", # inválido
  "image_001.jpg", # válido
  "script.sh.txt", # válido
  "test_file.txt", # válido
  "file_name.", # inválido
  "my_resume.docx", # válido
  ".hidden-file.txt", # válido
  "important-file.text file", # inválido
  "file%name.jpg" # inválido
]
ejer12(file_names)

matriculas = [
    "AA-AA-AA", # inválida
    "LR-RB-32", # válida
    "1234LX", # inválida
    "PL 22 23", # válida
    "ZZ-99-ZZ", # válida
    "54-tb-34", # inválida
    "12 34 56", # inválida
    "42-HA BQ" # válida, mas inválida com o requisito extra
]

def matriculasVal(matriculas):
    for matricula in matriculas:
        elements = matricula.split("-")
        if(not len(elements)==3):
            return "invalid"
        contador = 0
        for element in elements:
            if(len(element)!=2):
                return "invalid"
            if(contador<2):
                if(element[0].isDigit() or element[1].isDigit()):
                    return "invalid"