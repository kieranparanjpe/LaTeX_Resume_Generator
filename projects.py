from typing import Callable

from LatexElements.latexelement import LatexElement

from LatexElements.projects_section import ProjectsSection


def myNN() -> ProjectsSection.Project:
    return ProjectsSection.Project(
        (r"""Custom Neural Network""", r"""https://github.com/kieranparanjpe/MyNN"""),
        r"""Python, NumPy""",
        (r"""June 2024""", r""""""),
        r"""Programmed a custom feedforward neural network in Python using NumPy without any machine learning libraries (like PyTorch) to classify the MNIST digit dataset with 95\% accuracy.""",
        r"""Implemented a deep learning network with over 25,000 trainable parameters by researching the underlying mathematics behind back propagation and gradient descent."""

    )


def url_shortener() -> ProjectsSection.Project:
    return ProjectsSection.Project(
        (r"""URL Shortener""", r"""https://github.com/kieranparanjpe/URL-Shortener"""),
        r"""Golang, TypeScript, Next.js, PostgreSQL, Docker, AWS EC2""",
        (r"""May 2024""", r""""""),
        r"""Developed a full-stack web application to shorten URLs using a Golang server that interacts with a PostgreSQL database, running on an AWS EC2 instance with a Next.js frontend.""",
        r"""Implemented middleware that handles JSON Web Tokens (JWT) to ensure users are properly authenticated.""",
        r"""Encapsulated the backend in a Docker container so it can be easily deployed on AWS."""

    )


def spotify_mp3() -> ProjectsSection.Project:
    return ProjectsSection.Project(
        (r"""Spotify MP3 Download \& Stats""", r"""https://github.com/kieranparanjpe/music-stats/"""),
        r"""TypeScript, Next.js""",
        (r"""January 2024""", r""""""),
        r"""Developed a web-app in TypeScript with Next.js that can download Spotify songs without Spotify Premium.""",
        r"""Displays top songs, artists, and genres for 3 different timeframes using the Spotify Web API.""",
        r"""Utilised the YouTube Data API to search for corresponding music videos to download."""

    )


def projects(*function_names: Callable) -> LatexElement:
    all_projects = (function() for function in function_names)

    return ProjectsSection(*all_projects)
