# Expose the main TrelloClient class at the package level for clean imports.
# Example usage: 'from trello_client import TrelloClient'
from .client import TrelloClient

# Define what is imported when 'from trello_client import *' is used
__all__ = ["TrelloClient"]

# You might also want a version number here
__version__ = "0.1.0"