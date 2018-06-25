from decisionengine.framework.modules import Module
from decisionengine.framework.modules import de_logger
from decisionengine.framework.modules import Publisher

class FakeCondorPublisher(Publisher.Publisher):
    def __init__(self, *args, **kwargs):
        self.logger = de_logger.get_logger()
        self.logger.info('>>> __init__ completed')

    def consumes(self):
        self.logger.info('>>> calling consumes')

    def publish(self, data_block=None):
        self.logger.info('>>> calling publish with data_block=%s' %data_block)
        #self.logger.info('>>> number of new glideins : %s' %data_block['n_glideins'][0][0])
        self.logger.info('>>> number of new glideins : %s' %data_block['n_glideins'])

    vc3 = VC3()
    vc3.list()


# -----------------------------------------------------------------------------

from vc3client.client import VC3ClientAPI
from vc3infoservice.infoclient import InfoClient
import datetime
from ConfigParser import SafeConfigParser
import os

class VC3(object):

    def __init__(self):

    self.log = de_logger.get_logger()
        self.config = SafeConfigParser()
        self.config.readfp(open('/etc/vc3/vc3-client.conf'))
        self.certfile  = os.path.expanduser(self.config.get('netcomm','certfile'))
        self.keyfile   = os.path.expanduser(self.config.get('netcomm', 'keyfile'))
        self.chainfile = os.path.expanduser(self.config.get('netcomm','chainfile'))
    self.client = VC3ClientAPI(self.config)     


    def list(self):

    self.log.debug('list of resources = %s' %self.client.listResources())       


    def request(self):


        now = datetime.datetime.utcnow()
        t_delta = datetime.timedelta(hours=1)
        expiration = now + t_delta
        expiration = expiration.replace(microsecond=0).isoformat()


        request = self.client.defineRequest("hepcloud", 
                                            "jcaballero", 
                                            "jcaballero-hepcloud", 
                                            ["jcaballero.vc3-test-pool"], 
                                            ["jcaballero-hepcloud"],
                                            "static-balanced",
                                            expiration,
                                            "hepcloud")

        self.client.storeRequest(request, "jcaballero")



