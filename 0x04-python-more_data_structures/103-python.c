#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_bytes - function entry-point
 *
 * Description: prints first 10 bytes of object or error message if p is
 * not a valid PyBytesObject
 * @p: PyBytesObject
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	int i, j, k;
	const char *s, *t;

	t = ((PyTypeObject *)(p)->ob_type)->tp_name;

	if (strcmp(t, "bytes") == 0)
	{
		j = PyBytes_Size(p);
		s = PyBytes_AsString(p);
		k = j < 10 ? j + 1 : 10;
		printf("[.] bytes object info\n");
		printf("  size: %d\n", j);
		printf("  trying string: %s\n", s);
		printf("  first %d bytes: ", k);
		for (i = 0;  i < k - 1; i++)
			printf("%.2hhx ", s[i]);
		if (j < 10)
			printf("%.2x\n", '\0');
		else
			printf("%.2hhx\n", s[i]);
	}
	else
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_list - function entry-point
 *
 * Description: prints some basic info about Python lists
 * @p: list of subtype PyObject
 * Return: void
 */

void print_python_list(PyObject *p)
{
	int i, j;
	const char *s;
	PyObject *q;

	i = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", i);
	printf("[*] Allocated = %ld\n", ((PyListObject *)(p))->allocated);
	for (j = 0; j < i; j++)
	{
		q = PyList_GET_ITEM(p, j);
		s = ((PyTypeObject *)(q)->ob_type)->tp_name;
		printf("Element %d: %s\n", j, s);
		if (strcmp(s, "bytes") == 0)
			print_python_bytes(q);
	}
}
