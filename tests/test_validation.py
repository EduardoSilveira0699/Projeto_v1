from utils.validation import validar_status


def test_status_pendente_valido():
    assert validar_status("pendente") is True


def test_status_concluido_valido():
    assert validar_status("concluido") is True


def test_status_invalido():
    assert validar_status("finalizado") is False
