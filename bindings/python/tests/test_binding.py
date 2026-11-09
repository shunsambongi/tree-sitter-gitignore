import tree_sitter
import tree_sitter_gitignore


def test_can_load_grammar():
    try:
        # Per tree-sitter >= 0.22 (API recente)
        language = tree_sitter.Language(tree_sitter_gitignore.language())
    except AttributeError:
        # Fallback per vecchie versioni dell'API python tree-sitter
        language = tree_sitter_gitignore.language()

    parser = tree_sitter.Parser()

    try:
        parser.set_language(language)
    except AttributeError:
        parser.language = language

    tree = parser.parse(b"*.log\n# comment\n")
    assert tree.root_node is not None
    assert tree.root_node.type == "document"
