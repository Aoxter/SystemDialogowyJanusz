from UserActType import UserActType
from UserAct import UserAct
import jsgf


class NLU:
    def __init__(self):
        self.book_grammar = jsgf.parse_grammar_file('book.jsgf')

    def get_dialog_act(self, rule):
        slots = []
        self.get_slots(rule.expansion, slots)
        print(rule)
        print(slots)
        return UserAct(UserActType[rule.name.upper()], slots)

    def get_slots(self, expansion, slots):
        if expansion.tag != '':
            slots.append((expansion.tag, expansion.current_match))
            return

        for child in expansion.children:
            self.get_slots(child, slots)

        if not expansion.children and isinstance(expansion, jsgf.NamedRuleRef):
            self.get_slots(expansion.referenced_rule.expansion, slots)

    def parse_user_input(self, text: str) -> UserAct:
        matched_rules = self.book_grammar.find_matching_rules(text)
        if matched_rules:
            return self.get_dialog_act(matched_rules[0])
        return UserAct(UserActType.INVALID)
