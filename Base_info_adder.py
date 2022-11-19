import sqlite3 as sql
from Excel_reader1 import ListRow1
from Excel_reader1 import ListRow2

print("Інформацію додано в базу данних")

with sql.connect("Base_zvit1.db") as db:
    curs = db.cursor()
    curs.execute("DROP TABLE IF EXISTS customers")
    curs.execute("""CREATE TABLE IF NOT EXISTS 'customers' (
                    'id' INTEGER NOT NULL UNIQUE,
                    'lastName',
                    'firstName',
                    'fathersName',
                    'phone_number',
                    'e_mail',
                    'city',
                    'company',
                    'doc_numb',
                    PRIMARY KEY('id' AUTOINCREMENT)
                    );""")
    db.commit()

    curs.execute("DROP TABLE IF EXISTS sales")
    curs.execute("""CREATE TABLE IF NOT EXISTS 'sales' (
                    'id' INTEGER NOT NULL UNIQUE,
                    'customer',
                    'sale_sum',
                    'sale_date',
                    'doc_numb' TEXT,
                    'manager',
                    'company',
                    PRIMARY KEY('id' AUTOINCREMENT)
                    );""")
    db.commit()

    curs.execute("""CREATE VIEW IF NOT EXISTS tmp1 AS SELECT DISTINCT manager FROM sales""")
    curs.executemany("""INSERT INTO customers (lastName,
                                                firstName,
                                                fathersName,
                                                phone_number,
                                                e_mail,
                                                city,
                                                company,
                                                doc_numb)
                                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", ListRow1)
    db.commit()

    curs.executemany("""INSERT INTO sales (customer,
                                            sale_sum,
                                            sale_date,
                                            doc_numb,
                                            manager,
                                            company)
                                            VALUES (?, ?, ?, ?, ?, ?)""", ListRow2)

    rows = curs.execute("""SELECT manager, SUM(sale_sum) as SUMA FROM sales GROUP BY manager ORDER BY SUMA DESC""")
    Zvitr_1 = []
    while True:
        next_row = curs.fetchone()
        if next_row:
            ZvitCell = []
            Zvitr_1.append(list(next_row))
        else:
            break
    
    print("Данні для звыту під назвою 'Сума продаж ВЗ за весь час' успішно сформовані")
    # for i in Zvitr_1:
    #     print(i)

    rows2 = curs.execute("""SELECT DISTINCT tmp1.manager, IFNULL(sum(s.sale_sum) OVER (PARTITION BY tmp1.manager), 0) AS Sales_suma FROM tmp1 LEFT JOIN (SELECT Sale_sum, manager FROM sales WHERE strftime('%Y', sale_date) = '2020') AS s ON s.manager = tmp1.manager ORDER BY Sales_suma DESC""")
    Zvitr_2 = []
    while True:
        next_row2 = curs.fetchone()
        if next_row2:
            ZvitCell2 = []
            Zvitr_2.append(list(next_row2))
        else:
            break  

    print("Данні для звыту під назвою 'Сума продаж ВЗ за 2020 рік' успішно сформовані")
    # for i in Zvitr_2:
    #     print(i)

    rows3 = curs.execute("""SELECT city, SUM(sale_sum) as Sales_suma FROM sales s JOIN customers c ON s.company = c.company GROUP BY City ORDER BY Sales_suma DESC""")
    Zvitr_3 = []
    while True:
        next_row3 = curs.fetchone()
        if next_row3:
            ZvitCell3 = []
            Zvitr_3.append(list(next_row3))
        else:
            break

    print("Данні для звыту під назвою 'Рейтинг міст по сумі збуту за весь час' успішно сформовані")
    for i in Zvitr_3:
        print(i)
    db.commit()