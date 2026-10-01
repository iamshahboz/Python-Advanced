from unittest.mock import Mock 

fake_response = Mock()
fake_response.json.return_value = {"temperature": 25}

print (fake_response.json())

"""
Key idea: Mock object will let you call any method or access any attribute on it.
It just makes them up on the fly. You control what a method returns using .return_value 

"""