from abc import ABC, abstractmethod
from typing import List, Tuple
import re


class LatexElement(ABC):

    @abstractmethod
    def get_latex(self) -> str:
        pass

    @abstractmethod
    def text(self) -> str:
        pass

    def __str__(self) -> str:
        return self.get_latex()

    @staticmethod
    def inject_variable(string: str, *variables: any, key='/ARG[0-9]/', delimiter="\n") -> str | ValueError:

        variables = variables[0] if len(variables) == 1 and isinstance(variables[0], list) else list(variables)
        while len(variables) > 0:
            arg_form = re.search(key, string)
            if not arg_form:
                raise ValueError("Variable ARG quantity mismatch")

            n_args = int(arg_form.group()[4])
            variables_to_inject = []
            if n_args == 0:
                variables_to_inject = variables[:]
                del variables[:]
            else:
                variables_to_inject = variables[0:n_args]
                del variables[0:n_args]
            string = string.replace(arg_form.group(), delimiter.join([str(v) for v in variables_to_inject]), 1)

        return string

