#include <python.h>

/**
 * print_python_list_info - print standard about python list.
 * @p: PyObject.
 */
void print_python_list_info(PyObject *p)
{
  int size, alloc, i;
  pyObject *obj;

  size = Py_size(p);
  alloc = ((PyListObject *)p)->allocated;

  printf("[*] Size of the Python List = %d\n", size);
  printf("[*] Allocated = %d\n", allco);

  for (i =0; i < size; i++)
    {
      printf("Element %d: ", i);

      obj = PyList_GetItem(p, i);
      printf("%s\n", PyTYBE(obj)->tp_name);
    }
}
      
