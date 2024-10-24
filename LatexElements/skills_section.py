

from typing import List, Dict, Tuple
from LatexElements.latexelement import LatexElement


class SkillsSection(LatexElement):
    class Skill(LatexElement):
        def __init__(self, title: str, skills: str):
            self.title = title
            self.skills = skills

        def text(self) -> str:
            return f"{self.title}: {self.skills}"

        def get_latex(self) -> str:
            structure = r"""\textbf{/ARG1/}{: /ARG1/} \\"""
            return LatexElement.inject_variable(structure, self.title, self.skills)

    def __init__(self, *skills: Skill):
        self.skills = list(skills)

    def text(self):
        return "\n".join([c.text() for c in self.skills])

    def get_latex(self) -> str:
        structure = r"""\section{Skills}
        \begin{itemize}[leftmargin=0.15in, label={}]
        \small{\item{
        /ARG0/

        \end{itemize}"""
        return LatexElement.inject_variable(structure, self.skills)
