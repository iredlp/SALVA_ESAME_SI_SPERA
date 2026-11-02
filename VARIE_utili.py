import copy
import itertools
import random
import networkx as nx
from requests.utils import prepend_scheme_if_needed
#from database.DAO import DAO

# Numero nodi
self._grafo.number_of_nodes()

# Numero archi
self._grafo.number_of_edges()

# Grado massimo
max(self._grafo.nodes,
    key=lambda x: self._grafo.degree(x))

# Grado pesato
self._grafo.degree(x, weight="weight")

# Vicini
self._grafo.neighbors(x)

# Peso arco
self._grafo[a][b]["weight"]

# Verifica arco
self._grafo.has_edge(a, b)

# Componenti connesse
nx.connected_components(self._grafo)

# Ordinamento
sorted(lista, key=lambda x: x...)

    def getRandomNode(self):
    index = random.randint(0, len(self._teams) - 1)
    return self._teams[index]

    def getAllNodes(self, genere):
        return DAO.getAllNodes(genere)

    def getProdottoById(self, idP):
        return self._idMapA[int(idP)]


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