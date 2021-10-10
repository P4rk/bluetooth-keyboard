import struct

from keyboard.bluetooth.advertising import flags, types, service_class, appearance


def generate_payload(name: str) -> bytes:
    """
    Generate the advertising payload that is 0-31 bytes long.
    Advertising data consists of one or more Advertising Data (AD) elements.
    Each element is formatted as follows:
        1st byte: length of the element (excluding the length byte itself)
        2nd byte: AD type – specifies what data is included in the element
        AD data – one or more bytes - the meaning is defined by AD type

    """
    ad_flags = (
        types.FLAGS,
        flags.LE_ONLY_GENERAL_DISC_MODE,
    )

    ad_service_type = (
        types.COMPLETE_LIST_OF_16_BIT_SERVICE_CLASS_UUIDS,
        service_class.HUMAN_INTERFACE_DEVICE,
    )
    ad_appearance = (
        types.APPEARANCE,
        appearance.KEYBOARD,
    )

    ad_name = (
        types.COMPLETE_LOCAL_NAME,
        bytes(name, 'UTF-8'),
    )

    payload = []
    for ad in [
        ad_flags,
        ad_service_type,
        ad_appearance,
        ad_name,
    ]:
        ad_type_and_data = []
        for byte in ad:
            if isinstance(byte, int):
                byte = int_to_bytes(byte)
            ad_type_and_data.append(byte)

        ad_type_and_data = b"".join(ad_type_and_data)

        length_of_element = int_to_bytes(len(ad_type_and_data))
        payload.append(length_of_element + ad_type_and_data)

    return b"".join(payload)


def int_to_bytes(value) -> bytes:
    number_of_bytes = 1
    while 2**(8*number_of_bytes) < value:
        number_of_bytes += 1

    # Note the reversed byte order
    # (multibyte values in BLE packets are in little-endian order).
    return value.to_bytes(number_of_bytes, 'little')
