# Implements a BLE HID keyboard
from typing import Tuple

import struct
import bluetooth

from keyboard.bluetooth.advertising.payloads import generate_payload
from keyboard.bluetooth.constants import HID_REPORT_MAP, hid_service
from keyboard.bluetooth.handlers.events import (
    BluetoothEvent,
    handle_event,
)
from keyboard.keys import Key
from keyboard.modifiers import Modifier, NoModifier


class Bluetooth:
    def __init__(self, name):
        self.name = name
        self.ble = bluetooth.BLE()
        self.ble.active(1)
        self.ble.irq(self._bluetooth_event)

        self._conn_handle = None

        # register services
        self.ble.config(gap_name=self.name)
        handles = self.ble.gatts_register_services((hid_service,))
        (
            self.h_info,
            self.h_hid,
            _,
            self.h_rep,
            self.h_d1,
            _,
            self.h_d2,
            self.h_proto
        ) = handles[0]

        # set initial data
        self.ble.gatts_write(
            self.h_info,
            b"\x01\x01\x00\x02",  # HID info: ver=1.1, country=0, flags=normal
        )
        self.ble.gatts_write(self.h_hid, HID_REPORT_MAP)  # HID report map
        self.ble.gatts_write(self.h_d1, struct.pack("<BB", 1, 1))  # report: id=1, type=input
        self.ble.gatts_write(self.h_d2, struct.pack("<BB", 1, 2))  # report: id=1, type=output
        self.ble.gatts_write(self.h_proto, b"\x01")  # protocol mode: report
        self._advertise()

    @property
    def conn_handler(self):
        return self._conn_handle

    @conn_handler.setter
    def conn_handle(self, value):
        if isinstance(value, bytes):
            self._conn_handle = int.from_bytes(value, 'little')
            return
        elif isinstance(value, int):
            self._conn_handle = value
            return
        elif value is None:
            self._conn_handle = None
            self._advertise()
            return
        raise RuntimeError(f'conn_handle not bytes or int is ({type(value)}){value}')

    def _bluetooth_event(self, event: BluetoothEvent, data: Tuple) -> None:
        """
        Bluetooth event callback.
        :param event: A constant defining the type of event. Defined as a BluetoothEvent
        :param data: An event-specific tuple of values
        :return: None
        """
        handle_event(self, event, data)

    def _advertise(self):
        """
        Advertise the bluetooth connection

        https://community.silabs.com/s/article/kba-bt-0201-bluetooth-advertising-data-basics?language=en_US
        """
        payload = generate_payload(self.name)
        self.ble.gap_advertise(100_000, payload)

    """
    Public Interface
    """
    def send_key(self, key: Key, mod: Modifier = NoModifier):
        if self.conn_handle is not None:
            self.ble.gatts_notify(
                self.conn_handle,
                self.h_rep,
                struct.pack("8B", mod, 0, key, 0, 0, 0, 0, 0),
            )
            self.ble.gatts_notify(
                self.conn_handle,
                self.h_rep,
                struct.pack("8B", 0, 0, 0, 0, 0, 0, 0, 0),
            )
        else:
            print('Conn handle None')

