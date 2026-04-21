from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.apis.views.auth_views import RegisterView
from apps.apis.views.category_machine_views import (
    CategoryMachinesListCreate, 
    CategoryMachinesDetail
)
from apps.apis.views.machine_views import (
    MachinesListCreate,
    MachinesDetail
)

from apps.apis.views.department_views import (
    DepartmentsListCreate,
    DepartmentsDetail
)

from apps.apis.views.tag_definitions_views import (
    TagDefinitionsListCreate,
    TagDefinitionsDetail
)

urlpatterns = [
    # user authentication
    path("register/", RegisterView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),

    # category machines
    path("category-machines/", CategoryMachinesListCreate.as_view(), name="category-machines-list-create"),
    path("category-machines/<int:pk>/", CategoryMachinesDetail.as_view(), name="category-machines-detail"),

    # machines
    path("machines/", MachinesListCreate.as_view(), name="machines-list-create"),
    path("machines/<int:pk>/", MachinesDetail.as_view(), name="machines-detail"),
    
    # departments
    path("departments/", DepartmentsListCreate.as_view(), name="departments-list-create"),
    path("departments/<int:pk>/", DepartmentsDetail.as_view(), name="departments-detail"),

    # tag definitions
    path("tag-definitions/", TagDefinitionsListCreate.as_view(), name="tag-definitions-list-create"),
    path("tag-definitions/<int:pk>/", TagDefinitionsDetail.as_view(), name="tag-definitions-detail"),
]