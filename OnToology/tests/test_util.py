

from tests import MongoTestCase
from OnToology.models import *
from api_util import *


class TestUtil(MongoTestCase):
    def setUp(self):
        delete_all_repos_from_db()

    def test_delete_repos_from_db(self):
        delete_all_repos_from_db()

    def test_create_repo(self):
        create_repo()

    def test_create_user(self):
        create_user()

    def test_delete_all_publishnames(self):
        delete_all_publishnames()

    def test_create_publishname(self):
        create_publishname()

    def test_get_repo_resource_dir(self):
        get_repo_resource_dir()

