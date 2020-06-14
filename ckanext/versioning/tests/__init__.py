import json
import shutil
import tempfile

from ckan.common import config
from ckan.tests import helpers

from ckanext.versioning import model


class FunctionalTestBase(helpers.FunctionalTestBase):

    _load_plugins = ['package_versioning', 'resource_versioning']

    def setup(self):
        if not model.tables_exist():
            model.create_tables()
        super(FunctionalTestBase, self).setup()


class MetastoreBackendTestBase(FunctionalTestBase):

    def setup(self):
        super(MetastoreBackendTestBase, self).setup()
        self._backend_dir = tempfile.mkdtemp()
        config['ckanext.versioning.backend_config'] = json.dumps({"uri": self._backend_dir})

    def teardown(self):
        super(MetastoreBackendTestBase, self).setup()
        shutil.rmtree(self._backend_dir)
