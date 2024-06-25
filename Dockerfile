FROM python:3.9.17

RUN apt update 
RUN mkdir pasta_projeto

COPY requirements.txt /pasta_projeto/requirements.txt
COPY back_end.py /pasta_projeto/back_end.py 
COPY front__end.py /pasta_projeto/front__end.py 
COPY modelo.sav /pasta_projeto/modelo.sav

WORKDIR /pasta_projeto
RUN pip install -r requirements.txt
RUN back_end.py



CMD [ "streamlit", "run", "--server.address", "0.0.0.0", "--server.port", "8501", "front_end.py" ]


