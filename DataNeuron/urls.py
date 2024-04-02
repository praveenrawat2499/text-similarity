
from django.contrib import admin
from django.urls import path
from api.views import TextSimilarityAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 'text-similarity/' is the api endpoint
    path('text-similarity/', TextSimilarityAPI.as_view(), name='text_similarity_api'),
    
]

