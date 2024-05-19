#include <stdio.h>
#include <string.h>
#include <dirent.h>
#include <stdlib.h> // 用于 calloc、free、realloc、exit 函数
#include <ctype.h>  // 用于 tolower 函数


#define MAX_PATH_LEN 1024
#define MAX_EXT_LEN 16

// 结构体定义
typedef struct FileList {
    char extension[MAX_EXT_LEN];
    char **files;
    size_t num_files;
} FileList;

// 函数声明
void listFiles(const char *path, FileList **fileLists);
void addFile(FileList **fileLists, const char *extension, const char *filePath);
void writeToFile(FileList **fileLists);

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <directory>\n", argv[0]);
        return 1;
    }

    const char *directory = argv[1]; // 目录

    // 创建并初始化哈希表数组
    FileList **fileLists = calloc(256, sizeof(FileList *));
    if (!fileLists) {
        perror("Memory allocation failed");
        return 1;
    }

    // 遍历目录并分类文件
    listFiles(directory, fileLists);

    // 将分类结果写入文档
    writeToFile(fileLists);

    // 释放内存
    for (int i = 0; i < 256; ++i) {
        if (fileLists[i]) {
            for (size_t j = 0; j < fileLists[i]->num_files; ++j) {
                free(fileLists[i]->files[j]);
            }
            free(fileLists[i]->files);
            free(fileLists[i]);
        }
    }
    free(fileLists);

    return 0;
}

// 遍历目录下的文件并分类
void listFiles(const char *path, FileList **fileLists) {
    DIR *dir;
    struct dirent *entry;

    // 打开目录
    if (!(dir = opendir(path))) {
        perror("opendir");
        return;
    }

    // 读取目录中的每一个文件
    while ((entry = readdir(dir)) != NULL) {
        // 构建文件的完整路径
        char filePath[MAX_PATH_LEN];
        snprintf(filePath, sizeof(filePath), "%s/%s", path, entry->d_name);

        if (entry->d_type == DT_REG) { // 普通文件
            // 获取文件后缀
            char *dot = strrchr(entry->d_name, '.');
            if (dot && dot != entry->d_name) {
                // 使用哈希表存储文件
                addFile(fileLists, dot + 1, filePath);
            }
        } else if (entry->d_type == DT_DIR) { // 子目录
            // 忽略 . 和 ..
            if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
                continue;

            // 递归遍历子目录
            listFiles(filePath, fileLists);
        }
    }

    closedir(dir);
}

// 将文件添加到哈希表中
void addFile(FileList **fileLists, const char *extension, const char *filePath) {
    // 转换后缀为小写
    char ext[MAX_EXT_LEN];
    size_t i;
    for (i = 0; extension[i] && i < MAX_EXT_LEN - 1; ++i) {
        ext[i] = tolower(extension[i]);
    }
    ext[i] = '\0';

    // 计算哈希值
    unsigned char hash = 0;
    for (i = 0; ext[i]; ++i) {
        hash += ext[i];
    }

    // 检查哈希表中是否已存在后缀
    if (!fileLists[hash]) {
        // 创建新的后缀列表
        fileLists[hash] = calloc(1, sizeof(FileList));
        if (!fileLists[hash]) {
            perror("Memory allocation failed");
            exit(1);
        }
        strncpy(fileLists[hash]->extension, ext, MAX_EXT_LEN);
    }

    // 添加文件路径到后缀列表中
    fileLists[hash]->files = realloc(fileLists[hash]->files, (fileLists[hash]->num_files + 1) * sizeof(char *));
    if (!fileLists[hash]->files) {
        perror("Memory allocation failed");
        exit(1);
    }
    fileLists[hash]->files[fileLists[hash]->num_files] = strdup(filePath);
    if (!fileLists[hash]->files[fileLists[hash]->num_files]) {
        perror("Memory allocation failed");
        exit(1);
    }
    ++fileLists[hash]->num_files;
}

// 将分类结果写入文档
void writeToFile(FileList **fileLists) {
    for (int i = 0; i < 256; ++i) {
        if (fileLists[i]) {
            char outputFilePath[MAX_PATH_LEN];
            snprintf(outputFilePath, sizeof(outputFilePath), "%s.txt", fileLists[i]->extension);

            FILE *output = fopen(outputFilePath, "w");
            if (!output) {
                perror("Error opening output file");
                return;
            }

            for (size_t j = 0; j < fileLists[i]->num_files; ++j) {
                fprintf(output, "%s\n", fileLists[i]->files[j]);
            }

            fclose(output);
        }
    }
}
