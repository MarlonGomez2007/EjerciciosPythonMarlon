valorCompra=int(input("Digite el valor de la compra : "))
descuento=int(input("Digite el descuento : "))
#declaro primero las variables y con el comando input pido la informacion al usuario
obtenerDescuento=descuento / 100
#hacemos la operacion de dividir el descuento sobre 100
multiplicar=obtenerDescuento * valorCompra
#multiplique el descuento por el valor de la compra para saber cuanto se le va restar al valor final
valorFinal=valorCompra - multiplicar
#aca se coge el valor de la compra y se le resta el valor del descuento
print("La compra fue",valorCompra,"con un descuento de",descuento ,"%","el valor final a pagar es",valorFinal)
#el comando print se imprime el valor de la compra, el descuento, precio final y con la "," concateno las variables