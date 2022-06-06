import logging
import pytest

logger = logging.getLogger()
logger.setLevel('INFO')

# Write test documentation. Something like:
#
# def test_blablabla():
#
# """
#
# Description:
#
# Pre-conditions:
#
# 1.
#
# 2.
#
# Steps:
#
# 1.
#
# 2.
#
#
#
# Expected:
#
# 1.
#
# """
#
# test_code

@pytest.mark.regression
def test_human_check_status(create_human):
    """
    Description: test checks whether Human is alive or dead by calling Human "status" property.
    When alive returns "alive", dead returns "dead".

    Pre-conditions:
    1. Create Human entity Anna with age 22 (in range alive)

    Steps:
    1. Check that Human Anna is alive

    Expected:
    1. Receive 'alive' when checking Human Anna "status" property
    :param create_human: calles fixture "create_human" in order to create Human class instance
    :return: fixme
    """
    human_alive = create_human(name='Anna', age=22, gender='female')
    assert human_alive.status == "alive", f"\n{human_alive.status} status is not as expected " \
                                       f"\nActual: {human_alive.status} \nExpected: 'alive' "

def test_check_human_age(create_human):
    """
    Description: test checks whether Human is alive or dead by calling Human "status" property.
    When alive returns "alive", dead returns "dead".

    Pre-conditions:
    1. Create Human entity Anna with age 22 (in range alive)

    Steps:
    1. Check that Human Anna is alive

    Expected:
    1. Receive 'alive' when checking Human Anna "status" property
    :param create_human: calles fixture "create_human" in order to create Human class instance
    :return: fixme
    """
    pass
