# main.py
import tkinter as tk
from tkinter import ttk, messagebox
from datos import menu, selector_de_precios

class RestauranteApp:
    def __init__(self, root):
        """
        Constructor de la clase.
        Se ejecuta automáticamente al crear la aplicación.
        'self' es como 'this' en otros lenguajes.
        """
        self.root = root
        self.root.title("🍽️ Menú Digital - Restaurante")
        self.root.geometry("900x700")
        self.root.configure(bg='#f5f5f5')
        
        # Diccionario para almacenar el pedido actual
        # Estructura: {"bebidas": ["Café Americano"], "almuerzos": ["Pasta Carbonara"]}
        self.pedido = {
            "bebidas": [],
            "desayunos": [],
            "almuerzos": [],
            "acompanantes": []
        }
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea todos los elementos visuales de la ventana"""
        
        # ========== TÍTULO PRINCIPAL ==========
        titulo = tk.Label(
            self.root,
            text="🍽️ Menú Digital",
            font=("Helvetica", 24, "bold"),
            bg='#f5f5f5',
            fg='#2c3e50'
        )
        titulo.pack(pady=20)
        
        # ========== NOTEBOOK (PESTAÑAS) ==========
        # ttk.Notebook crea un contenedor con pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Crear una pestaña por cada categoría
        for categoria in menu["productos"].keys():
            self.crear_pestaña(categoria)
        
        # ========== PANEL INFERIOR (PEDIDO Y TOTAL) ==========
        panel_inferior = tk.Frame(self.root, bg='#ecf0f1', relief='raised', bd=2)
        panel_inferior.pack(fill='x', padx=20, pady=10)
        
        # Botón para ver el pedido
        btn_ver_pedido = tk.Button(
            panel_inferior,
            text="📋 Ver Pedido Actual",
            command=self.mostrar_pedido,
            bg='#3498db',
            fg='white',
            font=("Helvetica", 12, "bold"),
            padx=20,
            pady=10,
            cursor='hand2'
        )
        btn_ver_pedido.pack(side='left', padx=10, pady=10)
        
        # Botón para calcular total
        btn_calcular = tk.Button(
            panel_inferior,
            text="💰 Calcular Total",
            command=self.calcular_y_mostrar,
            bg='#27ae60',
            fg='white',
            font=("Helvetica", 12, "bold"),
            padx=20,
            pady=10,
            cursor='hand2'
        )
        btn_calcular.pack(side='left', padx=10, pady=10)
        
        # Botón para limpiar pedido
        btn_limpiar = tk.Button(
            panel_inferior,
            text="🗑️ Limpiar Pedido",
            command=self.limpiar_pedido,
            bg='#e74c3c',
            fg='white',
            font=("Helvetica", 12, "bold"),
            padx=20,
            pady=10,
            cursor='hand2'
        )
        btn_limpiar.pack(side='left', padx=10, pady=10)
    
    def crear_pestaña(self, categoria):
        """
        Crea una pestaña para cada categoría del menú.
        
        Args:
            categoria (str): Nombre de la categoría ("bebidas", "desayunos", etc.)
        """
        # Frame = contenedor rectangular
        frame = tk.Frame(self.notebook, bg='white')
        self.notebook.add(frame, text=f"  {categoria.upper()}  ")
        
        # Canvas + Scrollbar para que se pueda hacer scroll
        canvas = tk.Canvas(frame, bg='white')
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        frame_scrollable = tk.Frame(canvas, bg='white')
        
        frame_scrollable.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=frame_scrollable, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Recorrer todos los productos de esta categoría
        for producto in menu["productos"][categoria]:
            self.crear_tarjeta_producto(frame_scrollable, categoria, producto)
    
    def crear_tarjeta_producto(self, parent, categoria, producto):
        """
        Crea una tarjeta visual para cada producto.
        
        Args:
            parent: El contenedor donde se colocará la tarjeta
            categoria (str): Categoría del producto
            producto (dict): Diccionario con nombre, descripción y precio
        """
        # Frame de la tarjeta con bordes
        tarjeta = tk.Frame(
            parent,
            bg='#ffffff',
            relief='ridge',
            bd=2,
            highlightbackground='#bdc3c7',
            highlightthickness=1
        )
        tarjeta.pack(fill='x', padx=15, pady=10)
        
        # Nombre del producto
        nombre = tk.Label(
            tarjeta,
            text=producto["nombre"],
            font=("Helvetica", 14, "bold"),
            bg='white',
            fg='#2c3e50',
            anchor='w'
        )
        nombre.pack(fill='x', padx=10, pady=(10, 5))
        
        # Descripción
        descripcion = tk.Label(
            tarjeta,
            text=producto["descripcion"],
            font=("Helvetica", 10),
            bg='white',
            fg='#7f8c8d',
            anchor='w',
            wraplength=600,  # Ajusta el texto si es muy largo
            justify='left'
        )
        descripcion.pack(fill='x', padx=10, pady=5)
        
        # Frame inferior con precio y botón
        frame_inferior = tk.Frame(tarjeta, bg='white')
        frame_inferior.pack(fill='x', padx=10, pady=10)
        
        # Precio
        precio_label = tk.Label(
            frame_inferior,
            text=f"${producto['precio']:.2f}",
            font=("Helvetica", 16, "bold"),
            bg='white',
            fg='#27ae60'
        )
        precio_label.pack(side='left')
        
        # Botón para agregar al pedido
        # lambda: función anónima que se ejecuta al hacer clic
        btn_agregar = tk.Button(
            frame_inferior,
            text="➕ Agregar",
            command=lambda: self.agregar_producto(categoria, producto["nombre"]),
            bg='#3498db',
            fg='white',
            font=("Helvetica", 10, "bold"),
            padx=15,
            pady=5,
            cursor='hand2'
        )
        btn_agregar.pack(side='right')
    
    def agregar_producto(self, categoria, nombre_producto):
        """
        Agrega un producto al pedido actual.
        
        Args:
            categoria (str): Categoría del producto
            nombre_producto (str): Nombre del producto
        """
        self.pedido[categoria].append(nombre_producto)
        messagebox.showinfo(
            "✅ Producto Agregado",
            f"'{nombre_producto}' agregado al pedido"
        )
    
    def mostrar_pedido(self):
        """Muestra el pedido actual en una ventana emergente"""
        if not any(self.pedido.values()):  # Si el pedido está vacío
            messagebox.showwarning("Pedido Vacío", "No has agregado ningún producto")
            return
        
        # Crear ventana nueva
        ventana = tk.Toplevel(self.root)
        ventana.title("📋 Pedido Actual")
        ventana.geometry("500x600")
        ventana.configure(bg='white')
        
        # Título
        tk.Label(
            ventana,
            text="Tu Pedido",
            font=("Helvetica", 18, "bold"),
            bg='white'
        ).pack(pady=20)
        
        # Text widget con scrollbar
        frame_texto = tk.Frame(ventana, bg='white')
        frame_texto.pack(fill='both', expand=True, padx=20, pady=10)
        
        scrollbar = ttk.Scrollbar(frame_texto)
        scrollbar.pack(side='right', fill='y')
        
        texto = tk.Text(
            frame_texto,
            font=("Courier", 11),
            bg='#f8f9fa',
            yscrollcommand=scrollbar.set,
            wrap='word'
        )
        texto.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=texto.yview)
        
        # Llenar el texto con los productos
        for categoria, productos in self.pedido.items():
            if productos:
                texto.insert('end', f"\n{'='*40}\n")
                texto.insert('end', f"  {categoria.upper()}\n")
                texto.insert('end', f"{'='*40}\n")
                for i, prod in enumerate(productos, 1):
                    precio = selector_de_precios(categoria, prod)
                    texto.insert('end', f"{i}. {prod} - ${precio:.2f}\n")
        
        texto.config(state='disabled')  # Solo lectura
    
    def calcular_y_mostrar(self):
        """Calcula el total del pedido y lo muestra"""
        if not any(self.pedido.values()):
            messagebox.showwarning("Pedido Vacío", "No has agregado ningún producto")
            return
        
        total = self.calcular_total()
        
        # Ventana de resultado
        ventana = tk.Toplevel(self.root)
        ventana.title("💰 Total del Pedido")
        ventana.geometry("400x300")
        ventana.configure(bg='#2c3e50')
        
        tk.Label(
            ventana,
            text="Total a Pagar",
            font=("Helvetica", 20, "bold"),
            bg='#2c3e50',
            fg='white'
        ).pack(pady=30)
        
        tk.Label(
            ventana,
            text=f"${total:.2f}",
            font=("Helvetica", 48, "bold"),
            bg='#2c3e50',
            fg='#2ecc71'
        ).pack(pady=20)
        
        tk.Label(
            ventana,
            text="(IVA 16% y Servicio 10% incluidos)",
            font=("Helvetica", 10),
            bg='#2c3e50',
            fg='#95a5a6'
        ).pack()
    
    def calcular_total(self):
        """
        Calcula el total del pedido con IVA y servicio.
        (Copiado de tu código original)
        """
        subtotal = 0.0
        for categoria, productos in self.pedido.items():
            for producto in productos:
                precio = selector_de_precios(categoria, producto)
                if isinstance(precio, (int, float)):
                    subtotal += precio
        
        IVA = 0.16
        SERVICIO = 0.10
        total = subtotal * (1 + IVA + SERVICIO)
        return total
    
    def limpiar_pedido(self):
        """Vacía el pedido actual"""
        respuesta = messagebox.askyesno(
            "Confirmar",
            "¿Estás seguro de limpiar el pedido?"
        )
        if respuesta:
            for categoria in self.pedido:
                self.pedido[categoria] = []
            messagebox.showinfo("✅ Listo", "Pedido limpiado")


# ========== EJECUCIÓN DEL PROGRAMA ==========
if __name__ == "__main__":
    root = tk.Tk()  # Crear ventana principal
    app = RestauranteApp(root)  # Crear la aplicación
    root.mainloop()  # Mantener la ventana abierta