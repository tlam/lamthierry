import datetime
from google.appengine.ext import bulkload, db
from google.appengine.tools import bulkloader
from myprofile.models import Skill

class SkillLoader(bulkloader.Loader):
#class SkillLoader(bulkload.Loader):
    def __init__(self):
        fields = [
            ('name', str),
            ('level', int),
            ('level_type', str),
            ('active', bool),
            ('picture', str),
            ('learnt_date', lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').date()),
            ('relearnt_date', lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').date() if x else None)
        ]

        #bulkload.Loader.__init__(self, 'Skill', fields)
        bulkloader.Loader.__init__(self, 'Skill', fields)

loaders = [SkillLoader]
#if __name__ == '__main__':
#bulkload.main(SkillLoader())
