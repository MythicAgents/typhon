FROM itsafeaturemythic/mythic_python_base:latest
RUN pip3 install defusedxml
RUN pip3 install sanic==23.3.0
RUN pip3 install requests

WORKDIR /Mythic/

CMD ["python3", "main.py"]