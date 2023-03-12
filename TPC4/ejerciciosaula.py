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