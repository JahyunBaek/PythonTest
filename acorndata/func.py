from urllib.request import urlopen, Request
import sys

def fetch_words(url):
    """
    url주소에서 파일을 가져와 단어 리스트를 반환합니다.
    :param url: 불러올 url
    :return:
    """
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_words(story_words):
   for word in story_words:
       print(word)

def main(url):
    words = fetch_words(url)
    print_words(words)


if __name__ == '__main__':
   main(sys.argv[1])
   