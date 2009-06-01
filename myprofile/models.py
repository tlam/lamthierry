from google.appengine.ext import db
import datetime

class Skill(db.Model):
    name = db.StringProperty()
    level = db.IntegerProperty()
    level_type = db.StringProperty(choices=set(['week', 'month', 'year']))
    active = db.BooleanProperty()
    picture = db.StringProperty()
    learnt_date = db.DateProperty('date learnt')
    relearnt_date = db.DateProperty('date relearnt', required=False)

    def __unicode__(self):
        return self.name

'''
s = Skill(name='Python', level=4, active=True, picture='python.gif', learnt_date=datetime.datetime.now())
s = Skill(name='Perforce', level=3, level_type='month', active=True, picture='python.gif', learnt_date=datetime.datetime.now())
s.put()
'''
