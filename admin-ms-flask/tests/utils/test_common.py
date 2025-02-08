from app.utils.common import CommonUtil

class TestCommonUtil:

    def test_is_empty_none(self):
        assert CommonUtil().is_empty(None) is True

    def test_is_empty_empty_string(self):
        assert CommonUtil().is_empty("") is True    

    def test_is_empty_non_empty_string(self):
        assert CommonUtil().is_empty("Hello") is False 

    def test_is_empty_empty_list(self):
        assert CommonUtil().is_empty([]) is True      

    def test_is_empty_non_empty_list(self):
        assert CommonUtil().is_empty([1]) is False   

    def test_is_empty_empty_tuple(self):
        assert CommonUtil().is_empty(tuple()) is True      

    def test_is_empty_non_empty_tuple(self):
        assert CommonUtil().is_empty((1,)) is False      

    def test_is_empty_empty_set(self):
        assert CommonUtil().is_empty(set()) is True      

    def test_is_empty_non_empty_set(self):
        assert CommonUtil().is_empty({1,2}) is False   

    def test_is_empty_empty_dict(app):
        assert CommonUtil().is_empty({}) is True

    def test_is_empty_non_empty_dict(app):
        assert CommonUtil().is_empty({"key": "value"}) is False

    def test_is_empty_zero_integer(app):
        assert CommonUtil().is_empty(0) is True

    def test_is_empty_non_zero_integer(app):
        assert CommonUtil().is_empty(10) is False

    def test_is_empty_zero_float(app):
        assert CommonUtil().is_empty(0.0) is True

    def test_is_empty_non_zero_float(app):
        assert CommonUtil().is_empty(3.14) is False

    def test_is_empty_non_zero_negative_integer(app):
        assert CommonUtil().is_empty(-1) is False

    def test_is_empty_non_zero_negative_float(app):
        assert CommonUtil().is_empty(-3.14) is False      

