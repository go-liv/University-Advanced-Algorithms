import concurrent.futures
import newspaper
from newspaper import Article

def get_headlines(url):
    headlines = []
    result = newspaper.build(url, memoize_articles=False)
    for i in range(1,6):
        art = result.articles[i]
        art.download()
        art.parse()
        headlines.append(art.title)
    return headlines

def concurrent_func(): 
    #Had to remove cnn website since it was giving an index out of list error
    URLs = ['http://www.foxnews.com/',
            'http://europe.wsj.com/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com',]

    #   Here we start by creating the thread pool executor with 4 max workers since there are 4 websites
    #and we only need 4 processes to run the data from the websites
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        #   This variable will contain the data from the get_headlines method for each url, this also means
        #that it contains the status of completed or uncompleted
        headlines = {executor.submit(get_headlines, url): url for url in URLs}
        #   Everytime the executor completes a get_headlines that url is saved so that the concurrent.futures
        #can be used to check what as been completed, therefore when a url is fully used and data is extracted
        #we can then print that data that was extracted
        for future in concurrent.futures.as_completed(headlines):
            print('\n''The headlines from %s are' % headlines[future], '\n')
            for each in future.result():
                print('%s' % each)

if __name__ == '__main__':
    import timeit
    elapsed_time = timeit.timeit("concurrent_func()", setup="from __main__ import concurrent_func", number=2)/2             
    print(elapsed_time) 
