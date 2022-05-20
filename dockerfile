FROM alpine

RUN apk -U --no-cache add \
            python3 && \
    mkdir -p /spidertrap

COPY spidertrap.py /spidertrap

# Start wordpot
STOPSIGNAL SIGINT
CMD ["/usr/bin/python3","spidertrap.py"
