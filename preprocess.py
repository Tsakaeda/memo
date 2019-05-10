# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import re


def delete_gavage_char(src_str):
    '''
    @brief 数字、アルファベット、ひらがな、カタカナ、漢字、よく使う記号以外の文字を大体消す関数
    @param src_str 文字列 文字列以外が入力されたらエラーになる
    
    下記URLを見て必要に応じて編集
    https://ja.wikipedia.org/wiki/Unicode%E4%B8%80%E8%A6%A7_0000-0FFF
    
    以下、ユニコードの説明
    \u0021-\u007E: 数字、アルファベット(半角)
    \u2E80-\u2FFF: 漢字
    \u3041-\u30FF: ひらがな、カタカナなど
    \u4E00-\u9FFF: 漢字(常用、非常用含む)(\u3400-\4DFFも漢字だが多分中国語)
    \uF900-\uFAFF: 漢字
    \uFF00-\uFF9F: 全角アルファベット、全角記号、半角カタカナなど
    '''
    return re.sub(r'[^\u0021-\u007E\u2E80-\u2FFF\u3041-\u30FF\u4E00-\u9FFF\uF900-\uFAFF\uFF00-\uFF9F]', '', src_str)



