# spidertrap
Traps web crawlers

`docker run --rm --name spidertrap -p 80:80 justsky/spidertrap`

- You can also provide your own wordlist

`docker run --rm -i --name spidertrap -p 80:80 justsky/spidertrap wordlist.txt`

```yml
version "3"

services:
  spidertrap:
    name: spidertrap
    image: justsky/spidertrap
    restart: unless-stopped
    port:
      - 80:80
```
