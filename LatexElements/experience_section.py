from typing import List, Dict, Tuple

from LatexElements.has_bullet_points import HasBulletPoints
from LatexElements.bullet_points import BulletPoints
from LatexElements.date_section import DateSection
from LatexElements.latexelement import LatexElement
from LatexElements.title_link import TitleLink


class ExperienceSection(LatexElement):
    class Experience(LatexElement, HasBulletPoints):
        def __init__(self, job_title: Tuple[str, str], skills: str, company: str, dates: Tuple[str, str|None],
                     location: str, *bullet_points: str):
            self.job_title = TitleLink(job_title[0], job_title[1])
            self.skills = skills
            self.company = company
            self.date = DateSection(dates[0], dates[1])
            self.location = location
            self.bullet_points = BulletPoints(*bullet_points)

        def update_bullet_points(self, *bullet_points: str):
            self.bullet_points = BulletPoints(*bullet_points)

        def update_job_title(self, job_title: Tuple[str, str]):
            self.job_title = TitleLink(job_title[0], job_title[1])

        def get_latex(self) -> str:
            structure = r"""\resumeExperienceSubheading
            {\textbf{/ARG1/ }{$|$ \emph{/ARG1/}}}{/ARG1/}
            {/ARG1/}{/ARG1/}
            /ARG1/
            """

            return LatexElement.inject_variable(structure, self.job_title.get_latex(), self.skills, self.date.get_latex(),
                                                self.company, self.location,
                                                self.bullet_points.get_latex())

    def __init__(self, *experiences: Experience):
        self.experiences = list(experiences)

    def get_latex(self) -> str:
        structure = r"""\section{Experience}
        \resumeSubHeadingListStart
        /ARG0/
        \resumeSubHeadingListEnd"""
        return LatexElement.inject_variable(structure, [experience.get_latex() for experience in self.experiences])
