#include <Python.h>

void print_python_list(PyObject *p)
{
    long int size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    char *str;
    Py_ssize_t size, i;

    printf("[*] Python bytes\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  Size of the Python Bytes = %ld\n", size);
    printf("  Trying string: %s\n", str);
    printf("  First 10 bytes: ");
    for (i = 0; i < size && i < 10; i++)
        printf("%02hhx ", str[i]);
    printf("\n");
}

void print_python_float(PyObject *p)
{
    double value;

    printf("[*] Python float\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("  value: %lf\n", value);
}
