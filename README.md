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

**Важные замечания:**

*   Замените `YOUR_TOKEN` на ваш токен доступа.
*   Замените `"my-new-public-repo"` на желаемое имя репозитория.
*   Не забудьте настроить другие параметры по необходимости.
*   Успешный запрос вернет HTTP-статус `201 Created` и JSON с информацией о созданном репозитории.
*   Возможные ошибки: проверьте статус-коды ответа (например, `401 Unauthorized` - неверный токен, `422 Unprocessable Entity` - ошибка в теле запроса).


<footer>

<!--
  <<< Author notes: Footer >>>
  Add a link to get support, GitHub status page, code of conduct, license link.
-->

---

Get help: [Post in our discussion board](https://github.com/orgs/skills/discussions/categories/introduction-to-github) &bull; [Review the GitHub status page](https://www.githubstatus.com/)

&copy; 2024 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

</footer>
