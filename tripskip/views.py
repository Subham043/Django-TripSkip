from django.shortcuts import render, redirect
from django.http import HttpResponse
from tripskip.models import IndexSearch,Offer,Routes,FAQ,Flights,AirportOption,HotelCarousel,HotelFAQ,HotelDestination,HotelList,UserProfile,ComplaintMessage,FlightOrderBooked,HotelOrderBooked
from django.contrib.auth import login, authenticate
from tripskip.forms import SignUpForm,UserUpdateForm,UserProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import random
import razorpay
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def index(request):
	#process the data
	indexSearch = IndexSearch.objects.get(id=2)
	offer = Offer.objects.all()
	route = Routes.objects.all()
	faq = FAQ.objects.all()
	airport = AirportOption.objects.all()
	context = {'indexSearch':indexSearch, 'offer':offer, 'route':route, 'faq':faq, 'airport':airport}

	return render(request,'index.html',context)


def OfferPage(request,pk):
	offer = Offer.objects.get(pk = pk)
	context = {'offer':offer}
	return render(request,'offer.html',context)


def FlightSearch(request,dept,arr):
	dept = dept
	newDept = ''
	for d in dept :
		if d != '[':
			newDept = newDept + d
		else :
			break
	newDept = newDept[:-1]
	print(newDept)
	newArr = ''
	arr = arr
	for a in arr :
		if a != '[':
			newArr = newArr + a
		else :
			break
	newArr = newArr[:-1]
	a = random.randint(1,15)
	b = random.randint(16,30)
	flight = Flights.objects.all()[a:b]
	numFlight = len(flight)
	airport = AirportOption.objects.all()
	departure = AirportOption.objects.get(airport = newDept)
	arrival = AirportOption.objects.get(airport = newArr)
	context = {'flight':flight, 'airport':airport,'departure':departure, 'arrival': arrival,'numFlight':numFlight}
	return render(request,'flightsearch.html',context)

def TopRoute(request,pk,dept,arr):
	dept = dept
	newDept = ''
	for d in dept :
		if d != ' ':
			newDept = newDept + d
		else :
			break
	newArr = ''
	arr = arr
	for a in arr :
		if a != ' ':
			newArr = newArr + a
		else :
			break
	a = random.randint(1,15)
	b = random.randint(16,30)
	flight = Flights.objects.all()[a:b]
	numFlight = len(flight)
	airport = AirportOption.objects.all()
	departure = AirportOption.objects.get(place = newDept)
	arrival = AirportOption.objects.get(place = newArr)
	context = {'flight':flight, 'airport':airport,'departure':departure, 'arrival': arrival,'numFlight':numFlight}
	return render(request,'toproute.html',context)

@login_required
def FlightConfirm(request,num,dept,arr):
	dept = dept
	newDept = ''
	for d in dept :
		if d != ' ':
			newDept = newDept + d
		else :
			break
	newArr = ''
	arr = arr
	for a in arr :
		if a != ' ':
			newArr = newArr + a
		else :
			break
	flight = Flights.objects.get(flightnum = num)
	departure = AirportOption.objects.get(place = newDept)
	arrival = AirportOption.objects.get(place = newArr)
	context = {'flight':flight,'departure':departure, 'arrival': arrival,'num':num}
	if request.method == "POST":
		customerUsername = request.POST.get('customerUsername','')
		totalAmt = request.POST.get('totalAmt','')
		AdultName = request.POST.get('AdultName','')
		ChildName = request.POST.get('ChildName','')
		InfantName = request.POST.get('InfantName','')
		DeparturePlace = request.POST.get('DeparturePlace','')
		ArrivalPlace = request.POST.get('ArrivalPlace','')
		DepartureTime = request.POST.get('DepartureTime','')
		ArrivalTime = request.POST.get('ArrivalTime','')
		FlightDate = request.POST.get('FlightDate','')
		FlightNum = request.POST.get('FlightNum','')
		email = request.POST.get('Email','')
		phone = request.POST.get('Phone','')
		amount = int(totalAmt) * 100
		client = razorpay.Client(auth = ("rzp_test_NeysSsZI9pQXph","oQKACXIalTGdeOTzXjtfzfqk"))
		payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
		print(payment)
		flightOrderBooked = FlightOrderBooked(username=customerUsername,amount=totalAmt,payment_id=payment['id'],AdultName=AdultName,ChildName=ChildName,InfantName=InfantName,DeparturePlace=DeparturePlace,ArrivalPlace=ArrivalPlace,DepartureTime=DepartureTime,ArrivalTime=ArrivalTime,FlightDate=FlightDate,FlightNum=FlightNum,email=email,phone=phone)
		flightOrderBooked.save()
		print(customerUsername)
		print(totalAmt)
		context = {'flight':flight,'departure':departure, 'arrival': arrival,'num':num,'payment':payment}
		return render(request,'flightbook.html',context)
		
	return render(request,'flightbook.html',context)


def Hotel(request):
	indexSearch = IndexSearch.objects.get(id=4)
	hotelCarousel1 = HotelCarousel.objects.all()[:4]
	hotelCarousel2 = HotelCarousel.objects.all()[4:8]
	hotelCarousel3 = HotelCarousel.objects.all()[8:12]
	faq = HotelFAQ.objects.all()
	destname = HotelDestination.objects.all()
	context = {'indexSearch':indexSearch,'hotelCarousel1':hotelCarousel1,'hotelCarousel2':hotelCarousel2,'hotelCarousel3':hotelCarousel3,'faq':faq, 'destname':destname}
	return render(request,'hotel.html',context)

def HotelSearch(request,dest):
	destname = dest
	a = random.randint(1,15)
	b = random.randint(16,30)
	hotelList = HotelList.objects.all()[a:b]
	numHotel = len(hotelList)
	context = {'destname':destname,'hotelList':hotelList,'numHotel':numHotel}

	return render(request,'hotelsearch.html',context)

def HotelSearchFilter(request,dest,cond,filt):
	destname = dest
	cond = cond
	filt = filt
	if filt == '10000' and cond == 'price':
		hotelList = HotelList.objects.filter(price__gt=filt)
	elif filt == '2000' and cond == 'price':
		hotelList = HotelList.objects.filter(price__lt=filt)
	elif cond != 'price' and cond != 'star' and cond != 'amenities':
		hotelList = HotelList.objects.filter(price__gt=cond).exclude(price__gt=filt)
	elif cond == 'star':
		hotelList = HotelList.objects.filter(star=filt)
	elif cond == 'amenities':
		if HotelList.objects.filter(amen1=filt):
			hotelList = HotelList.objects.filter(amen1=filt)
		elif HotelList.objects.filter(amen2=filt):
			hotelList = HotelList.objects.filter(amen2=filt)
		elif HotelList.objects.filter(amen3=filt):
			hotelList = HotelList.objects.filter(amen3=filt)
		elif HotelList.objects.filter(amen4=filt):
			hotelList = HotelList.objects.filter(amen4=filt)
	numHotel = len(hotelList)
	context = {'destname':destname,'hotelList':hotelList,'numHotel':numHotel}
	return render(request,'hotelsearch.html',context)

@login_required
def HotelBook(request,dest,pk):
	destname = dest
	hotelList = HotelList.objects.get(id=pk)
	context = {'destname':destname,'hotelList':hotelList,}
	if request.method == "POST":
		customerUsername = request.POST.get('customerUsername','')
		totalAmt = request.POST.get('totalAmt','')
		tRoom = request.POST.get('tRoom','')
		tAdults = request.POST.get('tAdults','')
		tChild = request.POST.get('tChild','')
		HotelName = request.POST.get('HotelName','')
		checkIn = request.POST.get('checkIn','')
		checkOut = request.POST.get('checkOut','')
		FirstName = request.POST.get('FirstName','')
		LastName = request.POST.get('LastName','')
		email = request.POST.get('Email','')
		phone = request.POST.get('Phone','')
		amount = int(totalAmt) * 100
		client = razorpay.Client(auth = ("rzp_test_NeysSsZI9pQXph","oQKACXIalTGdeOTzXjtfzfqk"))
		payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
		print(payment)
		hotelOrderBooked = HotelOrderBooked(username=customerUsername,amount=totalAmt,payment_id=payment['id'],tRoom=tRoom,tAdults=tAdults,tChild=tChild,HotelName=HotelName,checkIn=checkIn,checkOut=checkOut,FirstName=FirstName,LastName=LastName,email=email,phone=phone)
		hotelOrderBooked.save()
		context = {'destname':destname,'hotelList':hotelList,'payment':payment}
		return render(request,'hotelbook.html',context)

	return render(request,'hotelbook.html',context)

def Support(request):
	if request.user == 'AnonymousUser':
		contacted = False
		context = {'contacted':contacted,}
	else:
		user_profile = UserProfile.objects.all()
		contacted = False
		context = {'contacted':contacted,'user_profile':user_profile}
	if request.method == "POST":
		username = request.POST.get('username','')
		name = request.POST.get('name','')
		email = request.POST.get('email','')
		phone = request.POST.get('contact','')
		msg = request.POST.get('message','')
		contact = ComplaintMessage(name=name,email=email,phone=phone,message=msg,username=username)
		contact.save()
		contacted = True
		context = {'contacted':contacted,'user_profile':user_profile}
		return render(request,'support.html',context)
	return render(request,'support.html',context)


def Signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			phone = form.cleaned_data['phone']
			user = form.save()
			c = UserProfile(username = username,phone = phone,user = user)
			c.save()
			login(request,user)
			return redirect('/')
	else:
		form = SignUpForm()

	return render(request, 'register.html', {'form':form})

def Login(request):
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('/')
	else:
		form = AuthenticationForm()
	return render(request,'accounts/login.html',{'form':form})

def Profile(request,user):
	user_profile = UserProfile.objects.get(username = request.user.username)
	complaint = ComplaintMessage.objects.filter(username = request.user.username)
	flight = FlightOrderBooked.objects.filter(username = user)
	hotel = HotelOrderBooked.objects.filter(username = user)
	if not complaint:
		complaint = 'empty'
	if request.method == "POST":
		userform = UserUpdateForm(request.POST,instance=request.user)
		userprofileForm = UserProfileUpdateForm(request.POST,instance=user_profile)
		if userform.is_valid() and userprofileForm.is_valid():
			userform.save()
			userprofileForm.save()
			updated = True
			context = {'userform':userform, 'userprofileForm':userprofileForm,'updated':updated,'complaint':complaint,'flight':flight,'hotel':hotel}
			return render(request,'profile.html',context)
	else:
		userform = UserUpdateForm(instance=request.user)
		userprofileForm = UserProfileUpdateForm(instance=user_profile)
	context = {'userform':userform, 'userprofileForm':userprofileForm,'complaint':complaint,'flight':flight,'hotel':hotel}
	return render(request,'profile.html',context)

@csrf_exempt
def Success(request,num,dept,arr):
	if request.method == 'POST':
		a = request.POST
		order_id = ""
		for key, val in a.items():
			if key == 'razorpay_order_id':
				order_id = val
				break
		userPaid = FlightOrderBooked.objects.filter(payment_id=order_id).first()
		userPaid.paid = True
		userPaid.save()
		userPaidDet = FlightOrderBooked.objects.get(payment_id=order_id)
		flightDet = Flights.objects.get(flightnum=num)
		deptPlace = AirportOption.objects.get(place=dept)
		arrPlace = AirportOption.objects.get(place=arr)
		print(a)
		print(userPaid)
		context = {'userPaidDet':userPaidDet,'flightDet':flightDet,'deptPlace':deptPlace,'arrPlace':arrPlace}
		return render(request,'success.html',context)
	return render(request,'success.html')


@csrf_exempt
def Success2(request):
	if request.method == 'POST':
		a = request.POST
		order_id = ""
		for key, val in a.items():
			if key == 'razorpay_order_id':
				order_id = val
				break
		userPaid = HotelOrderBooked.objects.filter(payment_id=order_id).first()
		userPaid.paid = True
		userPaid.save()
		print(a)
		print(userPaid)
		userPaidDet = HotelOrderBooked.objects.get(payment_id=order_id)
		context = {'userPaidDet':userPaidDet}
		return render(request,'success2.html',context)
	return render(request,'success2.html')



def ViewFlightTicket(request,num,dept,arr,orderid):
	userPaidDet = FlightOrderBooked.objects.get(payment_id=orderid)
	flightDet = Flights.objects.get(flightnum=num)
	deptPlace = AirportOption.objects.get(place=dept)
	arrPlace = AirportOption.objects.get(place=arr)
	context = {'userPaidDet':userPaidDet,'flightDet':flightDet,'deptPlace':deptPlace,'arrPlace':arrPlace}
	return render(request,'viewflightticket.html',context)


def ViewHotelTicket(request,orderid):
	userPaidDet = HotelOrderBooked.objects.get(payment_id=orderid)
	context = {'userPaidDet':userPaidDet}
	return render(request,'viewhotelticket.html',context)







