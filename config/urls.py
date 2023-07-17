from django.contrib import admin
from django.urls import path
from sr_public_webapp import views


urlpatterns = [

    ## main ---------------------------------------------------------
    path( 'browse_via_url/', views.browse_via_url_load, name='browse_via_url_load_url' ),
    path( 'browse_via_file/', views.browse_via_file_load, name='browse_via_file_load_url' ),
    path( 'info/', views.info, name='info_url' ),

    ## other --------------------------------------------------------
    path( '', views.root, name='root_url' ),
    path( 'admin/', admin.site.urls ),
    path( 'error_check/', views.error_check, name='error_check_url' ),
    path( 'version/', views.version, name='version_url' ),
    
]
