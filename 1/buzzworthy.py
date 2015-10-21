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

sentence = randrange(0,40)
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
elif sentence == 10:
	subject = chris + ' told me I was'
	ending = 'once. He must\'ve been looking in a mirror instead'
elif sentence == 11:
	subject = 'Showers women and showers himself. Could you ask for more class from a man this'
	ending = '? #hygiene'
elif sentence == 12:
	subject = 'The hype can\'t stop for the next Mr. PI ' + chrispacheco + '. #'
	ending = ''
elif sentence == 13:
	subject = 'Who was the most'
	ending = 'man you\'ve seen in the past week? Don\'t lie, it was probably ' + chris
elif sentence == 14:
	subject = 'How would I live without ' + chrispacheco + ' ? That man is too'
	ending = '.'
elif sentence == 15:
	subject = chris + ' should write a book on how to be as'
	ending = 'as him'
elif sentence == 16:
	subject = 'I hope the judges can handle how'
	ending = chris + ' is, we need them to hand him his sashes'
elif sentence == 17:
	subject = chrispacheco + ' is just another phrase for'
	ending = '.'
elif sentence == 18:
	subject = 'I got ' + chris + '\'s autograph once. His signature is as'
	ending = 'as he is'
elif sentence == 19:
	subject = 'There\'s a picture of ' + chrispacheco + ' in the dictionary, right next to the word:'
	ending = '.'
elif sentence == 20:
	hype = 'GO CHRIS!!'
elif sentence == 21:
	hype = 'I LOVE YOU CHRIS'
elif sentence == 22:
	hype = 'RUNNING OUT OF IDEAS BUT TWITTER GAME STRONG'
elif sentence == 23:
	hype = 'PAVING THE WAY FOR MR BUZZWORTHY 2014'
elif sentence == 24:
	hype = 'YOU GOT THIS CHRIS'
elif sentence == 25:
	hype = 'HYPE HYPE HYPE'
elif sentence == 26:
	hype = 'FUPAC REPPIN HARD THIS SUNDAY'
elif sentence == 27:
	hype = 'CHRIS^^^'
elif sentence == 28:
	hype = 'CHRIS GAME STRONG'
elif sentence == 29:
	hype = 'YAS CHRIS SLAY'
elif sentence == 30:
	hype = 'Chris boutta own this stage'
elif sentence == 31:
	hype = 'WWCD. What would Chris do?'
elif sentence == 32:
	hype = 'You know you want the C.'
elif sentence == 33:
	hype = 'True story: Chris smiled at me once.'
elif sentence == 34:
	hype = 'Always strive to be like Chris Pacheco'
elif sentence == 35:
	hype = 'Excuse me sir do you have a minute to listen about our lord and savior Chris Pacheco?'
elif sentence == 36:
	hype = 'Chris shook my hand once. Haven\'t washed it since. #noshame'
elif sentence == 37:
	hype = 'If Chris RT\'d this I would die a happy person'
elif sentence == 38:
	hype = 'T E A M   C H R I S'
elif sentence == 39:
	hype = 'asdfghjkl'

if sentence >= 0 and sentence < 20:
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

elif sentence >= 20:
	tweet = hype + ' ' + christag + ' ' + mrpitag

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
