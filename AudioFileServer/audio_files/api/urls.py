from django.urls import path
from .views import *


urlpatterns = [
    path('<audioFileType>/', AudioFilesListView.as_view()),
    path('<audioFileType>/<audioFileID>/', AudioFilesView.as_view())
]
