def makeURL(*args, **kargs):
    for result in args:
        result += 1
    myURL = "데스크아아나다안"
    for k, v in kargs.items():
        myURL += k + '=' + v + '&'
    
    myURL = myURL.rstrip('&')
    print(myURL)

makeURL(1,2,3,4,5, user='psycho', index = '5', page = '10')