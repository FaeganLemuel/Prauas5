import pandas as pd
from sklearn import *

df_kandang = pd.read_csv("data/kandang.csv")
df_wagyu = pd.read_csv("data/wagyu.csv")
df_ikan = pd.read_csv("data/ikan.csv")
df_beras = pd.read_csv("data/beras.csv")
df_sayur = pd.read_csv("data/sayur.csv")
df_buah = pd.read_csv("data/buah.csv")
df_musim = pd.read_csv("data/musim.csv")
df_jual = pd.read_csv("data/jual.csv")
df_pengunjung = pd.read_csv("data/pengunjung.csv")

df_farm = pd.read_csv("data/farm.csv")

reg_kandang = neighbors.KNeighborsClassifier()
reg_wagyu = linear_model.LinearRegression()
reg_ikan = linear_model.LinearRegression()
reg_farm = neighbors.KNeighborsClassifier()

reg_beras = linear_model.LinearRegression()
reg_sayur = linear_model.LinearRegression()
reg_buah = linear_model.LinearRegression()

reg_musim = neighbors.KNeighborsClassifier(n_neighbors=2)
reg_jual = linear_model.LinearRegression()
reg_pengunjung = neighbors.KNeighborsClassifier()

reg_kandang.fit(df_kandang[['temperatur', 'kelembaban', 'pakan']], df_kandang.kondisi)
reg_wagyu.fit(df_wagyu[['berat', 'kualitas', 'lemak']], df_wagyu.harga)
reg_ikan.fit(df_ikan[['berat', 'lemak', 'panjang']], df_ikan.harga)
reg_farm.fit(df_farm[['kandang', 'wagyu', 'ikan']], df_farm.kondisi)

reg_beras.fit(df_beras[['berat', 'aroma', 'air']], df_beras.harga)
reg_sayur.fit(df_sayur[['berat', 'warna', 'keasaman']], df_sayur.harga)
reg_buah.fit(df_buah[['berat', 'warna', 'keasaman']], df_buah.harga)

reg_musim.fit(df_musim[['angin', 'suhu', 'kelembaban']], df_musim.musim)
reg_jual.fit(df_jual[['makanan', 'minuman', 'service']], df_jual.harga)
reg_pengunjung.fit(df_pengunjung[['kepuasan', 'jumlah', 'promosi']], df_pengunjung.kondisi)


def kandang(tepung, garam, ragi):
    return float(reg_kandang.predict([[tepung, garam, ragi]]))


def wagyu(tepung, coklat, ragi):
    return float(reg_wagyu.predict([[tepung, coklat, ragi]]))


def ikan(tepung, keju, ragi):
    return float(reg_ikan.predict([[tepung, keju, ragi]]))


def beras(tepung, garam, ragi):
    return float(reg_beras.predict([[tepung, garam, ragi]]))


def sayur(tepung, coklat, ragi):
    return float(reg_sayur.predict([[tepung, coklat, ragi]]))


def buah(tepung, keju, ragi):
    return float(reg_buah.predict([[tepung, keju, ragi]]))


def musim(tepung, garam, ragi):
    return float(reg_musim.predict([[tepung, garam, ragi]]))


def jual(tepung, coklat, ragi):
    return float(reg_jual.predict([[tepung, coklat, ragi]]))


def pengunjung(tepung, keju, ragi):
    return float(reg_pengunjung.predict([[tepung, keju, ragi]]))


def farm(tepung, keju, ragi):
    return float(reg_farm.predict([[tepung, keju, ragi]]))
