#CURSO DE PYTHON 
#Este programa recolecta información del usuario y 
# calcula el salario bruto que recibe al mes.



NOMBRE=input('Introduzca su nombre:')
EDAD=input('Introduzca se edad:')
DIRECCIÓN=input('Introduzaca su dirección:')
NÚMERO_TELEFÓNICO=input('Introduzca su número telefónico:')

print('Hola', NOMBRE, ', tu tienes', EDAD, 'años', 'y vives en', DIRECCIÓN)

print('Por favor, ayudame con estos datos para calcular tu salario bruto')

HORAS=float(input('Introduzca horas diarias de trabajo:'))
PRECIO=float(input('Introduzca tarifa diaria:'))

SALARIO=HORAS*PRECIO*4

print('SALARIO:', SALARIO)

print(NOMBRE, 'tu salario mensual es', SALARIO, 'dólares')

print('Gracias!!', end='.')
