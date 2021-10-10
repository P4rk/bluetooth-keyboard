from keyboard.bluetooth.advertising.payloads import generate_payload, int_to_bytes


def test_generate_payload():
    name = 'test name'
    payload = generate_payload(name)
    assert payload == (
        b'\x02\x01\x06'
        b'\x03\x03\x12\x18'
        b'\x03\x19\xc1\x03'
        b'\n\ttest name'
    )


def test_int_to_multi_bytes():
    bytes_ = int_to_bytes(0x1812)
    assert bytes_ == b'\x12\x18'


def test_int_to_bytes():
    bytes_ = int_to_bytes(0x01)
    assert bytes_ == b'\x01'
