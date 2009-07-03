import datetime

from google.appengine.ext import db


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

    def current_xp(self):
        if self.relearnt_date:
            return self.level + relearnt_date
        else:
            return self.learnt_date
