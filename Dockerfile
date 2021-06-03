FROM python:latest
COPY . /app
WORKDIR /app
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y vim
RUN pip install . --no-cache-dir
RUN mkdir instance && touch instance/config.py
RUN echo API_KEY='"<your key here>"' >> instance/config.py
RUN echo SEARCH_ENGINE_ID='"<your search engine id here>"' >> instance/config.py
CMD ["/bin/bash"]
