@_default:
    just --list

# Generate .gitignore file
gitignore:
    curl -sL https://www.toptal.com/developers/gitignore/api/node > .gitignore

# Run tests
test:
    tree-sitter test
    tree-sitter parse -qs test/gitignore/templates/*.gitignore
