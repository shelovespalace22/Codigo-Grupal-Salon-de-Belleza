#Codigo de Miguel: Pagina principal y menu "Consultar Informacion de la Empresa."


print("¡Bienvenido a Vain Women! El mejor salon de belleza de la ciudad.")
print("1) Consultar informacion de la empresa.")
print("2) Comprar un producto.")
print("3) Agendar una cita ")
print("4) Servicio al cliente ")
menu=int(input("Por favor digite una de las opciones vistas anteriormente: "))
if menu==1 :
    print("Somos una empresa dedicada a ofrecer servicios de cuidado personal y estética, atendiendo a las demandas y necesidades de los clientes.")
    print("Informacion de contacto:  ")
    print("*Via telefonica: 3195199095")
    print("*Correo electronico saladebelleza@gmail.com")
    print("Encuentranos en las redes como: ")
    print("*Facebook:  @saladebelleza")
    print("*Instagram:  @saladebelleza01")
    print("Encuentranos en la Av. de las Americas Carrera 6 # 8-45 local 102")

#Codigo de Daniel Piñeros: Menu Comprar un producto y Agendar una cita.

elif menu==2:
    print("Tenemos los siguientes productos: ")
    print("1 Crema para peinar  $15.000")
    print("2 Shampoo con Savila  $25.000")
    print("3 Shampoo Anti caspa   $35.000")
    print("4 Shampoo para Cabello Rizado $28.000")
    compras=int(input("Por favor seleccione un producto: "))
    if compras==1 or compras==2 or compras==3 or compras==4 :
        print("Metodos de pago: 1. Mastercard, 2. Dinners Club, 3. Visa, 4. American Express, 5. Efecty")
        metpago=int(input("Seleccione un metodo de pago: "))
        if metpago==1 or metpago==2 or metpago==3 or metpago==4 or metpago==5:
            print("Gracias por su compra ")
            print("Que lo disfrute :)")
elif menu==3:
    print("¿Que tratamineto se desea hacer?")
    print("1 Keratina ")
    print("2 Corte de cabello ")
    print("3 Alisado ")
    print("4 Manicure")
    print("5 Pedicure") 
    trata=int(input("Por favor escoga un tratamiento: "))
    if trata==1 or trata==2 or trata==3 or trata==4 or trata==5:
        print("Muy bien ahora escoge la fecha y hora de la cita ")
        print("Citas disponibles: ")
        print("1.) lunes 4:00 pm")
        print("2.) martes  6:00 pm")
        print("3.) juves  8:00 am")
        print("4.) sabado  10:00 am")
        cita=int(input("Por favor escoga una de las citas disponibles: "))
        if cita==1 or cita==2 or cita==3 or cita==4:
            print("Su cita ha sido generada con exito!")
