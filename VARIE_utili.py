import copy
import itertools
import random
import networkx as nx
from requests.utils import prepend_scheme_if_needed
#from database.DAO import DAO

def getRandomNode(self):
    index = random.randint(0, len(self._teams) - 1)
    return self._teams[index]

#PER RESTITUIRE UN INT
@staticmethod
    def getPopolarita(idA,genere):
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select sum(inv.Quantity) as quantity
                    from  album al, track t ,  invoiceline inv, genre g 
                    where inv.TrackId =t.TrackId and al.ArtistId =%s
                    and t.AlbumId =al.AlbumId and t.GenreId = g.GenreId
                and g.Name = %s
                      """

        cursor.execute(query, (idA,genere))
        row = cursor.fetchone()
       # for row in cursor:
        #    results.append(row["quantity"])

        cursor.close()
        conn.close()
        # Se non ci sono vendite sum() restituisce None, quindi usiamo or 0
        if row and row["quantity"] is not None:
            return int(row["quantity"])
        return 0

       # return results