from django.urls import URLPattern, path
from . import views

# Adding this, makes the templates for this app "polls" unique,
# in case another app in the project has shared view names
# https://docs.djangoproject.com/en/4.2/intro/tutorial03/#namespacing-url-names.
app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    path("details/<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
