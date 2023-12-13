from django.urls import URLPattern, path
from . import views

# Adding this, makes the templates for this app "polls" unique,
# in case another app in the project has shared view names
# https://docs.djangoproject.com/en/4.2/intro/tutorial03/#namespacing-url-names.
app_name = "polls"
# Using Django generic views
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("details/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

# "hard-coded way"
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("details/<int:question_id>/", views.detail, name="detail"),
#     path("<int:question_id>/results", views.results, name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]
