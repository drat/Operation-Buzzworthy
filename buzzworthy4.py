import twitter
from random import randrange
from OAuthSettings4 import settings

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
    subject = 'One day I hope to be as'
    ending = 'as ' + chrispacheco
elif sentence == 1:
    subject = 'Will I ever be'
    ending = 'like Chris?'
elif sentence == 2:
    subject = chrispacheco + 'was awarded the most'
    ending = 'gentleman of the Philippines'
elif sentence == 3:
    subject = 'The Queen of England is planning to have Chris knighted. Who could be surprised with a' 
    ending = 'gentleman like him?'
elif sentence == 4:
    subject = 'I met ' + chrispacheco + ' once. He was as'
    ending = 'as the rumors said'
elif sentence == 5:
    subject = 'Mr PI 2014 should be renamed to MR Chris 2014. It\'s obvious someone as'
    ending = 'as ' + chris + ' has it in the bag'
elif sentence == 6:
    subject = 'Ain\'t nobody ready today for this'
    ending = 'piece of man'
elif sentence == 7:
    subject = 'I heard ' + chrispacheco + ' is so beautiful you could become legally blind. Who could be surprised with a'
    ending = 'gentleman like him?'
elif sentence == 8:
    subject = 'It\'s only due to ' + chris + '\'s unbelievably'
    ending = 'persona that I\'m at Mr. PI today. Kill em, ' + chris
elif sentence == 9:
    subject = 'Mr. PI 2014? A man this'
    ending = 'has been Mr. PI in my book for awhile.'
elif sentence == 10:
	subject = chris + ' told me I was'
	ending = 'today. Like have you looked in the mirror?'
elif sentence == 11:
	subject = 'Chris is all about that suit and tie. Could you ask for more class from a man this'
	ending = '?'
elif sentence == 12:
	subject = 'The hype can\'t stop for the today\'s Mr. PI Chris "'
	ending = '" Pacheco'
elif sentence == 13:
	subject = 'Who was the most'
	ending = 'man you\'ve seen in the past week? It\'s okay, admit it. It was ' + chris
elif sentence == 14:
	subject = 'A life without Chis Pacheco is a life without reason.' + 'The man is too'
	ending = '.'
elif sentence == 15:
	subject = chris + ' should write for GQ: "how to be'
	ending = 'like Chris'
elif sentence == 16:
	subject = 'I hope the judges can handle how'
	ending = chris + ' is today...'
elif sentence == 17:
	subject = chrispacheco + ' is synonymous with'
	ending = '.'
elif sentence == 18:
	subject = 'I got ' + chris + ' to look at me once. His stare is as'
	ending = 'as he is'
elif sentence == 19:
	hype = 'Chris Pacheco won a grammy before Leonardo Dicaprio did'
elif sentence == 20:
	hype = 'Sam Smith told you to leave your lover for Chris Pacheco'
elif sentence == 21:
	hype = 'He is Pacheco. Chris Pacheco is his name. A Haiku for Chris.'
elif sentence == 22:
	hype = 'Then God said, "And now we will make Chris Pacheco-that was the sixth day"'
elif sentence == 23:
	hype = 'PAVING THE WAY FOR MR BUZZWORTHY 2014'
elif sentence == 24:
	hype = 'Chris looked at me. I cri.'
elif sentence == 25:
	hype = 'What is 9+10? Chris knows it\'s not 21.'
elif sentence == 26:
	hype = 'Why must we be swift as the coursing river when we can be Chris?'
elif sentence == 27:
	hype = 'Why date a musician when you can date Chris?'
elif sentence == 28:
	hype = 'Bruh. Do you lift tho? Because Chris does.'
elif sentence == 29:
	hype = 'Because you know I\'m all about that Chris, no trouble.'
elif sentence == 30:
	hype = 'Why make a man out of you when you can be Chris?'
elif sentence == 31:
	hype = 'Hype for Chris Pacheco.'
elif sentence == 32:
	hype = 'Chris knows my name. My life is complete.'
elif sentence == 33:
	hype = 'I dislike Chris. Said no one ever.'
elif sentence == 34:
	hype = 'Why be yourself when you can be like Chris?'
elif sentence == 35:
	hype = 'Those dimples tho.'
elif sentence == 36:
	hype = 'Chris is mysterious as the dark side of the moon.'
elif sentence == 37:
	hype = 'Rumor has it, Beyonce and Jay-Z are naming their next kid after Chris Pacheco.'
elif sentence == 38:
	hype = 'T E A M   C H R I S'
elif sentence == 39:
	hype = 'Why shower when Chris can shower you?'

if sentence >= 0 and sentence < 19:
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

elif sentence >= 19:
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
