import numpy as np


class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.points = []
    
    def add_point(self, x, y):
        self.points.append((x, y))
    
    def predict(self, X_query):
        if not self.points:
            raise ValueError("No data points available for prediction.")
        
        points = np.array(self.points)
        X_train, Y_train = points[:, 0], points[:, 1]
        # Compute Euclidean (L2) distances
        distances = np.abs(X_train - X_query)
        
        # Get indices of k nearest neighbors
        k_indices = np.argsort(distances)[:self.k]
        
        # Compute predicted Y as the average of k nearest neighbors
        return np.mean(Y_train[k_indices])

def main():
    N = int(input("Enter the number of data points (N): "))
    k = int(input("Enter the number of nearest neighbors (k): "))
    
    if k > N:
        print("Error: k cannot be greater than N")
        return
    
    regressor = KNNRegressor(k)
    print("Enter the data points (x, y):")
    for i in range(N):
        x = float(input(f"Enter x{i+1}: "))
        y = float(input(f"Enter y{i+1}: "))
        regressor.add_point(x, y)
    
    X_query = float(input("Enter the X value for prediction: "))
    
    # Perform k-NN Regression
    Y_pred = regressor.predict(X_query)
    
    print(f"Predicted Y value: {Y_pred}")


if __name__ == "__main__":
    main()
