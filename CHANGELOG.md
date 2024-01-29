## [0.1.0] - 2024-01-13

### Added

- **Initial Page Setup**: Implemented an initial page with a header and a data request button.
- **State Transition**: Added a state transition feature which shows a circular loading spinner during data loading, and an error snackbar for failed transitions.
- **Data Display**: Functionality to display data below the header with a button upon successful data loading.
- **Service Module**: Developed `service.py` to fetch data from an external service.
- **Routing**: Established two routes in `routes.py`: one for rendering the initial site HTML template, and another for the list of dog breeds rendered as partial HTML.
- **Digital Signature**: Created `digital_signature.py` for signing responses, enabling clients to verify the authenticity of data from the server. (Note: functional but not yet in use)
- **Testing Framework**: 
  - Wrote tests for the server, including the service and routes.
  - Implemented end-to-end tests that combine `routes.py` and `service.py`, mock the HTTP client, and verify the route responses.
- **Project documentation**: README.md as an entry point for the project.
- **License handling**: LICENSE file for the project, as well as THIRD_PARTY_LICENSES for crediting third party dependencies (some dependencies not part of version control, but linked/referenced as dependencies).
- **Versioning:** This CHANGELOG.md added for documenting version control.

## [0.1.1] - 2024-01-14

### Added

- **Fix changelog:** Added a few missing items from the v0.1.0 version.
- **Licensing:** Added notes to comments in the main .gitignore file, comments that reference specific external repositories. Made a note of the licenses those repositories are published under.

## [0.1.2] - 2024-01-15

- **Maintain Versioning Integrity Across Project:**  Added a Python script that looks for files known to reference current project version and commits to testing them if they do contain that reference. The script then it validates whether all of the files in the project that reference curr_ver reference the same version, returns information on succesful matches and errors. Returns with exit code sys.exit(1) if errors are found.

## [0.1.3] - 2024-01-15

- **CI/CD test for Versioning Integrity:"** Added a lightweight CI/CD script that should reject commits that don't demonstrate integrity in how they express the current project version across different files and/or communincation paths ways. Expressing the same information across all fronts is important; it is not only a mark of diligence, but also a valuable indicator towards evaluating honesty.

- **Moved to staging:** Move to staging to guard the master/main branch against commits that haven't passed testing. Apparently github has blocked access to using workflows as a precommit guard for commits for non-enterprise repositories, so this is a viable workaround, at least for a non-collaborative repository.

## [0.1.4] - 2024-01-15

- **Added acknowledgements sections to README.md:** To ensure contributions are acknowledgeded.

## [0.1.5] - 2024-01-18
- **Updated CI/CD script** With changes tested in isolated environment at the GitHub repository [TestMergeBranches](https://github.com/mittons/TestMergeBranches). The additions of, and changes to, the automated scripts that react to git push commands two days ago were a bit chaotic and not tested in an isolated environment, however the current changes should perform better, at the very least get a quick resolution if something goes wrong.
- **Fixed link error in README:** Removed additional parenthesis from README.md that was preventing correct hyperlink generation.


## [0.1.6] - 2024-01-23

- **Updated Flask Init Args in main.py:** Debug mode is off, the server is hardcoded to run listen on localhost (for now), on port 5678.

- **Changed name of project:** from ~~PythonDogDisplay~~ to DogDisplayForPython. Safer for potential licensing issues. Places the focus on the functionaly developed in this source code. Shows that the project functions in conjuction with the language, while maintaining distinctiveness as an independent project.

- **Prepare for Showcase and Build from Source Instructions:** Added a script or two, that will at least for a while, be a used as part of showcasing and testing the project in the next few updates.

## [0.2.0] - 2024-01-29

### Added

- **Build Instructions:** Detailed instructions on how to set up the application from source added in BUILD.md

- **Showcase Instructions:** Instructions on how to run the application from source and showcase its functionality. Includes a GitHub Actions setup-build-test-run script.

### Changed

- **Readme Sections for Installation and Showcase:** Changed sections in README.md to refer to added build instructions and the showcase instructions, rather than detailing parts of that in the README. This both streamlines the README and offers the option of more indepth instructions in separate files (that, while detailed, are still structured with a clear intro, offering opt-in to further reading).

 - **Showcase_scripts:** - Made a change to the test_server_endpoints.py script, previous version worked on Ubuntu but apparently needed just a little touch, a bit of spice, to work on Windows.

*Current version of the ChangeLog is powered by OpenAI, ChatGPT-4*