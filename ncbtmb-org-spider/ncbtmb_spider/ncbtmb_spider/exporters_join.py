from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter

class CSVColripItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        kwargs['fields_to_export'] = settings.getlist('EXPORT_FIELDS') or None
        kwargs['encoding'] = settings.get('EXPORT_ENCODING', 'utf-8')
        super(CSVColripItemExporter, self).__init__(*args, **kwargs)
        self._join_multivalued = settings.get('MY_CSV_DELIMITER', ',')