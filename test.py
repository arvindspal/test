import makeprediction

class Test():
    def __init__(self):
        self.name = 'test'
        
    def predict(self):        
        classObj = makeprediction.makePrediction()
        pred = classObj.arvind()
        return pred
