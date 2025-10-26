import requests
from config.settings import CONFIG


class TrelloAPIClient:
    """
    A client to interact with the Trello REST API.
    Handles authentication and builds the full URL for endpoints.
    """

    def __init__(self):
        # Base parameters containing key and token for all authenticated requests
        self.auth_params = {
            'key': CONFIG.API_KEY,
            'token': CONFIG.API_TOKEN
        }
        self.base_url = CONFIG.BASE_URL

    def _request(self, method, endpoint, **kwargs):
        """
        Generic request handler. Appends auth parameters and handles responses.
        """
        url = f"{self.base_url}{endpoint}"

        # Merge global auth params with any other params passed in kwargs
        params = kwargs.pop('params', {})
        params.update(self.auth_params)
        kwargs['params'] = params

        print(f"Executing {method} request to: {url}")

        # Use requests.Session in a real framework for connection pooling,
        # but a direct call is sufficient for this example.
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error for {endpoint}: {e}")
            print(f"Response Body: {response.text}")
            raise
        except requests.exceptions.RequestException as e:
            print(f"A Connection Error occurred: {e}")
            raise

    # --- Specific API Methods ---

    def get_my_boards(self):
        """Retrieves a list of boards belonging to the current member ('me')."""
        endpoint = "/members/me/boards"
        # We only want the name and ID for this test
        params = {'fields': 'name,id', 'lists': 'none'}
        response = self._request("GET", endpoint, params=params)
        return response.json()

    def create_board(self, name):
        """Creates a new Trello board."""
        endpoint = "/boards"
        data = {'name': name}
        response = self._request("POST", endpoint, data=data)
        return response.json()

    def delete_board(self, board_id):
        """Deletes a Trello board by ID."""
        endpoint = f"/boards/{board_id}"
        # DELETE requests typically don't need a body, just the auth params
        response = self._request("DELETE", endpoint)
        return response.status_code


class TrelloClient:
    pass