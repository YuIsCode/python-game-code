# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:20:55 2022

@author: bimab
"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re

nltk.download('punkt')
print("\n\n")

text_data1 = "Saya suka belajar, Karena ingin menjadi pintar. Selain itu, saya ingin membuat bahagia kedua orang tua."
sent_tokenize(text_data1)

def sentence_tokenization(s):
  sentences_list = sent_tokenize(s)
  return sentences_list

text_data2 = "Saya suka belajar, Karena ingin menjadi pintar. Selain itu, saya ingin membuat bahagia kedua orang tua."
sent_tokenize(text_data2)