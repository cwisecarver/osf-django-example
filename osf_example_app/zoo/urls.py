from rest_framework.routers import DefaultRouter
from zoo import views

router = DefaultRouter()

router.register(r'geneses', views.GenusViewSet)
router.register(r'cats', views.CatViewSet)
router.register(r'bigcats', views.BigCatViewSet)
router.register(r'dogs', views.DogViewSet)

urlpatterns = router.urls
