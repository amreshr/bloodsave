from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
keyz = ['Need blood urgently','emergency blood','please need blood','blood required']

def sortdata(tweet):
   
   a = tokenizer.tokenize(tweet)
   for key in keyz:
      kid = tokenizer.tokenize(key)
      
      z = set(a) & set(kid)
      if len(z) == len(kid):
        
        return True
