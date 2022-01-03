# -*- coding:utf-8 -*-

import time
from bert_base.client import BertClient
from pro_process import load_label_config, pro_process, pro_process2


# 指定服务器的IP
with BertClient(ip='0.0.0.0', ner_model_dir='./output', 
				show_server_config=False, check_version=False,
				check_length=False, mode='NER') as bc:
    start_t = time.perf_counter()
    str = '神清，颈静脉无怒张，双肺呼吸音清，未闻及干湿罗音。心界不大，心率96次/分，律齐，未闻及无杂音。腹平软，无压痛及反跳痛，四肢活动自如，肌力V级，肌张力正常，双下肢无浮肿。病理征未引出。2016-4-3我院BNP 335pg/ml；心肌酶：AST 118U/L，LDH 705U/L，CK 835u/l，CKMB 108.5u/l; TnT:0.39ng/ml， TnI 19.6ng/ml；血常规未见明显异常；胸片：双肺纹理稍增强；心电图：窦性心律；入科心电图：V1-3 ST段改变。  术前诊断:1. 冠心病 急性前壁心肌梗死 心脏不大 窦性心律 心功能I级(killip分级)；2.高血压病2级 很高危。'
    rst = bc.encode([str])  #测试同时输入两个句子，多个输入同理
    print('rst:', rst) 
    # body, chec, symp, cure, dise = pro_process(str, rst[0])
    body, chec, cure, symp, dise = pro_process2(str, rst[0])
    print('body', body)
    print('check', chec)
    print('symp', symp)
    print('cure', cure)
    print('dise', dise)
    print(time.perf_counter() - start_t)
    
