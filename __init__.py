from mycroft import MycroftSkill, intent_file_handler


class GrocyIntegration(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('integration.grocy.intent')
    def handle_integration_grocy(self, message):
        self.speak_dialog('integration.grocy')


def create_skill():
    return GrocyIntegration()

