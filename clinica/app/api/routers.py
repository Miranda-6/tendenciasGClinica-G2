from rest_framework.routers import DefaultRouter
from ..medicineInventory.views import *

router = DefaultRouter()

#define your path here 
router.register(r'medicineInventory', medicineInventoryViewset, basename='Inventory')

urlpatterns = router.urls 