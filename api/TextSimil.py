
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


path = f'/Users/hp/Desktop/DataNeuron_Text_Similarity.csv'
df = pd.read_csv(path)

# df['text1']

'''
get_similarity function : 

@desc : It Creates TF-IDF vectorizer, Fit and transform the sentences and Compute cosine similarity. 

'''
def get_similarity(sentence1, sentence2):
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the sentences
    tfidf_matrix = vectorizer.fit_transform([sentence1, sentence2])

    # Compute cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

    return similarity[0][0]

df['processed'] = df.apply(lambda col: get_similarity(col['text1'], col['text2']), axis=1)

# df

# text1 = "praveen singh rawat"
# text2 = "praveen rawat"
# res = round(get_similarity(text1, text2), 1)

# print(res)