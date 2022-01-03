import os
import json

def load_label_config(label_config:str):
    """
    :param label_config: path of label config, .json
    :return: dir whose key is label, value is idx
    """
    with open(label_config) as f:
        data = json.load(f)
        label = data['config']['vocab2idx']
    f.close()
    return label

def pro_process(text: str, rst: list):
    state = ''
    length = len(rst)
    # body_idx, chec_idx, symp_idx, cure_idx, dise_idx
    body_idx, chec_idx, symp_idx, cure_idx, dise_idx = [], [], [], [], []
    tmp_body_B, tmp_chec_B, tmp_symp_B, tmp_cure_B, tmp_dise_B = 0, 0, 0, 0, 0
    tmp_body_E, tmp_chec_E, tmp_symp_E, tmp_cure_E, tmp_dise_E = 0, 0, 0, 0, 0
    for cnt in range(length):
        if rst[cnt] == '[PAD]':     # 0
            pass
        elif rst[cnt] == 'O':       # 1
            pass
        elif rst[cnt] == 'I-chec':  # 2
            pass
            # if state == 'B-chec':
            #     continue;
            # else:
            #     state = 'O'
        elif rst[cnt] == 'I-body':  # 3
            pass
            # if state == 'B-body':   # 4
            #     continue
            # else:
            #     state = 'O'
        elif rst[cnt] == 'B-body':  # 4
            if state == 'O':
                state = 'B-body'
                tmp_body_B = cnt
            else:
                state = 'B-body'
                tmp_body_B = cnt
        elif rst[cnt] == 'B-chek':  # 5
            if state == 'O':
                state = 'B-chec'
                tmp_chec_B = cnt
            else:
                state = 'B-chec'
                tmp_chec_B = cnt
        elif rst[cnt] == 'E-chec':  # 6
            if state == 'B-chec':
                tmp_chec_E = cnt
                chec_idx.append([tmp_chec_B, tmp_chec_E])
                state = 'O'
            else:
                tmp_chec_E = cnt
                chec_idx.append([tmp_chec_B, tmp_chec_E])
                state = 'O'
        elif rst[cnt] == 'I-cure':  # 7
            pass
            # if state == 'B-cure':
            #     continue
            # else:
            #     state = 'O'
        elif rst[cnt] == 'E-body':  # 8
            if state == 'B-body':
                tmp_body_E = cnt
                body_idx.append([tmp_body_B, tmp_body_E])
                state = 'O'
            else:
                tmp_body_E = cnt
                body_idx.append([tmp_body_B, tmp_body_E])
                state = 'O'
        elif rst[cnt] == 'B-symp':  # 9
            if state == 'O':
                state = 'B-symp'
                tmp_symp_B = cnt
            else:
                state = 'B-symp'
                tmp_symp_B = cnt
        elif rst[cnt] == 'E-symp':  # 10
            if state == 'B-symp':
                state = 'O'
                tmp_symp_E = cnt
                symp_idx.append([tmp_symp_B, tmp_symp_E])
            else:
                state = 'O'
                tmp_symp_E = cnt
                symp_idx.append([tmp_symp_B, tmp_symp_E])
        elif rst[cnt] == 'I-dise':  # 11
            pass
        elif rst[cnt] == 'B-cure':  # 12
            if state == 'O':
                state = 'B-cure'
                tmp_cure_B = cnt
            else:
                state = 'B-cure'
                tmp_cure_B = cnt
        elif rst[cnt] == 'E-cure':  # 13
            if state == 'B-cure':
                state = 'O'
                tmp_cure_E = cnt
                cure_idx.append([tmp_cure_B, tmp_cure_E])
            else:
                state = 'O'
                tmp_cure_E = cnt
                cure_idx.append([tmp_cure_B, tmp_cure_E])
        elif rst[cnt] == 'E-dise':  # 14
            if state == 'B-dise':
                tmp_dise_E = cnt
                dise_idx.append([tmp_dise_B, tmp_dise_E])
                state = 'O'
            else:
                tmp_dise_E = cnt
                dise_idx.append([tmp_dise_B, tmp_dise_E])
                state = 'O'
        elif rst[cnt] == 'B-dise':  # 15
            if state == 'O':
                state = 'B-dise'
                tmp_dise_B = cnt
            else:
                state = 'B-dise'
                tmp_dise_B = cnt
        elif rst[cnt] == 'I-symp':  # 16
            pass
    body, chec, symp, cure, dise = [], [], [], [], []

    for idx in body_idx:
        body.append(text[idx[0]:idx[1]+1])
    for idx in chec_idx:
        chec.append(text[idx[0]:idx[1]+1])
    for idx in symp_idx:
        symp.append(text[idx[0]:idx[1]+1])
    for idx in cure_idx:
        cure.append(text[idx[0]:idx[1]+1])
    for idx in dise_idx:
        dise.append(text[idx[0]:idx[1]+1])

    # return body_idx, chec_idx, symp_idx, cure_idx, dise_idx
    return body, chec, symp, cure, dise

def pro_process2(text, rst):
    length = len(rst)
    body, chec, cure, symp, dise = "", "", "", "", ""
    for cnt in range(length):
        if rst[cnt] == '[PAD]':
            pass
        elif rst[cnt] == 'O':
            pass
        elif rst[cnt][2] == 'b':
            body += text[cnt]
            if rst[cnt][0] == 'E':
                body += ' '
        elif rst[cnt][2] == 'c':
            if rst[cnt][3] == 'h':
                chec += text[cnt]
                if rst[cnt][0] == 'E':
                    body += ' '
            else:
                print("ccccure:", cnt)
                cure += text[cnt]
                if rst[cnt][0] == 'E':
                    body += ' '
        elif rst[cnt][2] == 's':
            symp += text[cnt]
            if rst[cnt][0] == 'E':
                body += ' '
        else:
            dise += text[cnt]
            if rst[cnt][0] == 'E':
                body += ' '

    return body, chec, cure, symp, dise



if __name__=='__main__':
    label_config = './config/label_processor.json'
    label = load_label_config(label_config)
    rst = [[]]
    length = len(rst[0])







# [PAD] 0
# O 1
# I-chec 2
# I-body 3
# B-body 4
# B-chec 5
# E-chec 6
# I-cure 7
# E-body 8
# B-symp 9
# E-symp 10
# I-dise 11
# B-cure 12
# E-cure 13
# E-dise 14
# B-dise 15
# I-symp 16





