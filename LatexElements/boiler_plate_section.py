from LatexElements.latexelement import LatexElement


class BoilerPlateSection(LatexElement):
    def __init__(self, *content: LatexElement):
        self.content = list(content)

    def text(self):
        return "\n".join([c.text() for c in self.content])
    def get_latex(self):
        form = r"""
        %-------------------------
        % Resume in Latex
        % Author : Kieran Paranjpe
        % Based on "Jake's Resume" by Jake Gutierrez
        % License : MIT
        %------------------------
        
        \documentclass[letterpaper,10pt]{article}
        
        \usepackage{latexsym}
        \usepackage[empty]{fullpage}
        \usepackage{titlesec}
        \usepackage{marvosym}
        \usepackage[usenames,dvipsnames]{color}
        \usepackage{verbatim}
        \usepackage{enumitem}
        \usepackage[hidelinks]{hyperref}
        \usepackage{fancyhdr}
        \usepackage[english]{babel}
        \usepackage{fontawesome}
        \usepackage{tabularx}
        \input{glyphtounicode}
        
        
        %----------FONT OPTIONS----------
        % sans-serif
        % \usepackage[sfdefault]{FiraSans}
        % \usepackage[sfdefault]{roboto}
        % \usepackage[sfdefault]{noto-sans}
        % \usepackage[default]{sourcesanspro}
        
        % serif
        % \usepackage{CormorantGaramond}
        \usepackage{charter}
        
        
        \pagestyle{fancy}
        \fancyhf{} % clear all header and footer fields
        \fancyfoot{}
        \renewcommand{\headrulewidth}{0pt}
        \renewcommand{\footrulewidth}{0pt}
        
        % Adjust margins
        \addtolength{\oddsidemargin}{-0.5in}
        \addtolength{\evensidemargin}{-0.5in}
        \addtolength{\textwidth}{1in}
        \addtolength{\topmargin}{-.5in}
        \addtolength{\textheight}{1.0in}
        
        \urlstyle{same}
        
        \raggedbottom
        \raggedright
        \setlength{\tabcolsep}{0in}
        
        % Sections formatting
        \titleformat{\section}{
          \vspace{-10pt}\scshape\raggedright\large
        }{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]
        
        % Ensure that generate pdf is machine readable/ATS parsable
        \pdfgentounicode=1
        
        %-------------------------
        % Custom commands
        \newcommand{\resumeItem}[1]{
          \item\small{
            {#1 \vspace{-2pt}}
          }
        }
        
        \newcommand{\resumeSubheading}[4]{
          \vspace{-2pt}\item
            \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
              \small{#1} & #2 \\
              \textit{\small#3} & \textit{\small #4} \\
            \end{tabular*}\vspace{-7pt}
        }
        
        \newcommand{\resumeExperienceSubheading}[4]{
          \vspace{-2pt}\item
            \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
              \small{#1} & #2 \\
              \textit{\small#3} & \textit{\small #4} \\
            \end{tabular*}\vspace{-7pt}
        }
        
        \newcommand{\resumeSubSubheading}[2]{
            \item
            \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
              \textit{\small#1} & \textit{\small #2} \\
            \end{tabular*}\vspace{-7pt}
        }
        
        \newcommand{\resumeProjectHeading}[2]{
            \item
            \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
              \small#1 & #2 \\
            \end{tabular*}\vspace{-7pt}
        }
        
        \newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}
        
        \renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}
        
        \newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
        \newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
        \newcommand{\resumeItemListStart}{\begin{itemize}}
        
        \newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}
        %-------------------------------------------
        %%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
        
        \begin{document}
        /ARG0/
        \end{document}
                """
        return LatexElement.inject_variable(form, self.content)
