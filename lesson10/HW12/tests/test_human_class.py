import logging
import pytest

logger = logging.getLogger()
logger.setLevel('INFO')


@pytest.mark.regression
def test_human_check_status_alive(create_human):
    """
    Description: test checks whether Human is alive by calling Human "status" property.
    When alive returns "alive", else: AssertionError will be raised.

    Pre-conditions:
    1. Create Human entity Anna with age 22 (in range alive)

    Steps:
    1. Check that Human Anna is alive

    Expected:
    1. Receive 'alive' when checking Human Anna "status" property
    """
    name_Anna = 'Anna'
    age_Anna = 22
    gender_Anna = 'female'
    human_alive = create_human(name=name_Anna, age=age_Anna, gender=gender_Anna)
    assert human_alive.status == "alive", f"\n{human_alive.status} status is not as expected " \
                                          f"\nActual: {human_alive.status} \nExpected: 'alive' "


@pytest.mark.regression
def test_check_human_age(create_human):
    """
    Description: test checks Human age by creating instance of Human class and
    calling Human "age" property, checking that the age is the same as passed into
    Human parameters.

    Pre-conditions:
    1. Create Human entity Liza with age 23 (in range alive)

    Steps:
    1. Check that Human Liza is 23 y.o.

    Expected:
    1. Receive 22 when checking Human Anna "age" property
    """
    name_Liza = 'Liza'
    age_Liza = 23
    gender_Liza = 'female'
    human_age_check = create_human(name=name_Liza, age=age_Liza, gender=gender_Liza)
    assert human_age_check.age == age_Liza, f"\n{human_age_check.age} age is not as expected " \
                                            f"\nActual: {human_age_check.age} \nExpected: {age_Liza} "


@pytest.mark.regression
@pytest.mark.parametrize("name, age, expected", [["Petro", 22, 23], ["Zhenya", 104, 105]])
def test_check_human_grow(create_human, name, age, expected):
    """
    Description: test checks Human age after calling "grow" method. Creates instance of Human class and
    calling Human "grow" method, checking that the age has increased for 1 year.

    Pre-conditions:
    1. Create Human entity Petro with age 26 (in range alive)

    Steps:
    1. Call method "grow" for Petro
    2. Check that "age" property returns age increased by 1

    Expected:
    1. Receive 27 when checking Human Petro "age" property
    """
    logger.info(f"\n TEST START for user {name}")
    name_user = name
    age_user = age
    gender_Petro = 'male'
    human_grow_check = create_human(name=name_user, age=age_user, gender=gender_Petro)
    human_grow_check.grow()
    assert human_grow_check.age == expected, f"\n{human_grow_check.age} age is not as expected " \
                                             f"\nActual: {human_grow_check.age} \nExpected: {expected} "


@pytest.mark.regression
def test_check_dead_human_grow(create_human):
    """
    Description: test checks change of status from "alive" to "dead" for Human with age more than 105 y.o
    age after calling "grow" method. Human age does not increase.

    Pre-conditions:
    1. Create Human entity Lana with age 105 (in range alive, border value)

    Steps:
    1. Call method "grow" for Lana
    2. Check that "age" property does not return age increased by 1 and raises exception, "status" has changed to "dead"

    Expected:
    1. While checking "age" increased for 1 we expect Exception and while checking "status" we expect "dead"
    """
    name_Lana = 'Lana'
    age_Lana = 106
    gender_Lana = 'female'
    human_dead_check = create_human(name=name_Lana, age=age_Lana, gender=gender_Lana)
    human_dead_check.grow()
    assert human_dead_check.age != age_Lana + 1, f"\n{human_dead_check.age} age is not as expected " \
                                                 f"\nActual: {human_dead_check.age} \nExpected: {age_Lana} "
    assert human_dead_check.status == "dead", f"\n{human_dead_check.status} status is not as expected " \
                                              f"\nActual: {human_dead_check.status} \nExpected: 'dead' "


@pytest.mark.regression
@pytest.mark.skip("Test is skipped unless bug with possibility of creation dead human is fixed")
def test_attribute_status_for_dead_human(create_human):
    """
   Description: test checks whether it is possible to create dead Human (with age gt 105)

   Pre-conditions:
   1. Create Human entity Lana with age 110 (in range dead)

   Steps:
   1. Check that "status" property returns "dead"

   Expected:
   1. While checking "status" we expect "dead"
   """
    name_Lana = 'Lana'
    age_Lana = 110
    gender_Lana = 'female'
    human_dead_check = create_human(name=name_Lana, age=age_Lana, gender=gender_Lana)
    assert human_dead_check.status == "dead", f"\n{human_dead_check.status} status is not as expected " \
                                              f"\nActual: {human_dead_check.status} \nExpected: 'dead' "


@pytest.mark.regression
def test_check_human_name(create_human):
    """
    Description: test checks Human name by creating instance of Human class and
    calling Human "name" property, checking that the name is the same as passed into
    Human parameters.

    Pre-conditions:
    1. Create Human entity Olga

    Steps:
    1. Check that "name" property for Human Olga returns name Olga

    Expected:
    1. Receive Olga when checking Human "name" property
    """
    name_Olga = 'Olga'
    age_Olga = 34
    gender_Olga = 'female'
    human_name_check = create_human(name=name_Olga, age=age_Olga, gender=gender_Olga)
    assert human_name_check.name == name_Olga, f"\n{human_name_check.name} name is not as expected " \
                                               f"\nActual: {human_name_check.name} \nExpected: {name_Olga} "


@pytest.mark.regression
def test_check_change_name_positive(create_human):
    """
    Description: test checks setting of new name by method "change_name".

    Pre-conditions:
    1. Create Human entity Lama

    Steps:
    1. Call method "change_name" for Lama
    2. Check that "name" property returns new name different from Lama (Kira)

    Expected:
    1. After calling method "change_name" when calling property "name" receive name Kira
    """
    name_Lama = 'Lama'
    age_Lama = 106
    gender_Lama = 'female'
    human_name_change = create_human(name=name_Lama, age=age_Lama, gender=gender_Lama)
    new_name = "Kira"
    human_name_change.change_name(new_name)
    assert human_name_change.name == new_name, f"\n{human_name_change.name} age is not as expected " \
                                               f"\nActual: {human_name_change.name} \nExpected: {new_name} "


@pytest.mark.negative
@pytest.mark.regression
def test_check_change_name_negative(create_human):
    """
    Description: test checks impossibility of setting of new name in lowercase and less than 10 letters
    by method "change_name".

    Pre-conditions:
    1. Create Human entity with right name

    Steps:
    1. Call method "change_name" for Human and pass as parameter with incorect name
    2. Check method "change_name" raises exception due to lowercase prohibition/incorrect length for "name" parameter

    Expected:
    1. After calling method "change_name" with parameter in lowercase/with length lt 10 letters we receive an exception
    """
    name = "Lama"
    age_user_neg = 88
    gender_user_neg = 'female'
    human_name_change = create_human(name=name, age=age_user_neg, gender=gender_user_neg)
    new_name = "lama"
    with pytest.raises(SyntaxError) as e:
        human_name_change.change_name(new_name)
    # assert e.value == SyntaxError('Name should starts with capital letter') #fixme


@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.skip("Skipping test until fixed possibility of setting name in lowercase")
def test_check_change_name_negative_length_gt_10(create_human):
    """
    Description: test checks impossibility of setting of new name in lowercase by method "change_name".

    Pre-conditions:
    1. Create Human entity with right name

    Steps:
    1. Call method "change_name" for Human and pass as parameter with incorrect name - lowercase, gt 10 letter length
    2. Check method "change_name" raises exception due to lowercase prohibition

    Expected:
    1. After calling method "change_name" with parameter in lowercase we receive an exception
    """
    name = "Bamboleyo"
    age_user_neg = 88
    gender_user_neg = 'female'
    new_name = "lamklajsuiopefbnm"
    human_name_change = create_human(name=name, age=age_user_neg, gender=gender_user_neg)
    human_name_change.change_name(new_name)
    with pytest.raises(Exception):
        human_name_change.change_name(new_name)


@pytest.mark.regression
def test_check_human_gender(create_human):
    """
    Description: test checks Human gender by creating instance of Human class and
    calling Human "gender" property, checking that the gender is the same as passed into
    Human parameters. Setting gender by using gender.setter.

    Pre-conditions:
    1. Create Human entity Liza with gender "female"

    Steps:
    1. Check that Human Liza's gender is "female" by calling "gender" property
    2. Change gender to "male" by using gender.setter
    3. Check that Human Liza's gender is "male" by calling "gender" property

    Expected:
    1. Receive "female" gender when passing the same parameter when creating Human entity.
     Receive "male" gender after using using gender.setter
    """
    name_Liza = 'Liza'
    age_Liza = 20
    gender_Liza = 'female'
    gender_new = 'male'
    human_gender_check = create_human(name=name_Liza, age=age_Liza, gender=gender_Liza)
    assert human_gender_check.gender == gender_Liza, f"\n{human_gender_check.gender} gender is not as expected " \
                                                     f"\nActual: {human_gender_check.gender} \nExpected: {gender_Liza} "
    human_gender_check.gender = gender_new
    assert human_gender_check.gender == gender_new, f"\n{human_gender_check.gender} gender is not as expected " \
                                                    f"\nActual: {human_gender_check.gender} \nExpected: {gender_new} "


@pytest.mark.negative
@pytest.mark.regression
def test_check_human_gender_negative(create_human):
    """
    Description: test checks Human gender.setter by creating instance of Human class with
    allowed gender. Setting gender to incorrect by using gender.setter.

    Pre-conditions:
    1. Create Human Valya with gender "male"

    Steps:
    1. Check that Human Valya's gender is "female" by calling "gender" property
    2. Change gender to "male" by using gender.setter
    3. Check that Human Valya's gender is "male" by calling "gender" property

    Expected:
    1. Receive "female" gender when passing the same parameter when creating Human entity.
     Receive "male" gender after using using gender.setter
    """
    name_Valya = "Valya"
    age_Valya = 20
    gender_Valya = 'female'
    gender_new = 'cat'
    human_gender_check = create_human(name=name_Valya, age=age_Valya, gender=gender_Valya)
    with pytest.raises(Exception):
        human_gender_check.gender = gender_new


@pytest.mark.interaction
def test_check_make_friend(create_human):
    """
    Description: test checks Human make_friends and get_friends methods by creating instance of
    Human class, checking quantity of friends with get_friends. Creating friend and checking
    quantity of friends afterwards

    Pre-conditions:
    1. Create Human Valya
    2. Create Human Sveta

    Steps:
    1. Check Human Valya's friends' quantity by calling get_friends
    2. Call method make_friends for Human Valya and add Sveta as a friend
    3. Check that Human Valya's list of friends has been amended with Sveta

    Expected:
    1. Receive empty list when calling get_friends for freshly created Human, successfully amend
    friends attribute of Human after calling make_friends method
    """
    name_Valya = "Valya"
    age = 20
    gender = 'female'
    name_Sveta = "Sveta"
    human_Valya = create_human(name=name_Valya, age=age, gender=gender)
    human_friend = create_human(name=name_Sveta, age=age, gender=gender)
    assert human_Valya.friends == [], f"Freshly created Human with name {human_Valya.name} cannot have friends"
    human_Valya.make_friends(human_friend)
    assert human_Valya.friends == [human_friend], f"Human with name {human_Valya.name} should have friend with " \
                                                  f"name {human_friend.name}"


@pytest.mark.skip("Skipped untill bug of adding a friend with age within 'dead' range is fixed")
@pytest.mark.negative
@pytest.mark.interaction
def test_check_make_friend_negative(create_human):
    """
    Description: test checks Human make_friends raises Exception in case we pass as a parameter Human
    with age in range 'dead'

    Pre-conditions:
    1. Create Human Valya
    2. Create Human Katya with age in range "dead"

    Steps:
    1. Check Human Valya's friends' quantity by calling get_friends
    2. Call method make_friends for Human Valya and cgeck that Exception has been raised
    3. Check that Human Valya's list of friends hasn't been amended with Katya

    Expected:
    1. Impossible to add as a friend Human with age in range "dead"
    """
    name_Valya = "Valya"
    age = 20
    gender = 'female'
    name_Katya = "Katya"
    age_friend = 107
    human_Valya = create_human(name=name_Valya, age=age, gender=gender)
    human_friend = create_human(name=name_Katya, age=age_friend, gender=gender)
    with pytest.raises(Exception):
        human_Valya.make_friends(human_friend)
    assert human_Valya.friends == [], f"Human with name {human_Valya.name} should not have friend as friend " \
                                      f"added was in range of 'dead'"
