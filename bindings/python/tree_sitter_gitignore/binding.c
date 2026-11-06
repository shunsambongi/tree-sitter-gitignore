#include <Python.h>
#include <tree_sitter/parser.h>

TSLanguage *tree_sitter_gitignore(void);

static PyObject* _binding_language(PyObject *self, PyObject *args) {
    return PyCapsule_New(tree_sitter_gitignore(), "tree_sitter.Language", NULL);
}

static PyMethodDef methods[] = {
    {"language", _binding_language, METH_NOARGS,
     "Get the Tree-sitter language for Gitignore."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "_binding",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit__binding(void) {
    return PyModule_Create(&module);
}
