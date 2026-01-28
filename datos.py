# Aprovechamos el uso de JSON para almacenar y cargar los datos del menu.
import json

menu = {
    "productos": {
        "bebidas": [
            {
                "nombre": "Jugo Natural de Lulo",
                "descripcion": "Refrescante jugo de fruta tropical recién exprimido.",
                "precio": 3.50
            },
            {
                "nombre": "Limonada de Coco",
                "descripcion": "Mezcla cremosa de limón fresco y leche de coco.",
                "precio": 4.50
            },
            {
                "nombre": "Café Americano",
                "descripcion": "Grano premium seleccionado con tueste medio.",
                "precio": 2.00
            },
            {
                "nombre": "Té Frío de la Casa",
                "descripcion": "Té negro con infusión de frutos rojos y menta.",
                "precio": 2.75
            },
            {
                "nombre": "Batido de Proteína",
                "descripcion": "Plátano, avena y mantequilla de maní.",
                "precio": 5.00
            }
        ],
        "desayunos": [
            {
                "nombre": "Desayuno Tradicional",
                "descripcion": "Dos huevos al gusto, arepa con queso y chocolate caliente.",
                "precio": 7.50
            },
            {
                "nombre": "Tostadas Francesas",
                "descripcion": "Pan brioche con miel de maple y frutos del bosque.",
                "precio": 8.00
            },
            {
                "nombre": "Omelette Vegetariano",
                "descripcion": "Claras de huevo con espinaca, champiñones y pimentón.",
                "precio": 7.00
            },
            {
                "nombre": "Bowl de Acaí",
                "descripcion": "Base de acaí orgánico con granola artesanal y coco rallado.",
                "precio": 9.50
            }
        ],
        "almuerzos": [
            {
                "nombre": "Bowl de Pollo Teriyaki",
                "descripcion": "Pechuga a la plancha, arroz jazmín y vegetales salteados.",
                "precio": 12.00
            },
            {
                "nombre": "Pasta Carbonara",
                "descripcion": "Pasta larga en salsa de crema, tocineta crocante y parmesano.",
                "precio": 11.50
            },
            {
                "nombre": "Hamburguesa Artesanal",
                "descripcion": "Carne de res (200g), queso cheddar, cebolla caramelizada y pan brioche.",
                "precio": 13.00
            },
            {
                "nombre": "Salmón a las Hierbas",
                "descripcion": "Filete de salmón sellado con costra de finas hierbas.",
                "precio": 16.50
            },
            {
                "nombre": "Ensalada César con Camarones",
                "descripcion": "Lechuga romana, crotones, aderezo césar y camarones al grill.",
                "precio": 14.00
            }
        ],
        "acompanantes": [
            {
                "nombre": "Papas Nativas",
                "descripcion": "Papas rústicas sazonadas con sal de mar y romero.",
                "precio": 3.00
            },
            {
                "nombre": "Arroz Blanco",
                "descripcion": "Porción de arroz esponjoso cocinado al vapor.",
                "precio": 2.00
            },
            {
                "nombre": "Plátano Madurito",
                "descripcion": "Tajadas de plátano frito con un toque de queso rallado.",
                "precio": 2.50
            },
            {
                "nombre": "Vegetales al Wok",
                "descripcion": "Zucchini, brócoli y zanahoria salteados con soya.",
                "precio": 4.00
            }
        ]
    }
}

def selector_de_precios(categoria, producto):
    """Función para obtener el precio de un producto dado su categoría y nombre."""
    try:
        for item in menu["productos"][categoria]:
            if item["nombre"] == producto:
                return item["precio"]
        return "Producto no encontrado en la categoría especificada."
    except KeyError:
        return "Categoría no válida."