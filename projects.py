from typing import Callable

from LatexElements.latexelement import LatexElement

from LatexElements.projects_section import ProjectsSection

def jepaWorldModel() -> ProjectsSection.Project:
    return ProjectsSection.Project(
        (r"""JEPA World Model""",
         r"""https://github.com/kieranparanjpe/world-model-sandbox"""),
        r"""Python, PyTorch, Deep Learning""",
        (r"""July 2026""", r"""September 2026"""),
        r"""Trained an action-conditioned JEPA-based world model on various Gymnasium environments, including LunarLander, Humanoid, and Walker2d. """,
        r"""Implemented autoregressive training with a discounted loss function to improve prediction accuracy over longer time horizons. """,
        r"""Utilised an exponential moving average (EMA) on the target encoder to combat representation collapse. """,
    )

def ppoRL() -> ProjectsSection.Project:
    return ProjectsSection.Project(
        (r"""Reinforcement Learning Algorithm Implementation (PPO)""",
         r"""https://github.com/kieranparanjpe/My-RL-Impl"""),
        r"""Python, PyTorch, Reinforcement Learning""",
        (r"""May 2026""", r"""July 2026"""),
        r"""Implemented PPO (proximal policy optimisation), achieving successful results in the LunarLander, 
        HalfCheetah, and Humanoid gymnasium environments.""",
        r"""Developed policies for both discrete and continuous action spaces by parameterising the categorical 
        and beta distributions.""",
        r"""Utilised observation and reward standardisation to stabilise training.""",
        r"""Wrote a \href{https://kieranparanjpe.github.io/My-RL-Impl/report/PPO_Report.pdf}{
        \underline{\textbf{report}}} detailing the implementation and theory behind the project."""

    )

def myNN() -> ProjectsSection.Project:
    return ProjectsSection.Project(
        (r"""Custom Neural Network""", r"""https://github.com/kieranparanjpe/MyNN"""),
        r"""Python, NumPy""",
        (r"""June 2024""", r""""""),
        r"""Programmed a feedforward neural network in Python using NumPy \textbf{without any machine learning libraries} (like PyTorch) to classify the MNIST digit dataset with \textbf{95\% accuracy}.""",
        r"""Implemented a deep learning network with over 25,000 trainable parameters by researching the underlying linear algebra and calculus behind \textbf{backpropagation} and \textbf{gradient descent}."""

    )

def unity_dev() -> ProjectsSection.Project:
    return ProjectsSection.Project(
        (r"""KP Games (multiple projects)""", r"""https://kieranparanjpe.itch.io/"""),
        r"""C\#, Unity, JavaScript, Firebase, 3D Math, Blender""",
        ("September 2016", r"""August 2023"""),
        r"""\textbf{Published 12 video games over 7 years} on itch.io and Google Play using Unity and C\#, garnering \textbf{over 1000 total users}.""",
        r"""Developed an active ragdoll platforming game by applying Unity's \textbf{physics engine} to map \textbf{rigged animations} onto physical joints.""",
        r"""Implemented \textbf{finite state machines} and \textbf{behaviour trees} alongside Unity's \textbf{NavMesh} across projects to bolster NPC intelligence.""",
        r"""Designed and created a \textbf{multiplayer first-person shooter} using Photon Unity Networking, including support for \textbf{matchmaking}, team game modes and free-for-all, automatic respawns, \textbf{synchronised movement}, shooting, and powerups.""",
    )


def url_shortener() -> ProjectsSection.Project:
    return ProjectsSection.Project(
        (r"""URL Shortener""", r"""https://github.com/kieranparanjpe/URL-Shortener"""),
        r"""Golang, TypeScript, Next.js, PostgreSQL, Docker, AWS EC2""",
        (r"""May 2024""", r""""""),
        r"""Developed a full-stack web application to shorten URLs using a Golang server that interacts with a \textbf{PostgreSQL} database, running on an AWS EC2 instance with a Next.js frontend.""",
        r"""Implemented middleware that handles \textbf{JSON Web Tokens} (JWT) to ensure users are properly authenticated.""",
        r"""Encapsulated the backend in a \textbf{Docker} container to allow for easy deployment on \textbf{AWS EC2}."""

    )


def spotify_mp3() -> ProjectsSection.Project:
    return ProjectsSection.Project(
        (r"""Spotify MP3 Download \& Stats""", r"""https://github.com/kieranparanjpe/music-stats/"""),
        r"""TypeScript, Next.js""",
        (r"""January 2024""", r""""""),
        r"""Developed a web app in TypeScript with Next.js that can \textbf{download Spotify songs without Spotify Premium}.""",
        r"""Displays top songs, artists, and genres for 3 different timeframes using the Spotify Web API.""",
        r"""Utilised the YouTube Data API to search for corresponding music videos to download."""

    )


def projects(*function_names: Callable) -> LatexElement:
    all_projects = (function() for function in function_names)

    return ProjectsSection(*all_projects)
