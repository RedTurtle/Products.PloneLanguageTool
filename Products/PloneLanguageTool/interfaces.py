try:
    from Interface import Interface
except ImportError:
    # for Zope versions before 2.6.0
    from Interface import Base as Interface

class ITranslatable(Interface):
    """
    Interface for translatable content.
    """

    def isTranslation():
        """
        return language if this object is used as multilingual content, 0 otherwise
        """

    def addTranslation(language, **kwargs):
        """
        Add a new language translation of this content.
        """

    def removeTranslation(language):
        """
        Removes a translation
        """

    def getTranslation(language):
        """
        Return the object corresponding to a translated version or None.
        """
 
    def getTranslationLanguages():
        """
        Return a list of language codes
        """

    def getTranslations():
        """
        Return a dict of {lang : [object, wf_state]}
        """

    def isCanonical():
        """
        boolean, is this the original, canonical translation of the content.
        """

    def getCanonicalLanguage():
        """
        Return the language code for the canonical translation of this content.
        """

    def getCanonical():
        """
        Return the original, canonical translation of this content.
        """

    def setTranslationLanguage(language):
        """
        Sets the language for the current translation
        """

    def getTranslationLanguage():
        """
        Returns the language of this translation
        """

    def initializeTranslation():
        """
        Initializes the object as a translation, would typically be called by
        addTranslation.
        """