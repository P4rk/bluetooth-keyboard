"""
A list of events fired and used and passed to the callback function passed to
`bluetooth.ble.irq`
"""

from micropython import const
CENTRAL_CONNECT = const(1)
CENTRAL_DISCONNECT = const(2)
GATTS_WRITE = const(3)
GATTS_READ_REQUEST = const(4)
SCAN_RESULT = const(5)
SCAN_DONE = const(6)
PERIPHERAL_CONNECT = const(7)
PERIPHERAL_DISCONNECT = const(8)
GATTC_SERVICE_RESULT = const(9)
GATTC_SERVICE_DONE = const(10)
GATTC_CHARACTERISTIC_RESULT = const(11)
GATTC_CHARACTERISTIC_DONE = const(12)
GATTC_DESCRIPTOR_RESULT = const(13)
GATTC_DESCRIPTOR_DONE = const(14)
GATTC_READ_RESULT = const(15)
GATTC_READ_DONE = const(16)
GATTC_WRITE_DONE = const(17)
GATTC_NOTIFY = const(18)
GATTC_INDICATE = const(19)
GATTS_INDICATE_DONE = const(20)
MTU_EXCHANGED = const(21)
L2CAP_ACCEPT = const(22)
L2CAP_CONNECT = const(23)
L2CAP_DISCONNECT = const(24)
L2CAP_RECV = const(25)
L2CAP_SEND_READY = const(26)
CONNECTION_UPDATE = const(27)
ENCRYPTION_UPDATE = const(28)
GET_SECRET = const(29)
SET_SECRET = const(30)

BluetoothEvent = const


def _central_connect_handler(bluetooth_cls, event, data):
    bluetooth_cls.conn_handle, addr_type, addr = data


def _default_handler(bluetooth_cls, event, data):
    print("event: ", event, data)


EVENT_MAP = {
    CENTRAL_CONNECT: _central_connect_handler,
}


def handle_event(bluetooth_cls, event, data):
    func = EVENT_MAP.get(event, _default_handler)
    func(bluetooth_cls, event, data)
