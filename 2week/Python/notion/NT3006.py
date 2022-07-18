import json
from pprint import pprint
from re import template


def movie_info(movies, genres):
    result = []
    genre_id_name = {}

    for i in genres :
        genre_id_name[i['id']] = i['name']
    
    for j in range(len(movies)) :
        genre_name = []
        for k in movies[j]['genre_ids'] :
            genre_name.append(genre_id_name[k])
        movies[j]['genre_names'] = genre_name

    for l in movies :
        mv_template = {}
        mv_template['genre_names'] = l['genre_names']
        mv_template['id'] = l['id']
        mv_template['overview'] = l['overview']
        mv_template['title'] = l['title']
        mv_template['vote_average'] = l['vote_average']
        result.append(mv_template)
    return result
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
    