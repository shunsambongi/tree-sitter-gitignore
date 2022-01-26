@_default:
    just --list

# Generate .gitignore file
gitignore:
    curl -sL https://www.toptal.com/developers/gitignore/api/node > .gitignore
