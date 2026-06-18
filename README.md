# Spidertrap

> A modern Python 3 successor to [ADHDproject/spidertrap](https://github.com/adhdproject/spidertrap) — traps web crawlers and spiders in an infinite maze of dynamically generated pages.

[![Docker Build](https://github.com/just5ky/spidertrap/workflows/Docker/badge.svg)](https://github.com/just5ky/spidertrap/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/justsky/spidertrap)](https://hub.docker.com/r/justsky/spidertrap)
[![Docker Image Size](https://img.shields.io/docker/image-size/justsky/spidertrap?color=orange)](https://hub.docker.com/r/justsky/spidertrap)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

## What's new vs the original

| | [ADHDproject/spidertrap](https://github.com/adhdproject/spidertrap) | **This project** |
|---|---|---|
| Runtime | Python 2 | Python 3 |
| Logging | None | Integrated — stdout + file |
| Docker | No | Multi-arch (amd64, arm64, arm/v7, arm/v6, 386, ppc64le, s390x) |
| Maintenance | Archived | Active |
| Distribution | Source only | Docker Hub + GHCR |

## How it works

Every request is seeded by the URL path, so links are infinite but deterministic — the same URL always returns the same page. Crawlers follow links forever, consuming bandwidth and CPU while getting nowhere.

## Quick start

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

Browse to `http://127.0.0.1` — each page renders randomly generated links that lead to more pages without end.

## Logging

Mount a host directory to `/log` and access logs are written to `spidertrap.log` in Apache Combined Log Format:

```
1.2.3.4 - - [21/May/2022 09:59:55] "GET /yf/XhuQwxZqdZwFG_6_U HTTP/1.1" 200 - "https://example.com/" "Mozilla/5.0 (compatible; Googlebot/2.1)"
1.2.3.4 - - [21/May/2022 09:59:56] "GET /favicon.ico HTTP/1.1" 200 - "-" "wget/1.21.3"
```

Logs also stream to stdout (visible via `docker logs spidertrap`).

## Custom link file

Pass a file of URLs (one per line) to serve real-looking links instead of random strings:

```sh
# bare Python
python3 spidertrap.py urls.txt

# Docker
docker run --rm --name spidertrap \
  -v .:/log \
  -v ./urls.txt:/spidertrap/urls.txt \
  -p 80:80 \
  justsky/spidertrap urls.txt
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

## Multi-arch support

`linux/amd64` · `linux/arm64` · `linux/arm/v7` · `linux/arm/v6` · `linux/386` · `linux/ppc64le` · `linux/s390x`

## Roadmap

- [ ] ENV var configuration (`PORT`, `DELAY`, `LINKS_PER_PAGE`) — no source edits needed in Docker
- [ ] CLI flags (`--port`, `--delay`, `--file`) replacing hardcoded constants
- [ ] `robots.txt` honeypot — serve `Allow: /` to actively invite crawlers
- [ ] `sitemap.xml` with infinite entries — amplify trap surface
- [ ] Realistic HTML — fake titles, meta tags, body text to evade trap-detection heuristics
- [ ] `/metrics` Prometheus endpoint — request counts and unique IPs
- [ ] Dockerfile `HEALTHCHECK`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

See [SECURITY.md](SECURITY.md).

## License

[GNU General Public License v3.0](LICENSE)
