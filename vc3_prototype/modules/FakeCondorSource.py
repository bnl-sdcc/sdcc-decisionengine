#!/usr/bin/python
import argparse
import pprint
import pandas
import numpy

from decisionengine.framework.modules import Source
from decisionengine.framework.modules import de_logger

from libfactory import htcondorlib, info


PRODUCES = ['job_manifests']


class FakeCondorSource(Source.Source):

    def __init__ (self, *args, **kwargs):
        #kif args:
        #k    config = args[0]
        #kelse:
        #k    config = {}

    self.logger = de_logger.get_logger()
    self.schedd = htcondorlib.HTCondorSchedd()
    self.logger.info('__init__ completed')


    def produces(self):
        """
        Return list of items produced
        """
    self.logger.debug('>>> starting produces()')
        return PRODUCES


    def acquire(self):
        """
        Acquire jobs from the HTCondor Schedd
        :rtype: :obj:`~pd.DataFrame`
        """

        self.logger.debug('starting acquire()')

        job_l = self.schedd.condor_q(['jobstatus', 'clusterid', 'procid'])  
        job_l_status = info.StatusInfo(job_l)
        group_by_status = info.GroupByKey('jobstatus')
        length = info.Length()
        job_l_status = job_l_status.group(group_by_status)
        job_l_status = job_l_status.reduce(length)
        return {'job_manifests': job_l_status.getraw()}

        ## fake output of condor_q
        #job_l = [
        #         {'clusterid':1, 'procid':0, 'jobstatus':1},
        #         {'clusterid':1, 'procid':1, 'jobstatus':2},
        #        ]
        #
        #dataframe = pandas.DataFrame()
        #df = pandas.DataFrame(job_l)
        #dataframe = dataframe.append(df, ignore_index=True)
        #    
        #self.logger.debug('>>> finishing acquire(). Returning %s' %dataframe)
        #return {'job_manifests': dataframe}

