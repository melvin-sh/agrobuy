from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from farmer.views import see
from ml.views import req

urlpatterns = [
    path('admin/', admin.site.urls),
    path('farmer/',see,name="see_det"),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('ml/',req,name="req"),
    path('', include('shop.urls', namespace='shop')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
