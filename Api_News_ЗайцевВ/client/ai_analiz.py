import os
from dotenv import load_dotenv
from mistralai.client import Mistral
from datetime import datetime, timedelta
from client.api_methods import get_everything

load_dotenv()

def analyze_news(topic=None):
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    topic = input("Введите тему: ")

    response = get_everything(
        api_key=os.getenv('NEWS_API_KEY'),
        q=topic,
        from_param=yesterday,
        language='ru',
    )

    news_text = ""
    articles = response.get('articles', [])
    for i, art in enumerate(articles[:15], 1):
        title = art.get('title', '')
        desc = art.get('description', '')
        news_text += f"{i}. {title}\n   {desc}\n\n"

    print("Анализирую...")

    prompt = f"""Проанализируй эти новости на тему "{topic}" и напиши аннотацию на русском языке (250-300 слов):
     {news_text}
     Аннотация (выдели главное, дай оценку, сделай вывод):"""

    client = Mistral(api_key=os.getenv('MISTRAL_API_KEY'))
    result = client.chat.complete(
        model="mistral-medium-latest",
        messages=[{"role": "user", "content": prompt}]
    )

    annotation = result.choices[0].message.content

    print("\n" + annotation)
    with open('text.txt', 'w', encoding='utf-8') as f:
        f.write(annotation)

    print("\n Аннотация сохранена в файл text.txt")