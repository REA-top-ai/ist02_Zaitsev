from client.api_methods import get_top_headlines, get_sources, get_everything
from client.ai_analiz import analyze_news
from pprint import pprint


if __name__ == '__main__':

    headlines_result = get_top_headlines('0de5f8492c0d4ddea5f736788d4c5944', q = 'apple')
    sources_result = get_sources('0de5f8492c0d4ddea5f736788d4c5944', language='ru', country='ru')
    everything_result = get_everything('0de5f8492c0d4ddea5f736788d4c5944', q = 'apple', language='en')
    # pprint(headlines_result)
    # pprint(sources_result)
    # pprint(everything_result)
    pprint(analyze_news())