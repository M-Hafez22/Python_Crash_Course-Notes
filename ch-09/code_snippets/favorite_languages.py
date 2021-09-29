from collections import OrderedDict

favorite_languages = OrderedDict()
# favorite_languages = {}

favorite_languages['hafez'] = 'JavaScript'
favorite_languages['linus'] = 'c'
favorite_languages['edward'] = 'python'
favorite_languages['phil'] = 'JavaScript'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
