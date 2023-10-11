#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - function entry-point
 *
 * Description: prints some basic info about Python lists
 * @p: list of subtype PyObject
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int i, j;

	i = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", i);
	printf("[*] Allocated = %ld\n", ((PyListObject *)(p))->allocated);
	for (j = 0; j < i; j++)
		printf("Element %d: %s\n", j, Py_TYPE(PyList_GetItem(p, j))->tp_name);
}

