
# reintegro,trasferencia

nombre = str(input('Nombre de el propietario de la cuenta bancaria: '))
valor = float(input('valor inicial de la cuneta vancaria '))

class Cuenta:
    inicio = 1
    while inicio == 1:
        def __init__(self,nombre,ingreso):
            ingreso = ingreso
            pregunta = int(input('1 = Ingresar dinero, 2 = retirar dinero, 3 hacer una trasferencia bancaria.'))
            if pregunta == 1:
                ingresar = float(input('valor a ingresar a la cuenta: '))
                cuenta = str(ingreso) + str(ingresar)
                print(input('El valor de el sr' + ' ' + nombre + ' en su cuenta bancaria es de: ' + str(cuenta)))
            elif pregunta == 2:
                retirar = float(input('Valor a retirar de su cuenta bancaria: '))
                if retirar > ingreso:
                    print(input('La operacion que ustd desea hacer no es permitida ya que el valor que ustd desea retirar es mayor a el valor que tiene actualmente en su cuenta bancaria.'))
                else:
                    ingreso = ingreso - retirar
                    print(input('El retiro de su cuenta por el valor de ' + str(retirar) + ' fue realizado con exito por lo cual deja la cuenta con un valor de: ' + str(ingreso)))
            elif pregunta == 3:
                nombre = str(input('Nombre de la persona a la cual le va a trasferir dinero de su cuenta bancaria: '))
                valor = float(input('valor a trasferir: '))
                if valor > ingreso:
                    print(input('Trasfererencia fallida ya que el monto ingresado es mayor al monto de su cuenta bancaria la cual cuenta con: ' + str(ingreso)))
                else:
                    ingreso = ingreso - valor
                    print(input('La rasferencia a la cuneta de el sr ' + nombre  + ' a sido un exito, la cuenta a quedado con un valor de: ' + str(ingreso)))
        inicio += 1


primerCuenta = Cuenta(nombre,valor)