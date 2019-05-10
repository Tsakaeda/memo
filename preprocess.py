# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import re


def delete_gavage_char(src_str):
    '''
    @brief �����A�A���t�@�x�b�g�A�Ђ炪�ȁA�J�^�J�i�A�����A�悭�g���L���ȊO�̕������̏����֐�
    @param src_str ������ ������ȊO�����͂��ꂽ��G���[�ɂȂ�
    
    ���LURL�����ĕK�v�ɉ����ĕҏW
    https://ja.wikipedia.org/wiki/Unicode%E4%B8%80%E8%A6%A7_0000-0FFF
    
    �ȉ��A���j�R�[�h�̐���
    \u0021-\u007E: �����A�A���t�@�x�b�g(���p)
    \u2E80-\u2FFF: ����
    \u3041-\u30FF: �Ђ炪�ȁA�J�^�J�i�Ȃ�
    \u4E00-\u9FFF: ����(��p�A���p�܂�)(\u3400-\4DFF��������������������)
    \uF900-\uFAFF: ����
    \uFF00-\uFF9F: �S�p�A���t�@�x�b�g�A�S�p�L���A���p�J�^�J�i�Ȃ�
    '''
    return re.sub(r'[^\u0021-\u007E\u2E80-\u2FFF\u3041-\u30FF\u4E00-\u9FFF\uF900-\uFAFF\uFF00-\uFF9F]', '', src_str)



