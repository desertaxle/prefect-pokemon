from dataclasses import dataclass
from typing import Optional
import httpx

class PokemonClient():
    def get_pokemon(self, name: str):
        response = httpx.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
        return response.json()

    def get_type(self, name: str):
        response = httpx.get(f"https://pokeapi.co/api/v2/type/{name}/")
        return response.json()

@dataclass
class PokemonCredentials:
    token: Optional[str] = None

    def get_client(self):
        return PokemonClient()