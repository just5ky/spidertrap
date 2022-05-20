FROM alpine

RUN apk -U --no-cache add \
            python3 \
    mkdir -p /spidertrap && \

# Setup user, groups and configs
    addgroup -g 2000 COPY spidertrap.py /spidertrap && \
    adduser -S -H -s /bin/ash -u 2000 -D -g 2000 spidertrap && \
    chown spidertrap:spidertrap -R /spidertrap && \

COPY spidertrap.py /spidertrap

# Start spidertrap
STOPSIGNAL SIGINT
USER spidertrap:spidertrap
CMD ["/usr/bin/python3","spidertrap.py"
