<header>

# Introduction 

_Краткое описание API._

</header>

## GitHubAPI: Create public repository

**Метод:** `POST`

**URL:** `/user/repos` или `/orgs/{org}/repos`

*   `/user/repos` - для создания репозитория в аккаунте пользователя.
*   `/orgs/{org}/repos` - для создания репозитория в организации, где `{org}` нужно заменить на имя организации.

**Аутентификация:**

*   Необходим токен доступа (Personal Access Token) с правом `repo`.
*   Токен передаётся в заголовке `Authorization: token YOUR_TOKEN`.

**Тело запроса (JSON):**

```json
{
  "name": "имя-вашего-репозитория",
  "description": "описание-вашего-репозитория",
  "homepage": "адрес-вашего-сайта (необязательно)",
  "private": false,
  "has_issues": true,
  "has_projects": true,
  "has_wiki": true,
  "is_template": false
}
```

**Параметры в теле запроса:**

*   `name` (обязательно): Имя репозитория.
*   `description` (необязательно): Описание репозитория.
*   `homepage` (необязательно): URL домашней страницы проекта.
*   `private` (обязательно): `true` для приватного репозитория, `false` для публичного. В вашем случае должно быть `false`.
*   `has_issues` (необязательно): `true` для включения Issue Tracker, `false` для выключения. По умолчанию `true`.
*   `has_projects` (необязательно): `true` для включения Projects, `false` для выключения. По умолчанию `true`.
*   `has_wiki` (необязательно): `true` для включения Wiki, `false` для выключения. По умолчанию `true`.
*   `is_template` (необязательно): `true` для создания репозитория-шаблона, `false` для обычного репозитория. По умолчанию `false`.

**Пример запроса (cURL):**

```bash
curl \
  -H "Authorization: token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-new-public-repo",
    "description": "This is a test repository created via API",
    "private": false
  }' \
  https://api.github.com/user/repos
```

## GitHubAPI: Delete public repository


**Метод:** `DELETE`

**URL:** `/repos/{owner}/{repo}`

*   `{owner}`: Имя пользователя или организации, владеющей репозиторием.
*   `{repo}`: Имя репозитория, который нужно удалить.

**Аутентификация:**

*   Необходим токен доступа (Personal Access Token) с правами `repo`.
*   Токен передается в заголовке `Authorization: token YOUR_TOKEN`.

**Тело запроса:**

*   У запроса на удаление репозитория **нет** тела.

**Пример запроса (cURL):**

```bash
curl \
  -H "Authorization: token YOUR_TOKEN" \
  -X DELETE \
  https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO
```

**Пример запроса (Python с библиотекой `requests`):**

```python
import requests

token = "YOUR_TOKEN"
username = "YOUR_USERNAME"
repo_name = "YOUR_REPO"
headers = {
    "Authorization": f"token {token}",
}
url = f"https://api.github.com/repos/{username}/{repo_name}"

response = requests.delete(url, headers=headers)

if response.status_code == 204:
    print("Репозиторий успешно удален!")
else:
    print(f"Ошибка удаления репозитория: {response.status_code}")
    print(response.text)
```

**Важные замечания:**

*   Замените `YOUR_TOKEN` на ваш токен доступа.
*   Замените `YOUR_USERNAME` на имя пользователя или организации, владеющей репозиторием.
*   Замените `YOUR_REPO` на имя репозитория, который нужно удалить.
*   Успешный запрос вернет HTTP-статус `204 No Content`.
*   Удаление репозитория - это **безвозвратная операция**. Будьте осторожны, используя этот API.
*   Возможные ошибки:
    *   `401 Unauthorized`: Неверный или отсутствующий токен.
    *   `404 Not Found`: Репозиторий не найден.
    *   `403 Forbidden`: Недостаточно прав для удаления репозитория.
*   Нельзя удалить репозиторий, если он является шаблоном и используется в качестве шаблона в других репозиториях.
*   У пользователя, который удаляет репозиторий, должны быть права администратора в этом репозитории.

**Ссылки на официальную документацию:**

*   [Delete a repository](https://docs.github.com/en/rest/repos/repos#delete-a-repository)


<footer>

</footer>
