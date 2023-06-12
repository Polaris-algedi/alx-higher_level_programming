#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: PyObject pointer
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;
	const char *type_name;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);

	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type_name = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, type_name);
	}
}
