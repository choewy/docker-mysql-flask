# Docker-compose Mysql + Flask

```yaml
services:
  db:
    build: ./mysql/
    cap_add:
      - SYS_NICE
    command: --authentication_policy=mysql_native_password
    restart: always
    volumes:
      - ./mysql/mysql_data:/var/lib/mysql
      - ./mysql/sqls:/docker-entrypoint-initdb.d
    ports:
      - 33061:3306
    environment:
      MYSQL_ROOT_PASSWORD: root

  app:
    depends_on:
      - db
    build: ./src/
    restart: always
    ports:
      - 2000:5000
```