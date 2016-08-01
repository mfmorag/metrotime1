import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from geopy.distance import vincenty
from transporte.models import *
from transporte.forms import VehiculoForm
from transporte.forms import ConductorForm
from transporte.forms import RutaVehiculoForm
from django.views.generic import ListView
# Create your views here.

def InicioView(request):
    return render(request, 'index.html')

def RutasView(request):
    return render(request, 'index-1.html')

def UbicacionView(request):
    return render(request, 'index-2.html')

def RutaTView(request):
    return render(request, 'index-Ruta-T.html')

def RutaNorteView(request):
    return render(request, 'index-Ruta-Norte.html')

def RutaSurView(request):
    return render(request, 'index-Ruta-Sur.html')

def RutaCentroView(request):
    return render(request, 'index-Ruta-Centro.html')

def RutaEsteView(request):
    return render(request, 'index-Ruta-Este.html')

def RutaNOesteView(request):
    return render(request, 'index-Ruta-NorOeste.html')

def RutaSOesteView(request):
    return render(request, 'index-Ruta-SurOeste.html')

def UbT1View(request):
    return render(request, 'index-T1.html')

def UbT2View(request):
    return render(request, 'index-T2.html')

def UbT3View(request):
    return render(request, 'index-T3.html')

def R25JPView(request):
    return render(request, 'R-25Julio-Pradera.html')

def RalboradaView(request):
    return render(request, 'R-alborada.html')

def RcausarinaView(request):
    return render(request, 'R-causarina.html')

def RcentroView(request):
    return render(request, 'R-centro.html')

def RestelaView(request):
    return render(request, 'R-estelaMaris-Pradera.html')

def RfertisaView(request):
    return render(request, 'R-fertisa.html')

def RflorbastionView(request):
    return render(request, 'R-flor-de-bastion.html')

def RflorestaView(request):
    return render(request, 'R-floresta.html')

def RfloridarotView(request):
    return render(request, 'R-florida-rotonda.html')

def RgarzotaView(request):
    return render(request, 'R-garzota.html')

def RguasmocentralView(request):
    return render(request, 'R-GuasmoCentral.html')

def RguasmosurcristalView(request):
    return render(request, 'R-GuasmoSur-Cristal.html')

def RguayacanesView(request):
    return render(request, 'R-Guayacanes.html')
def RiguanasView(request):
    return render(request, 'R-iguanas.html')

def RjuanmontalvoView(request):
    return render(request, 'R-juan-montalvo.html')

def RjuantancaView(request):
    return render(request, 'R-juan-tancamarengo.html')

def RlaPlayitaView(request):
    return render(request, 'R-laPlayita.html')

def RmapasingueEView(request):
    return render(request, 'R-mapasingue-este.html')

def RmapasingueOView(request):
    return render(request, 'R-mapasingue-oeste.html')

def RmucholoteGView(request):
    return render(request, 'R-mucholote-G.html')

def RmucholoteOView(request):
    return render(request, 'R-mucholote-O.html')

def RorellanaView(request):
    return render(request, 'R-orellana.html')

def RpascualesView(request):
    return render(request, 'R-pascuales.html')

def RpuertoView(request):
    return render(request, 'R-puertomaritimo.html')

def RsamanesView(request):
    return render(request, 'R-samanes.html')

def RsaucesView(request):
    return render(request, 'R-sauces.html')

def RtrinipuertoView(request):
    return render(request, 'R-trinipuerto.html')

def Rtrinitaria2View(request):
    return render(request, 'R-trinitaria-2dopuente.html')

def RUBastionView(request):
    return render(request, 'R-UdeBastion.html')

def RVialaCostaView(request):
    return render(request, 'R-VialaCosta.html')

def RatahualpaSAView(request):
    return render(request, 'R-atahualpa-SanAgustin.html')

def RlosEsterosView(request):
    return render(request, 'R-losEsteros.html')

def RmartinAvilesView(request):
    return render(request, 'R-martinAviles.html')

def RplayitaSAView(request):
    return render(request, 'R-playita-SanAgustin.html')

def MiRutaView(request):
    return render(request, 'index-miRuta.html')

def AdminView(request):
    return render(request, 'indexadmin.html')

def trazarMapa(request):
    return render_to_response("R-alborada.html", context_instance=RequestContext(request))

def VerMapa(request, id_v):
    return render_to_response("R-alborada.html", {"id_v": id_v}, context_instance=RequestContext(request))

def InformacionView(request):
    return render(request, 'informacionVehiculo.html')

def EditarView(request):
    return render(request, 'editar.html')

def VelocimetroView(request):
    listacodigo=Vehiculo.objects.all()
    return render(request, 'velocimetro.html',locals())

def ParadasView(request):
    return render(request, 'paradas.html')

def RutaVehiculoView(request):
    return render(request, 'RutaVehiculo.html')

def Create_conductoresView(request):
    if request.method == 'POST':
        data = {
            'id_vehiculo': request.POST.get('id_vehiculo'),
            'nombres': request.POST.get('nombres'),
            'apellidos': request.POST.get('apellidos'),
            'edad': request.POST.get('edad'),
            'cedula': request.POST.get('cedula'),
            'telefono': request.POST.get('telefono'),
            'correo': request.POST.get('correo'),
        }
        form = ConductorForm(data)
        if form.is_valid():
            form.save()
            return redirect('admin')
        else:
            return render_to_response("agregarconductores.html", {'mensaje': 'Los datos no fueron guardados'},context_instance=RequestContext(request))
    else:
        form=ConductorForm()
    listacodigo = Vehiculo.objects.all()
    return render(request, 'agregarconductores.html',locals(),context_instance=RequestContext(request))


def Create_VehiculoView(request):
    if request.method == 'POST':
        data={
            'id_est':'1',
            'placa':request.POST.get('placa'),
            'numero_gsm':request.POST.get('numero_gsm'),
            'codigo':request.POST.get('codigo'),
            'estado':request.POST.get('estado'),
        }
        form = VehiculoForm(data)
        if form.is_valid():
           form.save()
           return redirect('agregarConductores')
        else:
            return render_to_response("agregarVehiculo.html",{'mensaje':'Los datos no fueron guardados'},context_instance=RequestContext(request))
    else:
        form = VehiculoForm()
    listaest=Estado.objects.all()
    return render_to_response('agregarVehiculo.html',locals(),context_instance=RequestContext(request))


def Create_Ruta_VehiculoView(request):
    if request.method == 'POST':
        form = RutaVehiculoForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('createrutavehiculo')
    else:
        form = RutaVehiculoForm()
    listarv = RutaVehiculo.objects.all()
    return render(request, 'RutaVehiculo.html', {'form': form, 'listarv': listarv})

def listaubicacionvehiculo(request):
    listauv= Ubicacion.objects.all()
    return render(request, 'infoUbicacionVehiculo.html', {'listauv': listauv})


def listavehiculo(request):
    lista= Vehiculo.objects.all()
    return render(request, 'informacionVehiculo.html', {'lista': lista})

def listaconductores(request):
    listac= Conductor.objects.all()
    return render(request, 'informacionConductores.html', {'listac': listac})


@csrf_exempt
def create_posCar(request):
    id_vehiculo = request.POST.get("id_vehiculo")
    lat = request.POST.get("latitud")
    longi = request.POST.get("longitud")
    vel = request.POST.get("velocidad")
    u = Ubicacion()
    print id_vehiculo
    u.id_vehiculo = Vehiculo.objects.get(placa=id_vehiculo)
    print  u.id_vehiculo
    u.latitud = lat
    u.longitud = longi
    u.velocidad= vel
    u.save()
    return HttpResponse("True")


@csrf_exempt
def get_posfinal(request): #funcion para devolver la ultima posicion

    try:
        id_posicion = request.POST.get("id_posicion")
        ubicacion = Ubicacion.objects.filter(Vehiculo=Vehiculo.objects.get(codigo=id_posicion))
        total = len(ubicacion)
        ult_ubicacion_pre = ubicacion[total-2]
        ult_ubicacion = ubicacion[total-1]
        ult_ubicacion = ult_ubicacion.vel
        if ult_ubicacion.vel == ult_ubicacion_pre.vel:
            ult_ubicacion = 0
    except:
        ult_ubicacion = 0

    return HttpResponse(ult_ubicacion)

@csrf_exempt
def get_pos_parada(request, id_p_ruta): #funcion para obtener una lista de las posiciones de las paradas
    posicion_parada = Parada.objects.filter(id_ruta=id_p_ruta)
    parada_list= map(lambda x: dict(
        nombre=x.nombre,
        latitud=float(x.latitud),
        longitud=float(x.longitud),
        order=x.order,
    ), posicion_parada)

    return HttpResponse(json.dumps(parada_list, indent=4), content_type="application/json")

@csrf_exempt
def get_lista(request, id_p_ruta): #funcion para obtener una lista de las posiciones de 2 paradas
    posicion_parada = Parada.objects.filter(id_ruta=id_p_ruta).order_by("order")
    total = 0
    lista = []
    for i in range(0, len(posicion_parada)-1):
        v1=posicion_parada[i]
        v2=posicion_parada[i+1]
        parcial = vincenty((float(v1.latitud), float(v1.longitud)), (float(v2.latitud), float(v2.longitud))).kilometers
        total += parcial
        lista.append(dict(
            lat1=float(v1.latitud),
            long1=float(v1.longitud),
            lat2=float(v2.latitud),
            long2=float(v2.longitud),
            dist=total,
            parcial=parcial,
        ))
    return HttpResponse(json.dumps(lista, indent=4), content_type="application/json")

@csrf_exempt
def get_rline(request, id_lr): #funcion para obtener una lista de las posiciones de la ruta
    punto_ruta = RLine.objects.filter(id_ruta=id_lr)
    ruta_list= map(lambda x: dict(
        latitud=float(x.latitud),
        longitud=float(x.longitud),
    ), punto_ruta)

    return HttpResponse(json.dumps(ruta_list), content_type="application/json")

@csrf_exempt
def get_pline(request, id_p_ruta): #funcion para obtener una lista de las posiciones de la ruta y sus lineas
    lista = []
    posicion_parada = Parada.objects.filter(id_ruta=id_p_ruta).order_by("order")
    vehiculo = RutaVehiculo.objects.filter(id_ruta_id=id_p_ruta)
    total = 0
    line_list = []
    parada_list = []
    for i in range(0, len(posicion_parada)):
        p1 = posicion_parada[i]
        punto_ruta = PLine.objects.filter(parada=p1.id)
        for j in range(0, len(punto_ruta) - 1):
            pr1 = punto_ruta[j]
            pr2 = punto_ruta[j + 1]
            parcial = vincenty((float(pr1.latitud), float(pr1.longitud)),
                               (float(pr2.latitud), float(pr2.longitud))).kilometers
            total += parcial
            line_list.append(dict(
                r_list=dict(num_parada=pr1.parada.order, rlat=pr1.latitud, rlong=pr1.longitud, dist=total,
                            parcial=parcial, ),
            ))
    for k in range(0, len(posicion_parada)):
        p2 = posicion_parada[k]
        parada_list.append(dict(orden=p2.order,nombre=p2.nombre,latitud=float(p2.latitud),longitud=float(p2.longitud), ))

        lista = (line_list,  parada_list)
    return HttpResponse(json.dumps(lista, indent=4), content_type="application/json")

@csrf_exempt
def get_pos_car(request, id_v): #funcion para obtener una lista de las posiciones del carro
    vehiculo = RutaVehiculo.objects.filter(id_ruta_id=id_v)
    car_list = []
    for x in range(0, len(vehiculo)):
        c = vehiculo[x]
        pos_vehiculo = Ubicacion.objects.filter(id_vehiculo=c.id_vehiculo)
        pos_list = map(lambda x: dict(
            latitud=float(x.latitud),
            longitud=float(x.longitud),
            velocidad=float(x.velocidad),
        ), pos_vehiculo)
        car_list.append(dict(carro=c.id_vehiculo_id, pos=pos_list))
    return HttpResponse(json.dumps(car_list, indent=4), content_type="application/json")

