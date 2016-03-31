#coding:utf8
from functools import partial
import manager
from util.config.flow import *
from util.config.ipte import *
from util.config.networkte import *
from util.conf import getconf
from util.config.delete import *

host = "202.102.27.50"
port = 22
username = 'root123'
password = 'Huawei@123'


def main():
    '''
    1 建立连接
    2 读取配置文件，根据operationid进行相关操作
    3 根据operatioid，将相关操作参数封装为xml
    4 向控制器发送配置信息
    '''
    m = None
    # 建立连接
    try:
        m = manager.connect \
            (host, port, username, device_params={'name': 'huawei'})
    except Exception as e:
        print e
        raise Exception("connect failed")
    # del_flow这个函数比较特殊，它在del之前需要先连上服务器获取当前的流的配置信息再决定如何删除
    # 需要两个参数 连接对象m,和配置信息，为了与其他函数相应的操作相一致，故而固定其中的一个参数
    del_flow_p = partial(del_flow, m)

    #获取配置参数
    data = getconf()
    operation = data.get('operation_id', 0)
    if not operation: raise Exception(u"operation_id不存在")

    #配置id和相应的操作对应表（id->操作函数）
    id2operation = {
        # 流量调整
        '11': vip_flow,
        '12': AS_flow,
        '13': src_dst_flow,
        # 网络拓扑
        '21': networkte_enable,
        '22': networkte_link,
        '23': networkte_node,
        '24': fp_static_peer,
        # 业务拓扑
        '31': ipte_enable,
        '32': ipte_link,
        '33': ipte_node,
        '34': ipte_south_enable,
        '35': ipte_link_policy,
        # 查询接口

        # 删除接口
        '51': del_flow_p,
    }

    xml = id2operation[operation](data)

    #发送配置
    try:
        m.edit_config(target='candidate', config=xml)
        m.commit()
    except Exception as e:
        print "!!!!!!erro!!!!!!r" + str(e)


if __name__ == '__main__':
    main()
