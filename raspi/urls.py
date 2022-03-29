from django.urls import path
from . import views


urlpatterns = [
    path('getstat1/<str:pk>', views.getLED1stat,name='getstat1'),
    path('getstat2/<str:pk>', views.getLED2stat,name='getstat2'),
    path('getstat3/<str:pk>', views.getLED3stat,name='getstat3'),
    path('getip1/<str:pk>', views.getimp1stat,name='getip1'),
    path('getip2/<str:pk>', views.getimp2stat,name='getip2'),
    path('getip3/<str:pk>', views.getimp3stat,name='getip3'),
    path('switch1/<str:pk>', views.ToggleLED1,name='toggle'),
    path('switch2/<str:pk>', views.ToggleLED2,name='toggle2'),
    path('switch3/<str:pk>', views.ToggleLED3,name='toggle3'),
    path('switchimp1/<str:pk>/<str:stat>', views.Toggleimp1,name='toggleimp'),
    path('switchimp2/<str:pk>/<str:stat>', views.Toggleimp2,name='toggleimp2'),
    path('switchimp3/<str:pk>/<str:stat>', views.Toggleimp3,name='toggleimp3'),
    path('control/<str:pk>', views.sendControl,name='control'),
    path('gettemp/<str:pk>', views.getTemp,name='gettemp'),
    path('settemp/<str:pk>/<str:temp>', views.setTemp,name='settemp'),
    path('led1control/<str:pk>/<int:state>', views.led1control,name='led1control'),
    path('led2control/<str:pk>/<int:state>', views.led2control,name='led2control'),
    path('led3control/<str:pk>/<int:state>', views.led3control,name='led3control'),
    path('ip1control/<str:pk>/<int:state>', views.imp1control,name='ip1control'),
    path('ip2control/<str:pk>/<int:state>', views.imp2control,name='ip2control'),
    path('ip3control/<str:pk>/<int:state>', views.imp3control,name='ip3control'),
    path('applogin',views.AppLogin,name='applogin')
]
