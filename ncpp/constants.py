# Module holding application constants.
from ncpp.util.filepaths import getAbsolutePath

APPLICATION_LABEL = 'ncpp'
CONFIG_FILEPATH = '/usr/local/ocgis/ocgis.cfg'
GEOMETRIES_FILEPATH = getAbsolutePath('config/ocgis_geometries.json')
CALCULATIONS_FILEPATH = getAbsolutePath('config/ocgis_calc.json')
DATASETS_DB = getAbsolutePath('../database/datasets.sqlite')

def enum(**enums):
    return type('Enum', (), enums)

    def isComplete(self):
        if (self.status=='ProcessSucceeded' or self.status=='ProcessFailed' or self.status=='Exception'):
            return True
        elif (self.status=='ProcessStarted'):
            return False
        elif (self.status=='ProcessAccepted' or self.status=='ProcessPaused'):
            return False
        else:
            raise Exception('Unknown process execution status: %s' % self.status)


JOB_STATUS = enum(UNKNOWN='Status Unknown', STARTED='Process Started', RUNNING='Process Running', SUCCESS='Process Succeeded', 
                  FAILED='Process Failed', ACCEPTED='Process Accepted', PAUSED='ProcessPaused', ERROR='Error')

MONTH_CHOICES = ( (1,'Jan'), (2,'Feb'), (3,'Mar'), (4,'Apr'),   (5,'May'),   (6,'Jun'),
                  (7,'Jul'), (8,'Aug'), (9,'Sep'), (10,'Oct'), (11,'Nov'), (12,'Dec'))
MONTH_DICT = dict(MONTH_CHOICES) # transform tuples to dictionary for easy indexing of keys

NO_VALUE_OPTION = ("","-- Please Select --")

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"