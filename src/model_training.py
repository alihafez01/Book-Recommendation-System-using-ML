from sklearn import neighbors

def train_model(features):
    model = neighbors.NearestNeighbors(n_neighbors=6, algorithm='ball_tree')
    model.fit(features)
    distances, idlist = model.kneighbors(features)  # Generate nearest neighbor indices
    return model, idlist  # Return both the model and idlist