import geopy.distance
import requests

# Diccionario de coordenadas de algunas ciudades de Chile y Argentina
cities = {
    "Santiago": {"country": "Chile", "coords": (-33.4489, -70.6693)},
    "Buenos Aires": {"country": "Argentina", "coords": (-34.6037, -58.3816)},
    "Valparaíso": {"country": "Chile", "coords": (-33.0472, -71.6127)},
    "Mendoza": {"country": "Argentina", "coords": (-32.8908, -68.8272)}
}

# Función para obtener la distancia entre dos ciudades
def get_distance(city1, city2):
    coords_1 = cities[city1]["coords"]
    coords_2 = cities[city2]["coords"]
    distance_km = geopy.distance.geodesic(coords_1, coords_2).km
    distance_miles = geopy.distance.geodesic(coords_1, coords_2).miles
    return distance_km, distance_miles

# Función para calcular la duración del viaje según el medio de transporte
def get_travel_time(distance_km, transport):
    speeds = {
        "auto": 80,  # km/h
        "bus": 60,  # km/h
        "avion": 800  # km/h
    }
    travel_time = distance_km / speeds[transport]
    return travel_time

# Función principal
def main():
    while True:
        print("Ingrese la Ciudad de Origen (o 's' para salir):")
        origin = input().strip()
        if origin.lower() == 's':
            break

        print("Ingrese la Ciudad de Destino:")
        destination = input().strip()
        
        if origin not in cities or destination not in cities:
            print("Ciudad no encontrada en la base de datos. Por favor, intente nuevamente.")
            continue
        
        distance_km, distance_miles = get_distance(origin, destination)
        
        print("Seleccione el medio de transporte (auto, bus, avion):")
        transport = input().strip().lower()
        if transport not in ["auto", "bus", "avion"]:
            print("Medio de transporte no válido. Por favor, intente nuevamente.")
            continue

        travel_time = get_travel_time(distance_km, transport)

        print(f"Distancia entre {origin} y {destination}:")
        print(f"{distance_km:.2f} kilómetros")
        print(f"{distance_miles:.2f} millas")
        print(f"Duración estimada del viaje en {transport}: {travel_time:.2f} horas")

        narrative = f"El viaje desde {origin}, {cities[origin]['country']} hasta {destination}, {cities[destination]['country']} "
        narrative += f"cubrirá una distancia de {distance_km:.2f} kilómetros ({distance_miles:.2f} millas) "
        narrative += f"y tomará aproximadamente {travel_time:.2f} horas en {transport}."
        print(narrative)
        print("\n")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
