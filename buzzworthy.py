import twitter
from random import randrange
from OAuthSettings import settings

#OAuth credentials
consumer_key = settings['consumer_key']
consumer_secret = settings['consumer_secret']
access_token_key = settings['access_token_key']
access_token_secret = settings['access_token_secret']

# create two hastags to tweet
christag = '#TeamChris'
mrpitag = '#MRPI2014'
chrispacheco = 'Chris Pacheco'
chris = 'Chris'

sentence = randrange(0,10)
if sentence == 0:
    subject = 'If only I could be as'
    ending = 'as ' + chrispacheco
elif sentence == 1:
    subject = 'Sometimes I just lie in bed wondering how I can be'
    ending = 'like ' + chris
elif sentence == 2:
    subject = 'They\'ll tell stories of how ' + chrispacheco + ' was the most'
    ending = 'gentleman of the Philippines'
elif sentence == 3:
    subject = 'Don\'t worry son, someday ' + chris + '\'s'
    ending = 'figure might rub off on you, too'
elif sentence == 4:
    subject = 'I met ' + chrispacheco + ' once. He was as'
    ending = 'as everyone said he would be'
elif sentence == 5:
    subject = 'Dunno why there\'s even a contest for Mr PI 2014. It\'s obvious someone as'
    ending = 'as ' + chris + ' has it in the bag'
elif sentence == 6:
    subject = chris + ' is about to grace the stage this Sunday! They ain\'t ready for someone so'
    ending = ''
elif sentence == 7:
    subject = 'I heard ' + chrispacheco + ' is going to be GQ\'s man of the year. Who could be surprised with a'
    ending = 'gentleman like him?'
elif sentence == 8:
    subject = 'It\'s only due to ' + chris + '\'s unbelievably'
    ending = 'persona that I have the strength to get up every morning. Thank you, ' + chrispacheco
elif sentence == 9:
    subject = 'Mr. PI 2014? A man this'
    ending = 'has been Mr. PI in my book for as long as I\'ve known him'

# choose a random operator
operator = randrange(0,34) 
if operator == 0:
    adj = 'gorgeous'
elif operator == 1:
    adj = 'stunning'
elif operator == 2:
    adj = 'cute'
elif operator == 3:
    adj = 'hot'
elif operator == 4:
    adj = 'sexy'
elif operator == 5:
    adj = 'attractive'
elif operator == 6:
    adj = 'handsome'
elif operator == 7:
    adj = 'appealing'
elif operator == 8:
    adj = 'admirable'
elif operator == 9:
    adj = 'beauteous'
elif operator == 10:
    adj = 'charming'
elif operator == 11:
    adj = 'classy'
elif operator == 12:
    adj = 'dazzling'
elif operator == 13:
    adj = 'delightful'
elif operator == 14:
    adj = 'divine'
elif operator == 15:
    adj = 'elegant'
elif operator == 16:
    adj = 'enticing'
elif operator == 17:
    adj = 'alluring'
elif operator == 18:
    adj = 'exquisite'
elif operator == 19:
    adj = 'excellent'
elif operator == 20:
    adj = 'fair'
elif operator == 21:
    adj = 'fascinating'
elif operator == 22:
    adj = 'fine'
elif operator == 23:
    adj = 'foxy'
elif operator == 24:
    adj = 'good-looking'
elif operator == 25:
    adj = 'grand'
elif operator == 26:
    adj = 'lovely'
elif operator == 27:
    adj = 'magnificent'
elif operator == 28:
    adj = 'marvelous'
elif operator == 29:
    adj = 'ravishing'
elif operator == 30:
    adj = 'sightly'
elif operator == 31:
    adj = 'shapely'
elif operator == 32:
    adj = 'statuesque'
elif operator == 33:
    adj = 'well-formed'
 
# format the Tweet nicely with spaces
tweet = subject + ' ' +  adj + ' ' +  ending + ' ' + christag + ' ' + mrpitag

#post to twitter
try:
    api = twitter.Api(
    consumer_key = consumer_key,
    consumer_secret = consumer_secret,
    access_token_key = access_token_key,
    access_token_secret = access_token_secret)

    status = api.PostUpdate(tweet)
    print ' post successful!!!'

except twitter.TwitterError:
    print 'error posting!'

#print tweet
