import sys
import json

def main():
    stopwords_file = open(sys.argv[1])
    tweets_file = sys.argv[2]
    
    list_of_stop_words =[]
    dict_words = {}
    total_words = 0

    for line in stopwords_file:
        for word in line.split():
            list_of_stop_words.append(word)
    with open(tweets_file) as tweets:
        for tweet in tweets:
            json_obj = json.loads(tweet) 
            line = json_obj['text']
            
            for word in line.split():
                flag_found_in_dict = 0
                flag_stopword = 0
                total_words = total_words + 1
                word = word.lower()
                word = word.strip('-~><{};?"$!&^*+ @#.,:[](1234567890)')
                if(word == ""):
                    continue
                if(word == "rt"):
                    continue
                for stopword in list_of_stop_words:
                    if(word == stopword):
                        flag_stopword = 1
                        break
                if(flag_stopword == 0):
                    for val in dict_words.keys():
                        if(word == val):
                            dict_words[val] = dict_words[val] + 1
                            flag_found_in_dict = 1
                    if(flag_found_in_dict == 0):
                        dict_words[word] = 1         
    for key in dict_words.keys(): 
        dict_words[key] ='{0:.10f}'.format( (dict_words[key]/total_words) )
    dict_list = sorted(dict_words.items(),key = lambda t: t[1], reverse =True)
    for key in dict_list:
        print(key[0]+" " + str(key[1])) 
if __name__ == '__main__':
    main()
