from model.model import Model

model = Model()
nodi = model.get_nodes('Road Bikes')
connessioni = model.dict_vendite('2016-01-01', '2018-12-28')
grafo = model.crea_grafo()

