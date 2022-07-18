import json
from pprint import pprint
from unittest import result


def movie_info(movie, genres):
    mv_info = {}
    genre_id = {}

    for i in genres :
        genre_id[i['id']] = i['name']

    genre_name = []
    for j in movie['genre_ids'] :
        genre_name.append(genre_id[j])
    movie['genre_names'] = genre_name
    mv_info['genre_names'] = movie['genre_names']
    mv_info['id'] = movie['id']
    mv_info['overview'] = movie['overview']
    mv_info['title'] = movie['title']
    mv_info['vote_average'] = movie['vote_average']

    return mv_info

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))