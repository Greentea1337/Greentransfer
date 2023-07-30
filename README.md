# GreenTransfer

GreenTransfer - это клиент-серверное приложение для безопасной передачи файлов по сети.

## Особенности

- Использует алгоритм SHA256 для проверки целостности передаваемых данных

- Поддерживает передачу файлов любого размера между клиентом и сервером

- Клиент может загружать файлы с сервера по имени

- Логирует процесс передачи на стороне сервера в файл

- Многопоточная архитектура сервера для обслуживания нескольких клиентов

## Безопасность
- Целостность файлов гарантируется благодаря хешированию чанками

- Нет разграничения прав доступа между клиентами

### Возможные улучшения

- Добавить шифрование TLS для защиты трафика

- Реализовать аутентификацию клиентов по логину/паролю

- Добавить авторизацию для ограничения доступа к файлам 

- Передавать хеши отдельно от данных для защиты от модификации

## Использование

Запустить сервер:
