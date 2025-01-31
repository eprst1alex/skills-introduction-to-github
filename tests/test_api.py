import unittest
import requests
import time

from tests import config
from constant import API_URL


class TestGitHubAPICase(unittest.TestCase):
    TEST_REPO_NAME = f"test-repo-{int(time.time())}"  # Динамическое имя репозитория

    def setUp(self):
        # Проверяем, что токен задан в окружении
        token = config("GITHUB_TOKEN", cast=str, default="none")

        if token == 'none':
            raise ValueError("GITHUB_TOKEN environment variable not set.")

        self.token = token

    def test_create_public_repo(self, repo_name, description="Test repository created with API"):
        """Создает публичный репозиторий на GitHub."""
        url = f"{API_URL}/user/repos"
        headers = {
            "Authorization": f"token {self.token}",
            "Content-Type": "application/json",
        }
        data = {
            "name": repo_name,
            "description": description,
            "private": False,
            "auto_init": True,
        }
        response = requests.post(url, headers=headers, json=data)

        self.assertEqual(response.status_code, 201,
                         f"Failed to create repository. Response code: {response.status_code} Response: {response.text}")

        self.assertEqual(response.json()["private"], False, "Repository should be public.")
        self.assertEqual(response.json()["name"], self.TEST_REPO_NAME, "Repository name does not match.")


#     def test_create_public_repo(self):
#         """Тест создания нового публичного репозитория."""
#         response = github_api.create_repo(self.TEST_REPO_NAME)
#
#         self.assertEqual(response.status_code, 201,
#                          f"Failed to create repository. Response code: {response.status_code} Response: {response.text}")
#
#         self.assertEqual(response.json()["private"], False, "Repository should be public.")
#         self.assertEqual(response.json()["name"], self.TEST_REPO_NAME, "Repository name does not match.")
#
#     def test_delete_created_repo(self):
#         """Тест удаления созданного репозитория."""
#         create_response = github_api.create_repo(self.TEST_REPO_NAME)
#
#         if create_response.status_code != 201:
#             self.fail(f"Failed to create repository, cannot test delete. Response: {create_response.text}")
#
#         delete_response = github_api.delete_repo(self.TEST_REPO_NAME)
#
#         self.assertEqual(delete_response.status_code, 204,
#                          f"Failed to delete repository. Response code: {delete_response.status_code} Response: {delete_response.text}")
#
#     @classmethod
#     def tearDownClass(cls):
#         # При завершении тестов удалим созданный репозиторий (если он был создан)
#         # Здесь можно обойтись и без вызова delete_repo
#         response = github_api.delete_repo(cls.TEST_REPO_NAME)
#         if response.status_code != 204:
#             print(
#                 f"Failed to cleanup repository: {cls.TEST_REPO_NAME}. Response code {response.status_code} and Response: {response.text}")
#
#
# if __name__ == "__main__":
#     unittest.main()