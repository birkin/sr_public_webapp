from django.contrib import admin
from django.urls import path
from sr_public_webapp import views


urlpatterns = [

    ## main ---------------------------------------------------------
    path( 'sample_string_var/', views.sample_string_var, name='sample_string_var_url' ),
    path( 'sample_array/', views.sample_array, name='sample_array_url' ),
    path( 'sample_json_array/', views.sample_json_array, name='sample_json_array_url' ),
    path( 'sample_browse_via_url/', views.sample_browse_via_url_load, name='sample_browse_via_url_load_url' ),
    path( 'sample_browse_via_file/', views.sample_browse_via_file_load, name='sample_browse_via_file_load_url' ),
    path( 'info/', views.info, name='info_url' ),

    ## other --------------------------------------------------------
    path( '', views.root, name='root_url' ),
    path( 'admin/', admin.site.urls ),
    path( 'error_check/', views.error_check, name='error_check_url' ),
    path( 'version/', views.version, name='version_url' ),
    
]
