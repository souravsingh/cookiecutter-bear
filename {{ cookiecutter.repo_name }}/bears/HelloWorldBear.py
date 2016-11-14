from coalib.bears.LocalBear import Loc


class HelloWorldBear:
    """
    Add description for you bear here!
    """
    LANGUAGES = {"Python", "Python 2", "Python 3"}
    AUTHORS = {full_name}
    REQUIREMENTS = {PipRequirement('mypy-lang', '0.*')}
    AUTHORS_EMAILS = {email}
    LICENSE = license
    ASCIINEMA_URL = 'https://asciinema.org/a/90736'

    def run(self,
            filename,
            file):
        self.debug("Hello World! Checking file", filename, ".")
