# [Spidertrap](https://github.com/adhdproject/spidertrap) dockerized
Trap web crawlers and spiders in an infinite set of dynamically
generated webpages.

This is a fork of [ADHDproject/Spidertrap](https://github.com/adhdproject/spidertrap) with added logging.

####  Supports multi-arch
```sh
╰─❯ docker run --rm mplatform/mquery justsky/spidertrap:latest
Image: justsky/spidertrap:latest (digest: sha256:98b61a1853b966015197024d2c8c9e82edab5367ee51bd7f5503d445e367df84)
 * Manifest List: Yes (Image type: application/vnd.docker.distribution.manifest.list.v2+json)
 * Supported platforms:
   - linux/amd64
   - linux/arm64
   - linux/arm/v7
   - linux/386
   - linux/ppc64le
   - linux/s390x
```

## Install and run
---
#### Using dockerhub image
`docker run --rm --name spidertrap -v .:/log/ -p 80:80 justsky/spidertrap`

#### Using github container repo image

`docker run --rm --name spidertrap -v .:/log/ -p 80:80 ghcr.io/just5ky/spidertrap:latest`

OR

#### Using docker-compose

```yml
version "3"

services:
  spidertrap:
    name: spidertrap
    image: justsky/spidertrap
    restart: unless-stopped
    port:
      - 80:80
    volumes:
      - .:/log/
```

Then visit 127.0.0.1:80 in a web
browser. 

You should see a page containing randomly generated links. If
you click on a link it will take you to a page with more randomly
generated links.

## Logging
---
Logs will be saved in spidertrap.log with Apache common log format

```log
1.2.3.4 - - [21/May/2022 09:59:55] "GET /yf/XhuQwxZqdZwFG_6_U HTTP/1.1" 200 -
1.2.3.4 - - [21/May/2022 09:59:56] "GET /favicon.ico HTTP/1.1" 200 -
```

Trapping a Wget Spider
--------------------

`sudo wget -m http://127.0.0.1:80`

Wget will run until either it or Spidertrap is killed.

Build it yourself
---

- Clone this Repo
- Inside the repo, run this

 ```sh
 docker build -t spidertrap .
 ```
