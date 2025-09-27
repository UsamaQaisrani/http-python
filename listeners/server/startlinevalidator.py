from dataclass.message import RequestType

class StartlineValidator:
    def __init__(self, input) -> None:
        self.input = input
        print("INIT")

    def validate_startline(self):
        group = self.input.split(" ").split(":")
        assert len(group) == 3, "Header startline is invalid"
        request_type = RequestType(group[0].lower())
        path = group[1]
        protocol_version = group[2]
        return (request_type, path, protocol_version)
