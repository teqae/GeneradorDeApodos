import random
import time
from colorama import init, Fore, Style
import os

# Inicializar colorama
init(autoreset=True)

def generar_apodo(nombre, genero, tipo_apodo):
    # Listas de posibles prefijos y sufijos para los diferentes tipos de apodos
    prefijos_cariñoso_hombre = ['Cariño', 'Querido', 'Amor', 'Dulce', 'Lindo', 'Tierno','Cielito', 'Amorcito', 'Bombón', 'Papacito', 'Príncipe', 'Rey', 'Angelito', 'Mi Todo', 'Solcito', 'Osito', 'Maravilloso',
                                'Adorado', 'Dulzón', 'Corazón de Melón', 'Gatito', 'Solesito', 'Estrellita', 'Cariñito', 'Mi Gran Amor', 'Amado', 'Vidita', 'Lucerito', 'Pulgarcito', 'Marido', 'Consentido', 'Pastelito', 'Cosita', 'Amiguito', 'Tiernito',
                                'Diamante', 'Soleado', 'Fresita', 'Mi Rey', 'Principito', 'Ratón', 'Cupido', 'Preciosidad', 'Caracolito', 'Chocolate', 'Amigazo', 'Bambino', 'Amante', 'Amigote', 'Bomboncito', 'Chiquitín', 'Cosote', 'Zorrito', 'Cielo Azul']
    
    
    prefijos_cariñoso_mujer = ['Cariña', 'Querida', 'Amor', 'Dulce', 'Linda', 'Tierna','Cielita',
                               'Amorcita', 'Muñequita', 'Mamacita', 'Princesa', 'Reina', 'Angelita', 'Mi Todo', 'Solecito', 'Osita', 'Maravillosa',
                               'Adorada', 'Dulzura', 'Corazoncito', 'Gatita', 'Solcito', 'Estrellita', 'Cariñito', 'Mi Gran Amor', 'Amada', 'Vidita', 'Lucerito', 'Dulzura', 'Mariposita', 'Consentida', 'Pastelito', 'Princesita',
                               'Amorcito', 'Diamantito', 'Fresita', 'Mi Reina', 'Principita', 'Ratona', 'Cupido', 'Preciosura', 'Caracolito', 'Chocolate', 'Amigaza', 'Bambina', 'Amante', 'Amigota', 'Bomboncita', 'Chiquitina', 'Cosi', 'Zorrita', 'Cielo Rosado']
    prefijos_gracioso_hombre = ['Loco', 'Risueño', 'Chistoso', 'Payaso', 'Travieso', 'Bromista','Chistosito', 'Reidor', 'Payasito', 'Bromazo', 'Burlón',
                                'Travesón', 'Risueñito', 'Juguetón', 'Divertidor', 'Chispeante', 'Festivo', 'Chistocito', 'Locochón', 'Risueñote', 'Risitas', 'Payasete',
                                'Chispeador', 'Juguetón', 'Traviesillo', 'Pícaro', 'Risueñador', 'Festejón', 'Bromazo', 'Chispeador', 'Juguetón', 'Pícaro', 'Bromistón', 'Chispeador',
                                'Risueñón', 'Burlador', 'Divertidón', 'Chispeador', 'Bromazo', 'Travesote', 'Festivo', 'Payasón', 'Divertidazo', 'Bromistón', 'Traviesote', 'Risueñazo', 'Bromistoso', 'Festejador',
                                'Juguetón', 'Bromistón', 'Travesón', 'Risueñote', 'Pillo']
    
    
    prefijos_gracioso_mujer = ['Loca', 'Risueña', 'Chistosa', 'Payasa', 'Traviesa', 'Bromista', 'Chistosita', 'Reidora', 'Payasita', 'Bromaza', 'Burlona',
                               'Traviesilla', 'Risueñita', 'Juguetona', 'Divertidora', 'Chispeante', 'Festiva', 'Chistocita', 'Locochona', 'Risueñota', 'Risitas', 'Payasita', 'Chispeadora', 'Juguetona',
                               'Traviesilla', 'Pícara', 'Risueñadora', 'Festejona', 'Bromaza', 'Chispeadora', 'Juguetona', 'Pícara', 'Bromista', 'Chispeadora', 'Risueñona', 'Burladora', 'Divertida', 'Chispeadora', 'Bromaza', 'Traviesota',
                               'Festiva', 'Payasa', 'Divertida', 'Bromista', 'Traviesota', 'Risueñaza', 'Bromistosa', 'Festejadora', 'Juguetona', 'Bromista', 'Traviesilla', 'Risueñota', 'Pilla']

    prefijos_amoroso_hombre = ['Mi Vida', 'Mi Amor', 'Mi Corazón', 'Mi Tesoro', 'Mi Cielo', 'Mi Media Naranja','Mi Adorado', 'Mi Amoroso', 'Mi Dulce', 'Mi Querido', 'Mi Hermoso', 'Mi Maravilloso', 'Mi Fantástico', 'Mi Soñado', 'Mi Querubín',
                               'Mi Encantador', 'Mi Apasionado', 'Mi Apreciado', 'Mi Deseado', 'Mi Devoto', 'Mi Admirado', 'Mi Anhelado', 'Mi Idolatrado', 'Mi Querido', 'Mi Querido', 'Mi Almejado', 'Mi Hechizado', 'Mi Adorado', 'Mi Fantaseado',
                               'Mi Dulce Pecado', 'Mi Fervoroso', 'Mi Hechicero', 'Mi Obsesionado', 'Mi Amante', 'Mi Aficionado', 'Mi Hechizado', 'Mi Obsesionado', 'Mi Amante', 'Mi Aficionado', 'Mi Protector', 'Mi Amigo', 'Mi Enamorado', 'Mi Cautivador',
                               'Mi Soñador', 'Mi Esclavo', 'Mi Idóneo', 'Mi Irresistible', 'Mi Apegado', 'Mi Atractivo', 'Mi Fidelísimo', 'Mi Fascinado', 'Mi Atraído', 'Mi Subyugado', 'Mi Apasionado', 'Mi Despampanante', 'Mi Deseado', 'Mi Ardiente']
    sufijos_amoroso_hombre = ['eterno <3', 'de mi vida <3', 'amado <3', 'de mi corazon <3', 'de mis sueños <3']
    
    
    prefijos_amoroso_mujer = ['Mi Vida', 'Mi Amor', 'Mi Corazón', 'Mi Tesoro', 'Mi Querida', 'Mi Media Naranja','Mi Adorada', 'Mi Amorosa', 'Mi Dulce', 'Mi Querida', 'Mi Hermosa', 'Mi Maravillosa', 'Mi Fantástica', 'Mi Soñada',
                              'Mi Querubina', 'Mi Encantadora', 'Mi Apasionada', 'Mi Apreciada', 'Mi Deseada', 'Mi Devota', 'Mi Admirada', 'Mi Anhelada', 'Mi Idolatrada', 'Mi Querida', 'Mi Querida', 'Mi Almejada', 'Mi Hechizada',
                              'Mi Adorada', 'Mi Fantaseada', 'Mi Dulce Pecado', 'Mi Fervorosa', 'Mi Hechicera', 'Mi Obsesionada', 'Mi Amante', 'Mi Aficionada', 'Mi Hechizada', 'Mi Obsesionada', 'Mi Amante', 'Mi Aficionada', 'Mi Protectora',
                              'Mi Amiga', 'Mi Enamorada', 'Mi Cautivadora', 'Mi Soñadora', 'Mi Esclava', 'Mi Idónea', 'Mi Irresistible', 'Mi Apegada', 'Mi Atractiva', 'Mi Fidelísima', 'Mi Fascinada', 'Mi Atraída', 'Mi Subyugada', 'Mi Apasionada',
                              'Mi Despampanante', 'Mi Deseada', 'Mi Ardiente']
    sufijos_amoroso_mujer = ['eterna <3', 'de mi vida <3', 'amada <3', 'amorosa <3', 'de mis sueños <3']

    insultos_hombre = ['Tonto', 'Despistado', 'Inútil', 'Molesto', 'Torpe', 'Perezoso', 'Fastidioso', 'Cargoso']
    insultos_mujer = ['Tonta', 'Despistada', 'Inútil', 'Molesta', 'Torpe', 'Perezosa', 'Fastidiosa', 'Cargosa']

    # Lógica para el tipo de apodo "cariñoso"
    if tipo_apodo == 'cariñoso':
        if genero == 'hombre':
            prefijo = random.choice(prefijos_cariñoso_hombre)
        elif genero == 'mujer':
            prefijo = random.choice(prefijos_cariñoso_mujer)
        else:
            return "Género no reconocido"

    # Lógica para el tipo de apodo "gracioso"
    elif tipo_apodo == 'gracioso':
        if genero == 'hombre':
            prefijo = random.choice(prefijos_gracioso_hombre)
        elif genero == 'mujer':
            prefijo = random.choice(prefijos_gracioso_mujer)
        else:
            return "Género no reconocido"

    # Lógica para el tipo de apodo "amoroso"
    elif tipo_apodo == 'amoroso':
        if genero == 'hombre':
            prefijo = random.choice(prefijos_amoroso_hombre)
            sufijo = random.choice(sufijos_amoroso_hombre)
        elif genero == 'mujer':
            prefijo = random.choice(prefijos_amoroso_mujer)
            sufijo = random.choice(sufijos_amoroso_mujer)
        else:
            return "Género no reconocido"

    # Lógica para el tipo de apodo "insulto"
    elif tipo_apodo == 'insulto':
        if genero == 'hombre':
            prefijo = random.choice(insultos_hombre)
        elif genero == 'mujer':
            prefijo = random.choice(insultos_mujer)
        else:
            return "Género no reconocido"
        sufijo = ""

    else:
        return "Tipo de apodo no reconocido"

    return f'{prefijo} {nombre}'

# Animación del mensaje de bienvenida al generador de apodos
mensaje_bienvenida = "¡Bienvenido al Generador de Apodos!"
espacios_inicio = " " * ((80 - len(mensaje_bienvenida)) // 2)

while True:
    for i in range(len(espacios_inicio) + 1):
        print(Fore.GREEN + espacios_inicio[:i] + mensaje_bienvenida, end='\r')
        time.sleep(0.05)

    print("\n\n")

    # Solicitar al usuario que ingrese su nombre, género y tipo de apodo
    nombre = input(Fore.CYAN + "• Ingresa tu nombre: ")
    genero = input(Fore.YELLOW + "• Ingresa tu género (hombre/mujer): ").lower()
    tipo_apodo = input(Fore.CYAN + "• Selecciona el tipo de apodo (cariñoso/gracioso/amoroso/insulto): ").lower()

    # Generar el apodo
    apodo = generar_apodo(nombre, genero, tipo_apodo)

    # Animar el apodo letra por letra con color
    print("Generando apodo...")
    for letra in apodo:
        print(Fore.YELLOW + letra, end='', flush=True)
        time.sleep(0.1)
    print()

    print(Fore.GREEN + f'\nTu apodo es: {apodo}')

    # Preguntar al usuario si desea volver o salir
    opcion = input(Fore.CYAN + "¿Desea volver (v) o salir (s)? ").lower()
    if opcion == 'v':
        # El usuario desea volver, el bucle volverá al inicio
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    elif opcion == 's':
        # El usuario desea salir, se muestra un mensaje de despedida y se rompe el bucle
        print("¡Hasta luego! Gracias por usar el Generador de Apodos.")
        break
    else:
        print("Opción no válida. Saliendo del programa.")
