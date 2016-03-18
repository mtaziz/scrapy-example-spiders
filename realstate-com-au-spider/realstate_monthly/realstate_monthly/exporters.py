# from scrapy.conf import settings
# from scrapy.exporters import CsvItemExporter

# class CSVItemExporter(CsvItemExporter):
#     def __init__(self, *args, **kwargs):
#         join_multivalued = settings.get('CSV_JOIN_MULTIVALUED', None)
#         if join_multivalued:
#             kwargs['join_multivalued'] = join_multivalued
#         kwargs['delimiter'] = settings.get('CSV_DELIMITER', ',')
#         kwargs['fields_to_export'] = settings.get('EXPORT_FIELDS', None)
#         super(CSVItemExporter, self).__init__(*args, **kwargs)

# class CsvItemExporter (scrapy.contrib.exporter.CsvItemExporter):

#     def __init__ (self, *args, **kwargs):
#         kwargs['fields_to_export'] = [
#             'search_title', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
#             'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'isbn', 'url']
#         super(CsvItemExporter, self).__init__(*args, **kwargs)

#  """
# The standard CSVItemExporter class does not pass the kwargs through to the
# CSV writer, resulting in EXPORT_FIELDS and EXPORT_ENCODING being ignored
# (EXPORT_EMPTY is not used by CSV).
# """

from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter
#CSV importer
class CSVRealstateItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
    	#kwargs['delimiter'] = settings.get('CSV_DELIMITER', ',')
        #kwargs['fields_to_export'] = settings.getlist('EXPORT_FIELDS') or None
        kwargs['fields_to_export'] = ['links', 'title', 'subur_name', 'unit_mly_jan', 'unit_mly_feb', 'unit_mly_mar', 'unit_mly_apr', 'unit_mly_may', 
        'unit_mly_jun', 'unit_mly_jul', 'unit_mly_aug', 'unit_mly_sep', 'unit_mly_oct', 'unit_mly_nov', 
        'unit_mly_dec', 'unit_mly_p_jan', 'unit_mly_p_feb', 'unit_mly_p_mar', 
        'unit_mly_p_apr', 'unit_mly_p_may', 'unit_mly_p_jun', 'unit_mly_p_jul', 'unit_mly_p_aug', 'unit_mly_p_sep', 
        'unit_mly_p_oct', 'unit_mly_p_nov', 'unit_mly_p_dec', 'unit_mly_nos_jan', 
        'unit_mly_nos_feb', 'unit_mly_nos_mar', 'unit_mly_nos_apr', 'unit_mly_nos_may', 'unit_mly_nos_jun', 
        'unit_mly_nos_jul', 'unit_mly_nos_aug', 'unit_mly_nos_sep', 'unit_mly_nos_oct', 'unit_mly_nos_nov', 'unit_mly_nos_dec',]

        #kwargs['encoding'] = settings.get('EXPORT_ENCODING', 'utf-8')
        super(CSVRealstateItemExporter, self).__init__(*args, **kwargs)