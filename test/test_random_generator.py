from alvian_challenge.custom_random.random_generator import (
    get_random_alphabetical, 
    get_random_alphanumeric,
    get_random_alphanumeric_between_space,
    get_random_int,
    get_random_real_number
)


def test_get_random_real_number():
    assert type(get_random_real_number()) == float


def test_get_random_int():
    assert type(get_random_int()) == int


def test_get_random_alphabetical():
    assert type(get_random_alphabetical()) == str


def test_get_random_alphanumeric():
    assert type(get_random_alphabetical()) == str
    assert any(char.isdigit() for char in get_random_alphanumeric())


def test_get_random_alphanumeric():
    assert type(get_random_alphanumeric_between_space()) == str
    assert any(char.isdigit() for char in get_random_alphanumeric_between_space())
    assert get_random_alphanumeric_between_space()[0] == " "
    assert get_random_alphanumeric_between_space()[-1] == " "