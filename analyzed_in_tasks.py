from watson_developer_cloud import ToneAnalyzerV3
import time
from textblob import Word
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
from textblob.wordnet import VERB, NOUN
from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk import word_tokenize


def tone_analyzer():
    tone_analyzer = ToneAnalyzerV3(
        iam_apikey="JTJoNis7PgdgNKHyuCIQUnXEf2CkHVsF26P38dnVJOW9",
        url="https://gateway-lon.watsonplatform.net/tone-analyzer/api",
        version='2019-01-12')
    return tone_analyzer


def analyze_tone(sentence):
    ta = tone_analyzer()
    json_output = ta.tone(data, content_type='text/plain')
    print("Analyzer's Result " + str(json_output.result))
    sentence = word_tokenize(sentence)
    pos_tagged = pos_tag(sentence)
    print("Parts of Speech in the Sentence: " + str(pos_tagged))
    return pos_tagged


def synonym_finder(word, pos_tag, lch_threshold):
    word = Word(word)
    for words in word.get_synsets(pos=pos_tag):
        print(words)
    # for net1 in wn.synsets(word):
    #     for net2 in wn.all_synsets():
    #         try:
    #             lch = net1.lch_similarity(net2)
    #         except:
    #             continue
    #         if lch >= lch_threshold:
    #             yield (net1, net2, lch)

if __name__ == '__main__':

    data = str(input("Enter the String to Analyze:\t"))
    analyze_tone(data)
    synonym_finder(str(input("Word:\t")), VERB, 2.0)
