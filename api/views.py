from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Texts
from api.serializers import TextsSerializer
from api.TextSimil import get_similarity


''' TextSimilarityAPI :  

@desc - accepts 'text1' and 'text2' and return their 'similarity_score'
@route - ['POST'] /text-similarity
@access - Public


'''
class TextSimilarityAPI(APIView):
    
    # get method returns the data stored in the database (if required to store the texts i.e text1 , text2).

    # def get(self, request):
    #     texts = Texts.objects.all()
    #     serializer = TextsSerializer(texts, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    # Post method posts the data to the API endpoint.
    def post(self, request):
        serializer = TextsSerializer(data=request.data)
        if serializer.is_valid():
            text1 = serializer.validated_data['text1']
            text2 = serializer.validated_data['text2']
            
            # similarity_score is calculated with the help of get_similarity Function. 
            # it takes 2 parameters 'text1' and 'text2'.
            # get_similarity function Creates TF-IDF vectorizer, Fit and transform the sentences and Compute cosine similarity. 
            similarity_score = round(get_similarity(text1, text2), 1)
            
            return Response({"similarity_score": similarity_score}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
