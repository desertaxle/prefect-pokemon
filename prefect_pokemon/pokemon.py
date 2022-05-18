from prefect import flow, task, get_run_logger

from prefect_pokemon.credentials import PokemonCredentials


@task(retries=3)
def get_pokemon(credentials: PokemonCredentials, name: str):
    logger = get_run_logger()
    client = credentials.get_client()

    logger.info(f"Fetching info for Pokemon {name}")
    return client.get_pokemon(name)


@task(retries=3)
def get_type(credentials: PokemonCredentials, name: str):
    logger = get_run_logger()
    client = credentials.get_client()

    logger.info(f"Fetching info for type {name}")
    return client.get_type(name)


@flow
def get_moves_for_type(credentials, type_name: str):
    type_info = get_type(credentials, type_name).result()
    return type_info["moves"]


@flow
def get_effective_move_against_pokemon(
    credentials: PokemonCredentials, pokemon_name: str
):
    logger = get_run_logger()
    pokemon = get_pokemon(credentials, pokemon_name).result()
    type_name = pokemon["types"][0]["type"]["name"]
    logger.info(f"type_name: {type_name}")

    type_info = get_type(credentials, type_name).result()
    move_type = type_info["damage_relations"]["double_damage_from"][0]["name"]
    logger.info(f"move_type: {move_type}")

    moves = get_moves_for_type(credentials=credentials, type_name=move_type).result()
    return moves[0]
