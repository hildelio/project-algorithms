import pytest

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("O miserável é um gênio", "kakaroto")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 23)

    assert encrypt_message("Morra inseto!", 5).strip() == "arroM_!otesni"
    assert encrypt_message(
        "Kakaroto, seu verme insolente!", 4
        ).strip() == "!etnelosni emrev ues ,otor_akaK"
    assert encrypt_message(
        "O orgulho é um deus dos tolos.", 40
        ).strip() == ".solot sod sued mu é ohlugro O"
