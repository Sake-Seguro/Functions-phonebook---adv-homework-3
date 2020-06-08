
### Creating classes for a Contact and a Phonebook

class Contact:

    def __init__(self, personal_name, personal_surname, phone_number, favourite=False, **adding_data):

        self.base_personal_name = personal_name
        self.base_second_name = personal_surname
        self.base_phone = phone_number
        self.base_favourite = favourite
        self.__dict__.update(adding_data)

    def __str__(self):

        print(f'\nName: {self.base_personal_name}')
        print(f'Surname: {self.base_second_name}')
        print(f'Contact phone: {self.base_phone}')
        if self.base_favourite:
            print(f'In favourites: Yes')
        else:
            print(f'In favourites: No')
        print(f"Additional info:")
        for key, value in self.__dict__.items():
            if key.startswith('base'):
                pass
            else:
                print('\t\t{} = {}'.format(key, value))


class Phonebook:

    def __init__(self, phonebook_name):
        self.phonebook_name = phonebook_name
        self.contacts = []

    def printing_contacts(self):

        """
        Printing contacts from the Phonebook
        """
        print('\n' + self.phonebook_name + '\n')
        for any_name in self.contacts:
            any_name.__str__()

    def adding_contact(self, name):

        """
        Adding a new contact to the Phonebook
        """

        self.contacts.append(name)

    def deleting_contact(self, phone_number):

        """
        Removing any contact by his/ her phone number
        """
        for any_contact in self.contacts:
            if any_contact.base_phone == phone_number:
                self.contacts.remove(any_contact)

    def selecting_favourite(self):

        """
        Searching for your favourites
        """
        for any_person in self.contacts:
            if any_person.base_favourite:
                any_person.__str__()

    def searching_person(self, fname, sname):

        """
        Searching for any contact by his/ her name & surname
        """
        for any_person in self.contacts:
            if any_person.base_personal_name == fname and any_person.base_second_name == sname:
                any_person.__str__()


if __name__ == '__main__':

  vovchik = Contact('Vovan', 'Kabaevich', '+70010020304', False, telegram='@russian_emperor', email='vovan@kremlin.com')

  dimon = Contact('Nedimon', 'Neshtangist', '+70020030405', True, viber='chudachek')

  alinka = Contact('Alina', 'Nekabaeva', '+70010010101', True,telegram='@uzbek_princess')

  
  ladies_and_gentlemen = Phonebook('Who is who in this world')
  ladies_and_gentlemen.adding_contact(alinka)
  ladies_and_gentlemen.adding_contact(dimon)
  ladies_and_gentlemen.adding_contact(vovchik)
  ladies_and_gentlemen.printing_contacts()
  # ladies_and_gentlemen.deleting_contact('+70020030405')
  # ladies_and_gentlemen.printing_contacts()
  # ladies_and_gentlemen.selecting_favourite()
  # ladies_and_gentlemen.searching_person('Alina', 'Nekabaeva')

