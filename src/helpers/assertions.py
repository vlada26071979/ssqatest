class Ensure:

    @staticmethod
    def is_equal(actual, expected, message=None):
        assert actual == expected, message or f"Expected '{expected}', but got '{actual}'"

    @staticmethod
    def is_not_equal(actual, expected, message=None):
        assert actual != expected, message or f"Did not expect '{expected}', but got it"

    @staticmethod
    def is_true(condition, message=None):
        assert condition is True, message or "Expected condition to be True, but it was False"

    @staticmethod
    def is_false(condition, message=None):
        assert condition is False, message or "Expected condition to be False, but it was True"

    @staticmethod
    def is_none(value, message=None):
        assert value is None, message or f"Expected value to be None, but got '{value}'"

    @staticmethod
    def is_not_none(value, message=None):
        assert value is not None, message or "Expected value not to be None"

    @staticmethod
    def is_in(member, container, message=None):
        assert member in container, message or f"Expected '{member}' to be in '{container}'"

    @staticmethod
    def is_not_in(member, container, message=None):
        assert member not in container, message or f"Expected '{member}' to not be in '{container}'"

    @staticmethod
    def contains_text(web_element, expected_text, message=None):
        actual_text = web_element.text
        assert expected_text in actual_text, message or f"Expected '{expected_text}' to be in '{actual_text}'"

    @staticmethod
    def has_attribute(web_element, attribute_name, expected_value=None, message=None):
        actual_value = web_element.get_attribute(attribute_name)
        if expected_value is None:
            assert actual_value is not None, message or f"Expected attribute '{attribute_name}' to be present"
        else:
            assert actual_value == expected_value, message or f"Expected attribute '{attribute_name}' to be '{expected_value}', but got '{actual_value}'"
