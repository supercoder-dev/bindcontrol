import re
class KeyBind():
    def __init__(self, key, name, page, contents = []):

        if type(contents) == str: contents = [contents]

        self.Key      = key      # actual key combo
        self.Name     = name     # friendly name, ie, "Select All Pets"
        self.Page     = page     # which tab the bind originated on
        self.Contents = contents # a list of strings to '$$'-join to create the actual payload

    # factory for PopulateBindFiles to use
    def MakeFileKeyBind(self, contents):
        if type(contents) == str: contents = [contents]
        self.Contents = contents

        return FileKeyBind(self.Key, self.Name, self.Page, contents)

class FileKeyBind(KeyBind):
    def __init__(self, key, name, page, contents):
        KeyBind.__init__(self, key, name, page, contents)

    def GetKeyBindString(self):

        payload = '$$'.join([i for i in self.Contents if i])

        # remove any initial $$ if we snuck in here with it.
        payload = re.sub(r'^\$\$', '', payload)
        # and any doubled up '$$'
        payload = re.sub(r'\$\$\$\$', '$$', payload)

        return f'{self.Key} "{payload}"\n'


