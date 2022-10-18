
#########################################################

## Commandes PipEnv :

# General recommendations :

==> Generally, keep both Pipfile and Pipfile.lock in version control.
==> Do not keep Pipfile.lock in version control if multiple versions of Python are being targeted.
==> Specify your target Python version in your Pipfile’s [requires] section. Ideally, you should only have one target Python version, as this is a deployment tool.
==> pipenv install is fully compatible with pip install syntax, for which the full documentation can be found

# Install pip

To install pip, securely download get-pip.py :

==> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

Inspect get-pip.py for any malevolence. Then run the following:

==> python get-pip.py

# Maj pip

==> pip install -U pip

## Pipenv == pip + virtualenv :

# Install pipenv

==> pip install --user pipenv

Pipenv manages dependencies on a per-project basis. To install packages, change into your project’s directory (or just an empty directory for this tutorial) and run:

==> pipenv install requests

Pipenv will install the excellent Requests library and create a Pipfile for you in your project’s directory. The Pipfile is used to track which dependencies your project needs in case you need to re-install them, such as when you share your project with others.

# Install from Pipfile, if there is one :

==> pipenv install

Then,
==> pipenv shell
==> python --version

# Install new package (à la main) :

==> pipenv install <package>

# Importing from requirements.txt

If you only have a requirements.txt file available when running pipenv install, pipenv will automatically import the contents of this file and create a Pipfile for you.

You can also specify :

==> pipenv install -r path/to/requirements.txt to import a requirements file.

If your requirements file has version numbers pinned, you’ll likely want to edit the new Pipfile to remove those, and let pipenv keep track of pinning. If you want to keep the pinned versions in your Pipfile.lock for now, run pipenv lock --keep-outdated.

#########################################################

### Example Pipenv Upgrade Workflow¶

# Find out what’s changed upstream 

==> pipenv update --outdated

	Upgrade packages, two options:

		Want to upgrade everything? Just do

		==> pipenv update
	
		Want to upgrade packages one-at-a-time? 

		==> pipenv update <pkg> (for each outdated package)

# To create a new virtualenv, using a specific version of Python you have installed (and on your PATH)

Use Python 3:

==> pipenv --python 3

Use Python3.6:

==> pipenv --python 3.6

# Run DataApp :

==> pipenv run python3 DataApp.py

# Activate Pipenv :

==> pipenv shell (and then python3 DataApp.py)

#########################################################

## Environment Management with Pipenv

The three primary commands you’ll use in managing your pipenv environment are :

# pipenv install

pipenv install is used for installing packages into the pipenv virtual environment and updating your Pipfile.

Along with the basic install command, which takes the form:

==> pipenv install [package names]

# pipenv uninstall

==> pipenv uninstall 	# supports all of the parameters in pipenv install, as well as two additional options, --all and --all-dev.

--all — This parameter will purge all files from the virtual environment, but leave the Pipfile untouched.
--all-dev — This parameter will remove all of the development packages from the virtual environment, and remove them from the Pipfile.

# pipenv lock

==> pipenv lock 

is used to create a Pipfile.lock, which declares all dependencies (and sub-dependencies) of your project, their latest available versions, and the current hashes for the downloaded files. This ensures repeatable, and most importantly deterministic, builds.

#########################################################

