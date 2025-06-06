# ETL-процесс и визуализация по данным о фильмах

Проект демонстрирует построение полноценного ETL-конвейера: от загрузки и очистки данных до агрегации и визуализации, используя Python и Jupyter.

## Структура данных

Используются 5 таблиц:
- `film_work.csv` — фильмы (id, title, creation_date, rating, type и др.)
- `genre.csv` — жанры
- `genre_film_work.csv` — связи фильмов и жанров (многие-ко-многим)
- `person.csv` — участники (актёры, режиссёры и т.д.)
- `person_film_work.csv` — связи фильмов и персон с ролями

## Этапы ETL

### 1. Extract
- Загрузка данных из `.xlsx` файлов

### 2. Transform
- Очистка и нормализация дат
- Восстановление рейтинга из ошибочного формата
- Обработка пропусков
- Удаление дубликатов
- Объединение таблиц через связи
- Агрегация жанров и участников по фильмам

### 3. Load / Visualization
- Построение графиков по годам, жанрам, рейтингам (опционально)