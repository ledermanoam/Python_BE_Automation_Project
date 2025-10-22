import pytest
from trello_client.client import TrelloAPIClient
import time
import uuid


@pytest.fixture(scope="session")
def trello_client():
    """
    Fixture that provides a TrelloAPIClient instance for all tests.
    The session scope means it's initialized once per test run.
    """
    return TrelloAPIClient()


@pytest.fixture
def clean_board(trello_client):
    """
    Fixture for creating and deleting a temporary board.

    Yields the ID of the created board to the test, and automatically
    deletes it afterwards (teardown).
    """
    # 1. Setup: Create a unique board
    unique_name = f"TestBoard-{int(time.time() * 1000)}"
    print(f"\n--- SETUP: Creating board: {unique_name} ---")
    board_data = trello_client.create_board(name=unique_name)
    board_id = board_data['id']

    # 2. Yield: Give the board_id to the test function
    yield board_id

    # 3. Teardown: Delete the board
    print(f"\n--- TEARDOWN: Deleting board: {board_id} ---")
    status = trello_client.delete_board(board_id)
    assert status == 200  # Ensure cleanup was successful
