class Router:
  def __init__(self, nombre, direccion_ip, mascara_subred):
    self.nombre = nombre
    self.direccion_ip = direccion_ip
    self.mascara_subred = mascara_subred
    self.conectado = False
   
  def conectar(self):
      self.conectado = True 
      print(f'El router {self.nombre} esta conectado.")
           
  def desconectar(self):
      self.conectado = False
      print(f'El Router {self.nombre} esta desconectado.")
            
   def enviar.paquete(self, destino, paquete):
        if self.conectado:
            print(f'Enviado paquete desde {self.direccion_ip} a {destino}: {paquete}")
        else:
            print(f'No se puede enviar el paquete. El Router {self.nombre} no esta conectado.")
                        

# Crear una instancia de Router
mi_router = Router("Router1", "192.168.1.1", "255.255.255.0")

# Conectar el router
mi_router.conectar()

# Enviar un paquete
mi_router.enviar_paquete("192.168.1.2", "Hola, este es un paquete de datos.")

# Desconectar el router
mi_router.desconectar()
                  
                  
                  
                  
