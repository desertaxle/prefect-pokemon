from prefect import flow

from prefect_pokemon.tasks import (
    goodbye_prefect_pokemon,
    hello_prefect_pokemon,
)


def test_hello_prefect_pokemon():
    @flow
    def test_flow():
        return hello_prefect_pokemon()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Hello, prefect-pokemon!"


def goodbye_hello_prefect_pokemon():
    @flow
    def test_flow():
        return goodbye_prefect_pokemon()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Goodbye, prefect-pokemon!"
