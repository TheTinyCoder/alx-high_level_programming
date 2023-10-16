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
	printf("[.] bytes object info\n");
	if (strcmp(t, "bytes") == 0)
	{
		j = PyBytes_Size(p);
		s = ((PyBytesObject *)(p))->ob_sval;
		k = j <= 10 ? j + 1 : 10;
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
		printf("  [ERROR] Invalid Bytes Object\n");
	fflush(stdout);
}

/**
 * print_python_float - function entry-point
 *
 * Description: prints first 10 bytes of object or error message if p is
 * not a valid PyFLoatObject
 * @p: PyFloatObject
 * Return: void
 */

void print_python_float(PyObject *p)
{
	const char *s;
	char *t;

	s = ((PyTypeObject *)(p)->ob_type)->tp_name;
	printf("[.] float object info\n");
	if (strcmp(s, "float") == 0)
	{
		t = PyOS_double_to_string(((PyFloatObject *)(p))->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", t);
		PyMem_Free(t);
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
	fflush(stdout);
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
	const char *s, *t;
	PyObject *q;

	t = ((PyTypeObject *)(p)->ob_type)->tp_name;
	printf("[*] Python list info\n");
	if (strcmp(t, "list") == 0)
	{
		i = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %d\n", i);
		printf("[*] Allocated = %ld\n", ((PyListObject *)(p))->allocated);
		for (j = 0; j < i; j++)
		{
			q = PyList_GET_ITEM(p, j);
			s = ((PyTypeObject *)(q)->ob_type)->tp_name;
			printf("Element %d: %s\n", j, s);
			if (strcmp(s, "bytes") == 0)
				print_python_bytes(q);
			else if (strcmp(s, "float") == 0)
				print_python_float(q);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
	fflush(stdout);
}
