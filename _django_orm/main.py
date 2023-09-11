import sqlite3
from dataclasses import dataclass

@dataclass
class Car:
    brand: str.

    horse_power: int

    def insert_into_db(self, db_file):
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        insert_query = "INSERT INTO table_name (brand, horse_power) VALUES (?, ?)"
        cursor.execute(insert_query, (self.brand, self.horse_power))
        connection.commit()
        connection.close()

    def select_all_from_db(self, db_file):
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        select_query = "SELECT * FROM table_name"
        cursor.execute(select_query)
        cars = []
        for row in cursor.fetchall():
            brand, horse_power = row
            cars.append(Car(brand, horse_power))
        connection.close()
        return cars

    def update_in_db(self, db_file, car_id, new_brand, new_horse_power):
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        update_query = "UPDATE table_name SET brand = ?, horse_power = ? WHERE id = ?"
        cursor.execute(update_query, (new_brand, new_horse_power, car_id))
        connection.commit()
        connection.close()

    def delete_by_id(self, db_file, car_id):
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        delete_query = "DELETE FROM table_name WHERE id = ?"
        cursor.execute(delete_query, (car_id,))
        connection.commit()
        connection.close()


db_file = "identifier.sqlite"

new_car = Car("BMW", 220)
new_car.insert_into_db(db_file)