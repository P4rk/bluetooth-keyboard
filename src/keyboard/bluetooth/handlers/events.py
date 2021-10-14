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


"""
Note: As an optimisation to prevent unnecessary allocations, the addr, adv_data,
char_data, notify_data, and uuid entries in the tuples are read-only memoryview instances
pointing to bluetooth’s internal ringbuffer, and are only valid during the invocation of 
the IRQ handler function. If your program needs to save one of these values to access 
after the IRQ handler has returned (e.g. by saving it in a class instance or global 
variable), then it needs to take a copy of the data, either by using bytes() or 
bluetooth.UUID()
"""


def _central_connect_handler(bluetooth_cls, event, data):
    # A central has connected to this peripheral
    conn_handle, addr_type, addr = data
    print(bytes(conn_handle))
    bluetooth_cls.conn_handle = bytes(conn_handle)


def _central_disconnect_handler(bluetooth_cls, event, data):
    # A central has disconnected from this peripheral.
    conn_handle, addr_type, addr = data
    bluetooth_cls.conn_handle = None


def _default_handler(bluetooth_cls, event, data):
    pass


EVENT_MAP = {
    CENTRAL_CONNECT: _central_connect_handler,
    CENTRAL_DISCONNECT: _central_disconnect_handler,
}


def handle_event(bluetooth_cls, event, data):
    print("event: ", event, data)
    func = EVENT_MAP.get(event, _default_handler)
    func(bluetooth_cls, event, data)
