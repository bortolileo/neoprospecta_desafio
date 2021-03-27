import csv
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import numpy
from numpy import loadtxt
import sys
import io
import os
import pytest
from pandas.tests.groupby.test_value_counts import df

tax = open(r"C:\Users\Leonardo\Desktop\desafio\arquivos-de-apoio\fas\tables\tax_table_amostras_novo.csv")

# data = loadtxt(r"C:\Users\Leonardo\Desktop\desafio\arquivos-de-apoio\fas\tables\otu_table_tax_amostras.txt", dtype=int,
# usecols=(20,))
# hist = numpy.histogram(tax)
# print(hist)
plot = plt.plot(r"C:\Users\Leonardo\Desktop\desafio\arquivos-de-apoio\fas\tables\tax_table_amostras_novo.csv")
#tentativa de colapsar linhas com o mesmo nome (duplicatas das espécies)
#print(df.groupby("OTU")
# plt.show()
# print(plot)
# plt.hist(data, bins=numpy.arange(data.min(), data.max()+1))