from alvian_challenge.custom_random.random_object import MyDefineObject



def test_define_is_integer():
    random_object = 1
    object_type =  MyDefineObject(random_object).define_object_type()
    assert object_type == "integer"
    random_object = "1"
    object_type =  MyDefineObject(random_object).define_object_type()
    assert object_type == "integer"

def test_define_is_real_number():
    random_object = 1.1
    object_type =  MyDefineObject(random_object).define_object_type()
    assert object_type == "real numbers"
    random_object = "1.1"
    object_type =  MyDefineObject(random_object).define_object_type()
    assert object_type == "real numbers"


def test_define_is_alphanumeric():
    random_object = " abc12   "
    object_type =  MyDefineObject(random_object).define_object_type()
    assert object_type == "alphanumeric"
    random_object = "   abc12 "
    object_type =  MyDefineObject(random_object).define_object_type()
    assert object_type == "alphanumeric"
    random_object = " abc12 "
    object_type =  MyDefineObject(random_object).define_object_type()
    assert object_type == "alphanumeric"


def test_define_is_alphabetical():
    random_object = "aaa"
    object_type =  MyDefineObject(random_object).define_object_type()
    assert object_type == "alphabetical strings"