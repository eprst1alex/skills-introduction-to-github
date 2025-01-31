from tests import config

token = config("TEST_GITHUB_TOKEN", cast=str, default="")

print(token)
