class PlanAhorro:
    cuotasPlan = 100 #Cantidad total de cuotas del plan
    cuotaMinLicitar = 20 # Cantidad minima de cuotas para Licitar
    #Atributos
    __codigo =0
    __modelo = ''
    __version  = ''
    __valorVehiculo = 0
    __cantidadCuotasPlan = 0
    __cantidadCuotasLicitar = 0

    #Metodos
    def __init__(self,codigo='',modelo=0,version=0,valor=0,cuotasPlan=0,cuotasLicitar=0):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valorVehiculo = valor
        self.__cantidadCuotasPlan = cuotasPlan
        self.__cantidadCuotasLicitar = cuotasLicitar
     
    def getCodigo(self):
         return self.__codigo
    def getModelo(self):
         return self.__modelo
    def getVersion(self):
         return self.__version
    def getValorVehiculo(self):
         return self.__valorVehiculo
    def getCantidadCuotasLicitar(self):
        return self.__cantidadCuotasLicitar
    def setValorVehiculo(self, valor=0):
         self.__valorVehiculo=valor
    

    def calcularCuotas(self):
        #valor=0
        #if((cuotas>0) and(importe>0)):
        valor=(float(self.__valorVehiculo)/int(self.__cantidadCuotasPlan))+(float(self.__valorVehiculo)*0.10)     
        return(valor)

    def actualizarValor(self, valorVehiculo=0):
        if(valorVehiculo>0):
            self.__valorVehiculo=valorVehiculo
    @classmethod       
    def getCuotaMinLicitar(cls):
        return cls.cuotaMinLicitar
        
    def setModiCantLicitar(self,newCuotaMinLicitar):
             
        error = False
        if type(newCuotaMinLicitar) == int and newCuotaMinLicitar >0: #Debe ser mayor a 0
              cuotaMinLicitar = newCuotaMinLicitar
        else:
               error = True #Hay error al cambiar
        return error 