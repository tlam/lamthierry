import datetime

from google.appengine.ext import db

class Portfolio(db.Model):
    title = db.StringProperty()
    url = db.StringProperty()
    implementation = db.StringProperty()
    accomplishment = db.StringProperty()
    completed = db.DateProperty()
    source = db.StringProperty()
    thumbnail = db.StringProperty()

    def __unicode__(self):
        return self.title
