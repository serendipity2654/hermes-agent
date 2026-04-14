# from toolsets import get_all_toolsets, get_toolset_info
from run_agent import main

if __name__ == "__main__":
    # all_toolsets = get_all_toolsets()
    # info_list = []
    # for name, toolset in all_toolsets.items():
    #     info = get_toolset_info(name)
    #     if info:
    #         info_list.append(info)
    api_key = "sk-26ad6960be8542a9b256b6236631e6c7"
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    model = "qwen3.5-plus"
    main(
        query="今天上海天气怎么样？",
        model=model,
        api_key=api_key,
        base_url=base_url,
        # list_tools=True,
        verbose=True,
        enabled_toolsets="file, vision, web, terminal, safe, research, development"
    )

    print("Done")