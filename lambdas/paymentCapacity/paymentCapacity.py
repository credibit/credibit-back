#def calculoPlan(puntosBuro, puntosSat, ingresoMensual, ingresoNeto, cantidadDeseada, plazoDeseado):

def paymentCapacity(event, context):
    puntosBuro=event['puntosBuro']
    puntosSat=event['puntosSat']
    ingresoMensual=event['ingresoMensual']
    ingresoNeto=event['ingresoNeto']
    cantidadDeseada=event['cantidadDeseada']
    plazoDeseado=event['plazoDeseado']

    puntos=(puntosBuro+puntosSat)/2
    opcion="-1"
    if(puntos>=85):
        if(ingresoMensual>(.083*cantidadDeseada)):
            opcion="A"
            totalPrestado=(cantidadDeseada*1.1)
            totalIntereses=(totalPrestado)*.25
            total=totalPrestado+totalIntereses
            return opcion,total
        elif(ingresoMensual>(.041*cantidadDeseada)):
            opcion="B"
            totalPrestado=(cantidadDeseada)
            totalIntereses=(totalPrestado)*.29
            total=totalPrestado+totalIntereses
            return opcion, total
        elif(ingresoMensual>(.021*cantidadDeseada)):
            opcion="C"
            totalPrestado=(cantidadDeseada)*.75
            totalIntereses=(totalPrestado)*.35
            total=totalPrestado+totalIntereses
            return opcion, total
        elif(ingresoMensual<(.021*cantidadDeseada)):
            opcion="D"
            return opcion, -1
    elif(puntos<=85 and puntos>59):
        if(ingresoMensual>(.041*cantidadDeseada)):
            opcion="B"
            totalPrestado=(cantidadDeseada)
            totalIntereses=(totalPrestado)*.29
            total=totalPrestado+totalIntereses
            return opcion, total
        elif(ingresoMensual>(.021*cantidadDeseada)):
            opcion="C"
            totalPrestado=(cantidadDeseada)*.75
            totalIntereses=(totalPrestado)*.35
            total=totalPrestado+totalIntereses
            return opcion, total
        elif(ingresoMensual<(.021*cantidadDeseada)):
            opcion="D"
            return opcion, -1
    elif(puntos<61 and puntos>44):
        if(ingresoMensual>(.021*cantidadDeseada)):
            opcion="C"
            totalPrestado=(cantidadDeseada)*.75
            totalIntereses=(totalPrestado)*.35
            total=totalPrestado+totalIntereses
            return opcion, total
        elif(ingresoMensual<(.021*cantidadDeseada)):
            opcion="D"
            return opcion, -1
    elif(puntos<45):
        if(ingresoMensual<(.021*cantidadDeseada)):
            opcion="D"
            return opcion,-1
    return -1,-1

"""
puntosBuro=80
puntosSat=98
ingresoMensual=67000
ingresoNeto=ingresoMensual*.20
cantidadDeseada=700000
plazoDeseado=36
"""
"""
puntosBuro=65
puntosSat=75
ingresoMensual=21000
ingresoNeto=ingresoMensual*.20
cantidadDeseada=335000
plazoDeseado=42


puntosBuro=24
puntosSat=91
ingresoMensual=75000
ingresoNeto=ingresoMensual*.20
cantidadDeseada=1200000
plazoDeseado=48


puntosBuro=10
puntosSat=20
ingresoMensual=39000
ingresoNeto=ingresoMensual*.20
cantidadDeseada=750000
plazoDeseado=60

print(calculoPlan(puntosBuro, puntosSat, ingresoMensual, ingresoNeto, cantidadDeseada, plazoDeseado))
"""
