from mcp.server.fastmcp import FastMCP
import requests
app = FastMCP("dorito")


@app.tool()
def obtener_habilidades_pokemon(nombre_pokemon:str) -> list:
    url         = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    response    = requests.get(url)

    if response.status_code == 200:
        pokemon = response.json()
        habilidades = [habilidad["ability"]["name"] for habilidad in pokemon["abilities"]]
        return habilidades
    else:
        return None
    
if __name__ == "__main__":
    app.run(transport="sse")