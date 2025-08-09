from django.urls import path


from .views import reviews, review, write_review, update_review, delete_review

urlpatterns = [
    path('<int:pk>/critiques/', reviews, name="reviews"),
    path('critique/<int:pk>/lecture/', review, name="review"),
    path('<int:pk>/critique/redaction/', write_review, name="write"),
    path('critique/<int:pk>/modification/', update_review, name="review_update"),
    path('critique/<int:pk>/suppression/', delete_review, name="review_delete"),
]