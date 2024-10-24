from typing import List, Dict, Tuple

from LatexElements.date_section import DateSection
from LatexElements.latexelement import LatexElement


class EducationSection(LatexElement):
    class Education(LatexElement):
        def __init__(self, school: str, dates: Tuple[str, str|None], description: str, location : str):
            self.school = school
            self.date = DateSection(dates[0], dates[1])
            self.description = description
            self.location = location

        def text(self):
            return f"{self.school}\n{self.date.text()}\n{self.description}\n{self.location}"

        def get_latex(self) -> str:
            structure = r"""\resumeSubheading
      {\textbf{/ARG1/}}{/ARG1/}
      {/ARG1/}{/ARG1/}

      """
            return LatexElement.inject_variable(structure, self.school, self.date.get_latex(), self.description, self.location)

    def __init__(self, *educations: Education):
        self.educations = list(educations)

    def text(self):
        return "\n".join([c.text() for c in self.educations])

    def get_latex(self) -> str:
        structure = r"""\section{Education}
        \resumeSubHeadingListStart
        /ARG0/
        \resumeSubHeadingListEnd"""
        return LatexElement.inject_variable(structure, [education.get_latex() for education in self.educations])
