def is_valid_IP(strng):

    import socket

    try:
        socket.inet_pton(socket.AF_INET, strng)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(strng)
        except socket.error:
            return False
        return strng.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True
