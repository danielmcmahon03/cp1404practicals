import wikipedia

search_phrase = input("Search for: ")
while search_phrase != "":
    try:
        search_result = wikipedia.page(search_phrase)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    print(search_result.title)
    print(search_result.summary)
    print(search_result.url)
    search_phrase = input("Search for: ")
