#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_string - function entry-point
 *
 * Description: prints string object or error message
 * if p is not a valid string
 * @p: PyObject
 * Return: void
 */

void print_python_string(PyObject *p)
{
	int i, j, k;
	const char *s, *t;

	t = ((PyTypeObject *)(p)->ob_type)->tp_name;
	printf("[.] string object info\n");

	if (strcmp(t, "str") == 0)
	{
		j = PyUnicode_GetLength(p);
		s = PyUnicode_AsUTF8(p);
		if (PyUnicode_IS_ASCII(p))
			printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");
		printf("  length: %d\n", j);
		printf("  value: %s\n", s);
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}
