# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from plone.supermodel import model

from collective.contact.widget import schema

from collective.contact.contactlist import _


class IContactList(model.Schema):
    """Interface for ContactList content type"""

    contacts = schema.ContactList(
        title=_("Contacts of the list"),
        )

class ICollectiveContactContactlistLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IUserLists(Interface):
    """Adapts user, portal and request to get user list location
    """

    def get_lists(self):
        """Get lists user can use
        """

    def get_lists_brains(self):
        """Get lists user can use
        """

    def get_container(self):
        """Get lists container
        """
