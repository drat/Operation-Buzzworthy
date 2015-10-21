import twitter
from random import randrange
from OAuthSettings5 import settings

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

sentence = randrange(0,80)
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
elif sentence == 40:
	hype = 'Chris\'s awkward silences aren\'t even awkward'
elif sentence == 41:
	hype = 'Chris is the type to do good for the sake of being good and genuine -- not for the sake of acknowledgement'
elif sentence == 42:
    hype = 'I would share my fruit gushers with Chris'
elif sentence == 43:
	hype = 'Priorities: Tweeting about Chris'
elif sentence == 44:
	hype = 'Chris makes babies smile'
elif sentence == 45:
    hype = 'My mother wonders why I can\'t be more like Chris'
elif sentence == 46:
    hype = 'Chris is more fun than bubble wrap'
elif sentence == 47:
    hype = 'Did you know that Chris it the 6th member of 1D? They had to kick him out because he was everyone\'s favorite.'
elif sentence == 48:
    hype = 'My mom always said that there would be haters. Not everyone can love ya. Except for Chris everybody loves Chris'
elif sentence == 49:
    hype = 'Chris, do you have a map? I just keep getting lost in your eyes.'
elif sentence == 50:
	hype = 'Every second, every minute, man I swear that Chris can get it'
elif sentence == 51:
	hype = 'Showers women and showers himself.'
elif sentence == 52:
	hype = 'Chris is the only right in this world full of wrongs.'
elif sentence == 53:
	hype = 'Chris by Chris Pacheco for Pacheco by Chris Pacheco'
elif sentence == 54:
	hype = 'Cameras aren\'t worthy to take Chris\'s picture.'
elif sentence == 55:
	hype = 'I would erase the memory of ever meeting Chris just so I can experience that moment all over again'
elif sentence == 56:
	hype = 'Why aren\'t there museums dedicated to Chris?'
elif sentence == 57:
	hype = 'I wish I was Chris\'s mirror'
elif sentence == 58:
	hype = 'Chris formed Destiny\'s Child'
elif sentence == 59:
	hype = 'During our darkest moments, we must focus to see Chris'
elif sentence == 60:
	hype = 'Chris rocks'
elif sentence == 61:
	hype = 'Sometimes I walk a little faster in the school hallway just to get next to Chris'
elif sentence == 62:
	hype = 'Chris is as sweet as lemonade on a hot summer day'
elif sentence == 63:
	hype = 'I don\'t think my parents will ever forgive me for not being Chris Pacheco. First off mom and dad, I\'m a girl.'
elif sentence == 64:
	hype = 'Chris, Yoda only Wan for me'
elif sentence == 65:
	hype = 'All these ceiling fans, and Chris is still cooler than you'
elif sentence == 66:
	hype = 'Eat, school, work, gym, drink, Chris, Chris, Chris.'
elif sentence == 67:
	hype = 'Sam Smith\'s ENTIRE album is about Chris.'
elif sentence == 68:
	hype = 'Kanye thinks Chris is a creative genius.'
elif sentence == 69:
	hype = 'But then again, if I go to sleep, Chris might be in my dreams..'
elif sentence == 70:
	hype = 'I just gotta let you know that I\'m really feelin\' your style, Chris'
elif sentence == 71:
	hype = 'Omg Chris favorited my tweet'
elif sentence == 72:
	hype = 'They changed \'Who Wants to be a Millionaire\' to \'Who Wants to be Chris\''
elif sentence == 73:
	hype = 'Chris would be the last survivor on The Walking Dead'
elif sentence == 74:
	hype = 'I would volunteer to take Chris\' place in the Hunger Games'
elif sentence == 75:
	hype = 'Chris could bring back dinosaurs if he wanted to'
elif sentence == 76:
	hype = 'For exams: the correct answer is always C. C is for Chris.'
elif sentence == 77:
	hype = 'The last time I took a trip to The Met, I saw a statue of Chris'
elif sentence == 78:
	hype = 'I pray my babies are as much of a gentleman as Chris is.'
elif sentence == 79:
	hype = 'When I grow up, I want to be Chris.'

operator = randrange(0,34) 
if operator == 0:
    adj = 'gorgeous'
elif operator == 1:
    adj = 'stunning'
elif operator == 2:
    adj = 'cute'
elif operator == 3:
    adj = 'bae'
elif operator == 4:
    adj = 'lovely'
elif operator == 5:
    adj = 'attractive'
elif operator == 6:
    adj = 'handsome'
elif operator == 7:
    adj = 'appealing'
elif operator == 8:
    adj = 'admirable'
elif operator == 9:
    adj = 'inspiring'
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
    adj = 'gentlemanly'
elif operator == 17:
    adj = 'buzzworthy'
elif operator == 18:
    adj = 'exquisite'
elif operator == 19:
    adj = 'excellent'
elif operator == 20:
    adj = 'incredible'
elif operator == 21:
    adj = 'wondrous'
elif operator == 22:
    adj = 'fine'
elif operator == 23:
    adj = 'foxy'
elif operator == 24:
    adj = 'amazing'
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
    adj = 'heavenly'
elif operator == 31:
    adj = 'chiseled'
elif operator == 32:
    adj = 'statuesque'
elif operator == 33:
    adj = 'beautiful'

if sentence >= 0 and sentence < 19:
	tweet = subject + ' ' + adj + ' ' + ending + ' ' + christag + ' ' + mrpitag
elif sentence >= 19:
	tweet = hype + ' #' + adj + ' ' + christag + ' ' + mrpitag

print tweet
#post to twitter
"""try:
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
"""