import pytest

from common.yaml_util import YamlUtil


@pytest.fixture(scope="function")
def conn_database():
    print("连接数据库")
    print("断开数据库")

@pytest.fixture(scope="session",autouse=True)
def clear_yaml(self=None):
    YamlUtil.clear_extact_yaml(self)