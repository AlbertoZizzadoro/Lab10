from database.DB_connect import DBConnect
from model.hub import Hub


class DAO:

    @staticmethod
    def get_all_hubs():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM hub"
        cursor.execute(query)
        for row in cursor:
            result.append(Hub(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_connessioni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        # La query raggruppa le spedizioni tra due hub (indipendentemente dalla direzione)
        # e calcola subito il peso (media del valore merce)
        query = """
            SELECT LEAST(id_hub_origine, id_hub_destinazione) as h1, 
                   GREATEST(id_hub_origine, id_hub_destinazione) as h2,
                   SUM(valore_merce) / COUNT(*) as peso
            FROM spedizione
            GROUP BY h1, h2
        """
        cursor.execute(query)
        for row in cursor:
            result.append((row['h1'], row['h2'], row['peso']))
        cursor.close()
        conn.close()
        return result