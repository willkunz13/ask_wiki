# Ask Wiki

Ask Wiki is a flask microservice that takes questions and searches wikipedia to provide an answer.  It utilizes the google search api to locate wikipedia pages that likely answer the question, and the huggingface deepset/roberta-base-squad2 [model](https://huggingface.co/deepset/roberta-base-squad2).

## Installation

This microservice requires interacting with the [Google Custom Search JSON](https://developers.google.com/custom-search/v1/overview).

When setting up your search api Sites to Search should be limited to www.wikipedia.org.

After setting up your search api you need to save your Google Api Key and Search Engine ID for later use.

This microservice will be installed and run through docker.  If you are unfamiliar docker, follow this [installation process](https://docs.docker.com/get-docker/).

Once docker is running you need to pull the docker image with:
```bash
docker pull willkunz/ask_wiki:latest
```

To launch the microservice:

```bash
docker run -it -p 8080:8080 willkunz/ask_wiki:latest
```

Now we need to enter your api key and search engine id.

```bash
vim instance/config.py
```

Enter in your api and search engine id where listed and write the file with :w.

Finally, launch the flask app with:
```bash
waitress-serve --call "flaskr:create_app"
```

## Usage

The microservice can be interacted with by posting questions to the '/search' endpoint.

To post the questions use the python requests package.  If you are unfamiliar you can download it with:

```bash
pip install requests
```

A sample script to post a question to the microservice:

```python
import requests

url = 'http://localhost:8080/search'
query = 'Who was the English King in 1530?'

response = requests.post(url, data=query)
```
