import xml.sax


class UserHandler(xml.sax.ContentHandler):
    # Call when an element starts
    def startElement(self, tag, attributes):
        print('startElement called for ', tag)

    # Call when a character is read
    def characters(self, content):
        print('characters called for ', content)

    # Call when an elements ends
    def endElement(self, tag):
        print('endElement called for ', tag)


if __name__ == "__main__":
    parser = xml.sax.make_parser()
    # override the default ContextHandler
    handler = UserHandler()
    parser.setContentHandler(handler)
    parser.parse(
        "C:/Users/amaheshwar24/Documents/pythontraining/DXCTraining/Examples/11SampleModules/xml/sax/users1.xml")
