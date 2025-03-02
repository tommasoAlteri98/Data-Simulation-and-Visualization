import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

giorni = 305
mediaVisitatori = 1200
deviazioneStd = 900
trendDecrescente = np.linspace(0, 600, giorni)

date_range = pd.date_range(start='2002-02-18', periods = giorni, freq='D')

np.random.seed(42)

visitatori = np.random.normal(loc = mediaVisitatori, scale = deviazioneStd, size = giorni)

visitatori = visitatori - trendDecrescente
visitatori = np.maximum(visitatori, 0)  #no negativi

patologie = np.random.choice(['ossa', 'cuore', 'testa'], size=giorni)

df = pd.DataFrame({'Visitatori': visitatori, 'Patologia': patologie}, index=date_range)
df.head()

df['Mese'] = df.index.month
df_mensile = df.groupby('Mese')['Visitatori'].mean()
std_mensile = df.groupby('Mese')['Visitatori'].std()

print("Numero medio di visitatori per mese e deviazione standard:")
print(df_mensile)

patologie = df['Patologia'].value_counts()
patologiaComune = patologie.idxmax()
patologiaRara = patologie.idxmin()

print("Media mensile dei visitatori:")
print(df_mensile)
print("\nDeviazione standard mensile dei visitatori:")
print(std_mensile)

print(f"Patologia più trovata: {patologiaComune}")
print(f"Patologia meno trovata: {patologiaRara}")

df['media_mobile'] = df['Visitatori'].rolling(window=10).mean()

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Visitatori'], label='Visitatori giornalieri', color='b', alpha=0.6)
plt.plot(df.index, df['media_mobile'], label='Media mobile 7 giorni', color='r', linewidth=2)
plt.xlabel('Data')
plt.ylabel('Numero di Visitatori')
plt.title('Andamento del numero di visitatori giornalieri in ospedale con Media Mobile 7 giorni')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(7, 7))
plt.pie(patologie, labels=patologie.index, autopct='%1.1f%%',
        colors=['blue', 'red', 'green'], startangle=90, explode=[0.05, 0.05, 0.05])
plt.title('Distribuzione delle Patologie tra i Visitatori')
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(df_mensile.index, df_mensile, yerr=std_mensile, color='blue', alpha=0.7, capsize=5)
plt.xlabel('Mese')
plt.ylabel('Numero Medio di Visitatori')
plt.title('Media Mensile dei Visitatori con Deviazione Standard')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()