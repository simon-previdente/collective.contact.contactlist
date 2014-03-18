from zope.component import getMultiAdapter, getUtility
from zope.intid.interfaces import IIntIds

from z3c.relationfield.relation import RelationValue

from plone import api as ploneapi

from collective.contact.contactlist.interfaces import IUserLists


def get_user_lists_adapter():
    """Get list storage of current user
    """
    user = ploneapi.user.get_current()
    portal = ploneapi.portal.get()
    adapter = getMultiAdapter((user, portal, portal.REQUEST),
                                IUserLists)
    return adapter


def create_list(title, description, contacts, list_type='contact_list'):
    """Create a list of contacts
    @param title: str - The title of the list of contacts
    @param description : str - The description of the list
    @param contacts: objects - A list of contact objects
    @param list_type: str - The portal type of contact_list to create
    @return: the contact list content object
    """
    container = get_user_lists_adapter().get_container()
    contact_list = ploneapi.content.create(container=container,
                                           type=list_type, title=title,
                                           description=description)
    intids = getUtility(IIntIds)
    contact_list.contacts = [RelationValue(intids.getId(obj))
                             for obj in contacts]
    return contact_list


def update_list(contact_list, contacts):
    """Add contacts to a contact list
    @param contact_list: object - The contact list object
    @param contacts: objects - A list of contact objects
    @return: objects - the list of contacts that have been actually added
    """
    current_contacts = [c.to_object for c in contact_list.contacts]
    new_contacts = []
    for contact in contacts:
        if contact not in current_contacts:
            new_contacts.append(contact)

    intids = getUtility(IIntIds)
    contact_list.contacts.extend([RelationValue(intids.getId(obj)) for obj in new_contacts])
    return new_contacts