import logging
import pytest
from lesson10.HW12.code_for_testing import Human

logger = logging.getLogger()
logger.setLevel('INFO')


# Write test cases for the provided file using pytest. Implement fixtures for your tests using yield or return,
# group tests using pytest marks, log fixture start and fixture end. Try parametrization for one TC.

@pytest.fixture()
def create_human():
    logger.info(msg='\nFixture "create_human" start')

    def human_factory(name, age, gender):
        return Human(name=name, age=age, gender=gender)

    yield human_factory
    logger.info(msg='\nFixture "create_human" finished')


@pytest.fixture()
def generate_data_for_human():
    logger.info(msg='\nFixture "generate_data_for_human" start')

    def data_factory(name, age, gender):
        dict_human_data = {"name": name, "age": age, "gender": gender}
        return dict_human_data

    yield data_factory
    logger.info(msg='\nFixture "generate_data_for_human" finished')
