# Copyright (C) 2011 Nippon Telegraph and Telephone Corporation.
# Copyright (C) 2011 Isaku Yamahata <yamahata at valinux co jp>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class RyuException(Exception):
    message = 'An unknown exception'

    def __init__(self, msg=None, **kwargs):
        self.kwargs = kwargs
        if msg is None:
            msg = self.message

        try:
            msg = msg % kwargs
        except Exception:
            msg = self.message

        super(RyuException, self).__init__(msg)


class OFPUnknownVersion(RyuException):
    message = 'unknown version %(version)x'

class OFPMalformedMessage(RyuException):
    message = 'malformed message'

class NetworkNotFound(RyuException):
    message = 'no such network id %(network_id)s'

class NetworkAlreadyExist(RyuException):
    message = 'network id %(network_id)s already exists'

class PortNotFound(RyuException):
    message = 'no such port (%(dpid)s, %(port)s) in network %(network_id)s'

class PortAlreadyExist(RyuException):
    message = 'port (%(dpid)s, %(port)s) in network %(network_id)s ' \
              'already exists'

class PortUnknown(RyuException):
    message = 'unknown network id for port (%(dpid)s %(port)s)'

class MacAddressDuplicated(RyuException):
    message = 'MAC address %(mac)s is duplicated'

class MacAddressNotFound(RyuException):
    message = 'No such MAC address %(mac)s found'

class BondAlreadyExist(RyuException):
    message = 'Bond id %(bond_id)s already exists'

class BondNotFound(RyuException):
    message = 'No such bond with id %(bond_id)s found'

class BondNetworkMismatch(RyuException):
    message = "Port's network id does not match network id for bond %(bond_id)s"

class BondPortNotFound(RyuException):
    message = 'Port number %(port)s does not exist in bond %(bond_id)s'

class BondPortAlreadyBonded(RyuException):
    message = 'Port number %(port)s already exists in bond %(bond_id)s'

class FlowSpaceIDAlreadyExist(RyuException):
   message = 'FlowSpace ID %(flowspace_id)s already exists'

class NetworkAlreadyAssigned(RyuException):
    message = 'Network ID %(network_id)s already assigned to slice %(sliceName)s'

