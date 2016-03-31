## 文档结构

**util.config** 所有可以用edit_config进行配置的操作
    - `flow` 流量调优
    - `ipte` 业务拓扑
    - `networkte` 网络拓扑
    - `delete` 删除配置信息


**util.get** 文件主要用来查看控制器上的配置信息
**util.conf** 主要用来获取配置文件中的信息
**util.test** 存放单元测试相关信息
    - mock_manager 是模拟与控制器连接对象的

**main** 存放主程序
**OLD** 之前的程序

## 流程
    1. 建立连接
    2. 读取配置文件，根据operationid进行相关操作
    3. 根据operatioid，将相关操作参数封装为xml
    4. 向控制器发送配置信息