# coding=utf-8
from Test_source_code import rect_area

height = 3
width = 4
correct_answer = 12
answer = rect_area(height, width)
if answer == correct_answer:
    print('Test passed.')
else:
    print('Test failed.')

# ### 测试驱动开发的基本步骤
# 1 - 确定并记录功能需求，再为之编写一个测试（必须确保测试是正确的，如果测试本身有错误，那么实际上什么都没有测试）；
# 2 - 编写实现功能的代码，让程序能够运行（不存在语法错误之类的问题），但可能无法通过测试；
# 3 - 确定测试失败的原因，编写能够通过测试的代码，不断重复此过程；
# 4 - 改进（重构）代码以全面而准确地实现所需要的功能，同时确保测试成功；
#
# ### 测试驱动编程
# 先编写测试，再编写让可以通过测试的程序；
# 测试程序是需求说明（主要是功能需求）的代码呈现，可帮助确保程序开发过程严格遵照需求说明；
#
# ### 关于测试
# 不要盲目信任测试，因为测试本身可能没有涵盖足够的场景；
# 务必要测试足够广泛和详尽的场景；
