# Security Policy

## Supported versions

| Version | Supported |
|---------|----------|
| latest  | ✓        |
| older   | ✗        |

## Reporting a vulnerability

**Do not open a public issue for security vulnerabilities.**

Report privately via [GitHub Security Advisories](https://github.com/just5ky/spidertrap/security/advisories/new) or email the maintainer directly.

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix if known

You will receive a response within 7 days. If the issue is confirmed, a patch will be released as soon as possible and credit given in the changelog.

## Scope

Spidertrap is intentionally an open HTTP server designed to attract malicious bots. It should always be:
- Run behind a reverse proxy or firewall
- Isolated from sensitive internal networks
- Not used as an authenticated service

Vulnerabilities in how it handles attacker-controlled input (e.g. path traversal leading to information disclosure) are in scope.
