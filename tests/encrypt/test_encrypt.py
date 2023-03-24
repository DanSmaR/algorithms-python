import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Testing raising TypeError Exception with invalid key argument
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("danilo", None)

    # Testing raising TypeError Exception with invalid message argument
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(None, 2)

    # Testing with key out of message length range, returning a reversed string
    MESSAGE = "danilo"
    expected_encrypted_message = "olinad"
    encrypted_message = encrypt_message(MESSAGE, 10)
    assert encrypted_message == expected_encrypted_message

    # Testing with odd key argument
    expected_encrypted_message = "nad_oli"
    encrypted_message = encrypt_message(MESSAGE, 3)
    assert encrypted_message == expected_encrypted_message

    # Testing with even key argument
    expected_encrypted_message = "ol_inad"
    encrypted_message = encrypt_message(MESSAGE, 4)
    assert encrypted_message == expected_encrypted_message
