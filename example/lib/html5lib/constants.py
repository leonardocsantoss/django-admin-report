import string, gettext
_ = gettext.gettext

try:
    frozenset
except NameError:
    # Import from the sets module for python 2.3
    from sets import Set as set
    from sets import ImmutableSet as frozenset

EOF = None

E = {
    "null-character": 
       _(u"Null character in input stream, replaced with U+FFFD."),
    "incorrectly-placed-solidus":
       _(u"Solidus (/) incorrectly placed in tag."),
    "incorrect-cr-newline-entity":
       _(u"Incorrect CR newline entity, replaced with LF."),
    "illegal-windows-1252-entity":
       _(u"Entity used with illegal number (windows-1252 reference)."),
    "cant-convert-numeric-entity":
       _(u"Numeric entity couldn't be converted to character "
         u"(codepoint U+%(charAsInt)08x)."),
    "illegal-codepoint-for-numeric-entity":
       _(u"Numeric entity represents an illegal codepoint: "
         u"U+%(charAsInt)08x."),
    "numeric-entity-without-semicolon":
       _(u"Numeric entity didn't end with ';'."),
    "expected-numeric-entity-but-got-eof":
       _(u"Numeric entity expected. Got end of file instead."),
    "expected-numeric-entity":
       _(u"Numeric entity expected but none found."),
    "named-entity-without-semicolon":
       _(u"Named entity didn't end with ';'."),
    "expected-named-entity":
       _(u"Named entity expected. Got none."),
    "attributes-in-end-tag":
       _(u"End tag contains unexpected attributes."),
    "expected-tag-name-but-got-right-bracket":
       _(u"Expected tag name. Got '>' instead."),
    "expected-tag-name-but-got-question-mark":
       _(u"Expected tag name. Got '?' instead. (HTML doesn't "
         u"support processing instructions.)"),
    "expected-tag-name":
       _(u"Expected tag name. Got something else instead"),
    "expected-closing-tag-but-got-right-bracket":
       _(u"Expected closing tag. Got '>' instead. Ignoring '</>'."),
    "expected-closing-tag-but-got-eof":
       _(u"Expected closing tag. Unexpected end of file."),
    "expected-closing-tag-but-got-char":
       _(u"Expected closing tag. Unexpected character '%(data)s' found."),
    "eof-in-tag-name":
       _(u"Unexpected end of file in the tag name."),
    "expected-attribute-name-but-got-eof":
       _(u"Unexpected end of file. Expected attribute name instead."),
    "eof-in-attribute-name":
       _(u"Unexpected end of file in attribute name."),
    "duplicate-attribute":
       _(u"Dropped duplicate attribute on tag."),
    "expected-end-of-tag-name-but-got-eof":
       _(u"Unexpected end of file. Expected = or end of tag."),
    "expected-attribute-value-but-got-eof":
       _(u"Unexpected end of file. Expected attribute value."),
    "eof-in-attribute-value-double-quote":
       _(u"Unexpected end of file in attribute value (\")."),
    "eof-in-attribute-value-single-quote":
       _(u"Unexpected end of file in attribute value (')."),
    "eof-in-attribute-value-no-quotes":
       _(u"Unexpected end of file in attribute value."),
    "expected-dashes-or-doctype":
       _(u"Expected '--' or 'DOCTYPE'. Not found."),
    "incorrect-comment":
       _(u"Incorrect comment."),
    "eof-in-comment":
       _(u"Unexpected end of file in comment."),
    "eof-in-comment-end-dash":
       _(u"Unexpected end of file in comment (-)"),
    "unexpected-dash-after-double-dash-in-comment":
       _(u"Unexpected '-' after '--' found in comment."),
    "eof-in-comment-double-dash":
       _(u"Unexpected end of file in comment (--)."),
    "unexpected-char-in-comment":
       _(u"Unexpected character in comment found."),
    "need-space-after-doctype":
       _(u"No space after literal string 'DOCTYPE'."),
    "expected-doctype-name-but-got-right-bracket":
       _(u"Unexpected > character. Expected DOCTYPE name."),
    "expected-doctype-name-but-got-eof":
       _(u"Unexpected end of file. Expected DOCTYPE name."),
    "eof-in-doctype-name":
       _(u"Unexpected end of file in DOCTYPE name."),
    "eof-in-doctype":
       _(u"Unexpected end of file in DOCTYPE."),
    "expected-space-or-right-bracket-in-doctype":
       _(u"Expected space or '>'. Got '%(data)s'"),
    "unexpected-end-of-doctype":
       _(u"Unexpected end of DOCTYPE."),
    "unexpected-char-in-doctype":
       _(u"Unexpected character in DOCTYPE."),
    "eof-in-bogus-doctype":
       _(u"Unexpected end of file in bogus doctype."),
    "eof-in-innerhtml":
       _(u"XXX innerHTML EOF"),
    "unexpected-doctype":
       _(u"Unexpected DOCTYPE. Ignored."),
    "non-html-root":
       _(u"html needs to be the first start tag."),
    "expected-doctype-but-got-eof":
       _(u"Unexpected End of file. Expected DOCTYPE."),
    "unknown-doctype":
       _(u"Erroneous DOCTYPE."),
    "expected-doctype-but-got-chars":
       _(u"Unexpected non-space characters. Expected DOCTYPE."),
    "expected-doctype-but-got-start-tag":
       _(u"Unexpected start tag (%(name)s). Expected DOCTYPE."),
    "expected-doctype-but-got-end-tag":
       _(u"Unexpected end tag (%(name)s). Expected DOCTYPE."),
    "end-tag-after-implied-root":
       _(u"Unexpected end tag (%(name)s) after the (implied) root element."),
    "expected-named-closing-tag-but-got-eof":
       _(u"Unexpected end of file. Expected end tag (%(name)s)."),
    "two-heads-are-not-better-than-one":
       _(u"Unexpected start tag head in existing head. Ignored."),
    "unexpected-end-tag":
       _(u"Unexpected end tag (%(name)s). Ignored."),
    "unexpected-start-tag-out-of-my-head":
       _(u"Unexpected start tag (%(name)s) that can be in head. Moved."),
    "unexpected-start-tag":
       _(u"Unexpected start tag (%(name)s)."),
    "missing-end-tag":
       _(u"Missing end tag (%(name)s)."),
    "missing-end-tags":
       _(u"Missing end tags (%(name)s)."),
    "unexpected-start-tag-implies-end-tag":
       _(u"Unexpected start tag (%(startName)s) "
         u"implies end tag (%(endName)s)."),
    "unexpected-start-tag-treated-as":
       _(u"Unexpected start tag (%(originalName)s). Treated as %(newName)s."),
    "deprecated-tag":
       _(u"Unexpected start tag %(name)s. Don't use it!"),
    "unexpected-start-tag-ignored":
       _(u"Unexpected start tag %(name)s. Ignored."),
    "expected-one-end-tag-but-got-another":
       _(u"Unexpected end tag (%(gotName)s). "
         u"Missing end tag (%(expectedName)s)."),
    "end-tag-too-early":
       _(u"End tag (%(name)s) seen too early. Expected other end tag."),
    "end-tag-too-early-named":
       _(u"Unexpected end tag (%(gotName)s). Expected end tag (%(expectedName)s)."),
    "end-tag-too-early-ignored":
       _(u"End tag (%(name)s) seen too early. Ignored."),
    "adoption-agency-1.1":
       _(u"End tag (%(name)s) violates step 1, "
         u"paragraph 1 of the adoption agency algorithm."),
    "adoption-agency-1.2":
       _(u"End tag (%(name)s) violates step 1, "
         u"paragraph 2 of the adoption agency algorithm."),
    "adoption-agency-1.3":
       _(u"End tag (%(name)s) violates step 1, "
         u"paragraph 3 of the adoption agency algorithm."),
    "unexpected-end-tag-treated-as":
       _(u"Unexpected end tag (%(originalName)s). Treated as %(newName)s."),
    "no-end-tag":
       _(u"This element (%(name)s) has no end tag."),
    "unexpected-implied-end-tag-in-table":
       _(u"Unexpected implied end tag (%(name)s) in the table phase."),
    "unexpected-implied-end-tag-in-table-body":
       _(u"Unexpected implied end tag (%(name)s) in the table body phase."),
    "unexpected-char-implies-table-voodoo":
       _(u"Unexpected non-space characters in "
         u"table context caused voodoo mode."),
    "unexpected-start-tag-implies-table-voodoo":
       _(u"Unexpected start tag (%(name)s) in "
         u"table context caused voodoo mode."),
    "unexpected-end-tag-implies-table-voodoo":
       _(u"Unexpected end tag (%(name)s) in "
         u"table context caused voodoo mode."),
    "unexpected-cell-in-table-body":
       _(u"Unexpected table cell start tag (%(name)s) "
         u"in the table body phase."),
    "unexpected-cell-end-tag":
       _(u"Got table cell end tag (%(name)s) "
         u"while required end tags are missing."),
    "unexpected-end-tag-in-table-body":
       _(u"Unexpected end tag (%(name)s) in the table body phase. Ignored."),
    "unexpected-implied-end-tag-in-table-row":
       _(u"Unexpected implied end tag (%(name)s) in the table row phase."),
    "unexpected-end-tag-in-table-row":
       _(u"Unexpected end tag (%(name)s) in the table row phase. Ignored."),
    "unexpected-select-in-select":
       _(u"Unexpected select start tag in the select phase "
         u"implies select start tag."),
    "unexpected-start-tag-in-select":
       _(u"Unexpected start tag token (%(name)s in the select phase. "
         u"Ignored."),
    "unexpected-end-tag-in-select":
       _(u"Unexpected end tag (%(name)s) in the select phase. Ignored."),
    "unexpected-char-after-body":
       _(u"Unexpected non-space characters in the after body phase."),
    "unexpected-start-tag-after-body":
       _(u"Unexpected start tag token (%(name)s)"
         u" in the after body phase."),
    "unexpected-end-tag-after-body":
       _(u"Unexpected end tag token (%(name)s)"
         u" in the after body phase."),
    "unexpected-char-in-frameset":
       _(u"Unepxected characters in the frameset phase. Characters ignored."),
    "unexpected-start-tag-in-frameset":
       _(u"Unexpected start tag token (%(name)s)"
         u" in the frameset phase. Ignored."),
    "unexpected-frameset-in-frameset-innerhtml":
       _(u"Unexpected end tag token (frameset) "
         u"in the frameset phase (innerHTML)."),
    "unexpected-end-tag-in-frameset":
       _(u"Unexpected end tag token (%(name)s)"
         u" in the frameset phase. Ignored."),
    "unexpected-char-after-frameset":
       _(u"Unexpected non-space characters in the "
         u"after frameset phase. Ignored."),
    "unexpected-start-tag-after-frameset":
       _(u"Unexpected start tag (%(name)s)"
         u" in the after frameset phase. Ignored."),
    "unexpected-end-tag-after-frameset":
       _(u"Unexpected end tag (%(name)s)"
         u" in the after frameset phase. Ignored."),
    "expected-eof-but-got-char":
       _(u"Unexpected non-space characters. Expected end of file."),
    "expected-eof-but-got-start-tag":
       _(u"Unexpected start tag (%(name)s)"
         u". Expected end of file."),
    "expected-eof-but-got-end-tag":
       _(u"Unexpected end tag (%(name)s)"
         u". Expected end of file."),
}

contentModelFlags = {
    "PCDATA":0,
    "RCDATA":1,
    "CDATA":2,
    "PLAINTEXT":3
}

scopingElements = frozenset((
    "button",
    "caption",
    "html",
    "marquee",
    "object",
    "table",
    "td",
    "th"
))

formattingElements = frozenset((
    "a",
    "b",
    "big",
    "em",
    "font",
    "i",
    "nobr",
    "s",
    "small",
    "strike",
    "strong",
    "tt",
    "u"
))

specialElements = frozenset((
    "address",
    "area",
    "base",
    "basefont",
    "bgsound",
    "blockquote",
    "body",
    "br",
    "center",
    "col",
    "colgroup",
    "dd",
    "dir",
    "div",
    "dl",
    "dt",
    "embed",
    "fieldset",
    "form",
    "frame",
    "frameset",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "head",
    "hr",
    "iframe",
    "image",
    "img",
    "input",
    "isindex",
    "li",
    "link",
    "listing",
    "menu",
    "meta",
    "noembed",
    "noframes",
    "noscript",
    "ol",
    "optgroup",
    "option",
    "p",
    "param",
    "plaintext",
    "pre",
    "script",
    "select",
    "spacer",
    "style",
    "tbody",
    "textarea",
    "tfoot",
    "thead",
    "title",
    "tr",
    "ul",
    "wbr"
))

spaceCharacters = frozenset((
    u"\t",
    u"\n",
    u"\u000B",
    u"\u000C",
    u" ",
    u"\r"
))

tableInsertModeElements = frozenset((
    "table",
    "tbody",
    "tfoot",
    "thead",
    "tr"
))

asciiLowercase = frozenset(string.ascii_lowercase)
asciiUppercase = frozenset(string.ascii_uppercase)
asciiLetters = frozenset(string.ascii_letters)
digits = frozenset(string.digits)
hexDigits = frozenset(string.hexdigits)

asciiUpper2Lower = dict([(ord(c),ord(c.lower()))
    for c in string.ascii_uppercase])

# Heading elements need to be ordered
headingElements = (
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6"
)

# XXX What about event-source and command?
voidElements = frozenset((
    "base",
    "link",
    "meta",
    "hr",
    "br",
    "img",
    "embed",
    "param",
    "area",
    "col",
    "input"
))

cdataElements = frozenset(('title', 'textarea'))

rcdataElements = frozenset((
    'style',
    'script',
    'xmp',
    'iframe',
    'noembed',
    'noframes',
    'noscript'
))

booleanAttributes = {
    "": frozenset(("irrelevant",)),
    "style": frozenset(("scoped",)),
    "img": frozenset(("ismap",)),
    "audio": frozenset(("autoplay","controls")),
    "video": frozenset(("autoplay","controls")),
    "script": frozenset(("defer", "async")),
    "details": frozenset(("open",)),
    "datagrid": frozenset(("multiple", "disabled")),
    "command": frozenset(("hidden", "disabled", "checked", "default")),
    "menu": frozenset(("autosubmit",)),
    "fieldset": frozenset(("disabled", "readonly")),
    "option": frozenset(("disabled", "readonly", "selected")),
    "optgroup": frozenset(("disabled", "readonly")),
    "button": frozenset(("disabled", "autofocus")),
    "input": frozenset(("disabled", "readonly", "required", "autofocus", "checked", "ismap")),
    "select": frozenset(("disabled", "readonly", "autofocus", "multiple")),
    "output": frozenset(("disabled", "readonly")),
}

# entitiesWindows1252 has to be _ordered_ and needs to have an index. It
# therefore can't be a frozenset.
entitiesWindows1252 = (
    8364,  # 0x80  0x20AC  EURO SIGN
    65533, # 0x81          UNDEFINED
    8218,  # 0x82  0x201A  SINGLE LOW-9 QUOTATION MARK
    402,   # 0x83  0x0192  LATIN SMALL LETTER F WITH HOOK
    8222,  # 0x84  0x201E  DOUBLE LOW-9 QUOTATION MARK
    8230,  # 0x85  0x2026  HORIZONTAL ELLIPSIS
    8224,  # 0x86  0x2020  DAGGER
    8225,  # 0x87  0x2021  DOUBLE DAGGER
    710,   # 0x88  0x02C6  MODIFIER LETTER CIRCUMFLEX ACCENT
    8240,  # 0x89  0x2030  PER MILLE SIGN
    352,   # 0x8A  0x0160  LATIN CAPITAL LETTER S WITH CARON
    8249,  # 0x8B  0x2039  SINGLE LEFT-POINTING ANGLE QUOTATION MARK
    338,   # 0x8C  0x0152  LATIN CAPITAL LIGATURE OE
    65533, # 0x8D          UNDEFINED
    381,   # 0x8E  0x017D  LATIN CAPITAL LETTER Z WITH CARON
    65533, # 0x8F          UNDEFINED
    65533, # 0x90          UNDEFINED
    8216,  # 0x91  0x2018  LEFT SINGLE QUOTATION MARK
    8217,  # 0x92  0x2019  RIGHT SINGLE QUOTATION MARK
    8220,  # 0x93  0x201C  LEFT DOUBLE QUOTATION MARK
    8221,  # 0x94  0x201D  RIGHT DOUBLE QUOTATION MARK
    8226,  # 0x95  0x2022  BULLET
    8211,  # 0x96  0x2013  EN DASH
    8212,  # 0x97  0x2014  EM DASH
    732,   # 0x98  0x02DC  SMALL TILDE
    8482,  # 0x99  0x2122  TRADE MARK SIGN
    353,   # 0x9A  0x0161  LATIN SMALL LETTER S WITH CARON
    8250,  # 0x9B  0x203A  SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
    339,   # 0x9C  0x0153  LATIN SMALL LIGATURE OE
    65533, # 0x9D          UNDEFINED
    382,   # 0x9E  0x017E  LATIN SMALL LETTER Z WITH CARON
    376    # 0x9F  0x0178  LATIN CAPITAL LETTER Y WITH DIAERESIS
)

entities = {
    "AElig;": u"\u00C6",
    "AElig": u"\u00C6",
    "AMP;": u"\u0026",
    "AMP": u"\u0026",
    "Aacute;": u"\u00C1",
    "Aacute": u"\u00C1",
    "Acirc;": u"\u00C2",
    "Acirc": u"\u00C2",
    "Agrave;": u"\u00C0",
    "Agrave": u"\u00C0",
    "Alpha;": u"\u0391",
    "Aring;": u"\u00C5",
    "Aring": u"\u00C5",
    "Atilde;": u"\u00C3",
    "Atilde": u"\u00C3",
    "Auml;": u"\u00C4",
    "Auml": u"\u00C4",
    "Beta;": u"\u0392",
    "COPY;": u"\u00A9",
    "COPY": u"\u00A9",
    "Ccedil;": u"\u00C7",
    "Ccedil": u"\u00C7",
    "Chi;": u"\u03A7",
    "Dagger;": u"\u2021",
    "Delta;": u"\u0394",
    "ETH;": u"\u00D0",
    "ETH": u"\u00D0",
    "Eacute;": u"\u00C9",
    "Eacute": u"\u00C9",
    "Ecirc;": u"\u00CA",
    "Ecirc": u"\u00CA",
    "Egrave;": u"\u00C8",
    "Egrave": u"\u00C8",
    "Epsilon;": u"\u0395",
    "Eta;": u"\u0397",
    "Euml;": u"\u00CB",
    "Euml": u"\u00CB",
    "GT;": u"\u003E",
    "GT": u"\u003E",
    "Gamma;": u"\u0393",
    "Iacute;": u"\u00CD",
    "Iacute": u"\u00CD",
    "Icirc;": u"\u00CE",
    "Icirc": u"\u00CE",
    "Igrave;": u"\u00CC",
    "Igrave": u"\u00CC",
    "Iota;": u"\u0399",
    "Iuml;": u"\u00CF",
    "Iuml": u"\u00CF",
    "Kappa;": u"\u039A",
    "LT;": u"\u003C",
    "LT": u"\u003C",
    "Lambda;": u"\u039B",
    "Mu;": u"\u039C",
    "Ntilde;": u"\u00D1",
    "Ntilde": u"\u00D1",
    "Nu;": u"\u039D",
    "OElig;": u"\u0152",
    "Oacute;": u"\u00D3",
    "Oacute": u"\u00D3",
    "Ocirc;": u"\u00D4",
    "Ocirc": u"\u00D4",
    "Ograve;": u"\u00D2",
    "Ograve": u"\u00D2",
    "Omega;": u"\u03A9",
    "Omicron;": u"\u039F",
    "Oslash;": u"\u00D8",
    "Oslash": u"\u00D8",
    "Otilde;": u"\u00D5",
    "Otilde": u"\u00D5",
    "Ouml;": u"\u00D6",
    "Ouml": u"\u00D6",
    "Phi;": u"\u03A6",
    "Pi;": u"\u03A0",
    "Prime;": u"\u2033",
    "Psi;": u"\u03A8",
    "QUOT;": u"\u0022",
    "QUOT": u"\u0022",
    "REG;": u"\u00AE",
    "REG": u"\u00AE",
    "Rho;": u"\u03A1",
    "Scaron;": u"\u0160",
    "Sigma;": u"\u03A3",
    "THORN;": u"\u00DE",
    "THORN": u"\u00DE",
    "TRADE;": u"\u2122",
    "Tau;": u"\u03A4",
    "Theta;": u"\u0398",
    "Uacute;": u"\u00DA",
    "Uacute": u"\u00DA",
    "Ucirc;": u"\u00DB",
    "Ucirc": u"\u00DB",
    "Ugrave;": u"\u00D9",
    "Ugrave": u"\u00D9",
    "Upsilon;": u"\u03A5",
    "Uuml;": u"\u00DC",
    "Uuml": u"\u00DC",
    "Xi;": u"\u039E",
    "Yacute;": u"\u00DD",
    "Yacute": u"\u00DD",
    "Yuml;": u"\u0178",
    "Zeta;": u"\u0396",
    "aacute;": u"\u00E1",
    "aacute": u"\u00E1",
    "acirc;": u"\u00E2",
    "acirc": u"\u00E2",
    "acute;": u"\u00B4",
    "acute": u"\u00B4",
    "aelig;": u"\u00E6",
    "aelig": u"\u00E6",
    "agrave;": u"\u00E0",
    "agrave": u"\u00E0",
    "alefsym;": u"\u2135",
    "alpha;": u"\u03B1",
    "amp;": u"\u0026",
    "amp": u"\u0026",
    "and;": u"\u2227",
    "ang;": u"\u2220",
    "apos;": u"\u0027",
    "aring;": u"\u00E5",
    "aring": u"\u00E5",
    "asymp;": u"\u2248",
    "atilde;": u"\u00E3",
    "atilde": u"\u00E3",
    "auml;": u"\u00E4",
    "auml": u"\u00E4",
    "bdquo;": u"\u201E",
    "beta;": u"\u03B2",
    "brvbar;": u"\u00A6",
    "brvbar": u"\u00A6",
    "bull;": u"\u2022",
    "cap;": u"\u2229",
    "ccedil;": u"\u00E7",
    "ccedil": u"\u00E7",
    "cedil;": u"\u00B8",
    "cedil": u"\u00B8",
    "cent;": u"\u00A2",
    "cent": u"\u00A2",
    "chi;": u"\u03C7",
    "circ;": u"\u02C6",
    "clubs;": u"\u2663",
    "cong;": u"\u2245",
    "copy;": u"\u00A9",
    "copy": u"\u00A9",
    "crarr;": u"\u21B5",
    "cup;": u"\u222A",
    "curren;": u"\u00A4",
    "curren": u"\u00A4",
    "dArr;": u"\u21D3",
    "dagger;": u"\u2020",
    "darr;": u"\u2193",
    "deg;": u"\u00B0",
    "deg": u"\u00B0",
    "delta;": u"\u03B4",
    "diams;": u"\u2666",
    "divide;": u"\u00F7",
    "divide": u"\u00F7",
    "eacute;": u"\u00E9",
    "eacute": u"\u00E9",
    "ecirc;": u"\u00EA",
    "ecirc": u"\u00EA",
    "egrave;": u"\u00E8",
    "egrave": u"\u00E8",
    "empty;": u"\u2205",
    "emsp;": u"\u2003",
    "ensp;": u"\u2002",
    "epsilon;": u"\u03B5",
    "equiv;": u"\u2261",
    "eta;": u"\u03B7",
    "eth;": u"\u00F0",
    "eth": u"\u00F0",
    "euml;": u"\u00EB",
    "euml": u"\u00EB",
    "euro;": u"\u20AC",
    "exist;": u"\u2203",
    "fnof;": u"\u0192",
    "forall;": u"\u2200",
    "frac12;": u"\u00BD",
    "frac12": u"\u00BD",
    "frac14;": u"\u00BC",
    "frac14": u"\u00BC",
    "frac34;": u"\u00BE",
    "frac34": u"\u00BE",
    "frasl;": u"\u2044",
    "gamma;": u"\u03B3",
    "ge;": u"\u2265",
    "gt;": u"\u003E",
    "gt": u"\u003E",
    "hArr;": u"\u21D4",
    "harr;": u"\u2194",
    "hearts;": u"\u2665",
    "hellip;": u"\u2026",
    "iacute;": u"\u00ED",
    "iacute": u"\u00ED",
    "icirc;": u"\u00EE",
    "icirc": u"\u00EE",
    "iexcl;": u"\u00A1",
    "iexcl": u"\u00A1",
    "igrave;": u"\u00EC",
    "igrave": u"\u00EC",
    "image;": u"\u2111",
    "infin;": u"\u221E",
    "int;": u"\u222B",
    "iota;": u"\u03B9",
    "iquest;": u"\u00BF",
    "iquest": u"\u00BF",
    "isin;": u"\u2208",
    "iuml;": u"\u00EF",
    "iuml": u"\u00EF",
    "kappa;": u"\u03BA",
    "lArr;": u"\u21D0",
    "lambda;": u"\u03BB",
    "lang;": u"\u3008",
    "laquo;": u"\u00AB",
    "laquo": u"\u00AB",
    "larr;": u"\u2190",
    "lceil;": u"\u2308",
    "ldquo;": u"\u201C",
    "le;": u"\u2264",
    "lfloor;": u"\u230A",
    "lowast;": u"\u2217",
    "loz;": u"\u25CA",
    "lrm;": u"\u200E",
    "lsaquo;": u"\u2039",
    "lsquo;": u"\u2018",
    "lt;": u"\u003C",
    "lt": u"\u003C",
    "macr;": u"\u00AF",
    "macr": u"\u00AF",
    "mdash;": u"\u2014",
    "micro;": u"\u00B5",
    "micro": u"\u00B5",
    "middot;": u"\u00B7",
    "middot": u"\u00B7",
    "minus;": u"\u2212",
    "mu;": u"\u03BC",
    "nabla;": u"\u2207",
    "nbsp;": u"\u00A0",
    "nbsp": u"\u00A0",
    "ndash;": u"\u2013",
    "ne;": u"\u2260",
    "ni;": u"\u220B",
    "not;": u"\u00AC",
    "not": u"\u00AC",
    "notin;": u"\u2209",
    "nsub;": u"\u2284",
    "ntilde;": u"\u00F1",
    "ntilde": u"\u00F1",
    "nu;": u"\u03BD",
    "oacute;": u"\u00F3",
    "oacute": u"\u00F3",
    "ocirc;": u"\u00F4",
    "ocirc": u"\u00F4",
    "oelig;": u"\u0153",
    "ograve;": u"\u00F2",
    "ograve": u"\u00F2",
    "oline;": u"\u203E",
    "omega;": u"\u03C9",
    "omicron;": u"\u03BF",
    "oplus;": u"\u2295",
    "or;": u"\u2228",
    "ordf;": u"\u00AA",
    "ordf": u"\u00AA",
    "ordm;": u"\u00BA",
    "ordm": u"\u00BA",
    "oslash;": u"\u00F8",
    "oslash": u"\u00F8",
    "otilde;": u"\u00F5",
    "otilde": u"\u00F5",
    "otimes;": u"\u2297",
    "ouml;": u"\u00F6",
    "ouml": u"\u00F6",
    "para;": u"\u00B6",
    "para": u"\u00B6",
    "part;": u"\u2202",
    "permil;": u"\u2030",
    "perp;": u"\u22A5",
    "phi;": u"\u03C6",
    "pi;": u"\u03C0",
    "piv;": u"\u03D6",
    "plusmn;": u"\u00B1",
    "plusmn": u"\u00B1",
    "pound;": u"\u00A3",
    "pound": u"\u00A3",
    "prime;": u"\u2032",
    "prod;": u"\u220F",
    "prop;": u"\u221D",
    "psi;": u"\u03C8",
    "quot;": u"\u0022",
    "quot": u"\u0022",
    "rArr;": u"\u21D2",
    "radic;": u"\u221A",
    "rang;": u"\u3009",
    "raquo;": u"\u00BB",
    "raquo": u"\u00BB",
    "rarr;": u"\u2192",
    "rceil;": u"\u2309",
    "rdquo;": u"\u201D",
    "real;": u"\u211C",
    "reg;": u"\u00AE",
    "reg": u"\u00AE",
    "rfloor;": u"\u230B",
    "rho;": u"\u03C1",
    "rlm;": u"\u200F",
    "rsaquo;": u"\u203A",
    "rsquo;": u"\u2019",
    "sbquo;": u"\u201A",
    "scaron;": u"\u0161",
    "sdot;": u"\u22C5",
    "sect;": u"\u00A7",
    "sect": u"\u00A7",
    "shy;": u"\u00AD",
    "shy": u"\u00AD",
    "sigma;": u"\u03C3",
    "sigmaf;": u"\u03C2",
    "sim;": u"\u223C",
    "spades;": u"\u2660",
    "sub;": u"\u2282",
    "sube;": u"\u2286",
    "sum;": u"\u2211",
    "sup1;": u"\u00B9",
    "sup1": u"\u00B9",
    "sup2;": u"\u00B2",
    "sup2": u"\u00B2",
    "sup3;": u"\u00B3",
    "sup3": u"\u00B3",
    "sup;": u"\u2283",
    "supe;": u"\u2287",
    "szlig;": u"\u00DF",
    "szlig": u"\u00DF",
    "tau;": u"\u03C4",
    "there4;": u"\u2234",
    "theta;": u"\u03B8",
    "thetasym;": u"\u03D1",
    "thinsp;": u"\u2009",
    "thorn;": u"\u00FE",
    "thorn": u"\u00FE",
    "tilde;": u"\u02DC",
    "times;": u"\u00D7",
    "times": u"\u00D7",
    "trade;": u"\u2122",
    "uArr;": u"\u21D1",
    "uacute;": u"\u00FA",
    "uacute": u"\u00FA",
    "uarr;": u"\u2191",
    "ucirc;": u"\u00FB",
    "ucirc": u"\u00FB",
    "ugrave;": u"\u00F9",
    "ugrave": u"\u00F9",
    "uml;": u"\u00A8",
    "uml": u"\u00A8",
    "upsih;": u"\u03D2",
    "upsilon;": u"\u03C5",
    "uuml;": u"\u00FC",
    "uuml": u"\u00FC",
    "weierp;": u"\u2118",
    "xi;": u"\u03BE",
    "yacute;": u"\u00FD",
    "yacute": u"\u00FD",
    "yen;": u"\u00A5",
    "yen": u"\u00A5",
    "yuml;": u"\u00FF",
    "yuml": u"\u00FF",
    "zeta;": u"\u03B6",
    "zwj;": u"\u200D",
    "zwnj;": u"\u200C"
}

encodings = frozenset((
    "ansi_x3.4-1968",
    "iso-ir-6",
    "ansi_x3.4-1986",
    "iso_646.irv:1991",
    "ascii",
    "iso646-us",
    "us-ascii",
    "us",
    "ibm367",
    "cp367",
    "csascii",
    "ks_c_5601-1987",
    "korean",
    "iso-2022-kr",
    "csiso2022kr",
    "euc-kr",
    "iso-2022-jp",
    "csiso2022jp",
    "iso-2022-jp-2",
    "iso-ir-58",
    "chinese",
    "csiso58gb231280",
    "iso_8859-1:1987",
    "iso-ir-100",
    "iso_8859-1",
    "iso-8859-1",
    "latin1",
    "l1",
    "ibm819",
    "cp819",
    "csisolatin1",
    "iso_8859-2:1987",
    "iso-ir-101",
    "iso_8859-2",
    "iso-8859-2",
    "latin2",
    "l2",
    "csisolatin2",
    "iso_8859-3:1988",
    "iso-ir-109",
    "iso_8859-3",
    "iso-8859-3",
    "latin3",
    "l3",
    "csisolatin3",
    "iso_8859-4:1988",
    "iso-ir-110",
    "iso_8859-4",
    "iso-8859-4",
    "latin4",
    "l4",
    "csisolatin4",
    "iso_8859-6:1987",
    "iso-ir-127",
    "iso_8859-6",
    "iso-8859-6",
    "ecma-114",
    "asmo-708",
    "arabic",
    "csisolatinarabic",
    "iso_8859-7:1987",
    "iso-ir-126",
    "iso_8859-7",
    "iso-8859-7",
    "elot_928",
    "ecma-118",
    "greek",
    "greek8",
    "csisolatingreek",
    "iso_8859-8:1988",
    "iso-ir-138",
    "iso_8859-8",
    "iso-8859-8",
    "hebrew",
    "csisolatinhebrew",
    "iso_8859-5:1988",
    "iso-ir-144",
    "iso_8859-5",
    "iso-8859-5",
    "cyrillic",
    "csisolatincyrillic",
    "iso_8859-9:1989",
    "iso-ir-148",
    "iso_8859-9",
    "iso-8859-9",
    "latin5",
    "l5",
    "csisolatin5",
    "iso-8859-10",
    "iso-ir-157",
    "l6",
    "iso_8859-10:1992",
    "csisolatin6",
    "latin6",
    "hp-roman8",
    "roman8",
    "r8",
    "ibm037",
    "cp037",
    "csibm037",
    "ibm424",
    "cp424",
    "csibm424",
    "ibm437",
    "cp437",
    "437",
    "cspc8codepage437",
    "ibm500",
    "cp500",
    "csibm500",
    "ibm775",
    "cp775",
    "cspc775baltic",
    "ibm850",
    "cp850",
    "850",
    "cspc850multilingual",
    "ibm852",
    "cp852",
    "852",
    "cspcp852",
    "ibm855",
    "cp855",
    "855",
    "csibm855",
    "ibm857",
    "cp857",
    "857",
    "csibm857",
    "ibm860",
    "cp860",
    "860",
    "csibm860",
    "ibm861",
    "cp861",
    "861",
    "cp-is",
    "csibm861",
    "ibm862",
    "cp862",
    "862",
    "cspc862latinhebrew",
    "ibm863",
    "cp863",
    "863",
    "csibm863",
    "ibm864",
    "cp864",
    "csibm864",
    "ibm865",
    "cp865",
    "865",
    "csibm865",
    "ibm866",
    "cp866",
    "866",
    "csibm866",
    "ibm869",
    "cp869",
    "869",
    "cp-gr",
    "csibm869",
    "ibm1026",
    "cp1026",
    "csibm1026",
    "koi8-r",
    "cskoi8r",
    "koi8-u",
    "big5-hkscs",
    "ptcp154",
    "csptcp154",
    "pt154",
    "cp154",
    "utf-7",
    "utf-16be",
    "utf-16le",
    "utf-16",
    "utf-8",
    "iso-8859-13",
    "iso-8859-14",
    "iso-ir-199",
    "iso_8859-14:1998",
    "iso_8859-14",
    "latin8",
    "iso-celtic",
    "l8",
    "iso-8859-15",
    "iso_8859-15",
    "iso-8859-16",
    "iso-ir-226",
    "iso_8859-16:2001",
    "iso_8859-16",
    "latin10",
    "l10",
    "gbk",
    "cp936",
    "ms936",
    "gb18030",
    "shift_jis",
    "ms_kanji",
    "csshiftjis",
    "euc-jp",
    "gb2312",
    "big5",
    "csbig5",
    "windows-1250",
    "windows-1251",
    "windows-1252",
    "windows-1253",
    "windows-1254",
    "windows-1255",
    "windows-1256",
    "windows-1257",
    "windows-1258",
    "tis-620",
    "hz-gb-2312",
    ))
