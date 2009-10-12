import datetime

from google.appengine.ext import bulkload, db
from google.appengine.tools import bulkloader

from portfolios.models import Portfolio


class PortfolioLoader(bulkloader.Loader):
    """Translate each row of data into a Portfolio object"""
    def __init__(self):
        fields = [
            ('title', str),
            ('url', str),
            ('implementation', str),
            ('accomplishment', str),
            ('completed', lambda x: datetime.datetime.strptime(x, '%B %Y').date()),
            ('source', str),
            ('thumbnail', str),
            ('image', str)
        ]

        bulkloader.Loader.__init__(self, 'Portfolio', fields)

loaders = [PortfolioLoader]
