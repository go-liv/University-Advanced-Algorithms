'''
    Concurrently retrieving headlines from news websites
    input: none needed
    output: the headlines of the news websites printed to the terminal finalized by the total running time 
'''

import concurrent.futures
import newspaper
from newspaper import Article

def get_headlines(url):                                                                         # retrieves the headlines of an url
    headlines = []                                                                              # start an empty list where the headlines can be
    result = newspaper.build(url, memoize_articles=False)                                       # by using the newspaper.build we can retrieve the data in the url per article
    for i in range(1,6):                                                                        # we only need the first 5 headlines so 5 articles
        art = result.articles[i]                                                                # go to this data extracted from the url and get the article
        art.download()                                                                          # downloads the article data to be used
        art.parse()                                                                             # parses the data so it can be used as a set of strings which have different attributes (such as title)
        headlines.append(art.title)                                                             # append the title of the article to the list (art.title is an usability from the newspaper library),
                                                                                                #it is allowed to be accessed like that after parsing the data downloaded (we can access other aspects such as art.author
                                                                                                #or art.publish_date)
    return headlines                                                                            # returns the list

def concurrent_func(): 
    # !!!   Had to remove cnn website since it was giving an index out of list error !!!
    URLs = ['http://www.foxnews.com/',
            'http://europe.wsj.com/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com',]                                                         # list of the urls to extract data from

    '''
       Here we start by creating the thread pool executor with 4 max workers 
    since there are 4 websites and we only need 4 processes to run the data 
    from the websites.
    '''
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:                      # using the ThreadPoolExecutor we can assign a number of workers to create a pool of threads that will execute the
                                                                                                #the function independently, so it will be as if we have a funtion per url and they would run at the same time
        '''
           This variable will contain the data from the get_headlines method 
        for each url, this also means that it contains the status of completed
        or uncompleted.
        '''
        headlines = {executor.submit(get_headlines, url): url for url in URLs}                  # each executor (as explained in the comment above) will run the function independently, saves the data on the variable

        '''
           Everytime the executor completes a get_headlines that url is saved 
        so that the concurrent.futures can be used to check what as been completed, 
        therefore when a url is fully used and data is extracted we can then print 
        that data that was extracted.
        '''
        for future in concurrent.futures.as_completed(headlines):                               # each time the executor completes a task it will be told in .as_completed so the order is for what finishes first
            print('\n''The headlines from %s are' % headlines[future], '\n')                    # printing the headlines from the current url
            for each in future.result():
                print('%s' % each)

if __name__ == '__main__':
    import timeit
    elapsed_time = timeit.timeit("concurrent_func()", setup="from __main__ import concurrent_func", number=2)/2     # timing the running time         
    print(elapsed_time) 
