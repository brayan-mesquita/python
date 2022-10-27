from pathlib import Path

p = Path()
p


#CRIANDO ARQUIVOS E PASTA
#arquivos
arquivo_teste = p / 'teste.txt'
arquivo_teste.touch()

#pastas
sub_pasta = p / 'subpasta'
sub_pasta.mkdir()
arquivo_em_subpasta = sub_pasta / 'aquivo_em_subpasta.txt'
arquivo_em_subpasta.touch()
arquivo_em_subpasta.parent





[x for x in p.iterdir() if x.is_dir()]