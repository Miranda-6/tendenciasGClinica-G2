from rest_framework.routers import DefaultRouter
from ..medicineInventory.views import *
from ..Employees.views import *
from ..Patients.views import *
from ..MedicalRecords.views import *

router = DefaultRouter()

#define your path here 
router.register(r'medicineInventory', medicineInventoryViewset, basename='Inventory')
router.register(r'Employees', EmployeesViewSet, basename='Employees')
router.register(r'Patients', PatientsViewSet, basename='Patients')
router.register(r'MedicalRecords', MedicalRecordViewSet, basename='Medical Records')

urlpatterns = router.urls 