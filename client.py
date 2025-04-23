from mcp import ClientSession
from mcp.client.sse import sse_client
import asyncio

# Función principal
async def run():
    url_servidor = "http://192.168.1.7:8000/sse"
    async with sse_client(url=url_servidor,timeout=5.0,sse_read_timeout=300.0) as (read, write):
        async with ClientSession( read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Herramientas disponibles:")
            for tool in tools.tools:
                print(f"- {tool.name}: {tool.description}")
            result = await session.call_tool("obtener_habilidades_pokemon", {"nombre_pokemon": "pikachu"})
            print(f"Habilidades de Pikachu:")
            for habilidad in result.content:
                print(f"- {habilidad.text}")

# Ejecutar
if __name__ == "__main__":
    asyncio.run(run())
