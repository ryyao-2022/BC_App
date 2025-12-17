from nicegui import ui

def content() -> None:
    with ui.column().classes('items-center'):
        with ui.card().classes('w-full max-w-3xl p-6').props('outlined'):
            ui.label('总体说明').classes('text-3xl font-bold mb-4')
            ui.markdown('''
            我们推出一套专为现代电网设计的创新型区块链解决方案。该方案基于开创性的“云-边-端”协同架构，巧妙利用现有的电网通信拓扑，通过嵌入式节点实现电力数据的便捷上链。我们充分考虑了实际应用的经济性，通过优化全局节点选择策略，有效降低了数据流通的通信成本与存储开销。为确保快速、无缝地部署，系统采用了数据主站与区块链模块解耦的“可插拔”设计。该架构的核心是为碳流数据量身定制的交互逻辑与区块格式，旨在为电网的碳足迹追踪提供前所未有的透明度、安全性和可追溯性。

            ''').classes('text-lg leading-relaxed') 
            with ui.row().classes('justify-center mt-6'):
                try:
                    ui.image('./overall scheme.png').classes('max-w-full h-auto rounded shadow')
                except Exception as e:
                    ui.label(f'⚠️ 图片加载失败: {str(e)}').classes('text-sm text-red-600')
            ui.label('图：总体架构示意图').classes('text-sm text-gray-600 mt-2')