from a10sdk.common.A10BaseClass import A10BaseClass


class AccessList(A10BaseClass):
    
    """Class Description::
    Configure Access List.

    Class access-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param extended_list: {"minItems": 1, "items": {"type": "extended"}, "uniqueItems": true, "array": [{"required": ["extd"], "properties": {"rules": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"icmp-type": {"description": "ICMP type number", "format": "number", "maximum": 254, "minimum": 0, "not": "any-type", "type": "number"}, "ip": {"default": 0, "not-list": ["tcp", "udp", "service-obj-group"], "type": "number", "description": "Any Internet Protocol", "format": "flag"}, "service-obj-group": {"description": "Service object group (Source object group name)", "format": "string", "minLength": 1, "not-list": ["tcp", "udp", "ip"], "maxLength": 63, "type": "string"}, "dst-eq": {"description": "Match only packets on a given destination port (port number)", "format": "number", "not-list": ["dst-gt", "dst-lt"], "maximum": 65535, "minimum": 1, "type": "number"}, "tcp": {"default": 0, "not-list": ["udp", "ip", "service-obj-group"], "type": "number", "description": "protocol TCP", "format": "flag"}, "src-range": {"description": "match only packets in the range of port numbers (Starting Port Number)", "format": "number", "not-list": ["src-eq", "src-gt"], "maximum": 65535, "minimum": 1, "type": "number"}, "any-code": {"default": 0, "not": "icmp-code", "type": "number", "description": "Any ICMP code", "format": "flag"}, "src-lt": {"description": "Match only packets with a lower port number", "format": "number", "not-list": ["src-eq", "src-gt"], "maximum": 65535, "minimum": 2, "type": "number"}, "src-mask": {"type": "string", "description": "Source Mask 0=apply 255=ignore", "format": "ipv4-rev-netmask"}, "src-port-end": {"description": "Ending Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "dst-port-end": {"description": "Edning Destination Port Number", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "dst-range": {"description": "Match only packets in the range of port numbers (Starting Destination Port Number)", "format": "number", "not-list": ["dst-eq", "dst-gt"], "maximum": 65535, "minimum": 1, "type": "number"}, "established": {"default": 0, "type": "number", "description": "TCP established", "format": "flag"}, "dst-mask": {"type": "string", "description": "Destination Mask 0=apply 255=ignore", "format": "ipv4-rev-netmask"}, "dst-gt": {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["dst-eq", "dst-lt"], "maximum": 65534, "minimum": 1, "type": "number"}, "src-any": {"default": 0, "not-list": ["src-host", "src-object-group"], "type": "number", "description": "Any source host", "format": "flag"}, "fragments": {"default": 0, "type": "number", "description": "IP fragments", "format": "flag"}, "icmp-code": {"description": "ICMP code number", "format": "number", "maximum": 254, "minimum": 0, "not": "any-code", "type": "number"}, "src-gt": {"description": "Match only packets with a greater port number", "format": "number", "not-list": ["src-eq", "src-lt"], "maximum": 65534, "minimum": 1, "type": "number"}, "udp": {"default": 0, "not-list": ["tcp", "ip", "service-obj-group"], "type": "number", "description": "protocol UDP", "format": "flag"}, "dst-subnet": {"not-list": ["dst-any", "dst-host"], "type": "string", "description": "Destination Address", "format": "ipv4-address"}, "src-subnet": {"not-list": ["src-any", "src-host"], "type": "string", "description": "Source Address", "format": "ipv4-address"}, "extd-remark": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Access list entry comment (Notes for this ACL)", "format": "string-rlx"}, "vlan": {"description": "VLAN ID", "minimum": 1, "type": "number", "maximum": 4094, "format": "number"}, "dscp": {"description": "DSCP", "minimum": 1, "type": "number", "maximum": 63, "format": "number"}, "icmp": {"default": 0, "not-list": ["tcp", "udp", "ip", "service-obj-group"], "type": "number", "description": "Internet Control Message Protocol", "format": "flag"}, "optional": true, "extd-action": {"enum": ["deny", "permit", "l3-vlan-fwd-disable"], "type": "string", "description": "'deny': Deny; 'permit': Permit; 'l3-vlan-fwd-disable': Disable L3 forwarding between VLANs; ", "format": "enum"}, "acl-log": {"default": 0, "type": "number", "description": "Log matches against this entry", "format": "flag"}, "src-object-group": {"description": "Network object group (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["src-any", "src-host"], "maxLength": 63, "type": "string"}, "dst-object-group": {"description": "Destination network object group name (Source network object group name)", "format": "string", "minLength": 1, "not-list": ["dst-any", "dst-host"], "maxLength": 63, "type": "string"}, "any-type": {"default": 0, "not": "icmp-type", "type": "number", "description": "Any ICMP type", "format": "flag"}, "dst-any": {"default": 0, "not-list": ["dst-host", "dst-object-group"], "type": "number", "description": "Any destination host", "format": "flag"}, "src-host": {"not-list": ["src-any", "src-object-group"], "type": "string", "description": "A single source host (Host address)", "format": "ipv4-address"}, "dst-lt": {"description": "Match only packets with a lesser port number", "format": "number", "not-list": ["dst-eq", "dst-gt"], "maximum": 65535, "minimum": 2, "type": "number"}, "special-code": {"not": "any-code", "enum": ["frag-required", "host-unreachable", "network-unreachable", "port-unreachable", "proto-unreachable", "route-failed"], "type": "string", "description": "'frag-required': Code 4, fragmentation required; 'host-unreachable': Code 1, destination host unreachable; 'network-unreachable': Code 0, destination network unreachable; 'port-unreachable': Code 3, destination port unreachable; 'proto-unreachable': Code 2, destination protocol unreachable; 'route-failed': Code 5, source route failed; ", "format": "enum"}, "special-type": {"not": "icmp-type", "enum": ["echo-reply", "echo-request", "info-reply", "info-request", "mask-reply", "mask-request", "parameter-problem", "redirect", "source-quench", "time-exceeded", "timestamp", "timestamp-reply", "dest-unreachable"], "type": "string", "description": "'echo-reply': Type 0, echo reply; 'echo-request': Type 8, echo request; 'info-reply': Type 16, information reply; 'info-request': Type 15, information request; 'mask-reply': Type 18, address mask reply; 'mask-request': Type 17, address mask request; 'parameter-problem': Type 12, parameter problem; 'redirect': Type 5, redirect message; 'source-quench': Type 4, source quench; 'time-exceeded': Type 11, time exceeded; 'timestamp': Type 13, timestamp; 'timestamp-reply': Type 14, timestamp reply; 'dest-unreachable': Type 3, destination unreachable; ", "format": "enum"}, "src-eq": {"description": "Match only packets on a given source port (port number)", "format": "number", "not-list": ["src-gt", "src-lt"], "maximum": 65535, "minimum": 1, "type": "number"}, "dst-host": {"not-list": ["dst-any", "dst-object-group"], "type": "string", "description": "A single destination host (Host address)", "format": "ipv4-address"}, "extd-seq-num": {"description": "Sequence number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}}}]}, "extd": {"description": "IP extended access list", "format": "number", "type": "number", "maximum": 199, "minimum": 100, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/access-list/extended/{extd}"}
    :param standard_list: {"minItems": 1, "items": {"type": "standard"}, "uniqueItems": true, "array": [{"required": ["std"], "properties": {"std": {"description": "IP standard access list", "format": "number", "type": "number", "maximum": 99, "minimum": 1, "optional": false}, "stdrules": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"subnet": {"not-list": ["any", "host"], "type": "string", "description": "Address to match", "format": "ipv4-address"}, "std-remark": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Access list entry comment (Notes for this ACL)", "format": "string-rlx"}, "log": {"default": 0, "type": "number", "description": "Log matches against this entry", "format": "flag"}, "seq-num": {"description": "Sequence number", "minimum": 1, "type": "number", "maximum": 8192, "format": "number"}, "rev-subnet-mask": {"type": "string", "description": "Network Mask 0=apply 255=ignore", "format": "ipv4-rev-netmask"}, "host": {"not-list": ["any", "subnet"], "type": "string", "description": "A single source host (Host address)", "format": "ipv4-address"}, "action": {"enum": ["deny", "permit", "l3-vlan-fwd-disable"], "type": "string", "description": "'deny': Deny; 'permit': Permit; 'l3-vlan-fwd-disable': Disable L3 forwarding between VLANs; ", "format": "enum"}, "optional": true, "any": {"default": 0, "not-list": ["host", "subnet"], "type": "number", "description": "Any source host", "format": "flag"}}}]}}}], "type": "array", "$ref": "/axapi/v3/access-list/standard/{std}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/access-list`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "access-list"
        self.a10_url="/axapi/v3/access-list"
        self.DeviceProxy = ""
        self.extended_list = []
        self.standard_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)

