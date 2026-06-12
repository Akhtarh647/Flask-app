import requests


def paraphrase(text):
    url = "https://paraphrasing-tool1.p.rapidapi.com/api/rewrite"
    payload = {
        "sourceText": text
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "1494c60817msh06d48a519ab7224p1c7299jsn21158a7eaf87",  # Insert your actual RapidAPI key
        "X-RapidAPI-Host": "paraphrasing-tool1.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def sentiment(text):
    url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/?text=great%20value%20in%20its%20price%20range!"
    payload = {
        "sourceText": text
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "1494c60817msh06d48a519ab7224p1c7299jsn21158a7eaf87",  # Insert your actual RapidAPI key
        "X-RapidAPI-Host": 'twinword-sentiment-analysis.p.rapidapi.com'
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()