# GAP Advertisement Flags
LE_LIMITED_DISC_MODE = 0x01  # < LE Limited Discoverable Mode.
LE_GENERAL_DISC_MODE = 0x02  # < LE General Discoverable Mode.
BR_EDR_NOT_SUPPORTED = 0x04  # < BR/EDR not supported.
LE_BR_EDR_CONTROLLER = 0x08  # < Simultaneous LE and BR/EDR, Controller.
LE_BR_EDR_HOST = 0x10  # < Simultaneous LE and BR/EDR, Host.
LE_ONLY_LIMITED_DISC_MODE = (
    LE_LIMITED_DISC_MODE
    | BR_EDR_NOT_SUPPORTED
)  # < LE Limited Discoverable Mode, BR/EDR not supported.
LE_ONLY_GENERAL_DISC_MODE = (
    LE_GENERAL_DISC_MODE
    | BR_EDR_NOT_SUPPORTED
)  # < LE General Discoverable Mode, BR/EDR not supported.
