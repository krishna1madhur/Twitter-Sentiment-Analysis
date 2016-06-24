import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    afinnfile = open("AFINN-111.txt")
    scores = {}
    tweet_sent_score = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = float(score) 

    with open(sys.argv[2]) as tweets:
        for tweet in tweets:
            json_obj = json.loads(tweet)
            line = json_obj['text'].replace('\n','')

            tweet_sentiment_score = 0
            for word in line.split():
                flag_found_in_dict = 0
                
                word = word.lower()
                word = word.strip('-~><{};?"$!&^*+ @#.,:[](1234567890)')
                if(word == ""):
                    continue
                if(word == "rt"):
                    continue
                for key in scores.keys():
                    if(word == key):
                        tweet_sentiment_score = tweet_sentiment_score + scores[key]
                        flag_found_in_dict = 1
                        break
            tweet_sent_score[line] = tweet_sentiment_score

    dict_list = sorted(tweet_sent_score.items(),key = lambda t: t[1], reverse =True)
    length_dictionary = len(dict_list)
    result_list_tweet = []
    result_list_value = []
    count_first = 0
    for key in dict_list:
        if count_first < 10:
            
            count_first = count_first + 1
           # result_list_tweet.append(key[0])
           # result_list_value.append(str(key[1]))
            print(str(key[1]) + ": " + key[0])

        elif(count_first >=(length_dictionary-10)):
          #  result_list_tweet.append(key[0])
          #  result_list_value.append(str(key[1]))
            count_first = count_first + 1
            print(str(key[1]) + ": " + key[0])

        else:
            count_first = count_first + 1
 
if __name__ == '__main__':
    main()
