import os
from datetime import datetime
import socket
import sys

data = datetime.today().strftime('%Y-%m-%d')
pc = socket.gethostname()

if sys.argv[1] == '1':
    terminal = f"cd Documentos/ESTUDO/mapas/ &&  git add . && git commit -m '{pc}, {data}' && git push"
    os.system(terminal)

if sys.argv[1] == '2':
     terminal = f"cd PROJETOS/Python/ &&  git add . && git commit -m '{pc}, {data}' && git push"
     os.system(terminal)

if sys.argv[1] == '3':
     os.system('cd Documentos/ESTUDO/mapas/ &&  git pull')
     os.system('cd PROJETOS/Python/ &&  git pull')


