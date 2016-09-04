def _pad(data, length):
    while len(data) < length:
        data.extend(b' ')
    return data


class Packer:

    def split(data, byte_size):
        if isinstance(byte_size, int) is False:
            raise Exception('byte length not integeric')
        parts = []
        current_part = bytearray()

        for i in range(0, len(bytes(data.encode())) - 1):
            current_part.extend(data[i].encode())
            if len(bytes(current_part)) == byte_size:
                parts.append(current_part)
                current_part = bytearray()

        if len(bytes(current_part)) < byte_size:
            _pad(current_part, byte_size)

            parts.append(current_part)

        return parts


