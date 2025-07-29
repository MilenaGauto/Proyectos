# Cargar residuos desde archivo
def cargar_residuos(nombre_archivo):
    residuos = {}
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(";")
            if len(partes) == 3:
                nombre, tipo, lugar = partes
                residuos[nombre.lower()] = {"tipo": tipo, "lugar": lugar}
    return residuos

# Guardar residuos desconocidos
def guardar_desconocido(residuo):
    with open("desconocidos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(residuo + "\n")

# Mostrar información del residuo
def clasificar_residuo(residuo, residuos):
    if residuo in residuos:
        print(f"\n👉 Tipo: {residuos[residuo]['tipo']}")
        print(f"📍 Llevar a: {residuos[residuo]['lugar']}\n")
    else:
        print("\n❌ Residuo no reconocido. Por favor, revisá si lo escribiste bien.")
        guardar_desconocido(residuo)

# Programa principal
def main():
    residuos = cargar_residuos("residuos.txt")
    
    print("♻️ Bienvenido al EcoClasificador ♻️")
    print("Escribí 'salir' para terminar.\n")
    
    while True:
        entrada = input("🔍 Ingresá el nombre del residuo: ").lower()
        if entrada == "salir":
            print("\nGracias por usar el EcoClasificador. 🌱")
            break
        clasificar_residuo(entrada, residuos)

# Ejecutar
main()
