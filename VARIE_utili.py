import copy
import itertools
import random
import networkx as nx
from requests.utils import prepend_scheme_if_needed
#from database.DAO import DAO

def getRandomNode(self):
    index = random.randint(0, len(self._teams) - 1)
    return self._teams[index]
