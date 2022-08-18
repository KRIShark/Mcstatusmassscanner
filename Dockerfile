FROM krishark110/mcstatuspython:latest

COPY pyscript /pyscript
VOLUME [ "/pyscript" ]

RUN cd /pyscript/
ENTRYPOINT [ "python3","/pyscript/main.py" ]