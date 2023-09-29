import numpy as np

class OurRegression:
    def __init__(self,X,y,lr=0.01,n_iter=5000):
        self.n_samples = len(y)
        self.W= np.random.rand(X.shape[1],1)
        self.X=X
        self.y=y
        self.lr=lr
        self.iter=n_iter
   
    #Compute cost
    def compute_cost(self):
        loss = np.mean((self.y-self.y_hat)**2)
        return loss
    
    #Update the coefficients
    def update_param(self):
        self.W = self.W - self.lr*np.dot(self.X.T,(self.y-self.y_hat))*(-2/self.n_samples)
        
    def fit(self):
        for i in range(self.iter):
            self.y_hat=np.dot(self.X,self.W)
            loss = self.compute_cost()
            self.update_param()
            i=i+1
        print("Updated params for numpy regression: ",self.W.reshape(3,))
     
    def predict(X_predict):        
        y_predict = np.dot(X_predict,self.W)
        return y_predict
    
