import hashlib


def generate_sha256(data):
    h = hashlib.sha256()
    h.update(str(data.user.id).encode('utf-8'))
    h.update(data.owner_name.encode('utf-8'))
    # h.update(data.state)
    # h.update(data.distict)
    # h.update(data.municiplity)
    # h.update(data.village)
    # h.update(data.address)
    h.update(str(data.coordinate).encode('utf-8'))
    h.update(str(data.area).encode('utf-8'))

    return h


# h = hashlib.sha256()
# h.update(str("test").encode('utf-8'))
# print(h.hexdigest())
