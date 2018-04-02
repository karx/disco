from holster.enum import Enum

VoiceOPCode = Enum(
    IDENTIFY=0,
    SELECT_PROTOCOL=1,
    READY=2,
    HEARTBEAT=3,
    SESSION_DESCRIPTION=4,
    SPEAKING=5,
    HEARTBEAT_ACK=6,
    RESUME=7,
    HELLO=8,
    RESUMED=9,
    CLIENT_DISCONNECT=13,
)