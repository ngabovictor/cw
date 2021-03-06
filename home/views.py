from django.shortcuts import render
from home.models import services, toPricing, portfolio, staff, prices, carousel
from control.models import mailbox, order
from datetime import datetime
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.
def home(request):
	data = {}
	data['carousels'] = carousel.objects.all()
	data['services'] = services.objects.all()
	data['portfolio'] = portfolio.objects.all()
	data['toPricings'] = toPricing.objects.all()
	data['prices'] = prices.objects.all()
	data['staff'] = staff.objects.all()

	return render(request, 'home/index.html', data)



def send_message(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST.get('message')
		classifications = 'Unread'
		date = datetime.today()

		mailbox.objects.create(
			name = name,
			email = email,
			message = message,
			classifications = classifications,
			date = date,
			)
	
		#send_mail(
			#'Message from web by %s'%email,
			#message,
			#'coredev2017@gmail.com',
			#['contact@corelabsplus.com'],
			#fail_silently=False,
		#)

	return HttpResponse(' ')

def order_now(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		tel = request.POST.get('phone')
		category = request.POST['category']
		description = request.POST['description']
		address = request.POST['address']
		# supporting_doc = request.FILES['supporting_doc']

		order.objects.create(
			name = name,
			email = email,
			tel = tel,
			address = address,
			category = category,
			description = description,
			classification = 'Unread',
			date = datetime.today(),
			# supporting_doc = supporting_doc,
			mailed= 'N',
			)
	
		#send_mail(
			#'New order from %s'%email,
			#description,
			#'coredev2017@gmail.com',
			#['orders@corelabsplus.com'],
			#fail_silently = False,
		#)

	return HttpResponseRedirect('thanks')

def thanks(request):

	contact = order.objects.get(mailed='N')
	
	email = contact.email
	
	#send_mail(
	   # 'Your order has been comfirmed - Core Labs+ Ltd.',
	    #'Thank you for requesting the service(s) at Core Labs+ Ltd, we are excited to start working with you.\n\nPlease, do not reply this email as it is auto generated. Instead, do not hesitate to contact us on support@corelabsplus.com.\nWe will be contacting you soon regarding your order.\nIf you wish, you may send supporting documents regarding your request on the given email address.\n\n\nCore Labs+ Ltd. Team.\nwww.corelabsplus.com\nOur Passion, Your Potential.',
	    #'coredev2017@gmail.com',
	   # [email],
	    #fail_silently = False,
	#)
	order.objects.filter(mailed='N').update(mailed='Y')

	# send_mail(
	#     'New order from %s'%email,
	#     description,
	#     'coredev2017@gmail.com',
	#     ['contact@corelabsplus.com'],
	#     fail_silently=False,
	# )
	return render(request, 'home/thanks.html')
