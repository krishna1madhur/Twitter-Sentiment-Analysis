import sys
import csv
def main():
    sent_file = open(sys.argv[1])
    csv_file = open(sys.argv[2])
#    file_reader = csv.reader(csv_file)
    afinnfile = open(sys.argv[1])
    scores = {}
    tweet_sent_score = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = float(score)

    list_of_actors = []
    with open(sys.argv[2], newline='') as f:
        reader = csv.reader(f)

        list_of_actors = []
        dict_actors_avg = {}
        seen = set()
        for row in reader:    
            if row[0] not in seen:
                list_of_actors.append(row[0])
                seen.add(row[0])
        list_of_actors.pop(0)
#        for val in list_of_actors:
#            print(val)
        
        for actor in list_of_actors:
            avg_of_tweets_score = 0
            count = 0
            total_tweet_score = 0
            with open(sys.argv[2], newline='') as f:
                reader = csv.reader(f)    
                for row in reader:
               
                    if(row[0] == actor):
                        
                        line = row[1]
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
                        total_tweet_score = total_tweet_score + tweet_sentiment_score
                        count = count + 1
                if(count > 0):
                    avg_of_tweets_score = (total_tweet_score/count)
                    dict_actors_avg[actor] = avg_of_tweets_score                                                       

#    for key in dict_actors_avg.keys():
#        print(key + " : " + str(dict_actors_avg[key])) 
    dict_list = sorted(dict_actors_avg.items(),key = lambda t: t[1], reverse =True)
    for key in dict_list:
        print(str(key[1]) + ": " + key[0])    

if __name__ == '__main__':
    main()
