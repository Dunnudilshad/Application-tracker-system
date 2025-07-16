from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(vector1,vector2):
    similarity = cosine_similarity([vector1],[vector2])[0][0]
    return round(similarity*100,2)