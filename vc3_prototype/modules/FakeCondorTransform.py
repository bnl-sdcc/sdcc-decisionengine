import numpy as np
import pandas as pd

from decisionengine.framework.modules import Transform
from decisionengine.framework.modules import de_logger



CONSUMES = ["job_manifests"]
PRODUCES = ["n_glideins"]

class FakeCondorTransform(Transform.Transform):

    def __init__(self, param_dict):
       	self.logger = de_logger.get_logger()
        self.logger.info('__init__ completed')


    def consumes(self): 
        self.logger.debug('>>> starting consumes()')
	return CONSUMES

    def produces(self,schema_id_list): 
        self.logger.debug('>>> starting produces()')
	return PRODUCES

    def transform(self, DataBlock):
        self.logger.debug('>>> starting transform() with input DataBlock = %s of type %s' %(DataBlock, DataBlock.__class__.__name__))
        self.logger.debug('>>> content of Datablock = %s of type %s ' %(DataBlock['job_manifests'], DataBlock['job_manifests'].__class__.__name__))
        #self.logger.debug('>>> content of Datablock = %s' %DataBlock['job_manifests'][0]['procid'] )
        #self.logger.debug('>>> content of Datablock = %s of type %s ' %(DataBlock['job_manifests'].getraw()))

	    df = pd.DataFrame([2])  # NOTE: it is not possible to initialize a DataFrame with just a number
        #self.logger.debug('>>> content of output dataframe = %s' %df) 
	    # the output is 
	    #    0
	    # 0  2
	    #
        #return {PRODUCES[0]:df}
        return {PRODUCES[0]:2}
