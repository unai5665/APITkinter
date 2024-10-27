import tkinter as tk
import requests
from PIL import Image, ImageTk
from models.api_response import APIResponse
from main import generar_pdf  # Importa la función generar_pdf


def show_product_list(product_list: APIResponse):
    root = tk.Tk()
    root.title("Lista de Productos")
    root.geometry("600x800")  # Ajuste del tamaño de la ventana

    # Índice inicial del producto
    current_index = [0]

    # Diccionario para caché de imágenes
    image_cache = {}

    # Función para actualizar la vista con el producto en el índice actual
    def update_product():
        product = product_list.products[current_index[0]]

        # Verificar si la imagen ya está en caché
        if product.thumbnail not in image_cache:
            # Si no está, descargarla y almacenarla en el caché
            r = requests.get(product.thumbnail, stream=True)
            img = Image.open(r.raw)
            img = img.resize((200, 200))
            image_cache[product.thumbnail] = ImageTk.PhotoImage(img)

        # Actualizar la imagen
        image = image_cache[product.thumbnail]
        img_label.config(image=image)
        img_label.image = image  # Necesario para que no se recoja el garbage

        # Actualizar título, precio y descripción
        title2_label.config(text=product.title)
        price_label.config(text=f"Precio: ${product.price:.2f}")
        descr_label.config(text=product.description)

    # Funciones para navegar entre productos
    def next_product():
        if current_index[0] < len(product_list.products) - 1:
            current_index[0] += 1
            update_product()

    def prev_product():
        if current_index[0] > 0:
            current_index[0] -= 1
            update_product()

    # Botón para generar PDF
    def on_generate_pdf():
        generar_pdf(product_list.products)  # Generar PDF con toda la lista de productos

    # Widgets en la ventana principal
    title_label = tk.Label(root, text="Lista de Productos", font=("Arial", 16))
    title_label.pack(pady=10)

    # Botón de búsqueda
    search_button = tk.Button(root, text="Buscar", command=open_search_window)
    search_button.pack()

    img_label = tk.Label(root)
    img_label.pack(pady=(10, 0))

    title2_label = tk.Label(root, font=("Arial", 16))
    title2_label.pack()

    price_label = tk.Label(root, font=("Arial", 14), fg="green")
    price_label.pack()

    descr_label = tk.Label(root, font=("Arial", 12), wraplength=400, justify="left")
    descr_label.pack(pady=(10, 20))

    # Botones de navegación
    prev_button = tk.Button(root, text="Anterior", command=prev_product)
    prev_button.pack(side=tk.LEFT, padx=20)

    next_button = tk.Button(root, text="Siguiente", command=next_product)
    next_button.pack(side=tk.RIGHT, padx=20)

    # Botón para generar PDF
    pdf_button = tk.Button(root, text="Generar PDF", command=on_generate_pdf)
    pdf_button.pack(pady=20)

    # Mostrar el primer producto inicialmente
    update_product()

    root.mainloop()
