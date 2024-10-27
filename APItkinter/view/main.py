import requests

from models.api_response import APIResponse
from dataclass_wizard import fromdict
from tkinter import messagebox as alert

from models.empresa import Empresa
from models.product import Product
from vistas import show_product_list


def main():
    response = requests.get("https://dummyjson.com/products")
    data_dict = response.json()
    product_list = fromdict(APIResponse, data_dict)
    show_product_list(product_list)

    # for product in product_list.products:
    #     print(product.title)
    #     for review in product.reviews:
    #         print(review.comment)
    #     print()
def generar_pdf(productos: list[Product]):
    empresa: Empresa = Empresa(
        nombre="Unai",
        titular="",
        cif="",
        direccion="",
        email="unaiperez5665@gmail.com"
    )
    #GENERO PDF (nombre=busqueda_resultado_202410241344SS.pdf)
    alert.showinfo("PDF Generado", "Se ha generado el PDF correctamente en")
    print()
    print()

    nombre_pdf="resultado_busqueda_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".pdf"
    HTML(string=contenido_pdf).write_pdf(nombre_pdf, presentational_hints=True)
    alert.showinfo("PDF Generado", "Se ha generado el PDF: " + nombre_pdf)
se:
    alert.showerror("No hay productos", "No se puede generar un PDF sin respuesta")
main()
