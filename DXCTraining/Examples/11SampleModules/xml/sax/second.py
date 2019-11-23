import xml.sax
class Handler( xml.sax.ContentHandler ):
   # Call when an element starts
   def startElement(self, tag, attributes):
      print('startElement called for ',tag)

    # Call when a character is read
   def characters(self, content):
      print('characters called for ',content)
	  
   # Call when an elements ends
   def endElement(self, tag):
      print('endElement called for ',tag)
if ( __name__ == "__main__"):
   # create an XMLReader
   parser = xml.sax.make_parser()
   # override the default ContextHandler
   handler = Handler()
   parser.setContentHandler( handler )
   parser.parse("users.xml")
   
   
   
   
   
   
   