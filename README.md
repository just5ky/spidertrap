# [Spidertrap](https://github.com/adhdproject/spidertrap) dockerized

Trap web crawlers and spiders in an infinite set of dynamically generated web pages.

[![Docker Build](https://github.com/just5ky/spidertrap/workflows/Docker/badge.svg)](https://github.com/just5ky/spidertrap/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/justsky/spidertrap)](https://hub.docker.com/r/justsky/spidertrap)
[![Docker Image Size](https://img.shields.io/docker/image-size/justsky/spidertrap?color=orange)](https://hub.docker.com/r/justsky/spidertrap)

Fork of [ADHDproject/Spidertrap](https://github.com/adhdproject/spidertrap) with integrated logging.

## Multi-arch support

`linux/amd64` · `linux/arm64` · `linux/arm/v7` · `linux/arm/v6` · `linux/386` · `linux/ppc64le` · `linux/s390x`

## Usage

### Docker Hub

```sh
docker run --rm --name spidertrap -v .:/log -p 80:80 justsky/spidertrap
```

### GitHub Container Registry

```sh
docker run --rm --name spidertrap -v .:/log -p 80:80 ghcr.io/just5ky/spidertrap:latest
```

### Docker Compose

```yaml
services:
  spidertrap:
    image: justsky/spidertrap
    restart: unless-stopped
    ports:
      - "80:80"
    volumes:
      - .:/log
```

Browse to `http://127.0.0.1` — each page renders randomly generated links leading to more pages.

## Logging

Mount a host directory to `/log` and access logs will be written to `spidertrap.log`:

```
1.2.3.4 - - [21/May/2022 09:59:55] "GET /yf/XhuQwxZqdZwFG_6_U HTTP/1.1" 200 -
1.2.3.4 - - [21/May/2022 09:59:56] "GET /favicon.ico HTTP/1.1" 200 -
```

## Trap a crawler

```sh
sudo wget -m http://127.0.0.1
```

Wget runs indefinitely until killed.

## Build locally

```sh
git clone https://github.com/just5ky/spidertrap
cd spidertrap
docker build -t spidertrap .
```
