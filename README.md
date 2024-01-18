# PythonDogDisplay

### **Welcome to the PythonDogDisplay Repository!**

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Running the Tests](#running-the-tests)
- [Versioning](#versioning)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)

## Introduction

**Technology: Python, HTML, CSS, Javascript**

**Overview:**
This project, PythonDogDisplay, is a web-based application mainly developed as a Python web server application. It's part of a series of implementations that showcase the same core functionality across different programming languages and frameworks. The primary objective of this project is to demonstrate my ability to adapt and replicate a consistent user experience and functionality in various technological environments.

**Functionality:**
At its heart, the application presents a simple, intuitive interface consisting of a header with a title and a centrally-located button. Upon user interaction with the button, the application initiates a state transition, displaying a loading spinner while processing an HTTP request. The outcomes are twofold:
1. **Success:** Displays a list of data in a structured format, fetched from the [The Dog API](https://www.thedogapi.com).
2. **Error Handling:** In case of request failure, an error snackbar is displayed to inform the user.

The application also implements a digital signature mechanism for a yet-to-be implemented/published cross-origin Single Page Application html client page. The signatures can be active, but they have no client side to authenticate them yet.

**Purpose:**
The primary purpose of this project is to:
- Illustrate my proficiency as a developer.
- Demonstrate my understanding of fundamental application components like state management, data fetching, UI/UX considerations, robust testing and a end to end CI/CD process.
- Showcase my ability to learn and efficiently replicate a functional design across multiple programming languages, underscoring my adaptability and quick learning capabilities in software development.

**Learning Journey:**
This project is part of a larger journey, where I replicate a base application concept in various languages, each serving as a testament to my growing skills and understanding of different tech stacks. It's designed not just as a technical demonstration, but also as a narrative of my learning process and commitment to continuous skill enhancement in the realm of software development.

## Installation
Instructions for installing your project. Include steps for cloning the repo and any configuration necessary.

```bash
git clone https://github.com/mittons/PythonDogDisplay.git
cd PythonDogDisplay
pip install -e .
pip install -r requirements.txt
```

## Usage
To run the application, use the following command based on your operating system:

- **For Linux/MacOS:**
  ```bash
  env FLASK_ENV=production python main.py
  ```
  This command sets `FLASK_ENV` to `production` temporarily and runs `main.py`.

- **For Windows:**
  ```cmd
  cmd /V /C "set FLASK_ENV=production && python main.py && set FLASK_ENV="
  ```
  This Windows command temporarily sets `FLASK_ENV` to `production`, executes `main.py`, and then resets `FLASK_ENV`.

By default, the application is configured to fetch data from a production server when `FLASK_ENV` is set to `production`. If `FLASK_ENV` is not set, the application attempts to connect to a local server.

## Running the Tests
To test the code run the following action while in the root directory:

```bash
python run_server_tests.py
```
## Versioning
We use [Semantic Versioning](https://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/mittons/PythonDogDisplay/tags). 

### Roadmap

Current Version: v0.1.5

As the application evolves, the following key developments are planned:

- [ ] **Testing Integration in CI/CD (Upcoming):** Implementation of automated testing on every code push. This will ensure code quality and stability by running a series of tests through a continuous integration/continuous deployment (CI/CD) pipeline.

- [ ] **Push to Deploy Enhancement (Future Phase):** Following testing integration, the next step will be to streamline the deployment process. The aim is to achieve a push-to-deploy mechanism in the CI/CD pipeline, allowing for efficient and reliable deployment of updates.

- [ ] **Codebase Improvements (Ongoing):** Continuous refactoring of the code to extract redundant boilerplate functionality is planned. The focus will be on enhancing the maintainability, scalability, and readability of the code. This will include adding comments and restructuring for better organization and clarity.

These steps are aimed at enhancing the application's overall quality and efficiency, aligning with the best practices in software development.

## Acknowledgements
- **The Dog API:** This application uses data from [The Dog API](https://www.thedogapi.com). I route the traffic through my own private backend proxy in order to secure my user key for the API, in line with the [The Dog API TOS](https://thedogapi.com/terms).

- **ChatGPT:** Powered by OpenAI, specifically ChatGPT-4. Files in this project vary from between being Content that is completely AI generated to being completely human-generated. The term Content, and other relevant definitions, can be observed on [The OpenAI TOS page](https://openai.com/policies/terms-of-use#using-our-services).

## License
This project is licensed under the [MIT LICENSE](LICENSE) - see the file for details.

Third party licenses used as dependencies are listed, and given credit, in the [THIRD_PARTY_LICENSES](THIRD_PARTY_LICENSES) file.

## Contact
Axel Gauti Guðmundsson - [@axelgauti](https://twitter.com/axelgauti) - axel@axelgauti.is