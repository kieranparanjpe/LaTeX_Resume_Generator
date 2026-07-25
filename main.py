# This is a sample Python script.
import exps
import projects
import skills
from LatexElements.boiler_plate_section import BoilerPlateSection
from LatexElements.education_section import EducationSection
from LatexElements.skills_section import SkillsSection
from LatexElements.title_section import TitleSection
import clipboard


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    title_section = TitleSection(
        r"""Kieran Paranjpe""",
        [r"""Vancouver, BC""", r"""Montreal, QC"""],
        [
            TitleSection.Links.Link(r"""kieranparanjpe@gmail.com""", None),
            TitleSection.Links.Link(r"""kieranparanjpe.com""", r"""https://kieranparanjpe.com"""),
            TitleSection.Links.Link(r"""linkedin.com/in/kieran-paranjpe""",
                                    r"""https://www.linkedin.com/in/kieran-paranjpe"""),
            TitleSection.Links.Link(r"""github.com/kieranparanjpe""", r"""https://github.com/kieranparanjpe""")
        ]
    )

    education_section = EducationSection(
        EducationSection.Education(
            r"""McGill University""",
            (r"""2027""", None),
            r"""BSc in Computer Science $\mid$ 3.95 GPA""",
            r"""Montreal, QC"""
        )
    )

    # ----- GENERAL SWE ----:
    skills_section_swe = skills.skills(skills.programming_reduced, skills.frameworks, skills.soft_skills)

    experience_section_swe = exps.experiences(exps.autodesk_2, exps.autodesk, exps.the_verse)
    projects_section_swe = projects.projects(projects.ppoRL, projects.url_shortener, projects.unity_dev)

    swe_resume = BoilerPlateSection(title_section, education_section, skills_section_swe, experience_section_swe,
                                    projects_section_swe)
    # ----- ML ----:

    skills_section_ml = skills.skills(skills.programming_reduced, skills.frameworks_ml, skills.soft_skills)

    experience_section_ml = exps.experiences(exps.autodesk_2, exps.autodesk, exps.the_verse_ml)

    projects_section_ml = projects.projects(projects.ppoRL, projects.myNN, projects.unity_dev)


    ml_resume = BoilerPlateSection(title_section, education_section, skills_section_ml, experience_section_ml,
                                   projects_section_ml)

    # ----- GameDev ----:
    skills_section_gd = skills.skills(skills.programming, skills.frameworks_gamedev, skills.soft_skills)

    experience_section_gd = exps.experiences(exps.autodesk, exps.the_verse,
                                          exps.unity_dev, exps.robotics)

    game_dev = BoilerPlateSection(title_section, education_section, skills_section_gd, experience_section_gd,
                                  projects_section_swe)

    # ----- Robotics ----:
    skills_section_rbt = skills.skills(skills.programming_reduced, skills.frameworks_robotics, skills.soft_skills)

    rbt_resume = BoilerPlateSection(title_section, education_section, skills_section_rbt, experience_section_ml,
                                   projects_section_ml)

    resume = ml_resume.get_latex()
    print(resume)
    clipboard.copy(resume)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
