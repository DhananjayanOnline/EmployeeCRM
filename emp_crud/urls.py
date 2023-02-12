from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup', Registration_view.as_view(), name='signup'),
    path('signin', Login_view.as_view(), name='signin'),
    path('logout', logout_view, name='signout'),
    path("", Index_view.as_view(), name='home'),
    path('emp/update/<int:pk>', Update_emp_view.as_view(), name='update'),
    path('emp/<int:pk>', Detail_emp_view.as_view(), name='details'),
    path('emp/delete/<int:pk>', Delete_emp_view.as_view(), name='delete'),
    path('pdf', generate_pdf_view, name="pdf"),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
