class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #    pass

new_journal = Journal()
new_journal.add_entry('I worked out today')
new_journal.add_entry('I ate good food')
print(f'Journal entries:\n{new_journal}')

file = r'D:\temp\journal.txt'
PersistenceManager.save_to_file(new_journal, file)

with open(file) as fh:
    print(fh.read())