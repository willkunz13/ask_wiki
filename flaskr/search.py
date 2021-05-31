from flask import (Blueprint, request, current_app)
import requests
from ask_wiki.models import roberta
import re

bp = Blueprint('search', __name__, url_prefix='/search')
answerer = roberta.Answerer()

@bp.route('', methods=["POST"])
def search():
    query = request.data.decode("utf-8")
    url = f"https://www.googleapis.com/customsearch/v1?key={current_app.config['API_KEY']}&cx={current_app.config['SEARCH_ENGINE_ID']}&q={query}&start=1&num=3"
    data = requests.get(url).json()
    search_items = data.get("items")
    QA_input = []
    for item in search_items:
        title = re.search('([^\/]+$)',item['link']).group(0)
        response = requests.get('https://en.wikipedia.org/w/api.php', params={'action': 'query','format': 'json','titles': title,'prop': 'extracts','explaintext': True,}).json()
        page = next(iter(response['query']['pages'].values()))['extract']
        QA_input.append({'question':query, 'context':page}) 
    res = answerer(QA_input)
    res = sorted(res, key = lambda i: (i['score']), reverse=True)
    return res[0]['answer']
