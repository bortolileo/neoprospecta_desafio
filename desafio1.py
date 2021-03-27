import io
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastxCommandline
from Bio.Blast.Applications import NcbiblastnCommandline
import os
import sys

# argumentos para o blast command line
# app para rodar o blastn localmente
blastn_path = r"C:\Users\Leonardo\AppData\Local\Programs\Python\Python37-32\Scripts\biopython-1.78\bin\blastn.exe"
# query para o command line
q = r"C:\Users\Leonardo\Desktop\desafio\arquivos-de-apoio\fas\banco.fasta"
# database de 16s rRNA baixado do NCBI para blast local
database = r"C:\Users\Leonardo\AppData\Local\Programs\Python\Python37-32\Scripts\biopython-1.78\DBs\16S_ribosomal_RNA.ndb"
# output para o resultado do blastn local
result = r"C:\Users\Leonardo\Desktop\desafio\arquivos-de-apoio\fas\bancoat.xml"

# primeira tentativa -> rodar blast online
# banconovo = NCBIWWW.qblast("blastn","nt",fasta_string)
# banconovo = NCBIWWW.qblast("blastn", "banco16s.fasta", "banco_n")
# with open("bancob.fasta", "w") as f:
#  print(banconovo, file=f)

# nao funcionou devido ao tamanho do arquivo

# segunda tentativa -> rodar blast local
blastn_cline = NcbiblastnCommandline(cmd=blastn_path, query=q, db=database, evalue=0.001, outfmt=5, out=result)
with open("bancoat.xml", "w") as f:
    print(blastn_cline, file=f)
stdout, stderr = blastn_cline()
result = open("bancoat.xml")
blast_record = NCBIXML.read(result)

#nao funcionou -> caminho para o database nao foi encontrado

#após as duas tentativas, dividi o "banco.fasta" em 5 bancos menores para rodar o blastn online. Após o resul-
#tado do blast, os bancos menores foram reagrupados, tendo eliminado as sequências não compatíveis com 16s rRNA.
#o arquivo correspondente ao banco de dados resultante se chama "banco_novo.fasta"