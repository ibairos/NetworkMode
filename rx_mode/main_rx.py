from rx_mode import rx_BD, tx_BD_ACK, rx_neighbor_list, rx_file, rx_token

state = "rx_BD"


# TODO code for the receiver
# Main function for the receiver code
def receiver():
    if state == "rx_BD":
        rx_BD.run()
    elif state == "tx_BD_ACK":
        tx_BD_ACK.run()
    elif state == "rx_neighbor_list":
        rx_neighbor_list.run()
    elif state == "rx_file":
        rx_file.run()
    elif state == "rx_token":
        rx_token.run()
