FROM alpine

RUN apk -U --no-cache add \
            python3 && \
    mkdir -p /spidertrap

COPY spidertrap.py /spidertrap
COpY log.py /spidertrap

# Start spidertrap
STOPSIGNAL SIGINT
CMD ["/usr/bin/python3","log.py"]
