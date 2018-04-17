from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt

def cms_users_put(request,identificador):
	if request.user.is_authenticated():
		ans = "<h1>Usuario: " +str(request.user) + "<a href=http://localhost:8000/logout/>Logout</a></h1>"
	else:
		ans = "Usuario no reconocido " + "<a href=http://localhost:8000/login>Login</a></p>"
	if request.method == "GET":
		try:
			pag = Pages.objects.get(name = identificador)
			ans += pag.page
		except Pages.DoesNotExist:
			ans = "No hay datos"
		return HttpResponse(ans)
	elif request.method == "PUT":
		if request.user.is_authenticated():
			try:	
				pag = Pages.objects.create(name = identificador,page =request.body.decode("utf-8")) 
				pag.save()
				ans += "Se ha creado una nueva pagina"
				return HttpResponse(ans)
			except:
				ans += "La página no se ha creado."
	else:
		ans += "Metodo no reconocido"
		return HttpResponse(ans)

def show_content(request):
	ans = "<h1>Lista de Paginas: </h1>"
	for pg in Pages.objects.all():
		ans += "<br/><a href='" + pg.name + "'>" + pg.name + "</a>"	

	if request.user.is_authenticated():
		ans += "<br>Usuario: " +str(request.user) + "<a href=http://localhost:8000/logout/>Logout</a></p>"
	else:
		ans += "<br>Usuario no reconocido " + "<a href=http://localhost:8000/login>Login</a></p>"
	return HttpResponse(ans)