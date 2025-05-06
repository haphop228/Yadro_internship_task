
## Предварительные требования

*   **Для Части 1:**
    *   Python 3
    *   Python-библиотека `requests` (`pip install requests`)
*   **Для Части 2:**
    *   Установленный и запущенный Docker Desktop или Docker Engine.
*   **Для Части 3:**
    *   Ansible (`pip install ansible`)
    *   Docker (Ansible попытается установить/настроить его, если он отсутствует на целевом хосте)
    *   Python `docker` SDK для Ansible (`pip install docker`)

## Часть 1: Python-скрипт (`part1_script`)

**Цель:** Выполнить 5 различных HTTP-запросов к сервису `https://httpstat.us` и логировать ответы. Статус-коды 1xx, 2xx, 3xx логируются как информационные сообщения. Статус-коды 4xx, 5xx вызывают исключение и логируются как ошибки.

**Файлы:**
*   `part1_script/http_requests.py`

**Инструкции:**

1.  **Перейдите в директорию со скриптом:**
    ```bash
    cd part1_script
    ```

2.  **Установите зависимости (если еще не установлены):**
    ```bash
    pip install requests
    ```

3.  **Запустите скрипт:**
    ```bash
    python3 http_requests.py
    ```

4.  **Ожидаемый вывод:**
    В консоли отобразятся логи для каждого запроса, указывающие на успех или неудачу, статус-коды и тело ответа. Для ответов со статус-кодами 4xx/5xx будут показаны исключения.

## Часть 2: Docker (`part2_docker`)

**Цель:** Контейнеризировать Python-скрипт из Части 1 с использованием Docker.

**Файлы:**
*   `part2_docker/Dockerfile`
*   `part2_docker/http_requests.py`

**Инструкции:**

1.  **Перейдите в директорию Docker:**
    ```bash
    cd part2_docker
    ```

2.  **Соберите Docker-образ:**
    ```bash
    docker build -t http-script-container .
    ```

3.  **Запустите контейнер из созданного образа:**
    ```bash
    docker run http-script-container
    ```

4.  **Проверьте логи контейнера:**
    Сначала найдите ID контейнера (если он еще работает):
    ```bash
    docker ps
    ```
    Если нет, то:
    ```bash
    docker ps -a
    ```
    Затем просмотрите логи:
    ```bash
    docker logs <ID_КОНТЕЙНЕРА>
    ```

## Часть 3: Автоматизация с помощью Ansible (`part3_ansible`)

**Цель:** Автоматизировать с помощью Ansible следующие процессы:
1.  Установку Docker на целевом хосте (локальном).
2.  Сборку Docker-образа из `part3_ansible/roles/docker/files/`.
3.  Запуск контейнера и проверку работоспособности Python-скрипта внутри Docker-контейнера (через `docker logs`).

**Файлы:**
*   `part3_ansible/inventory.ini` (определяет `localhost`)
*   `part3_ansible/playbook.yml` (основной плейбук)
*   `part3_ansible/roles/docker/tasks/main.yml` (задачи для установки Docker, сборки образа и запуска контейнера)
*   `part3_ansible/roles/docker/files/Dockerfile` (Dockerfile для сборки Ansible)
*   `part3_ansible/roles/docker/files/http_requests.py` (скрипт для Ansible)

**Инструкции:**

1.  **Перейдите в директорию Ansible:**
    ```bash
    cd part3_ansible
    ```

2.  **Убедитесь, что Ansible установлен и Python `docker` SDK доступен:**
    ```bash
    ansible --version
    pip show docker
    ```
    Если `docker` SDK не установлен, выполните:
    ```bash
    pip install docker
    ```

3.  **Запустите Ansible playbook:**
    Playbook настроен для работы на `localhost` и будет использовать `sudo` (через `become: yes`) для установки Docker и управления им. Вам может потребоваться ввести пароль.
    ```bash
    ansible-playbook -i inventory.ini playbook.yml
    ```

4.  **Ожидаемое поведение:**
    *   Ansible установит Docker (если он еще не установлен).
    *   Пользователь будет добавлен в группу `docker`.
    *   Служба Docker будет запущена и включена.
    *   Будет собран Docker-образ с именем `ansible-http-requests:latest` из файлов в `part3_ansible/roles/docker/files/`.
    *   Будет запущен контейнер с именем `http_script_container` из этого образа.
    *   Логи контейнера `http_script_container` будут выведены в консоль, показывая результат работы Python-скрипта.