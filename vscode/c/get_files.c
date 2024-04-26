#include <stdio.h>
#include <string.h>
#include <dirent.h>
#include <stdlib.h>

// 函数声明
void listFiles(const char *path, const char *extension, const char *outputFile);

int main(int argc, char *argv[]) {
    if (argc < 3 || argc > 4) {
        printf("Usage: %s <directory> <extension> [<output_file>]\n", argv[0]);
        return 1;
    }

    const char *directory = argv[1]; // 目录
    const char *extension = argv[2]; // 文件后缀
    const char *outputFile = "output.txt"; // 默认输出文件

    if (argc == 4) {
        outputFile = argv[3]; // 如果提供了第三个参数，则使用提供的输出文件名
    }

    listFiles(directory, extension, outputFile);
    return 0;
}

// 遍历目录下的文件及子目录下的文件，并将结果写入指定文件
void listFiles(const char *path, const char *extension, const char *outputFile) {
    FILE *output = fopen(outputFile, "a"); // 以追加模式打开输出文件
    if (!output) {
        perror("Error opening output file");
        return;
    }

    DIR *dir;
    struct dirent *entry;

    // 打开目录
    if (!(dir = opendir(path))) {
        perror("opendir");
        fclose(output);
        return;
    }

    // 读取目录中的每一个文件及子目录
    while ((entry = readdir(dir)) != NULL) {
        // 构建子目录的路径
        char subpath[1024];
        snprintf(subpath, sizeof(subpath), "%s/%s", path, entry->d_name);

        if (entry->d_type == DT_DIR) {
            // 忽略 . 和 ..
            if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
                continue;

            // 递归调用遍历子目录
            listFiles(subpath, extension, outputFile);
        } else if (entry->d_type == DT_REG) { // 普通文件
            // 检查文件名是否以指定的后缀结尾
            if (strstr(entry->d_name, extension) != NULL) {
                fprintf(output, "%s/%s\n", path, entry->d_name);
            }
        }
    }

    closedir(dir);
    fclose(output);
}