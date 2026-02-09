# main.py
# Este es el archivo principal de nuestro programa

# Importamos las librerías que necesitamos
import tkinter as tk  # Para crear ventanas y botones
from tkinter import messagebox  # Para mostrar mensajes emergentes
from datos import menu, selector_de_precios  # Importamos el menú desde datos.py


# Esta es nuestra aplicación principal
class RestauranteApp:
    
    def __init__(self, root):
        """
        Esta función se ejecuta automáticamente cuando arranca el programa.
        Aquí preparamos todo lo necesario.
        """
        self.root = root  # Guardamos la ventana principal
        self.root.title("Menú Digital - Restaurante")  # Título de la ventana
        self.root.geometry("800x600")  # Tamaño: 800 pixeles ancho x 600 alto
        self.root.configure(bg='#f0f0f0')  # Color de fondo gris claro
        
        # Variable para guardar el nombre del cliente
        self.nombre_cliente = ""
        
        # Diccionario (como una lista organizada) para guardar el pedido
        # Ejemplo: {"bebidas": ["Café"], "almuerzos": ["Pasta"]}
        self.pedido = {
            "bebidas": [],
            "desayunos": [],
            "almuerzos": [],
            "acompanantes": []
        }
        
        # Primero pedimos el nombre
        self.pedir_nombre()
    
    
    def pedir_nombre(self):
        """
        Esta función crea una ventana pequeña para pedir el nombre del cliente.
        """
        # Crear una ventana nueva (pequeña y centrada)
        ventana_nombre = tk.Toplevel(self.root)
        ventana_nombre.title("Bienvenido")
        ventana_nombre.geometry("400x250")
        ventana_nombre.configure(bg='white')
        
        # Hacer que esta ventana esté siempre al frente
        ventana_nombre.grab_set()
        
        # Título de bienvenida
        titulo = tk.Label(
            ventana_nombre,
            text="🍽️ Bienvenido al Restaurante",
            font=("Arial", 16, "bold"),
            bg='white',
            fg='#333333'
        )
        titulo.pack(pady=30)
        
        # Texto que dice "Por favor ingresa tu nombre"
        instruccion = tk.Label(
            ventana_nombre,
            text="Por favor, ingresa tu nombre:",
            font=("Arial", 12),
            bg='white'
        )
        instruccion.pack(pady=10)
        
        # Caja de texto donde el usuario escribe su nombre
        self.entrada_nombre = tk.Entry(
            ventana_nombre,
            font=("Arial", 14),
            width=25,
            justify='center'
        )
        self.entrada_nombre.pack(pady=10)
        self.entrada_nombre.focus()  # El cursor aparece aquí automáticamente
        
        # Botón para confirmar
        boton_confirmar = tk.Button(
            ventana_nombre,
            text="Continuar",
            command=lambda: self.guardar_nombre(ventana_nombre),
            bg='#4CAF50',
            fg='white',
            font=("Arial", 12, "bold"),
            width=15,
            cursor='hand2'
        )
        boton_confirmar.pack(pady=20)
        
        # Permitir presionar Enter para continuar
        self.entrada_nombre.bind('<Return>', lambda e: self.guardar_nombre(ventana_nombre))
    
    
    def guardar_nombre(self, ventana):
        """
        Guarda el nombre que escribió el usuario y cierra la ventana de bienvenida.
        """
        nombre = self.entrada_nombre.get()  # Obtener el texto escrito
        
        # Verificar que el usuario escribió algo
        if nombre.strip() == "":  # strip() quita espacios en blanco
            messagebox.showwarning("Error", "Por favor escribe tu nombre")
            return
        
        # Guardar el nombre
        self.nombre_cliente = nombre.strip()
        
        # Cerrar la ventana de nombre
        ventana.destroy()
        
        # Ahora sí, crear el menú principal
        self.crear_menu()
    
    
    def crear_menu(self):
        """
        Esta función crea todo el menú principal del restaurante.
        """
        # ========== TÍTULO CON NOMBRE DEL CLIENTE ==========
        titulo = tk.Label(
            self.root,
            text=f"🍽️ Menú Digital - Cliente: {self.nombre_cliente}",
            font=("Arial", 18, "bold"),
            bg='#f0f0f0',
            fg='#333333'
        )
        titulo.pack(pady=20)
        
        # ========== FRAME PARA EL MENÚ (área donde se muestran los productos) ==========
        # Frame es como una caja contenedora
        frame_menu = tk.Frame(self.root, bg='white')
        frame_menu.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Crear Canvas (área con scroll) para ver todos los productos
        canvas = tk.Canvas(frame_menu, bg='white')
        scrollbar = tk.Scrollbar(frame_menu, orient="vertical", command=canvas.yview)
        
        # Frame que va dentro del canvas
        self.frame_productos = tk.Frame(canvas, bg='white')
        
        # Configurar el scroll
        self.frame_productos.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.frame_productos, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Colocar canvas y scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # ========== MOSTRAR TODOS LOS PRODUCTOS ==========
        self.mostrar_productos()
        
        # ========== BOTONES INFERIORES ==========
        frame_botones = tk.Frame(self.root, bg='#e0e0e0')
        frame_botones.pack(fill='x', padx=20, pady=15)
        
        # Botón: Ver mi pedido
        boton_ver = tk.Button(
            frame_botones,
            text="📋 Ver Mi Pedido",
            command=self.ver_pedido,
            bg='#2196F3',
            fg='white',
            font=("Arial", 11, "bold"),
            width=18,
            height=2,
            cursor='hand2'
        )
        boton_ver.pack(side='left', padx=5)
        
        # Botón: Calcular Total
        boton_calcular = tk.Button(
            frame_botones,
            text="💰 Calcular Total",
            command=self.calcular_total,
            bg='#4CAF50',
            fg='white',
            font=("Arial", 11, "bold"),
            width=18,
            height=2,
            cursor='hand2'
        )
        boton_calcular.pack(side='left', padx=5)
        
        # Botón: Limpiar Pedido
        boton_limpiar = tk.Button(
            frame_botones,
            text="🗑️ Limpiar Pedido",
            command=self.limpiar_pedido,
            bg='#f44336',
            fg='white',
            font=("Arial", 11, "bold"),
            width=18,
            height=2,
            cursor='hand2'
        )
        boton_limpiar.pack(side='left', padx=5)
    
    
    def mostrar_productos(self):
        """
        Esta función muestra todos los productos del menú organizados por categoría.
        """
        # Recorrer cada categoría (bebidas, desayunos, almuerzos, acompañantes)
        for categoria in menu["productos"]:
            
            # ===== TÍTULO DE LA CATEGORÍA =====
            titulo_categoria = tk.Label(
                self.frame_productos,
                text=f"═══ {categoria.upper()} ═══",
                font=("Arial", 14, "bold"),
                bg='white',
                fg='#1976D2'
            )
            titulo_categoria.pack(pady=(20, 10))
            
            # Recorrer cada producto dentro de esta categoría
            for producto in menu["productos"][categoria]:
                self.crear_tarjeta(categoria, producto)
    
    
    def crear_tarjeta(self, categoria, producto):
        """
        Crea una tarjeta bonita para cada producto.
        
        Parámetros:
        - categoria: nombre de la categoría (ej: "bebidas")
        - producto: diccionario con nombre, descripción y precio
        """
        # Frame = caja contenedora para cada producto
        tarjeta = tk.Frame(
            self.frame_productos,
            bg='#fafafa',
            relief='solid',
            bd=1
        )
        tarjeta.pack(fill='x', padx=15, pady=8)
        
        # ===== NOMBRE DEL PRODUCTO =====
        nombre_label = tk.Label(
            tarjeta,
            text=producto["nombre"],
            font=("Arial", 12, "bold"),
            bg='#fafafa',
            fg='#212121',
            anchor='w'
        )
        nombre_label.pack(fill='x', padx=10, pady=(8, 2))
        
        # ===== DESCRIPCIÓN =====
        descripcion_label = tk.Label(
            tarjeta,
            text=producto["descripcion"],
            font=("Arial", 9),
            bg='#fafafa',
            fg='#666666',
            anchor='w',
            wraplength=500,
            justify='left'
        )
        descripcion_label.pack(fill='x', padx=10, pady=2)
        
        # ===== FRAME PARA PRECIO Y BOTÓN =====
        frame_abajo = tk.Frame(tarjeta, bg='#fafafa')
        frame_abajo.pack(fill='x', padx=10, pady=(5, 8))
        
        # Precio
        precio_label = tk.Label(
            frame_abajo,
            text=f"${producto['precio']:.2f}",
            font=("Arial", 14, "bold"),
            bg='#fafafa',
            fg='#4CAF50'
        )
        precio_label.pack(side='left')
        
        # Botón "Agregar"
        # lambda es una función pequeña que se ejecuta al hacer clic
        boton_agregar = tk.Button(
            frame_abajo,
            text="+ Agregar",
            command=lambda: self.agregar_al_pedido(categoria, producto["nombre"]),
            bg='#2196F3',
            fg='white',
            font=("Arial", 9, "bold"),
            cursor='hand2',
            width=12
        )
        boton_agregar.pack(side='right')
    
    
    def agregar_al_pedido(self, categoria, nombre_producto):
        """
        Agrega un producto a la lista del pedido.
        
        Parámetros:
        - categoria: la categoría del producto (ej: "bebidas")
        - nombre_producto: el nombre del producto (ej: "Café Americano")
        """
        # Agregar el producto a la lista
        self.pedido[categoria].append(nombre_producto)
        
        # Mostrar mensaje de confirmación
        messagebox.showinfo(
            "Producto Agregado",
            f"✅ '{nombre_producto}' agregado a tu pedido"
        )
    
    
    def ver_pedido(self):
        """
        Muestra una ventana con todos los productos que el cliente ha pedido.
        """
        # Verificar si hay productos en el pedido
        tiene_productos = False
        for productos in self.pedido.values():
            if len(productos) > 0:
                tiene_productos = True
                break
        
        if not tiene_productos:
            messagebox.showwarning(
                "Pedido Vacío",
                "Aún no has agregado ningún producto"
            )
            return
        
        # ===== CREAR VENTANA NUEVA =====
        ventana = tk.Toplevel(self.root)
        ventana.title("Mi Pedido")
        ventana.geometry("500x550")
        ventana.configure(bg='white')
        
        # Título
        titulo = tk.Label(
            ventana,
            text=f"📋 Pedido de {self.nombre_cliente}",
            font=("Arial", 16, "bold"),
            bg='white',
            fg='#333333'
        )
        titulo.pack(pady=20)
        
        # ===== ÁREA DE TEXTO CON SCROLL =====
        frame_texto = tk.Frame(ventana, bg='white')
        frame_texto.pack(fill='both', expand=True, padx=20, pady=10)
        
        scrollbar = tk.Scrollbar(frame_texto)
        scrollbar.pack(side='right', fill='y')
        
        texto = tk.Text(
            frame_texto,
            font=("Courier", 10),
            bg='#f9f9f9',
            yscrollcommand=scrollbar.set,
            wrap='word',
            height=20
        )
        texto.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=texto.yview)
        
        # ===== LLENAR CON LOS PRODUCTOS =====
        subtotal = 0
        
        for categoria in self.pedido:
            productos = self.pedido[categoria]
            
            if len(productos) > 0:  # Si hay productos en esta categoría
                # Escribir el título de la categoría
                texto.insert('end', f"\n{'='*45}\n")
                texto.insert('end', f"  {categoria.upper()}\n")
                texto.insert('end', f"{'='*45}\n")
                
                # Escribir cada producto
                contador = 1
                for prod in productos:
                    precio = selector_de_precios(categoria, prod)
                    texto.insert('end', f"{contador}. {prod}\n")
                    texto.insert('end', f"   Precio: ${precio:.2f}\n\n")
                    subtotal = subtotal + precio
                    contador = contador + 1
        
        # ===== MOSTRAR SUBTOTAL =====
        texto.insert('end', f"\n{'='*45}\n")
        texto.insert('end', f"SUBTOTAL: ${subtotal:.2f}\n")
        texto.insert('end', f"{'='*45}\n")
        
        # Hacer que no se pueda editar el texto
        texto.config(state='disabled')
        
        # Botón para cerrar
        boton_cerrar = tk.Button(
            ventana,
            text="Cerrar",
            command=ventana.destroy,
            bg='#757575',
            fg='white',
            font=("Arial", 10, "bold"),
            width=15
        )
        boton_cerrar.pack(pady=15)
    
    
    def calcular_total(self):
        """
        Calcula el total del pedido (con IVA y servicio) y lo muestra.
        """
        # Verificar que haya productos
        tiene_productos = False
        for productos in self.pedido.values():
            if len(productos) > 0:
                tiene_productos = True
                break
        
        if not tiene_productos:
            messagebox.showwarning(
                "Pedido Vacío",
                "Debes agregar productos primero"
            )
            return
        
        # ===== CALCULAR SUBTOTAL =====
        subtotal = 0
        for categoria in self.pedido:
            for producto in self.pedido[categoria]:
                precio = selector_de_precios(categoria, producto)
                subtotal = subtotal + precio
        
        # ===== CALCULAR IVA Y SERVICIO =====
        iva = subtotal * 0.16  # 16% de IVA
        servicio = subtotal * 0.10  # 10% de servicio
        total = subtotal + iva + servicio
        
        # ===== CREAR VENTANA DE RESULTADO =====
        ventana = tk.Toplevel(self.root)
        ventana.title("Total a Pagar")
        ventana.geometry("450x400")
        ventana.configure(bg='#263238')
        
        # Título
        tk.Label(
            ventana,
            text=f"Cliente: {self.nombre_cliente}",
            font=("Arial", 14, "bold"),
            bg='#263238',
            fg='#B0BEC5'
        ).pack(pady=(20, 10))
        
        # Línea separadora
        tk.Label(
            ventana,
            text="─" * 40,
            bg='#263238',
            fg='#546E7A'
        ).pack()
        
        # Subtotal
        tk.Label(
            ventana,
            text=f"Subtotal: ${subtotal:.2f}",
            font=("Arial", 12),
            bg='#263238',
            fg='white'
        ).pack(pady=10)
        
        # IVA
        tk.Label(
            ventana,
            text=f"IVA (16%): ${iva:.2f}",
            font=("Arial", 12),
            bg='#263238',
            fg='white'
        ).pack(pady=5)
        
        # Servicio
        tk.Label(
            ventana,
            text=f"Servicio (10%): ${servicio:.2f}",
            font=("Arial", 12),
            bg='#263238',
            fg='white'
        ).pack(pady=5)
        
        # Línea separadora
        tk.Label(
            ventana,
            text="─" * 40,
            bg='#263238',
            fg='#546E7A'
        ).pack(pady=10)
        
        # TOTAL GRANDE
        tk.Label(
            ventana,
            text="TOTAL A PAGAR",
            font=("Arial", 14, "bold"),
            bg='#263238',
            fg='#B0BEC5'
        ).pack(pady=5)
        
        tk.Label(
            ventana,
            text=f"${total:.2f}",
            font=("Arial", 36, "bold"),
            bg='#263238',
            fg='#4CAF50'
        ).pack(pady=10)
        
        # Botón cerrar
        tk.Button(
            ventana,
            text="Cerrar",
            command=ventana.destroy,
            bg='#546E7A',
            fg='white',
            font=("Arial", 11, "bold"),
            width=15
        ).pack(pady=20)
    
    
    def limpiar_pedido(self):
        """
        Borra todos los productos del pedido actual.
        """
        # Preguntar si está seguro
        respuesta = messagebox.askyesno(
            "Confirmar",
            "¿Estás seguro de limpiar todo el pedido?"
        )
        
        if respuesta:  # Si hizo clic en "Sí"
            # Vaciar todas las listas
            self.pedido["bebidas"] = []
            self.pedido["desayunos"] = []
            self.pedido["almuerzos"] = []
            self.pedido["acompanantes"] = []
            
            messagebox.showinfo("Listo", "✅ Pedido limpiado correctamente")


# ========== AQUÍ EMPIEZA EL PROGRAMA ==========
if __name__ == "__main__":
    # Crear la ventana principal
    ventana_principal = tk.Tk()
    
    # Crear la aplicación
    app = RestauranteApp(ventana_principal)
    
    # Mantener la ventana abierta (ciclo infinito hasta que se cierre)
    ventana_principal.mainloop()