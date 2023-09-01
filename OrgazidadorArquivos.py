# Importa os módulos necessários
import os  
from tkinter.filedialog import askdirectory

# Abre uma janela para selecionar o diretório 
caminho = askdirectory(title="Selecione uma pasta")

# Obtém uma lista de arquivos no diretório selecionado
lista_arquivos = os.listdir(caminho) 

# Dicionário mapeando extensões para nomes de pastas
locais = {
    "Imagens": [".png", ".jpge", ".jpg"],
    "Planilhas": [".xlsx", ".xls", ".csv"],
    "PDFs": [".pdf"],
    "Executáveis": [".exe"],
    "BlocoDeNotas": [".txt"],
    "Compactados": [".rar"],
    "Graficos": [".JNB"],
    "Python": [".py"],
    "Word": [".doc", ".docx"]
}

# Loop pelos arquivos
for arquivos in lista_arquivos:

# Separa o nome do arquivo da extensão
    nome, extensao = os.path.splitext(f"{caminho}/{arquivos}")
    
# Loop pelos tipos de arquivo
    for pasta in locais:
      
# Verifica se a extensão atual pertence a este tipo
        if extensao in locais[pasta]:
          
# Cria a pasta se não existir 
          if not os.path.exists(f"{caminho}/{pasta}"):
              os.mkdir(f"{caminho}/{pasta}")
              
# Move o arquivo para a pasta          
          os.rename(f"{caminho}/{arquivos}", f"{caminho}/{pasta}/{arquivos}")