
class ChatMemory:

    def __init__(self, system_prompt=None, welcome_prompt=None):
        if system_prompt is None:
            system_prompt = """
                TODO: Implement system prompt
            """

        if welcome_prompt is None:
            welcome_prompt = """
                TODO: Implement welcome prompt
            """

        self.system_prompt = system_prompt
        self.welcome_prompt = welcome_prompt

        self.context = [
            self.system_prompt,
            self.welcome_prompt
        ]

    def add(self, query):
        self.context.append(query)

    def get_last(self):
        return self.context[-1]

    def get_all(self):
        return self.context

    def clean(self, keep_config=True):
        if keep_config:
            self.context = [
                self.system_prompt,
                self.welcome_prompt
            ]
        else:
            self.context = []

    def __str__(self):
        return '\n'.join(self.context)

    def __repr__(self):
        return '\n'.join(self.context)

    def __len__(self):
        return len(self.context)

    def __getitem__(self, key):
        return self.context[key]

    def __setitem__(self, key, value):
        self.context[key] = value

    def __delitem__(self, key):
        del self.context[key]

    def __iter__(self):
        return iter(self.context)

    def __contains__(self, item):
        return item in self.context
