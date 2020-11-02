# boto3-playground

learn [boto3](https://github.com/boto/boto3), the Amazon Web Services (AWS) SDK for Python

```sh
# install virtual env and dependencies
pipenv install

# activate python virtual env (optional)
pipenv shell

# run on change
make dev

# --- running via jupyter notebook ---

# in vscode
# click on `main.ipynb`.  this will automatically start jupyter notebook and connect
# ctrl+enter to run cell
# see [How to use Pipenv with Jupyter and VSCode](https://towardsdatascience.com/how-to-use-pipenv-with-jupyter-and-vscode-ae0e970df486)

# manually run jupyter notebook
pipenv run jupyter notebook

# access via browser manually (auto opens via above command)
open http://localhost:8888/tree

```

## Notes

for vscode, install [Pylance&#32;-&#32;Visual&#32;Studio&#32;Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extension

## Resources

* [Boto3 documentation](https://boto3.readthedocs.io/)
* [boto/boto3](https://github.com/boto/boto3)
* [boto3-stubs](https://pypi.org/project/boto3-stubs/) - for code completion
* [How to use Pipenv with Jupyter and VSCode](https://towardsdatascience.com/how-to-use-pipenv-with-jupyter-and-vscode-ae0e970df486)