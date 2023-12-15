import requests_with_caching
import json


def get_movies_from_tastedive(mName):
    baseurl = 'https://tastedive.com/api/similar'
    param = {}
    param['q'] = mName
    param['limit'] = 5
    param['type'] = 'movies'

    resp = requests_with_caching.get(baseurl, params=param)
    return json.loads(resp.text)


def extract_movie_titles(dictionary):
    return ([num['Name'] for num in dictionary['Similar']['Results']])


def get_related_titles(movie_list):
    listMvtitles = []
    for movie in movie_list:
        new_titles = extract_movie_titles(get_movies_from_tastedive(movie))
        for title in new_titles:
            if title not in listMvtitles:
                listMvtitles.append(title)
    return listMvtitles


def get_movie_data(mName):
    baseurl = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = mName
    param['r'] = 'json'
    resp = requests_with_caching.get(baseurl, params=param)
    return json.loads(resp.text)


def get_movie_rating(dic):
    raking = dic['Ratings']
    for dic_item in raking:
        if dic_item['Source'] == 'Rotten Tomatoes':
            return int(dic_item['Value'][:-1])
    return 0


def get_sorted_recommendations(movie_list):
    titrate = {}
    for title in get_related_titles(movie_list):
        titrate[title] = get_movie_rating(get_movie_data(title))

    return [num[0] for num in sorted(titrate.items(), key=lambda elem: (elem[1], elem[0]), reverse=True)]


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

