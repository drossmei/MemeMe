from random import randint
import json

# parse json file
with open('memeformat.json') as j:
    data = json.load(j)

emotions = list(data.keys())
cache = []

def random_emotion_string(e:list)->str:
    ''' returns a random string of the emotions list'''
    return e[randint(0, len(e)-1)]


def random_caption_string(emotion:str)->str:
    ''' returns a random string of phrases under emotions'''
    phrases_indexes = len(data[emotion])-1
    random_num = randint(0, phrases_indexes)
    return data[emotion][random_num]


def chooseMeme(emotions)->str:
    ''' Chooses a phrase for the caption '''
    emotion = random_emotion_string(emotions)
    caption = random_caption_string(emotion)

    while (caption in cache):
        emotion = random_emotion_string(emotions)
        caption = random_caption_string(emotion)

    limit_and_reset(cache)
    cache.append(caption)

    return caption


def limit_and_reset(cache):
    ''' if the cache is too large, it frees up one spot '''
    if (len(cache) > 5):
        cache.pop(0)
    return cache

