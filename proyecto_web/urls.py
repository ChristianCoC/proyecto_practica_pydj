from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("demo/", views.demo, name="demo"),
    path("ingles/", views.ingles, name="ingles"),
    path("frances/", views.frances, name="frances"),
    # URL Parametrizada
    path("saludar/<str:nombre>/", views.saludar, name="saludar"),
    path("articles/2003/", views.case_2003),
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
    # URL Parametrizada con Expresiones Regulares
    re_path(r"despedir/(?P<nombre>[a-z]+)/$", views.despedir, name="despedir"),
    re_path(r'^productos/(?P<id>[0-9]{4})', views.productos, name="productos"),
]
