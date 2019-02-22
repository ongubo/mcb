from .views import ListLoanView, ListProfileView
from django.urls import path, include
from . import views

# urlpatterns = [
#     # User Views
#     path('', views.home, name="home"),
# ]


urlpatterns = [
    path('loans/', ListLoanView.as_view(), name="loans-all"),
    path('loans/<int:pk>/', views.LoanDetailView.as_view()),
    path('profiles/', ListProfileView.as_view(), name="profiles-all"),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view()),
]
