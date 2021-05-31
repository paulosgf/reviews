class RepositoryDoesNotExist(Exception):
    """Unable to fetch the repository as it already exists"""


class InvalidGithubToken(Exception):
    """Unable to query Github using an empty or invalid Github Token"""
