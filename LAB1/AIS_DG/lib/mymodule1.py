STATIC_VALUE = 10

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last':last_name}
    return person

def build_person_with_title(title, first_name, last_name):
    """Return a dictionary of information about a person with title."""
    person = {'title': title, 'first': first_name, 'last':last_name}
    return person