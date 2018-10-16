from lxml import etree
from os.path import join
import glob
import sys

def validate(xml_path: str, xsd_schema: etree.XMLSchema) -> bool:
    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result

xmlschema_doc = etree.parse(join("smdx", "smdx.xsd"))
xmlschema = etree.XMLSchema(xmlschema_doc)

for filename in glob.glob("**/*.xml"):
    if "manifest" in filename:
        continue

    if not validate(filename, xmlschema):
        print("%s failed %s" % (filename, xmlschema.error_log))
        sys.exit(1)

sys.exit(0)
