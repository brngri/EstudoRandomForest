import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

dataBase = pd.read_csv('StudentsPerformance.csv')
dataBase.head()
print("Topo do cabeçalho\n:: ",dataBase.head())
print("Info dataframe:\n:",dataBase.info)
print("Tamanho dataframe",dataBase.shape)
print("Algum valor null?",dataBase.isnull().values.any())
print("Somar valores unicos:\n:",dataBase.isnull().sum())

