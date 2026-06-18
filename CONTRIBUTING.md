# Contributing

Thanks for taking the time to contribute.

## Reporting bugs

Open a [bug report](https://github.com/just5ky/spidertrap/issues/new?template=bug_report.yml). Include:
- Steps to reproduce
- Expected vs actual behaviour
- Spidertrap version / Docker image tag
- Host OS and architecture

## Suggesting features

Open a [feature request](https://github.com/just5ky/spidertrap/issues/new?template=feature_request.yml) before writing code. Describe the problem you're solving, not just the solution.

## Submitting a pull request

1. Fork the repo and create a branch from `latest`.
2. Make your changes.
3. Test locally:
   ```sh
   python3 -m py_compile spidertrap.py
   docker build -t spidertrap-test .
   docker run --rm -p 8080:80 spidertrap-test
   ```
4. Open a pull request against `latest`.

## Code style

- Python 3.8+ compatible
- No external dependencies (stdlib only)
- No comments explaining *what* the code does — only *why* when non-obvious
- Use f-strings, context managers, and type hints where practical

## License

By contributing you agree your changes will be licensed under [GPL v3](LICENSE).
