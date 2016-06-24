import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    afinnfile = open(sys.argv[1])
    scores = {}
    tweet_sent_score = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = float(score)

    dict_sent_total = {}
    dict_count = {}

    dict_states = {"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","DC":"District of Columbia","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"}

    dict_reverse = {v: k for k, v in dict_states.items()}

#    for key in dict_reverse.keys():
#        print(key + " : "+dict_reverse[key])

    with open(sys.argv[2]) as tweets:
        for tweet in tweets:
            json_obj = json.loads(tweet)
            if( json_obj['place'] != None ):
                line = json_obj['place']['full_name']
                
                for word in line.split(","):
                    for key in dict_states:
                        if(word.strip() == key or word.strip() == dict_states[key]):
                                       
                            tweet = json_obj['text']

                            tweet_sentiment_score = 0
                            for each_word in tweet.split():

                                each_word = each_word.lower()
                                each_word = each_word.strip('-~><{};?"$!&^*+ @#.,:[](1234567890)')
                                if(each_word == ""):
                                    continue
                                if(each_word == "rt"):
                                    continue
                                for key in scores.keys():
                                    if(each_word == key):
                                        tweet_sentiment_score = tweet_sentiment_score + scores[key]
                                        break
                            word = word.strip()
                            if( word in dict_reverse.keys()):
                                word = dict_reverse[word]

                            if word in dict_sent_total.keys():
                                dict_sent_total[word] = dict_sent_total[word] + tweet_sentiment_score
                            else:
                                dict_sent_total[word] = tweet_sentiment_score
                            if word in dict_count.keys():
                                dict_count[word] = dict_count[word] + 1
                            else:
                                dict_count[word] = 1
                            

 
            elif(json_obj['user']['location'] != None):
                line =  json_obj['user']['location']
                for word in line.split(): 
                    for key in dict_states:
                        if(word.strip()== key or word.strip() == dict_states[key]):        
                            
                            tweet = json_obj['text']

                            tweet_sentiment_score = 0
                            for each_word in tweet.split():
                                   
                                each_word = each_word.lower()
                                each_word = each_word.strip('-~><{};?"$!&^*+ @#.,:[](1234567890)')
                                if(each_word == ""):
                                    continue
                                if(each_word == "rt"):
                                    continue
                                for key in scores.keys():
                                    if(each_word == key):
                                        tweet_sentiment_score = tweet_sentiment_score + scores[key]
                                        break
                            word = word.strip() 
                            if( word in dict_reverse.keys()):
                                word = dict_reverse[word]             

                            if word in dict_sent_total.keys():
                                dict_sent_total[word] = dict_sent_total[word] + tweet_sentiment_score 
                            else:
                                dict_sent_total[word] = tweet_sentiment_score

                            if word in dict_count.keys():
                                dict_count[word] = dict_count[word] + 1
                            else:
                                dict_count[word] = 1
    dict_avg = {}
    for key in dict_sent_total.keys():
        dict_sent_total[key]= dict_sent_total[key]/dict_count[key]   

    dict_list = sorted(dict_sent_total.items(),key = lambda t: t[1], reverse =True)
    for key in dict_list:
        print( str(key[1]) + ": " + key[0])


if __name__ == '__main__':
    main()
