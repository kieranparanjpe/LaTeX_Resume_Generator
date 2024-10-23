from typing import Tuple

from LatexElements.has_bullet_points import HasBulletPoints
from LatexElements.bullet_points import BulletPoints
from LatexElements.date_section import DateSection
from LatexElements.latexelement import LatexElement
from LatexElements.title_link import TitleLink


class ProjectsSection(LatexElement):
    class Project(LatexElement, HasBulletPoints):

        def __init__(self, project_title: Tuple[str, str], skills: str, dates: Tuple[str, str | None],
                     *bullet_points: str):
            self.project_title = TitleLink(project_title[0], project_title[1])
            self.skills = skills
            self.date = DateSection(dates[0], dates[1])
            self.bullet_points = BulletPoints(*bullet_points)

        def update_bullet_points(self, *bullet_points: str):
            self.bullet_points = BulletPoints(*bullet_points)

        def get_latex(self) -> str:
            structure = r"""
            \resumeProjectHeading
            {\textbf{/ARG1/} $|$ \emph{/ARG1/}}{/ARG1/}
            /ARG1/
            """

            return LatexElement.inject_variable(structure, self.project_title.get_latex(), self.skills, self.date.get_latex(),
                                                self.bullet_points.get_latex())

    def __init__(self, *projects: Project):
        self.projects = list(projects)

    def get_latex(self) -> str:
        structure = r"""\section{Projects}
        \resumeSubHeadingListStart
        /ARG0/
        \resumeSubHeadingListEnd"""
        return LatexElement.inject_variable(structure, [project.get_latex() for project in self.projects])
