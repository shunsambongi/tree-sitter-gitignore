from setuptools import Extension, find_packages, setup

setup(
    name="tree-sitter-gitignore",
    version="0.1.0",
    packages=find_packages("bindings/python"),
    package_dir={"": "bindings/python"},
    ext_modules=[
        Extension(
            name="tree_sitter_gitignore._binding",
            sources=[
                "bindings/python/tree_sitter_gitignore/binding.c",
                "src/parser.c",
            ],
            include_dirs=["src"],
            extra_compile_args=["-std=c99"] if not False else [],
        )
    ],
    package_data={
        "tree_sitter_gitignore": ["*.pyi"],
    },
)
