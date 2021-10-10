import bluetooth
UUID = bluetooth.UUID

F_READ = bluetooth.FLAG_READ
F_WRITE = bluetooth.FLAG_WRITE
F_READ_WRITE = bluetooth.FLAG_READ | bluetooth.FLAG_WRITE
F_READ_NOTIFY = bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY

ATT_F_READ = 0x01
ATT_F_WRITE = 0x02

hid_service = (
    UUID(0x1812),  # Human Interface Device
    (
        (UUID(0x2A4A), F_READ),  # HID information
        (UUID(0x2A4B), F_READ),  # HID report map
        (UUID(0x2A4C), F_WRITE),  # HID control point
        (UUID(0x2A4D), F_READ_NOTIFY, ((UUID(0x2908), ATT_F_READ),)),  # HID report / reference
        (UUID(0x2A4D), F_READ_WRITE, ((UUID(0x2908), ATT_F_READ),)),  # HID report / reference
        (UUID(0x2A4E), F_READ_WRITE),  # HID protocol mode
    ),
)

HID_REPORT_MAP = bytes([
    0x05, 0x01,     # Usage Page (Generic Desktop)
    0x09, 0x06,     # Usage (Keyboard)
    0xA1, 0x01,     # Collection (Application)
    0x85, 0x01,     #     Report ID (1)
    0x75, 0x01,     #     Report Size (1)
    0x95, 0x08,     #     Report Count (8)
    0x05, 0x07,     #     Usage Page (Key Codes)
    0x19, 0xE0,     #     Usage Minimum (224)
    0x29, 0xE7,     #     Usage Maximum (231)
    0x15, 0x00,     #     Logical Minimum (0)
    0x25, 0x01,     #     Logical Maximum (1)
    0x81, 0x02,     #     Input (Data, Variable, Absolute); Modifier byte
    0x95, 0x01,     #     Report Count (1)
    0x75, 0x08,     #     Report Size (8)
    0x81, 0x01,     #     Input (Constant); Reserved byte
    0x95, 0x05,     #     Report Count (5)
    0x75, 0x01,     #     Report Size (1)
    0x05, 0x08,     #     Usage Page (LEDs)
    0x19, 0x01,     #     Usage Minimum (1)
    0x29, 0x05,     #     Usage Maximum (5)
    0x91, 0x02,     #     Output (Data, Variable, Absolute); LED report
    0x95, 0x01,     #     Report Count (1)
    0x75, 0x03,     #     Report Size (3)
    0x91, 0x01,     #     Output (Constant); LED report padding
    0x95, 0x06,     #     Report Count (6)
    0x75, 0x08,     #     Report Size (8)
    0x15, 0x00,     #     Logical Minimum (0)
    0x25, 0x65,     #     Logical Maximum (101)
    0x05, 0x07,     #     Usage Page (Key Codes)
    0x19, 0x00,     #     Usage Minimum (0)
    0x29, 0x65,     #     Usage Maximum (101)
    0x81, 0x00,     #     Input (Data, Array); Key array (6 bytes)
    0xC0,           # End Collection
])
