# How to contribute

## How to get started

To first get up and running you must first start the docker container that contains the necessary development environment. Run the following command to build the docker container and launch it. This will take a significant amount of time (>20min), but will be faster on future runs.
 - <data_path>: the absolute path to where the data you want to mount into the container is located. This mount will be available at `/home/jovyan/data`
 - <port>: The port you want to be able to access the jupyter lab interface from.
 - --build: Optional flag that when present will build from scratch the docker container. On future runs, just omit the `--build` flag to not rebuild the docker container.
```
bash start.sh <data_path> <port> --build
```

Once the container has launched, log into the container through the jupyter lab interface by going to your browser and typing `localhost:<port>`. When prompted for a password input `asdf`. Another way to log into the docker container can be using `docker exec -it <container_name>`. After you are in the container, please install the git hooks that run automatic scripts during each commit, format all your nbs according to our style, and merge to strip the notebooks of superfluous metadata (and avoid merge conflicts) and install the library locally. Run the following commands from the root of the repository (`/home/jovyan/work`):
```
nbdev_install_git_hooks
pip install -e .
pre-commit install
```

## Did you find a bug?

* Ensure the bug was not already reported by searching on GitHub under Issues.
* If you're unable to find an open issue addressing the problem, open a new one. Be sure to include a title and clear description, as much relevant information as possible, and a code sample or an executable test case demonstrating the expected behavior that is not occurring.
* Be sure to add the complete error messages.

#### Did you write a patch that fixes a bug?

* Open a new GitHub pull request with the patch.
* Ensure that your PR includes a test that fails without your patch, and pass with it.
* Ensure the PR description clearly describes the problem and solution. Include the relevant issue number if applicable.

## PR submission guidelines

* Keep each PR focused. While it's more convenient, do not combine several unrelated fixes together. Create as many branches as needing to keep each PR focused.
* Do not mix style changes/fixes with "functional" changes. It's very difficult to review such PRs and it most likely get rejected.
* Do not add/remove vertical whitespace. Preserve the original style of the file you edit as much as you can.
* Do not turn an already submitted PR into your development playground. If after you submitted PR, you discovered that more work is needed - close the PR, do the required work and then submit a new PR. Otherwise each of your commits requires attention from maintainers of the project.
* If, however, you submitted a PR and received a request for changes, you should proceed with commits inside that PR, so that the maintainer can see the incremental fixes and won't need to review the whole PR again. In the exception case where you realize it'll take many many commits to complete the requests, then it's probably best to close the PR, do the work and then submit it again. Use common sense where you'd choose one way over another.

## Do you want to contribute to the documentation?

* Docs are automatically created from the notebooks in the nbs folder.

