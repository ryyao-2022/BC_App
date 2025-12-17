from nicegui import ui


def content() -> None:
    with ui.column().classes('items-start w-full'):
        ui.label('🔍 链上信息浏览').classes('text-3xl font-bold mb-6')
        ui.markdown('''
        在此页面可以浏览已上链的碳流相关数据。示例功能：

        **主要功能：**
        - 按时间/节点筛选记录
        - 查看区块摘要与元数据
        - 导出查询结果为 CSV

        （此处将接入链上数据查询接口并展示结果表格）
        ''').classes('text-lg leading-relaxed')
