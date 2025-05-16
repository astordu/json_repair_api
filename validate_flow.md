# validate.py 主流程 Mermaid 流程图

```mermaid
flowchart TD
    A[程序入口: __main__] --> B[定义 test_cases 测试用例列表]
    B --> C[遍历 test_cases]
    C --> D{第 i 个用例}
    D --> E[获取检测函数和错误类型]
    E --> F[打印测试用例编号和错误类型]
    F --> G[打印输入内容]
    G --> H[调用检测函数]
    H --> I[调用 repair_json]
    I --> J[返回修复后的 JSON 字符串]
    J --> K[打印输出结果]
    K --> L[打印分隔线]
    L --> C

    subgraph 检测函数
        direction LR
        H1[缺失引号的键] --> I
        H2[缺失转义字符] --> I
        H3[缺失逗号] --> I
        H4[缺失右括号] --> I
        H5[被截断的JSON] --> I
        H6[单引号] --> I
        H7[特殊引号] --> I
        H8[特殊空白字符] --> I
        H9[None/True/False] --> I
        H10[多余结尾逗号] --> I
        H11[注释] --> I
        H12[代码块标记] --> I
        H13[省略号] --> I
        H14[JSONP格式] --> I
        H15[多余转义符] --> I
        H16[每行一个JSON对象] --> I
    end

    style 检测函数 fill:#f9f,stroke:#333,stroke-width:1px
```

---

## 说明
- 每个检测函数（如“缺失引号的键”等）都只是简单地调用了 `repair_json`，并没有独立的逻辑。
- 主流程是遍历测试用例，依次调用对应的检测函数，打印输入和输出。
- `repair_json` 是核心处理函数，所有检测函数都调用它。

如需更详细的分支（比如 `repair_json` 内部的处理细节），请补充其实现代码。 