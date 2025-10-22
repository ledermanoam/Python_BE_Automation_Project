import os
from dotenv import load_dotenv

# Load environment variables from .env file (if running locally)
# In CI/CD (GitHub Actions), these will be loaded as secrets.
load_dotenv()


class TrelloConfig:
    """
    Configuration class to securely hold Trello API credentials and base URL.
    """
    # Base URL for Trello REST API
    BASE_URL = "https://api.trello.com/1"

    # API Key and Token are mandatory for authentication.
    # They MUST be sourced from environment variables.
    API_KEY = os.getenv("TRELLO_API_KEY")
    API_TOKEN = os.getenv("TRELLO_API_TOKEN")

    if not API_KEY or not API_TOKEN:
        raise ValueError(
            "TRELLO_API_KEY and TRELLO_API_TOKEN must be set as environment variables."
        )


# Instantiate the config object
CONFIG = TrelloConfig()
