import json


# json.JSONEncoder
class ExtendedJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):  # complex
            return {"__type__": "complex", "real": obj.real, "imag": obj.imag}
        elif isinstance(obj, range):  # range
            return {
                "__type__": "range",
                "start": obj.start,
                "stop": obj.stop,
                "step": obj.step,
            }
        return super().default(obj)


# json.JSONDecoder
class ExtendedJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        if dct.get("__type__") == "complex":
            return complex(dct["real"], dct["imag"])
        elif dct.get("__type__") == "range":
            return range(dct["start"], dct["stop"], dct["step"])
        return dct


# dumps and loads
def dumps(obj, *args, **kwargs):
    return json.dumps(obj, cls=ExtendedJSONEncoder, *args, **kwargs)


def loads(s, *args, **kwargs):
    return json.loads(s, cls=ExtendedJSONDecoder, *args, **kwargs)
