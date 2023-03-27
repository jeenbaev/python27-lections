# Slash commands
* \l - список всех баз данных
* \c - показывает через какого юзера и к какой бд мы подключились
* \c name_of_db - подключаемся к какой-то бд
* \du - список всех юзеров в postges
* \dt - список всех таблиц в текущей бд
* \d+ - немного побольше инфы в таблице
* \d+ name_of_table - немного побольше инфы об этой таблице name_of_table
* \q - выход из субд (psql)
* СУБД - система управления бд (psql)
* БД - база данных



# Создание бд и таблиц
```sql
CREATE DATABASE name_of_db;
--создание бд
```


```sql
CREATE TABLE name_of_table(
    column1 data_type1,
    column2 data_type2,
    ...
);
--создание таблицы с полями
```

# Удаление бд и таблиц
```sql
DROP DATABASE name_of_db
--удаление бд
```

```sql
DROP TABLE name_of_table
--удаление таблицы
```


# Заполнение таблиц
```sql
INSERT INTO name_of_db VALUE
(val1, val2),
(val1.2, val2.2);
--запись данных в таблицу (хаполненик всех полей)
```

# Вывод данных из таблиц
``sql
SELECT * FROM name_of_table;
--вывод всех записей и вывод всех полей
```

```sql
SELECT column1, column3 FROM name_of_table;
--вывод конкретных полей
```


# Условия
```sql
DELETE FROM name_of_table WHERE condition;
--удаление всех записей из таблицы соответсвующих данному условию
```



