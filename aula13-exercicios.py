import requests
import json

def checkMovies(title):
    quant = 0
    try:
        req = requests.get('http://www.omdbapi.com/?s=' +title+ '&type=movie&apikey=13189dfc')
        answer = json.loads(req.text)
    except:
        print('Connection lost with server')
        return quant

    if answer['Response'] == 'True':
        quant = answer['totalResults']
    return quant

print(checkMovies('matrix'))

def list_movies(title):
    list = []
    for i in range(1,101):
        try:
            print('Searching in page:', i)
            url = ('http://www.omdbapi.com/?s=' + title + '&type=movie&page='+str(i)+'&apikey=13189dfc')
            req = requests.get(url)
            answer = json.loads(req.text)
            if answer['Response'] == 'True':
                for movie in answer['Search']:
                    tit = movie['Title']
                    year = movie['Year']
                    string = tit + ' (' + year + ')'
                    list.append(string)
            else:
                print("Search finished")
                break
        except:
            print('Connection lost with server')
    return list

exit = False
while not exit:
    op = input("Search for a movie or type EXIT: ")
    if op == "EXIT":
        exit = True
    else:
        list_of_movies = list_movies(op)
        print('')
        print("Movies found: ", len(list_of_movies))
        print('')
        for movie in list_of_movies:
            print("\n", movie)


#req = requests.get('http://www.omdbapi.com/?s=star+wars&type=movie&apikey=13189dfc')

#dictionary = json.loads(req.text)

#print(dictionary['Search'][0]['Title'])
