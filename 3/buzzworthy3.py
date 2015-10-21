import twitter
from random import randrange
from OAuthSettings3	 import settings

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

begin = randrange(0,20)
if begin == 0:
	hype = 'YAS'
elif begin == 1:
	hype = 'CHRIS'
elif begin == 2:
	hype = 'OMG'
elif begin == 3:
	hype = 'GO'
elif begin == 4:
	hype = 'WIN'
elif begin == 5:
	hype = 'SLAY'
elif begin == 6:
	hype = 'ASDFGHJKL'
elif begin == 7:
	hype = 'TURNT'
elif begin == 8:
	hype = 'FUPAC^^^'
elif begin == 9:
	hype = 'CAN\'T WAIT'
elif begin == 10:
	hype = 'IDK'
elif begin == 11:
	hype = 'TODAY'
elif begin == 12:
	hype = 'HYPE'
elif begin == 13:
	hype = 'HYPED'
elif begin == 14:
	hype = 'SO HYPED'
elif begin == 15:
	hype = 'YOU GOT THIS'
elif begin == 16:
	hype = 'MR BUZZWORTHY'
elif begin == 17:
	hype = 'DOPE'
elif begin == 18:
	hype = 'CLUTCH'
elif begin == 19:
	hype = 'FIYAH'

middle = randrange(0,20)
if middle == 0:
	hyper = 'YAS'
elif middle == 1:
	hyper = 'CHRIS'
elif middle == 2:
	hyper = 'OMG'
elif middle == 3:
	hyper = 'GO'
elif middle == 4:
	hyper = 'WIN'
elif middle == 5:
	hyper = 'SLAY'
elif middle == 6:
	hyper = 'ASDFGHJKL'
elif middle == 7:
	hyper = 'TURNT'
elif middle == 8:
	hyper = 'FUPAC^^^'
elif middle == 9:
	hyper = 'CAN\'T WAIT'
elif middle == 10:
	hyper = 'IDK'
elif middle == 11:
	hyper = 'TODAY'
elif middle == 12:
	hyper = 'HYPE'
elif middle == 13:
	hyper = 'HYPED'
elif middle == 14:
	hyper = 'SO HYPED'
elif middle == 15:
	hyper = 'YOU GOT THIS'
elif middle == 16:
	hyper = 'MR BUZZWORTHY'
elif middle == 17:
	hyper = 'DOPE'
elif middle == 18:
	hyper = 'CLUTCH'
elif middle == 19:
	hyper = 'FIYAH'

end = randrange(0,20)
if end == 0:
	hypest = 'YAS'
elif end == 1:
	hypest = 'CHRIS'
elif end == 2:
	hypest = 'OMG'
elif end == 3:
	hypest = 'GO'
elif end == 4:
	hypest = 'WIN'
elif end == 5:
	hypest = 'SLAY'
elif end == 6:
	hypest = 'ASDFGHJKL'
elif end == 7:
	hypest = 'TURNT'
elif end == 8:
	hypest = 'FUPAC^^^'
elif end == 9:
	hypest = 'CAN\'T WAIT'
elif end == 10:
	hypest = 'IDK'
elif end == 11:
	hypest = 'TODAY'
elif end == 12:
	hypest = 'HYPE'
elif end == 13:
	hypest = 'HYPED'
elif end == 14:
	hypest = 'SO HYPED'
elif end == 15:
	hypest = 'YOU GOT THIS'
elif end == 16:
	hypest = 'MR BUZZWORTHY'
elif end == 17:
	hypest = 'DOPE'
elif end == 18:
	hypest = 'CLUTCH'
elif end == 19:
	hypest = 'FIYAH'

tweet = hype + ' ' + hyper + ' ' + hypest + ' ' + christag + ' ' + mrpitag

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
