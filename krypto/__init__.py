import os

__version__ = "0.1.0"

token = os.getenv("TOKEN_GITHUB")
assert token is not None


from krypto.cli import cli as cli


# TODO[Enhancement]: Make config file
# Sometimes you might wanna have TODOs in your tests.
# Right now krypto will completely ignore any file with the
# configure this behaviour. Perhaps read from pyproject.toml?


# TODO[Enhancement, Bug]: Allow for different standard labels to be attached to the issues
# Mayhap I would like to assign a todo certain labels like `Enhancement`
# Possible syntax `# Enhancement: title here`
# or maybe `# TODO[Enhancement]: title here`
# Labels are overwritten right now instead of extended
