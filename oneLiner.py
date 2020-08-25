#No se que hago
#import dis

#print(dis.dis(a))


a=lambda x,y: list(zip(*[   iter(range(x,y))  ]*4) )+[list(range(y-y%4,y))] if y-8>x else lambda p : ValueError(".") ; print("\n".join([f"{i}" for i in a(int(input("Lower limit ")),int(input("Upper limir ")))]) )