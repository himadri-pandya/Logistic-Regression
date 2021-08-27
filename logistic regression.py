import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings( "ignore" )

# Logistic Regression
class Regression() :
	def __init__( self, learning_rate, iterations ) :		
		self.learning_rate = learning_rate		
		self.iterations = iterations
		
	# Function for model training	
	def fit( self, X, Y ) :		
		# no_of_training_examples, no_of_features		
		self.m, self.n = X.shape		
		# weight initialization		
		self.W = np.zeros( self.n ) # Weight		
		self.b = 0	# Bias	
		self.X = X		
		self.Y = Y
		
		# gradient descent learning
				
		for i in range( self.iterations ) :			
			self.update_weights()			
		return self
	
	# Helper function to update weights in gradient descent
	
	def update_weights( self ) :		
		A = 1 / ( 1 + np.exp( - ( self.X.dot( self.W ) + self.b ) ) )
		
		# calculate gradients		
		tmp = ( A - self.Y.T )		
		tmp = np.reshape( tmp, self.m )		
		dW = np.dot( self.X.T, tmp ) / self.m		
		db = np.sum( tmp ) / self.m
		
		# update weights	
		self.W = self.W - self.learning_rate * dW	
		self.b = self.b - self.learning_rate * db
		
		return self
	
	# Hypothetical function h( x )
	
	def predict( self, X ) :	
		Z = 1 / ( 1 + np.exp( - ( X.dot( self.W ) + self.b ) ) )		
		Y = np.where( Z > 0.5, 1, 0 )		
		return Y


# Driver code

def main() :
	
	# Importing test dataset	
	df = pd.read_csv( "ds1_test.csv" ) # Can be replaced with "ds2_test.csv"
	X_test = df.iloc[:,:-1].values
	Y_test = df.iloc[:,-1:].values

    # Importing train dataset	
	df1 = pd.read_csv( "ds1_train.csv" ) # Can be replaced with "ds2_train.csv"
	X_train = df1.iloc[:,:-1].values
	Y_train = df1.iloc[:,-1:].values
	
	# Model training	
	model = Regression( learning_rate = 0.01, iterations = 1000 )
	
	model.fit( X_train, Y_train )	
	
	# Prediction on test set
	Y_pred = model.predict( X_test )	
	
	# measure performance	
	correctly_classified = 0	
	
	# counter	
	count = 0	
	for count in range( np.size( Y_pred ) ) :
		
		if Y_test[count] == Y_pred[count] :			
			correctly_classified = correctly_classified + 1
			
		count = count + 1
		
	print( "Accuracy on test set by our model	 : ", (
	correctly_classified / count ) * 100 )

if __name__ == "__main__" :	
	main()