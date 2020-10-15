from django.urls import path
from tripskip.views import index,OfferPage,FlightSearch,TopRoute,FlightConfirm,Hotel,HotelSearch,Support,Signup,Login,HotelSearchFilter,HotelBook,Profile,Success,Success2,ViewFlightTicket,ViewHotelTicket


app_name = 'tripskip'

urlpatterns = [
    path('', index, name = 'index'),
    path('offer/<int:pk>/',OfferPage,name = 'offer'),
    path('flightsearch/<str:dept>/<str:arr>/',FlightSearch,name = 'flightsearch'),
    path('flightconfirm/<str:num>/<str:dept>/<str:arr>/',FlightConfirm,name = 'flightconfirm'),
    path('toproute/<int:pk>/<str:dept>/<str:arr>/',TopRoute,name = 'toproute'),
    path('Hotel/',Hotel, name = 'Hotel'),
    path('hotelsearch/<str:dest>/',HotelSearch, name = 'hotelsearch'),
    path('hotelsearchfilter/<str:dest>/<str:cond>/<str:filt>/',HotelSearchFilter, name = 'hotelsearchfilter'),
    path('hotelbook/<str:dest>/<int:pk>/',HotelBook,name = 'hotelbook'),
    path('Support/',Support, name = 'Support'),
    path('profile/<str:user>/',Profile, name = 'profile'),
    path('signup/', Signup, name="signup"),
    path('accounts/login/', Login, name="login"),
    path('flightbooked/<str:num>/<str:dept>/<str:arr>/', Success, name = 'success'),
    path('hotelbooked/', Success2, name = 'hotelbooked'),
    path('viewflightticket/<str:num>/<str:dept>/<str:arr>/<str:orderid>/', ViewFlightTicket, name = 'viewflightticket'),
    path('viewhotelticket/<str:orderid>/', ViewHotelTicket, name = 'viewhotelticket'),
     
]