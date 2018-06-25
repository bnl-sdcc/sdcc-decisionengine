from decisionengine.framework.modules import Module
from decisionengine.framework.modules import de_logger
from decisionengine.framework.modules import Publisher
import abc



#class FakeCondorPublisher(Module.Module):
#    def __init__(self, set_of_parameters):
#        Module.Module.__init__(self, set_of_parameters)
#        self.logger = de_logger.get_logger()
#        self.logger.info('__init__ completed')
#

#class GenericFakeCondorPublisher(Publisher.Publisher):
#
#    __metaclass__ = abc.ABCMeta
#
#    def __init__(self, *args, **kwargs):
#        #super(FakeCondorPublisher, self).__init__(*args, **kwargs)
#        self.logger = de_logger.get_logger()
#        self.logger.info('__init__ completed')
#
#    @abc.abstractmethod
#    def consumes(self, name_list):
#	return None
#
#    def publish(self, data_block=None):
#	self.logger.debug('>>> starting publish()')
#
#
#class FakeCondorPublisher(GenericFakeCondorPublisher):
#	def __init__(self, *k, **kw):
#		super(FakeCondorPublisher, self).__init__(*k, **kw)
#
#	def consumes(self):
#		self.logger.debug('>>> starting consumes()')


class FakeCondorPublisher(Publisher.Publisher):
    def __init__(self, *args, **kwargs):
        self.logger = de_logger.get_logger()
        self.logger.info('>>> __init__ completed')

    def consumes(self):
        self.logger.info('>>> calling consumes')

    def publish(self, data_block=None):
        self.logger.info('>>> calling publish with data_block=%s' %data_block)
        #self.logger.info('>>> number of new glideins : %s' %data_block['n_glideins'][0][0])
