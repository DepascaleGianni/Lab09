from database.DB_connect import DBConnect
from model.airport import Airport
from model.flight import Flight

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_all_airports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airports"

        cursor.execute(query, ())

        for row in cursor:
            result.append(Airport(row["ID"], row['IATA_CODE'], row["AIRPORT"]))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_selected_flights(avg):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """select *
                from (select f.ORIGIN_AIRPORT_ID as o1,f.DESTINATION_AIRPORT_ID as d1,count(*) as n1,avg(DISTANCE) as m1  from flights f group by f.ORIGIN_AIRPORT_ID,f.DESTINATION_AIRPORT_ID 
                having avg(DISTANCE) > %s) f1,
                (select f.ORIGIN_AIRPORT_ID as o2,f.DESTINATION_AIRPORT_ID as d2,count(*) as n2,avg(DISTANCE) as m2 from flights f group by f.DESTINATION_AIRPORT_ID,f.ORIGIN_AIRPORT_ID 
                having avg(DISTANCE) > %s) f2
                where f1.o1 =f2.d2 and f1.d1 = f2.o2 and o1<o2 
                """
        cursor.execute(query, (avg,avg))

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

if __name__ == '__main__':
    print(DAO.get_selected_flights(300))
    #print(DAO.get_all_airports())