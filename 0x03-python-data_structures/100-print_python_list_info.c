#include <Python.h>

/**                                                                    
 * print_python_list_info - print information about a Python list.          
 * @p: PyObject.                                                       
 */
void print_python_list_info(PyObject *p)
{
  int size, alloc, i;
  PyObject *obj;

  size = PyList_Size(p);
  alloc = ((PyListObject *)p)->allocated;

  printf("[*] Size of the Python List = %d\n", size);
  printf("[*] Allocated = %d\n", alloc);

  for (i = 0; i < size; i++)
  {
    printf("Element %d: ", i);

    obj = PyList_GetItem(p, i);
    printf("%s\n", Py_TYPE(obj)->tp_name);
  }
}
