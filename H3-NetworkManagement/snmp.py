from pysnmp import hlapi

class SnmpConnection:
    def __init__(self, ip, community, username, authKey, privKey, port = 161):
        self.ip = ip
        self.community = community
        self.username = username
        self.authKey = authKey
        self.privKey = privKey
        self.port = port

    def authorize(self):
        hlapi.CommunityData(self.community)
        hlapi.UsmUserData(self.username, authKey=self.authKey, privKey=self.privKey, authProtocol=hlapi.usmHMACSHAAuthProtocol, privProtocol=hlapi.usmAesCfb128Protocol)

    def get(self, oids, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
        handler = hlapi.getCmd(
            engine,
            hlapi.CommunityData(self.community),
            hlapi.UdpTransportTarget((self.ip, self.port)),
            context,
            *self.constructObjectTypes(oids)
        )
        data = self.fetch(handler, 1)[0]
        for k, v in data.items():
           return v

    def set(self, value_pairs, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
        handler = hlapi.setCmd(
            engine,
            hlapi.CommunityData(self.community),
            hlapi.UdpTransportTarget((self.ip, self.port)),
            context,
            *self.construct_value_pairs(value_pairs)
        )
        return self.fetch(handler, 1)[0]

    def constructObjectTypes(self, list_of_oids):
        object_types = []
        for oid in list_of_oids:
            object_types.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid)))
        return object_types

    def construct_value_pairs(self, list_of_pairs):
        pairs = []
        for k, v in list_of_pairs.items():
            pairs.append(hlapi.ObjectType(hlapi.ObjectIdentity(k), v))
        return pairs

    def fetch(self, handler, count):
        result = []
        for i in range(count):
            try:
                error_indication, error_status, error_index, var_binds = next(handler)
                if not error_indication and not error_status:
                    items = {}
                    for var_bind in var_binds:
                        items[str(var_bind[0])] = self.cast(var_bind[1])
                    result.append(items)
                else:
                    raise RuntimeError('Got SNMP error: {0}'.format(error_indication))
            except StopIteration:
                break
        return result

    def cast(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            try:
                return float(value)
            except (ValueError, TypeError):
                try:
                    return str(value)
                except (ValueError, TypeError):
                    pass
        return value