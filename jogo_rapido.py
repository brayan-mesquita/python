from datetime import datetime
import os

#=========NOME DO HOST============
nome_da_maquina = os.uname()[1]

#=======DATA E HORA ATUAL==========
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
print(data_e_hora_em_texto)