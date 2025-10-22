import pytest


# The fixtures (trello_client, clean_board) are auto-discovered by pytest
# via conftest.py and injected here.

class TestBoardManagement:

    def test_get_boards_returns_data(self, trello_client):
        """
        Verify that the /members/me/boards endpoint returns a 200 status
        and the result is a non-empty list.
        """
        boards = trello_client.get_my_boards()

        # 1. Assert the type is a list
        assert isinstance(boards, list), "API response should be a list of boards."

        # 2. Assert the list is not empty (assuming the user has at least one board)
        assert len(boards) > 0, "No boards found. Check Trello account or API access."

        # 3. Assert basic structure of a single board object
        if boards:
            first_board = boards[0]
            assert 'id' in first_board
            assert 'name' in first_board
            assert isinstance(first_board['id'], str)
            print(f"Successfully validated GET /members/me/boards. Found {len(boards)} boards.")

    def test_create_and_delete_board_lifecycle(self, clean_board, trello_client):
        """
        Tests the end-to-end lifecycle of a board:
        1. Creation (handled by clean_board setup)
        2. Verification that the board exists
        3. Deletion (handled by clean_board teardown)
        """
        # The clean_board fixture has already created the board and yielded its ID
        board_id = clean_board
        print(f"Test is running with temporary Board ID: {board_id}")

        # Verification step: Ensure the board ID is valid and exists in the user's list
        all_boards = trello_client.get_my_boards()

        # Check if the newly created board ID is present in the list of all boards
        board_ids = [board['id'] for board in all_boards]

        assert board_id in board_ids, f"Board with ID {board_id} was not found after creation."

        print(f"Successfully verified that board {board_id} exists and cleanup will proceed.")

    def test_invalid_board_deletion(self, trello_client):
        """
        Negative test case: Attempt to delete a non-existent board.
        Trello API should return a 404 Not Found or similar client error (4xx).
        """
        # Use a clearly invalid, but syntactically correct, Trello-like ID
        invalid_id = "000000000000000000000000"

        with pytest.raises(requests.exceptions.HTTPError) as excinfo:
            trello_client.delete_board(invalid_id)

        # Trello typically returns a 404 for missing resources
        assert "404 Client Error: Not Found" in str(excinfo.value)
        print(f"Successfully caught expected 404 error when attempting to delete invalid board ID {invalid_id}.")
