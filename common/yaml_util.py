import csv
import os
import yaml


class YamlUtil:
    def read_extract_yaml(self):
        with open(os.getcwd() + "/extract.yml", mode='r', encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data[self]

    def write_extact_yaml(self, data):
        with open(os.getcwd() + "/extract.yml", mode='w', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    def clear_extact_yaml(self):
        with open(os.getcwd() + "/extract.yml", mode='w', encoding='utf-8') as f:
            f.truncate()

    # 读取测试用例yaml
    def read_testcase_yaml(self, yaml_name):
        with open(os.getcwd() + "/common/" + yaml_name, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    # 读取csv文件
    def readCsvList(self):
        lists=[]
        with open(file='D:\\pythonProject\\test_data.csv',mode="r",encoding="gb2312") as f:
            reader = csv.reader(f)
            next(reader)
            for item in reader:
                lists.append(item)
        return lists


if __name__ == '__main__':
    print(YamlUtil().readCsvList())