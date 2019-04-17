from tx_mode import tx_BD, rx_BD_ACK, tx_neighbor_list, tx_file, tx_token

state = "tx_BD"
# TODO define neighbor list structure
neighbor_list = None
neighbors_with_file = None


# TODO code for the transmitter
def transmitter():
    if state == "tx_BD":
        tx_BD.run()
    elif state == "rx_BD_ACK":
        rx_BD_ACK.run()
    elif state == "tx_neighbor_list":
        tx_neighbor_list.run()
    elif state == "tx_file":
        tx_file.run()
    elif state == "tx_token":
        tx_token.run()
