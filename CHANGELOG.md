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
 - This script is currently set up to fail and as a result this commit not be added to the main/master branch commit history (as per my research), as no other files referencing the current version have been updated to express version 0.1.3. Integrity is lacking. For testing purposes.


*Current version of the ChangeLog is powered by OpenAI, ChatGPT-4*