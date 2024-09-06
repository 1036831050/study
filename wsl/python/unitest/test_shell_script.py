import unittest
import subprocess
import os

class TestShellScript(unittest.TestCase):
    
    def setUp(self):
        # 准备测试所需的文件和目录
        open("test.txt", "w").close()
        open("script.sh", "w").close()

    def tearDown(self):
        # 清理测试后的状态
        os.remove("test.txt")
        os.remove("script.sh")
        for directory in os.listdir():
            if os.path.isdir(directory):
                os.rmdir(directory)

    def test_shell_script(self):
        # 使用subprocess模块运行Shell脚本
        subprocess.run(["bash", "organize_files.sh"], input=b"y\n", text=True, check=True)
        
        # 断言预期的目录结构是否正确
        self.assertTrue(os.path.isdir("txt"))
        self.assertTrue(os.path.isdir("sh"))
        self.assertTrue(os.path.exists("txt/test.txt"))
        self.assertTrue(os.path.exists("sh/script.sh"))

if __name__ == "__main__":
    unittest.main()
