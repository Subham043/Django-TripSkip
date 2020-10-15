from django.contrib import admin
from tripskip.models import IndexSearch,Offer,Routes,FAQ,Flights,AirportOption,HotelCarousel,HotelFAQ,HotelDestination,HotelList,UserProfile,ComplaintMessage,FlightOrderBooked,HotelOrderBooked
# Register your models here.
admin.site.register(IndexSearch)
admin.site.register(Offer)
admin.site.register(Routes)
admin.site.register(FAQ)
admin.site.register(Flights)
admin.site.register(AirportOption)
admin.site.register(HotelCarousel)
admin.site.register(HotelFAQ)
admin.site.register(HotelDestination)
admin.site.register(HotelList)
admin.site.register(UserProfile)
admin.site.register(ComplaintMessage)
admin.site.register(FlightOrderBooked)
admin.site.register(HotelOrderBooked)