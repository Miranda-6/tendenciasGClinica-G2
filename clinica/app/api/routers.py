from rest_framework.routers import DefaultRouter
from ..medicineInventory.views import *
from ..Employees.views import *

router = DefaultRouter()

#define your path here 
router.register(r'medicineInventory', medicineInventoryViewset, basename='Inventory')
router.register(r'Employees', EmployeesViewSet, basename='Employees')

urlpatterns = router.urls 