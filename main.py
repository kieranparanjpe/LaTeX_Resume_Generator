# This is a sample Python script.
import exps
import projects
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
            TitleSection.Links.Link(r"""kieranparanjpe\@gmail.com""", None),
            TitleSection.Links.Link(r"""kieranparanjpe.com""", r"""https://kieranparanjpe.com"""),
            TitleSection.Links.Link(r"""linkedin.com/in/kieran-paranjpe""",
                                    r"""https://www.linkedin.com/in/kieran-paranjpe"""),
            TitleSection.Links.Link(r"""github.com/kieranparanjpe""", r"""https://github.com/kieranparanjpe""")
        ]
    )

    education_section = EducationSection(
        EducationSection.Education(
            r"""McGill University""",
            (r"""August 2023""", r"""April 2027"""),
            r"""BSc in Computer Science (AI), Minor in Cognitive Science $\mid$ 4.00 GPA""",
            r"""Montreal, QC"""
        )
    )

    skills_section = SkillsSection(
        SkillsSection.Skill(
            r"""Languages""",
            r"""C\#, Java, Python, SQL, JavaScript, TypeScript, Golang, Bash, HTML, CSS, C"""
        ),
        SkillsSection.Skill(
            r"""Frameworks/Tools""",
            r"""Git, Docker, PyTorch, React.js, Express.js, Unity, Linux, Firebase"""
        ),
        SkillsSection.Skill(
            r"""Soft Skills""",
            r"""Public Speaking, Leadership, Concise Communication, Quick Learning, Teamwork"""
        )
    )

    ml_skills_section = SkillsSection(
        SkillsSection.Skill(
            r"""Languages""",
            r"""Python, SQL, C\#, Java, JavaScript, TypeScript, Golang, Bash, HTML, CSS, C"""
        ),
        SkillsSection.Skill(
            r"""Frameworks/Tools""",
            r"""Git, PyTorch, Docker, React.js, Express.js, Unity, Linux, Firebase"""
        ),
        SkillsSection.Skill(
            r"""Soft Skills""",
            r"""Public Speaking, Leadership, Concise Communication, Quick Learning, Teamwork"""
        )
    )

    experience_section = exps.experiences(exps.the_verse, exps.hack4i,
                                          exps.unity_dev, exps.robotics,
                                          exps.stemphilic)
    projects_section = projects.projects(projects.myNN, projects.url_shortener, projects.spotify_mp3)

    ml_experience = exps.experiences(exps.the_verse_ml, exps.hack4i,
                                          exps.unity_dev, exps.robotics, exps.stemphilic)

    swe_resume = BoilerPlateSection(title_section, education_section, skills_section, experience_section,
                                     projects_section)

    ml_resume = BoilerPlateSection(title_section, education_section, ml_skills_section, ml_experience,
                                     projects_section)

    resume = ml_resume.get_latex()
    print(resume)
    clipboard.copy(resume)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
