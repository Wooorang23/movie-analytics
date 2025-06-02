import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 1. Источник данных (Extract)

film_work        = 'data/raw/content_film_work.xlsx'
genre            = 'data/raw/content_genre.xlsx'
genre_film_work  = 'data/raw/content_genre_film_work.xlsx'
person           = 'data/raw/content_person.xlsx'
person_film_work = 'data/raw/content_person_film_work.xlsx'

df_fw   = pd.read_excel(film_work)
df_g    = pd.read_excel(genre)
df_gfw  = pd.read_excel(genre_film_work)
df_p    = pd.read_excel(person)
df_pfw  = pd.read_excel(person_film_work)

tables = [df_fw, df_g, df_gfw, df_p, df_pfw]


# 2. Трансформация данных (Transform)

# Поменяем тип для creation_date, сделав его datetime, 
# передав туда created в формате datetime
df_fw['creation_date'] = pd.to_datetime(
    pd.to_datetime(df_fw['created'], errors='coerce')
)

# Оставим только год
df_fw['creation_date'] = df_fw['creation_date'].dt.year


# Поменяем предварительно тип для rating на datetime
df_fw['rating'] = pd.to_datetime(df_fw['rating'], errors='coerce')

# Видно, что рейтинг, вида 8.6 записан в формате year-06-08, 
# поэтому извлекаем день + месяц / 10
df_fw['rating'] = df_fw['rating'].dt.day + df_fw['rating'].dt.month / 10

# Заполняем пропуски средней оценкей по всей выборке
df_fw['rating'] = df_fw['rating'].fillna(df_fw['rating'].mean())

# Дропаем дубликаты
for df in [df_fw, df_g, df_gfw, df_p, df_pfw]:
    df.drop_duplicates(inplace=True)