import datetime

from google.appengine.ext import db

class Portfolio(db.Model):
    title = db.StringProperty()
    slug = db.StringProperty()
    url = db.StringProperty()
    implementation = db.StringProperty()
    accomplishment = db.StringProperty()
    completed = db.DateProperty()
    source = db.StringProperty()
    thumbnail = db.StringProperty()
    image = db.StringProperty()

    def __unicode__(self):
        return self.title
