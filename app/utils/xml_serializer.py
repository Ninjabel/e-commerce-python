import dicttoxml

def to_xml(obj):
    return dicttoxml.dicttoxml(obj.__dict__).decode()