import Bio, pandas
from Bio import SeqIO
from matplotlib import pyplot as plt, axes
import argparse, sys, time, getpass, locale
from argparse import RawTextHelpFormatter
import matplotlib

#argumentos para o gráfico
desc = "fasta_lenght_hist"
parser = argparse.ArgumentParser(description=desc, formatter_class=RawTextHelpFormatter)
banconovo = open("banco_novo.fasta").read()

inp = parser.add_argument(banconovo, help="The fasta file to process", type=str)
# out = parser.add_argument(graph, type=str)

# args = parser.parse_args()
# input_path = args.input
# output_path = args.out
# x_log = bool(args.x_log)
# y_log = bool(args.y_log)

#montagem do grafico
lengths = map(len,
              Bio.SeqIO.parse(r"C:\Users\Leonardo\Desktop\desafio\arquivos-de-apoio\fas\banco_novo.fasta", 'fasta'))
values = pandas.Series(lengths)  # .hist(color='gray', bins=1000)
fig = plt.figure()

#parametros
axes = values.hist(color='gray', bins=1000)
figa = plt.gcf()
title = "Distribuição do comprimento das sequências"
axes.set_title(title)
axes.set_xlabel('Número de nucleotídeos na sequência')
axes.set_ylabel('Número de sequências com este comprimento')
width = 18.0
height = 10.0
largura = fig.set_figwidth(width)
altura = fig.set_figheight(height)

plt.show()

#salvar o grafico
save = fig.savefig("graph.pdf", format='pdf')