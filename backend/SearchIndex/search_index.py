import pickle

class SearchIndex():
    def __init__(self):
        self.obj = pickle.load(open('./SearchIndex/data/menu_index.pkl', 'rb'))
    
    def query(self, query):
        rtn = list()
        arr = self.obj['menu_index'].get(query, list())
        for k in arr:
            rtn.append(self.obj['iid2item'][k])
        return rtn
