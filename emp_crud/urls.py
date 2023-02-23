from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup', Registration_view.as_view(), name='signup'),
    path('', Login_view.as_view(), name='signin'),
    path('logout', logout_view, name='signout'),
    path('index', Index_view.as_view(), name='home'),
    path('emp/update/<int:pk>', Update_emp_view.as_view(), name='update'),
    path('emp/<int:pk>', Detail_emp_view.as_view(), name='details'),
    path('exp/update/<int:pk>', Update_experience_view.as_view(), name='update-exp'),
    path('emp/delete/<int:pk>', Delete_emp_view.as_view(), name='delete'),
    path('exp/delete/<int:pk>', Delete_experience.as_view(), name='delete-exp'),
    path('exp/add/<int:pk>', add_exprerience, name="addexp"),
    path('exp/display/<int:pk>', get_user_experience, name="display-exp"),
    path('pdf', generate_pdf_view, name="pdf"),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
