# spidertrap docker
Traps web crawlers

`docker run --rm --name spidertrap -p 80:80 justsky/spidertrap`

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
#
### Build it yourself
- Clone this Repo
- Inside the repo, run this
 ```sh
 docker build -t spidertrap .
 ```
