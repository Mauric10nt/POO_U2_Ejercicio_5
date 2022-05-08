import csv
from claseMenu import Menu
from PlanAhorro import PlanAhorro
def leerPlanAhorro():
    planAhorro = PlanAhorro()
    nomAr = 'planes.csv'
    archivo = open(nomAr)
    reader = csv.reader(archivo,delimiter=';')
    bandera = True
    for fila in reader:
        if bandera:
            bandera = False
        else:
            print('Datos: {}'.format(fila))
            planAhorro.addPlanAhorro(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
    archivo.close()
    
if __name__=='__main__':
    __listaPlanes = []
    # Cargo planes
    nomAr = 'planes.csv'
    archivo = open(nomAr)
    reader = csv.reader(archivo,delimiter=';')
    bandera = True
    for fila in reader:
        print('Datos: {}'.format(fila))
        planAhorro = PlanAhorro(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
        __listaPlanes.append(planAhorro)
    
    archivo.close()
    menuPrincipal = Menu()
    menuPrincipal.define_menu(['[1]- Actiualizar Valor de los Vehículos','[2]- Ingrese un Valor','[3]- Ver el Monto para Licitar','[4]- Modificar Cantidad de Cuotas para Licitar','[0]- Salir'])
    menuPrincipal.showMenu(1)# le mando 1 para que solo limpie la pantalla al principio
    op = menuPrincipal.selectOption()
    cantPlan=len(__listaPlanes)
    while op != 0:
        if op == 1:
            i=0
            print('Actiualizar Valor de los Vehículos')
            bandera=0
            print('Ingrese -1 para terminar')
            while ((i<cantPlan)and(bandera>=0)) :
                print('Código: ',__listaPlanes[i].getCodigo())
                print('Modelo: ',__listaPlanes[i].getModelo())
                print('Valor: ',__listaPlanes[i].getValorVehiculo())
                nuevoValor = input('Ingrese un Nuevo Valor: ')
                if(int(nuevoValor)>0):
                    __listaPlanes[i].setValorVehiculo(int(nuevoValor))
                    print('Se Actiualizo el Valor del Vehículo a: ',__listaPlanes[i].getValorVehiculo())
                    i=i+1
                else:
                    bandera=-1
        elif op == 2:
            print('Ingrese un Valor')
            valor = input()
            i=0
            while i<cantPlan:
                if(int(__listaPlanes[i].getValorVehiculo())<int(valor)):
                    print('Código: ',__listaPlanes[i].getCodigo())
                    print('Modelo: ',__listaPlanes[i].getModelo())
                    print('Versión: ',__listaPlanes[i].getVersion())
                    print('')
                i=i+1
        elif op == 3: 
            print('Ver el Monto para Licitar')
            i=0
            while i<cantPlan:
                importeCuota=__listaPlanes[i].calcularCuotas()
                print (importeCuota)
                print(__listaPlanes[i].getCuotaMinLicitar())
                montoApagar=int(__listaPlanes[i].getCuotaMinLicitar())*importeCuota
                print('Modelo: ',__listaPlanes[i].getModelo(),' Versión: ',__listaPlanes[i].getVersion())
                print('Monto para Licitar :',round(montoApagar, 2))
                print('')
                i=i+1
        elif op == 4:
            i=0
            print('Modificar Cantidad de Cuotas para Licitar')
            bandera=0
            print('Ingrese -1 para terminar')
            while ((i<cantPlan)and(bandera>=0)) :
                print('Código: ',__listaPlanes[i].getCodigo())
                print('Modelo: ',__listaPlanes[i].getModelo())
                print('Cuotas para Licitar: ',__listaPlanes[i].getCuotaMinLicitar())
               ## nuevoValor = input('Ingrese número de cuotas: ')
                newCant = int(input('Ingrese nueva cantidad de cuotas para licitar cantidad: '))
                if  (newCant>0):
                     
                     error = __listaPlanes[i].setModiCantLicitar(newCant)
                
                     if error == False:
                        print('Modificacion realizada con exito!')
                     else:
                         print('Error: No se pudo realizar la modificacion')
         
                     i=i+1
                else:
                     bandera=-1
        print('')           
        menuPrincipal.showMenu(0)# le mando 0 para que no limpie la pantalla 
        op = menuPrincipal.selectOption()
    
    