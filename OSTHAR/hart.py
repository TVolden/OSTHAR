import xml.etree.ElementTree as ET

def get_behavior_schemas():
    return [c.get('id') for c in get_codelists('behavior')]

def get_affect_schemas():
    return [c.get('id') for c in get_codelists('affect')]

def get_behaviors(schema):
    for codelist in get_codelists('behavior'):
        if codelist.get('id') == schema:
            return [item.get('id') for item in codelist.findall("item")]
    return []

def get_affects(schema):
    for codelist in get_codelists('affect'):
        if codelist.get('id') == schema:
            return [item.get('id') for item in codelist.findall("item")]
    return []

def get_codelists(name):
    tree = ET.parse('static/HARTSchemas.xml')
    root = tree.getroot()
    for category in root.findall("category"):
        if category.get('id') == name:
            return [c for c in category.findall('codelist')]
    return []
