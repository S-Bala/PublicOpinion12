from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Arsenal']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
            consumer_key = 'zmXuYNAB8FqxUjlnWG5pZVtvR',
            consumer_secret = '6jyvdvVPNN8xfml3YgWQCq2o1mayZlZM82aEPp72DplkxZHmmm',
            access_token = '77296006-bur7KzSwTjRjuliWYkh8YhaAB5uRaPFgp2sSTosxi',
            access_token_secret = 'iykekxTsyKl1yOq0xGxjnpB5y0fai5dxDkuVKcTgYv09a'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) ).encode('utf-8')

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)