#
#
#
FROM python:3.7-alpine
#RUN apk --no-cache add python-pip && \
#    pip install jsonify flask
RUN pip install flask requests
COPY organizer_svc.py /

EXPOSE 8080

ENTRYPOINT ["python", "/organizer_svc.py"]