# -*- coding:utf-8 -*-


def to_true(s):
    '''True変換、変換できなければそのまま返す'''
    return True if str(s).lower() in ['true', 't', '1'] else s


def to_false(s):
    '''False変換、変換できなければそのまま返す'''
    return False if str(s).lower() in ['false', 'f', '0'] else s


def to_bool(s):
    '''bool型変換、変換できなければそのまま返す'''
    return to_true(to_false(s))
