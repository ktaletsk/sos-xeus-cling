#!/usr/bin/env javascript
#
# Copyright (c) Konstantin Taletskiy
# Distributed under the terms of the MIT License.

# import os
# import unittest
# from ipykernel.tests.utils import assemble_output, execute, wait_for_idle
# from sos_notebook.test_utils import sos_kernel, get_result, get_display_data, clear_channels
# from time import sleep
from sos_notebook.test_utils import NotebookTest
import random

class TestDataExchange(NotebookTest):
    def _var_name(self):
        if not hasattr(self, '_var_idx'):
            self._var_idx = 0
        self._var_idx += 1
        return f'var{self._var_idx}'

    def get_from_SoS(self, notebook, sos_expr):
        var_name = self._var_name()
        notebook.call(f'{var_name} = {sos_expr}', kernel='SoS')
        return notebook.check_output(f'''\
            %get {var_name}
            {var_name}''', kernel='C++14')

    # def put_to_SoS(self, notebook, cpp_expr):
    #     var_name = self._var_name()
    #     notebook.call(f'''\
    #         %put {var_name}
    #         {var_type} {var_name} = {cpp_expr};
    #         ''',
    #                   kernel='C++14')
    #     return notebook.check_output(f'print(repr({var_name}))', kernel='SoS')

    # def test_get_none(self, notebook):
    #     assert 'NULL' == self.get_from_SoS(notebook, 'None')

    # def test_put_null(self, notebook):
    #     assert 'None' == self.put_to_SoS(notebook, 'NULL')

    # def test_get_numpy_inf(self, notebook):
    #     notebook.call('import numpy', kernel='SoS')
    #     assert 'Inf' == self.get_from_SoS(notebook, 'numpy.inf')

    # def test_put_inf(self, notebook):
    #     assert 'inf' == self.put_to_SoS(notebook, 'Inf')

    def test_get_int(self, notebook):
        assert '123' == self.get_from_SoS(notebook, '123')
        # assert '1234567891234' == self.get_from_SoS(
        #     notebook, '1234567891234')
        # longer int does not gurantee precision any more, I am not sure
        # if the following observation will be consistent (784 vs 789)
        # assert '123456789123456784' == self.get_from_SoS(
        #     notebook, '123456789123456789')

    # def test_put_int(self, notebook):
    #     assert '123' == self.put_to_SoS(notebook, '123')
    #     assert '1234567891234' == self.put_to_SoS(
    #         notebook, '1234567891234')
    #     # longer int does not gurantee precision any more, I am not sure
    #     # if the following observation will be consistent (784 vs 789)
    #     assert '123456789123456784' == self.put_to_SoS(
    #         notebook, '123456789123456789')

    # def test_get_double(self, notebook):
    #     # FIXME: can we improve the precision here? Passing float as string
    #     # is certainly a bad idea.
    #     val = str(random.random())
    #     assert abs(float(val) - float(self.get_from_SoS(notebook, val))) < 1e-10

    # def test_put_double(self, notebook):
    #     val = str(random.random())
    #     assert abs(float(val) - float(self.put_to_SoS(notebook, val))) < 1e-10

    # def test_get_logic(self, notebook):
    #     assert 'TRUE' == self.get_from_SoS(notebook, 'True')
    #     assert 'FALSE' == self.get_from_SoS(notebook, 'False')

    # def test_put_logic(self, notebook):
    #     assert 'True' == self.put_to_SoS(notebook, 'TRUE')
    #     assert 'False' == self.put_to_SoS(notebook, 'FALSE')

    # def test_get_num_array(self, notebook):
    #     assert '1' == self.get_from_SoS(notebook, '[1]')
    #     assert '1 2' == self.get_from_SoS(notebook, '[1, 2]')
    #     #
    #     assert '1.23' == self.get_from_SoS(notebook, '[1.23]')
    #     assert '1.4 2' == self.get_from_SoS(notebook, '[1.4, 2]')

    # def test_put_num_array(self, notebook):
    #     # Note that single element numeric array is treated as single value
    #     assert '1' == self.put_to_SoS(notebook, 'c(1)')
    #     assert '[1, 2]' == self.put_to_SoS(notebook, 'c(1, 2)')
    #     #
    #     assert '1.23' == self.put_to_SoS(notebook, 'c(1.23)')
    #     assert '[1.4, 2]' == self.put_to_SoS(notebook, 'c(1.4, 2)')

    # def test_get_logic_array(self, notebook):
    #     assert 'TRUE' == self.get_from_SoS(notebook, '[True]')
    #     assert 'TRUE FALSE TRUE' == self.get_from_SoS(notebook, '[True, False, True]')

    # def test_put_logic_array(self, notebook):
    #     # Note that single element numeric array is treated as single value
    #     assert 'True' == self.put_to_SoS(notebook, 'c(TRUE)')
    #     assert '[True, False, True]' == self.put_to_SoS(notebook, 'c(TRUE, FALSE, TRUE)')

    # def test_get_str(self, notebook):
    #     assert "'ab c d'" == self.get_from_SoS(notebook, "'ab c d'")
    #     assert "'ab\\td'" == self.get_from_SoS(notebook, r"'ab\td'")

    # def test_put_str(self, notebook):
    #     assert "'ab c d'" == self.put_to_SoS(notebook, "'ab c d'")
    #     assert "'ab\\td'" == self.put_to_SoS(notebook, r"'ab\td'")

    # def test_get_mixed_list(self, notebook):
    #     assert "1.4\nTRUE\n'asd'" == self.get_from_SoS(notebook, '[1.4, True, "asd"]')

    # def test_put_mixed_list(self, notebook):
    #     # R does not have mixed list, it just convert everything to string.
    #     assert "['1.4', 'TRUE', 'asd']" == self.put_to_SoS(notebook, 'c(1.4, TRUE, "asd")')

    # def test_get_dict(self, notebook):
    #     # Python does not have named ordered list, so get dictionary
    #     assert "$a\n1\n$b\n2\n$c\n'3'" == self.get_from_SoS(notebook, "dict(a=1, b=2, c='3')")

    # def test_put_named_list(self, notebook):
    #     assert "{'a': 1, 'b': 2, 'c': '3'}" == self.put_to_SoS(notebook, "list(a=1, b=2, c='3')")

    # def test_get_set(self, notebook):
    #     output = self.get_from_SoS(notebook, "{1.5, 'abc'}")
    #     assert "1.5\n'abc'" == output or "'abc'\n1.5" == output

    # def test_put_unnamed_list(self, notebook):
    #     output = self.put_to_SoS(notebook, "list(1.5, 'abc')")
    #     assert "[1.5, 'abc']" == output or "['abc', 1.5]" == output

    # def test_get_complex(self, notebook):
    #     assert "1+2.2i" == self.get_from_SoS(notebook, "complex(1, 2.2)")

    # def test_put_complex(self, notebook):
    #     assert "(1+2.2j)" == self.put_to_SoS(notebook, "complex(real=1, imaginary=2.2)")

    # def test_get_recursive(self, notebook):
    #     assert "$a\n1\n$b\n$c\n3\n$d\n'whatever'" == self.get_from_SoS(notebook, "{'a': 1, 'b': {'c': 3, 'd': 'whatever'}}")

    # def test_put_recursive(self, notebook):
    #     assert "{'a': 1, 'b': {'c': 3, 'd': 'whatever'}}" == self.put_to_SoS(notebook, "list(a=1, b=list(c=3, d='whatever'))")

    # def test_get_series(self, notebook):
    #     notebook.call('import pandas as pd', kernel='SoS')
    #     assert "0\n5\n1\n6\n2\n7" == self.get_from_SoS(notebook, 'pd.Series([5 ,6, 7])')

    # def test_put_series(self, notebook):
    #     output = self.put_to_SoS(notebook, "setNames(c(11, 22, 33), c('a', 'b', 'c'))")
    #     assert 'a    11' in output and 'b    22' in output and 'c    33' in output

    # def test_get_matrix(self, notebook):
    #     notebook.call('import numpy as np', kernel='SoS')
    #     assert "0 1\n1 2\n3 4" == self.get_from_SoS(notebook, 'np.matrix([[1,2],[3,4]])')

    # def test_put_matrix(self, notebook):
    #     output = self.put_to_SoS(notebook, "matrix(c(2, 4, 3, 1, 5, 7), nrow=2)")
    #     assert 'array' in output and '[2., 3., 5.]' in output and '[4., 1., 7.]' in output

    # def test_get_dataframe(self, notebook):
    #     notebook.call('''\
    #         %put df --to R
    #         import pandas as pd
    #         import numpy as np
    #         arr = np.random.randn(1000)
    #         arr[::10] = np.nan
    #         df = pd.DataFrame({'column_{0}'.format(i): arr for i in range(10)})
    #         ''', kernel='SoS')
    #     assert '1000' == notebook.check_output('dim(df)[1]', kernel='R')
    #     assert '10' == notebook.check_output('dim(df)[2]', kernel='R')

    # def test_put_dataframe(self, notebook):
    #     notebook.call('%put mtcars', kernel='R')
    #     assert '32' == notebook.check_output('mtcars.shape[0]', kernel='SoS')
    #     assert '11' == notebook.check_output('mtcars.shape[1]', kernel='SoS')
    #     assert "'Mazda RX4'" == notebook.check_output('mtcars.index[0]', kernel='SoS')

    # def test_get_dict_with_special_keys(self, notebook):
    #     output = self.get_from_SoS(notebook, "{'11111': 1, '_1111': 'a', 11112: 2, (1,2): 3}")
    #     assert '$X11111' in output and '$X_1111' in output and '$X11112' in output and '$X_1__2_' in output

#OLD TESTS

# class TestCppKernel(unittest.TestCase):

#     def setUp(self):
#         self.olddir = os.getcwd()
#         if os.path.dirname(__file__):
#             os.chdir(os.path.dirname(__file__))

#     def tearDown(self):
#         os.chdir(self.olddir)

#     def testPythonToCppScalars(self):
#         with sos_kernel() as kc:
#             iopub = kc.iopub_channel
#             execute(kc=kc, code = '''
#                 import numpy as np
#                 int1 = 10
#                 int2 = 1000000000000000000
#                 int4 = np.intc(20)
#                 float1 = 0.1
#                 float2 = 1e+50
#                 float3 = np.longdouble("1e+1000")
#                 string1 = 'abc'
#                 bool1 = True
#                 ''')
#             wait_for_idle(kc)

#             execute(kc=kc, code='%use C++14')
#             wait_for_idle(kc)

#             execute(kc=kc, code='%get int1 int2 int4 float1 float2 float3 string1 bool1')
#             wait_for_idle(kc)

#             #Test int1
#             execute(kc=kc, code='std::cout << int1;')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'10')

#             #Test int2
#             execute(kc=kc, code='std::cout << int2;')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'1000000000000000000')

#             #Test int4
#             execute(kc=kc, code='std::cout << int4;')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'20')

#             #Test float1
#             execute(kc=kc, code='std::cout << float1;')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip()[:3],'0.1')

#             #Test float2
#             execute(kc=kc, code='std::cout << float2;')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'1e+50')

#             #Test float3
#             execute(kc=kc, code='std::cout << float3;')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'inf')

#             #Test string1
#             execute(kc=kc, code='std::cout << string1;')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'abc')

#             #Test bool1
#             execute(kc=kc, code='std::cout << (bool1?"true":"false");')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'true')

#             execute(kc=kc, code="%use sos")
#             wait_for_idle(kc)

#     def testPythonToCppDataframe(self):
#         with sos_kernel() as kc:
#             iopub = kc.iopub_channel
#             execute(kc=kc, code = '''
#                 import numpy as np
#                 import pandas as pd
#                 dataframe = pd.DataFrame(np.random.randn(1000,4), columns=list('ABCD'))
#                 ''')

#             wait_for_idle(kc)
#             execute(kc=kc, code='%use C++14')
#             wait_for_idle(kc)
#             execute(kc=kc, code='%get dataframe')
#             wait_for_idle(kc)

#             execute(kc=kc, code='std::cout << dataframe.size();')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'4000')

#             execute(kc=kc, code="%use sos")
#             wait_for_idle(kc)

#     def testCpptoPythonScalars(self):
#         with sos_kernel() as kc:
#             iopub = kc.iopub_channel

#             execute(kc=kc, code='%use C++14')
#             wait_for_idle(kc)
#             execute(kc=kc, code='''
#                 int i = 1;
#                 short int si = 32;
#                 long int li = 2000000000;
#                 long long int lli = 2000000000000000000;
#                 float f = 0.1f;
#                 double d = 1e+300;
#                 long double ld = 1e+1000L;
#                 bool b = true;
#                 char c = '*';
#                 std::map<int, int> m = {{1,2},{2,3}};
#                 std::map<std::string, float> m2 = {{"Alice", -1.0f},{"Bob", 1.0f}};
#                 std::map<std::string, bool> m3 = {{"Alice", true},{"Bob", false}};
#                 std::vector<int> v = {1,2,3,4,5};
#                 std::vector<bool> v2 = {true,false,true,false,true};
#                 std::vector<std::string> v3 = {"q","w","e","r","t","y"};
#                 xt::xarray<double> arr
#                       {{1.1, 2.2, 3.3},
#                        {4.4, 5.5, 6.6},
#                        {7.7, 8.8, 9.9}};          
#                 xt::xarray<std::string> arr2
#                       {{"1.1", "2.2", "a"},
#                        {"4.4", "5.5", "6.6"},
#                        {"7.7", "8.8", "9.9"}};
#                 ''')
#             wait_for_idle(kc)
#             execute(kc=kc, code='%put i si li lli f d ld b c m m2 m3 v v2 v3 arr arr2')
#             wait_for_idle(kc)
#             execute(kc=kc, code='%use sos')
#             wait_for_idle(kc)

#             execute(kc=kc, code='print(i)')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'1')

#             execute(kc=kc, code='print(si)')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'32')

#             execute(kc=kc, code='print(lli)')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'2000000000000000000')

#             execute(kc=kc, code='print(f)')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip()[:10],'0.10000000')

#             execute(kc=kc, code='print(d)')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'1e+300')

#             execute(kc=kc, code='print(ld)')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'1e+1000')

#             execute(kc=kc, code='print(b)')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'True')

#             execute(kc=kc, code='print(c)')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'*')

#             execute(kc=kc, code='print(m[2])')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'3')

#             execute(kc=kc, code='print(m2["Alice"])')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'-1.0')

#             execute(kc=kc, code='print(m3["Bob"])')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'False')

#             execute(kc=kc, code='print(v)')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'[1 2 3 4 5]')

#             execute(kc=kc, code='print(sum(v2))')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'3')

#             execute(kc=kc, code='print("".join(v3))')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'qwerty')

#             execute(kc=kc, code='print(arr[1,1])')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'5.5')

#             execute(kc=kc, code='print(arr2[0,2])')
#             stdout, _ = assemble_output(iopub)
#             self.assertEqual(stdout.strip(),'a')

# if __name__ == '__main__':
#     unittest.main()