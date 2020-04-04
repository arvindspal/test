import makeprediction

class Test:
    def __init__(self):
        self.name = 'test'
        
    def predict(self):        
        classObj = makeprediction.makePrediction()
        df = classObj.load_data()
        df2 = classObj.scale_data(df)
        classObj.get_test_data(df2)
        classObj.load_model()
        pred = classObj.make_prediction()
        return pred
        
