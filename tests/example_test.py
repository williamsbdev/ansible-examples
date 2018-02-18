from glob import glob
from os.path import dirname
from os.path import join
from subprocess import check_call

import pytest


def get_yaml_files():
    for file_name in glob(join(dirname(__file__), '../*.yml')):
        yield file_name


@pytest.fixture(scope="module", params=get_yaml_files())
def yaml_file(request):
    yield request.param


class TestAnsibleLint(object):

    def test_ansible_lint_compliance(self, yaml_file):
        # There are 16 Ansible linting rules
        # I chose to do the string join because it makes
        # it easier to see what changes in the command
        # if you exclude another rule
        command = ' '.join([
            'ansible-lint',
            '-x',
            'ANSIBLE0011',
            yaml_file
        ])
        try:
            result = check_call(command, shell=True)
        except Exception:
            result = 1
        assert 0 == result
