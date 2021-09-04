class MyMotor():
    def __init__(self):

        # 机器当前运行状态
        self.status_list = ['正常','故障','停机']
        # 机器当前故障状态
        self.status_fault_list = ['正常','开路','匝间短路']
        # 机器当前故障处理状态
        self.status_hold_list = ['无','已处理','待处理']
        #机器编号
        self.id = '001'
        # 加载数据地址
        self.data_path = 'page_online/data/normal_1'
        # 运行状态
        self.status = '停机'
        # 故障状态
        self.status_fault = '正常'
        # 故障处理状态
        self.status_hold ='无'