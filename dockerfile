FROM alpine

RUN apk -U --no-cache add \
            python3 && \
    mkdir -p /spidertrap

COPY spidertrap.py /spidertrap
COPY log.py /spidertrap

WORKDIR /spidertrap
# Start spidertrap
STOPSIGNAL SIGINT
CMD ["/usr/bin/python3","log.py"]
