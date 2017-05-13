import nltk

#speech made by George W Bush
trainText  = nltk.corpus.state_union.raw("2005-GWBush.txt")
sampleText = nltk.corpus.state_union.raw("2006-GWBush.txt") #check nltk.corpus.state_union.fileids() for all avaliable speeches

'''
    Here we will use PunktSentenceTokenizer which is unsupervised learning
    It could be trained according to our need but it is pretrained
'''
punktSentTokenizer = nltk.PunktSentenceTokenizer(trainText)

tokens = punktSentTokenizer.tokenize(sampleText)
'''
POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
'''

def processContent():
    try:
        for word in tokens:
            tagged = nltk.pos_tag(nltk.word_tokenize(word))
            print(tagged)
    except Exception as e:
        print(str(e))

processContent()

#abbreviation

print(nltk.help.upenn_tagset())