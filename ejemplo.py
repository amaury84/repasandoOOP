"""
autor:
fecha:
descripción: repaso OOP

métodos
  set  poner
  get  obtener
"""

class personas():
    
    def setCargo(self,cargo):
        self.cargo = cargo
    
    def getCargo(self):
        print(self.cargo)
    
    
admin = personas()
admin.setCargo("administrador")
admin.getCargo()

ventas = personas()
ventas.setCargo("supervisor")
ventas.getCargo()

getCargo()
        