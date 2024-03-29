# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/anelendata/tap-exchangeratehost/issues.

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

tap-exchangeratehost could always use more documentation, whether as part of the
official README.md, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/anelendata/_tap-exchangeratehost/issues.

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Submit a pull request through the GitHub website.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.

TODO: Set up Travis:
3. The pull request should work for Python 3.6, 3.7 and 3.8, and for PyPy. Check
   https://travis-ci.org/anelendata/tap-exchangeratehost/pull_requests
   and make sure that the tests pass for all supported Python versions.

## Deploying

Ask the current maintainers on (https://pypi.org/project/tap-exchangeratehost/)
so you can join as maintainer.

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.md, and AUTHORS.md).
Then run:

```
$ pip install -r requirements_dev.txt
$ bin/release_build  # Use username: __token__ and PyPi token whem prompted.
$ git tag v<Enter proper version like 0.1.2>
$ git push origin --tags
```

Update release info on GitHub (Copy & paste the current HISTORY entry should be enough):
https://github.com/anelendata/tap-exchangeratehost/releases

TODO: Set up Travis so it will then deploy to PyPI if tests pass.
