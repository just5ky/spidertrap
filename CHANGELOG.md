# Changelog

All notable changes to this project will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Planned
- ENV var configuration
- CLI flags (`--port`, `--delay`, `--file`)
- `robots.txt` and `sitemap.xml` honeypot endpoints
- Realistic HTML page templates
- Prometheus `/metrics` endpoint

## [2.0.0] — 2026-06-18

### Changed
- Merged `log.py` into `spidertrap.py` — eliminated subprocess wrapper and its file-handle race condition
- Integrated Python `logging` module: writes to stdout and `/log/spidertrap.log` with graceful fallback
- Renamed `dockerfile` → `Dockerfile` (standard casing)
- Fixed `actions/checkout` action version in CI
- Fixed invalid Docker Compose YAML in README
- Modernised README

### Fixed
- Race condition: both log threads previously opened the same file with `"w"`, truncating each other
- Bare `except:` now catches `Exception as e` and exits with code 1
- File read uses context manager (`with open(...)`)
- Unused loop variables changed to `_`

### Removed
- `log.py` (logic absorbed into `spidertrap.py`)

## [1.0.0] — 2022-05-21

### Added
- Initial fork of [ADHDproject/spidertrap](https://github.com/adhdproject/spidertrap)
- Ported to Python 3
- Added `log.py` subprocess wrapper for file logging
- Dockerfile with Alpine base and multi-arch CI
- Docker Hub + GHCR publishing
