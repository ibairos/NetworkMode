from rx_mode import main_rx
from tx_mode import main_tx
from util import util


while True:
    # We first check the role of the device
    role = util.check_role()

    # And then execute the corresponding code
    if role == "tx":
        main_tx.transmitter()
    elif role == "rx":
        main_rx.receiver()
    else:
        exit(0)
