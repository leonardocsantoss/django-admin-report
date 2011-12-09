import _base
import new

moduleCache = {}

def getETreeModule(ElementTreeImplementation, fullTree=False):
    name = "_" + ElementTreeImplementation.__name__+"builder"
    if name in moduleCache:
        return moduleCache[name]
    else:
        mod = new.module("_" + ElementTreeImplementation.__name__+"builder")
        objs = getETreeBuilder(ElementTreeImplementation, fullTree)
        mod.__dict__.update(objs)
        moduleCache[name] = mod    
        return mod

def getETreeBuilder(ElementTreeImplementation, fullTree=False):
    ElementTree = ElementTreeImplementation
    class Element(_base.Node):
        def __init__(self, name):
            self._element = ElementTree.Element(name)
            self.name = name
            self.parent = None
            self._childNodes = []
            self._flags = []
    
        def _setName(self, name):
            self._element.tag = name
        
        def _getName(self):
            return self._element.tag
    
        name = property(_getName, _setName)
    
        def _getAttributes(self):
            return self._element.attrib
    
        def _setAttributes(self, attributes):
            #Delete existing attributes first
            #XXX - there may be a better way to do this...
            for key in self._element.attrib.keys():
                del self._element.attrib[key]
            for key, value in attributes.iteritems():
                self._element.set(key, value)
    
        attributes = property(_getAttributes, _setAttributes)
    
        def _getChildNodes(self):
            return self._childNodes
    
        def _setChildNodes(self, value):
            del self._element[:]
            self._childNodes = []
            for element in value:
                self.insertChild(element)
    
        childNodes = property(_getChildNodes, _setChildNodes)
    
        def hasContent(self):
            """Return true if the node has children or text"""
            return bool(self._element.text or self._element.getchildren())
    
        def appendChild(self, node):
            self._childNodes.append(node)
            self._element.append(node._element)
            node.parent = self
    
        def insertBefore(self, node, refNode):
            index = self._element.getchildren().index(refNode._element)
            self._element.insert(index, node._element)
            node.parent = self
    
        def removeChild(self, node):
            self._element.remove(node._element)
            node.parent=None
    
        def insertText(self, data, insertBefore=None):
            if not(len(self._element)):
                if not self._element.text:
                    self._element.text = ""
                self._element.text += data
            elif insertBefore is None:
                #Insert the text as the tail of the last child element
                if not self._element[-1].tail:
                    self._element[-1].tail = ""
                self._element[-1].tail += data
            else:
                #Insert the text before the specified node
                children = self._element.getchildren()
                index = children.index(insertBefore._element)
                if index > 0:
                    if not self._element[index-1].tail:
                        self._element[index-1].tail = ""
                    self._element[index-1].tail += data
                else:
                    if not self._element.text:
                        self._element.text = ""
                    self._element.text += data
    
        def cloneNode(self):
            element = Element(self.name)
            for name, value in self.attributes.iteritems():
                element.attributes[name] = value
            return element
    
        def reparentChildren(self, newParent):
            if newParent.childNodes:
                newParent.childNodes[-1]._element.tail += self._element.text
            else:
                if not newParent._element.text:
                    newParent._element.text = ""
                if self._element.text is not None:
                    newParent._element.text += self._element.text
            self._element.text = ""
            _base.Node.reparentChildren(self, newParent)
    
    class Comment(Element):
        def __init__(self, data):
            #Use the superclass constructor to set all properties on the 
            #wrapper element
            self._element = ElementTree.Comment(data)
            self.parent = None
            self._childNodes = []
            self._flags = []
            
        def _getData(self):
            return self._element.text
    
        def _setData(self, value):
            self._element.text = value
    
        data = property(_getData, _setData)
    
    class DocumentType(Element):
        def __init__(self, name):
            Element.__init__(self, "<!DOCTYPE>") 
            self._element.text = name

        def _getPublicId(self):
            return self._element.get(u"publicId", None)

        def _setPublicId(self, value):
            if value is not None:
                self._element.set(u"publicId", value)

        publicId = property(_getPublicId, _setPublicId)
    
        def _getSystemId(self):
            return self._element.get(u"systemId", None)

        def _setSystemId(self, value):
            if value is not None:
                self._element.set(u"systemId", value)

        systemId = property(_getSystemId, _setSystemId)
    
    class Document(Element):
        def __init__(self):
            Element.__init__(self, "<DOCUMENT_ROOT>") 
    
    class DocumentFragment(Element):
        def __init__(self):
            Element.__init__(self, "<DOCUMENT_FRAGMENT>")
    
    def testSerializer(element):
        rv = []
        finalText = None
        def serializeElement(element, indent=0):
            if not(hasattr(element, "tag")):
                element = element.getroot()
            if element.tag == "<!DOCTYPE>":
                rv.append("|%s<!DOCTYPE %s>"%(' '*indent, element.text))
            elif element.tag == "<DOCUMENT_ROOT>":
                rv.append("#document")
                if element.text:
                    rv.append("|%s\"%s\""%(' '*(indent+2), element.text))
                if element.tail:
                    finalText = element.tail
            elif type(element.tag) == type(ElementTree.Comment):
                rv.append("|%s<!-- %s -->"%(' '*indent, element.text))
            else:
                rv.append("|%s<%s>"%(' '*indent, element.tag))
                if hasattr(element, "attrib"):
                    for name, value in element.attrib.iteritems():
                        rv.append('|%s%s="%s"' % (' '*(indent+2), name, value))
                if element.text:
                    rv.append("|%s\"%s\"" %(' '*(indent+2), element.text))
            indent += 2
            for child in element.getchildren():
                serializeElement(child, indent)
            if element.tail:
                rv.append("|%s\"%s\"" %(' '*(indent-2), element.tail))
        serializeElement(element, 0)
    
        if finalText is not None:
            rv.append("|%s\"%s\""%(' '*2, finalText))
    
        return "\n".join(rv)
    
    def tostring(element):
        """Serialize an element and its child nodes to a string"""
        rv = []
        finalText = None
        def serializeElement(element):
            if type(element) == type(ElementTree.ElementTree):
                element = element.getroot()
            
            if element.tag == "<!DOCTYPE>":
                rv.append("<!DOCTYPE %s>"%(element.text,))
            elif element.tag == "<DOCUMENT_ROOT>":
                if element.text:
                    rv.append(element.text)
                if element.tail:
                    finalText = element.tail
    
                for child in element.getchildren():
                    serializeElement(child)
    
            elif type(element.tag) == type(ElementTree.Comment):
                rv.append("<!--%s-->"%(element.text,))
            else:
                #This is assumed to be an ordinary element
                if not element.attrib:
                    rv.append("<%s>"%(element.tag,))
                else:
                    attr = " ".join(["%s=\"%s\""%(name, value) 
                                     for name, value in element.attrib.iteritems()])
                    rv.append("<%s %s>"%(element.tag, attr))
                if element.text:
                    rv.append(element.text)
    
                for child in element.getchildren():
                    serializeElement(child)
    
                rv.append("</%s>"%(element.tag,))
    
            if element.tail:
                rv.append(element.tail)
    
        serializeElement(element)
    
        if finalText is not None:
            rv.append("%s\""%(' '*2, finalText))
    
        return "".join(rv)
    
    class TreeBuilder(_base.TreeBuilder):
        documentClass = Document
        doctypeClass = DocumentType
        elementClass = Element
        commentClass = Comment
        fragmentClass = DocumentFragment
    
        def testSerializer(self, element):
            return testSerializer(element)
    
        def getDocument(self):
            if fullTree:
                return self.document._element
            else:
                return self.document._element.find("html")
        
        def getFragment(self):
            return _base.TreeBuilder.getFragment(self)._element
        
    return locals()
