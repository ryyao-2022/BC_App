from nicegui import ui


def content() -> None:
    with ui.column().classes('items-start w-full'):
        ui.label('⛓️ 碳流区块链框架').classes('text-3xl font-bold mb-6')
        ui.markdown('''
        本页面介绍系统的整体架构、节点部署策略与区块格式设计。

        **主要内容：**
        - 云-边-端协同架构概述
        - 全局节点选择与成本优化策略
        - 可插拔的区块链模块设计

        （此处可补充详细架构图和技术说明）
        ''').classes('text-lg leading-relaxed')
