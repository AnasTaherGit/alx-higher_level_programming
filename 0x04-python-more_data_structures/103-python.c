#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	long int alloc = ((PyListObject *)p)->allocated;
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %i: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
	}
}

void print_python_bytes(PyObject *p)
{
	long int size;
	char *trying_str = NULL;
	int i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	trying_str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", trying_str);

	if (size < 10)
	{
		printf("  first %ld bytes: ", size + 1);
	}
	else
	{
		printf("  first 10 bytes: ");
		size = 10;
	}

	for (i = 0; i < size; i++)
	{
		printf("%02hhx", trying_str[i]);
		if (i < size - 1)
		{
			printf(" ");
		}
	}
	printf("\n");
}
