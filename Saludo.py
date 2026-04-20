from abc import ABC, abstractmethod

class Documento(ABC):
    @abstractmethod
    def exportar(self):
        """Este método debe ser implementado por cualquier clase hija"""
        pass

class PDF(Documento):
    def exportar(self):
        return "Exportando contenido a formato PDF..."

class Word(Documento):
    def exportar(self):
        return "Guardando como archivo .docx..."

# No puedes hacer: doc = Documento() -> Lanzará un error
archivo = PDF()
print(archivo.exportar())