# vim: set fileencoding=utf-8
"""
pythoneda/__init__.py

This file ensures pythoneda is a namespace.

Copyright (C) 2023-today rydnr's pythoneda-artifact/git-application

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

try:
    from pythoneda.base_object import BaseObject
    from pythoneda.port import Port
    from pythoneda.formatting import Formatting
    from pythoneda.sensitive_value import SensitiveValue
    from pythoneda.value_object import attribute, filter_attribute, internal_attribute, primary_key_attribute, sensitive, ValueObject
    from pythoneda.domain_exception import DomainException
    from pythoneda.unsupported_event import UnsupportedEvent
    from pythoneda.entity import Entity
    from pythoneda.entity_in_progress import EntityInProgress
    from pythoneda.event import Event
    from pythoneda.event_emitter import EventEmitter
    from pythoneda.event_listener import listen, EventListener
    from pythoneda.primary_port import PrimaryPort
    from pythoneda.ports import Ports
    from pythoneda.repo import Repo
except ImportError:
    pass
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
