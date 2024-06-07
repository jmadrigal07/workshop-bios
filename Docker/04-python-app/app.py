import requests

def main():
    # Realizamos una solicitud HTTP GET a una URL de ejemplo
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    # Verificamos si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Imprimimos el contenido de la respuesta
        print("Contenido de la solicitud:")
        print(response.json())
    else:
        # Imprimimos un mensaje de error si la solicitud falla
        print("La solicitud falló. Código de estado:", response.status_code)

if __name__ == "__main__":
    main()

