import re
from typing import List
from json_repair import repair_json

# 1. 检查缺失引号的键
def has_missing_key_quotes(s):
    # 匹配 {name: 或 ,name: 但不是 {"name":
    return repair_json(s, ensure_ascii=False)

# 2. 检查缺失转义字符
def has_missing_escape(s):
    # 匹配 " 内部出现未转义的 "
    return repair_json(s, ensure_ascii=False)

# 3. 检查缺失逗号
def has_missing_comma(s):
    # 匹配 "value" "key" 或 数字 "key"
    return repair_json(s, ensure_ascii=False)

# 4. 检查缺失右括号
def has_missing_bracket(s):
    # 左右大括号数量不等
    return repair_json(s, ensure_ascii=False)

# 5. 检查被截断的 JSON
def has_truncated_json(s):
    # 以逗号结尾或只有一个 key
    return repair_json(s, ensure_ascii=False)

# 6. 检查单引号
def has_single_quotes(s):
    return repair_json(s, ensure_ascii=False)

# 7. 检查特殊引号
SPECIAL_QUOTES = ['"', '"', '"', '"', '"', '"']
def has_special_quotes(s):
    return repair_json(s, ensure_ascii=False)

# 8. 检查特殊空白字符
SPECIAL_SPACES = ['\u00A0', '\u2002', '\u2003', '\u2009', '\u3000']
def has_special_spaces(s):
    return repair_json(s, ensure_ascii=False)

# 9. 检查 None/True/False
PYTHON_LITERALS = ['None', 'True', 'False']
def has_python_literals(s):
    return repair_json(s, ensure_ascii=False)

# 10. 检查多余结尾逗号
def has_trailing_comma(s):
    return repair_json(s, ensure_ascii=False)

# 11. 检查注释
def has_comment(s):
    return repair_json(s, ensure_ascii=False)

# 12. 检查代码块标记
CODE_BLOCK_MARKS = ['```json', '```', '```\n']
def has_code_block_mark(s):
    return repair_json(s, ensure_ascii=False)

# 13. 检查省略号
def has_ellipsis(s):
    return repair_json(s, ensure_ascii=False)

# 14. 检查 JSONP 格式
def has_jsonp(s):
    return repair_json(s, ensure_ascii=False)

# 15. 检查多余转义符
# 这里简单判断字符串整体被包裹且内部有转义
def has_extra_escape(s):
    return repair_json(s, ensure_ascii=False)

# 16. 检查每行一个 JSON 对象
# 检查多行且每行以 { 开头
def has_multiline_json_objects(s):
    return repair_json(s, ensure_ascii=False)

# 总入口
ERROR_TYPES = [
    (has_missing_key_quotes, '缺失引号的键'),
    (has_missing_escape, '缺失转义字符'),
    (has_missing_comma, '缺失逗号'),
    (has_missing_bracket, '缺失右括号'),
    (has_truncated_json, '被截断的JSON'),
    (has_single_quotes, '单引号'),
    (has_special_quotes, '特殊引号'),
    (has_special_spaces, '特殊空白字符'),
    (has_python_literals, 'None/True/False'),
    (has_trailing_comma, '多余结尾逗号'),
    (has_comment, '注释'),
    (has_code_block_mark, '代码块标记'),
    (has_ellipsis, '省略号'),
    (has_jsonp, 'JSONP格式'),
    (has_extra_escape, '多余转义符'),
    (has_multiline_json_objects, '每行一个JSON对象'),
]



if __name__ == "__main__":
    test_cases = [
        # 1. 缺失引号的键
        '{name: "张三"}',
        # 2. 缺失转义字符
        '{"text": "He said "hello""}',
        # 3. 缺失逗号
        '{"a": 1 "b": 2}',
        # 4. 缺失右括号
        '{"a": 1, "b": 2',
        # 5. 被截断的 JSON
        '{"a": 1,',
        # 6. 单引号
        "{'a': 1, 'b': 2}",
        # 7. 特殊引号
        '{"a": 1, "b": 2}',
        # 8. 特殊空白字符
        '{"a":\u00A01, "b": 2}',
        # 9. None/True/False
        '{"a": None, "b": True, "c": False}',
        # 10. 多余结尾逗号
        '{"a": 1, "b": 2,}',
        # 11. 注释
        '{"a": 1, /* 注释 */ "b": 2}',
        # 12. 代码块标记
        '```json\n{"a": 1, "b": 2}\n```',
        # 13. 省略号
        '[1, 2, 3, ...]',
        # 14. JSONP 格式
        'callback({"a": 1, "b": 2})',
        # 15. 多余转义符
        '"{\\"a\\": 1, \\"b\\": 2}"',
        # 16. 每行一个 JSON 对象
        '{ "id": 1, "name": "张三" }\n{ "id": 2, "name": "李四" }',
    ]
    for i, case in enumerate(test_cases, 1):
        print(f"测试用例 {i}: {ERROR_TYPES[i-1][1]}")
        print(f"输入: {case}")
        ans = ERROR_TYPES[i-1][0](case)
        print(f"输出: {ans}")
        print("-" * 40)
