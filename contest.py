import pytest


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import lesson_5_23.helpers.selene.patch_selector_strategy  # noqa
    import lesson_5_23.helpers.selene.patch_element_mobile_commands  # noqa
