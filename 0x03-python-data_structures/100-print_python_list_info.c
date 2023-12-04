#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Print python info list
 *
 * @p: pointer
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t count;
	Py_ssize_t len = PyList_Size(p);
	PyListObject *pObj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %ld\n", pObj->allocated);

	for (count = 0; count < len; count++)
	{
		printf("Element %ld: %s\n", count, Py_TYPE(pObj->ob_item[count])->tp_name);
	}
}
