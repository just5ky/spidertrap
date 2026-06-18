FROM alpine

RUN apk -U --no-cache add python3 && \
    mkdir -p /spidertrap /log

COPY spidertrap.py /spidertrap/

WORKDIR /spidertrap
EXPOSE 80
STOPSIGNAL SIGINT
CMD ["/usr/bin/python3", "spidertrap.py"]
