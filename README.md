## Semantic Text Similarity API
This project provides a RESTful API for calculating the semantic similarity between pairs of texts using the Term Frequency-Inverse Document Frequency (TF-IDF) vectorization technique and cosine similarity metric.

### Technologies Used : 
  - Python
  - Django
  - Django REST
  - Sklearn
  - Pandas

Deployed on Render.com 

### Expected Input and Output Format :

URL: https://text-similarity-6bqi.onrender.com/text-similarity/
Endpoint : /text-similarity/
Method: POST
Request Body:
```
{
    "text1": "First text to compare",
    "text2": "Second text to compare"
}
```
Response:
```
{
    "similarity_score": 0.75
}
```

Use Postman or Thunder Client to Post the texts on this API Link 
Link: https://text-similarity-6bqi.onrender.com/text-similarity/

