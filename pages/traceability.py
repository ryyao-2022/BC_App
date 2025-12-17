from nicegui import ui


def content() -> None:
    with ui.column().classes('items-start w-full'):
        ui.label('🔐 碳流信息溯源').classes('text-3xl font-bold mb-6')
        ui.markdown('''
        本页面用于追溯单条或批量碳流记录的来源、变更历史与相关证明：

        **主要功能：**
        - 输入记录 ID 或批次号进行查询
        - 展示完整的交易和状态变更链
        - 提供可视化溯源路径图

        （此处将实现溯源查询与可视化组件）
        ''').classes('text-lg leading-relaxed')
