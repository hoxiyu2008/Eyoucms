import re
import requests
import pytest
from common.yaml_util import YamlUtil

proxies = {
"http": "http://127.0.0.1:8888",
"https": "http://127.0.0.1:8888",
}

class TestSendRequest:
    @pytest.mark.parametrize('caseinfo',YamlUtil().read_testcase_yaml(yaml_name='get_phpsessionid.yml'))
    def test_get_phpsessid(self,caseinfo):
        url = caseinfo['url']
        data = caseinfo['data']
        rep = requests.post(url=url, data=data)
        pattern = "PHPSESSID=(.*?);"
        phpsessid=re.findall(pattern,str(rep.headers))[0]

        if 'PHPSESSID' in str(rep.headers):
            YamlUtil.write_extact_yaml(self,{'phpsessid':phpsessid})
            assert 'PHPSESSID' in str(rep.headers)
        else:
            print("!!!!!!!error!!!!!!!")

    @pytest.mark.parametrize('testcase_name,clumn_username,url', YamlUtil().readCsvList())
    def test_add_clumn(self,testcase_name,clumn_username,url):
        value = YamlUtil.read_extract_yaml('phpsessid')
        cookies = {"PHPSESSID": value}
        print(testcase_name)
        print(clumn_username)
        # data={"typename": "今天下雨",
        #       "dirname": "",
        #       "current_channel": "1",
        #       "parent_id": "",
        #       "diy_dirpath": "",
        #       "dirpath": "",
        #       "is_hidden": "0",
        #       "is_part": "0",
        #       "typelink": "",
        #       "englist_name": "",
        #       "litpic_local": "",
        #       "litpic_remote": "",
        #       "templist": "lists_article.htm",
        #       "tempview": "view_article.htm",
        #       "rulelist": "{栏目目录}/list_{tid}_{page}.html",
        #       "ruleview": "{栏目目录}/{aid}.html",
        #       "seo_title": "",
        #       "seo_keywords": "",
        #       "seo_description": "",
        #       "grade": "0"}
        rep = requests.post(url=url,data=clumn_username,cookies=cookies,proxies=proxies)
        # print(rep.text)

if __name__ == '__main__':
    pytest.main(['-vs'])


