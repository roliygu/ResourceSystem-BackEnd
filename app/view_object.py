#! usr/bin/python
# coding=utf-8


class ValidateResult:
    def __init__(self, success, message):
        self.success = success
        self.message = message


class UploadResult:
    def __init__(self, success, message):
        self.success = success
        self.message = message


class TableCell:
    def __init__(self, value):
        self.value = value


class Table:
    def __init__(self, header: list, data: list):
        self.header = header
        self.data = data


ResourceHeader = [TableCell("资源名"), TableCell("原始文件名"), TableCell("路径"), TableCell("大小"), TableCell("创建时间"),
                  TableCell("更新时间")]
