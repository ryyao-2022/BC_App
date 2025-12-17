from contextlib import contextmanager
from menu import menu
from nicegui import ui, app

# Shared layout component
@contextmanager
def frame(navtitle: str):
    """Custom page frame to share the same styling and behavior across all pages"""
    ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
    
    with ui.header().classes(replace='row items-center') as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
        ui.label('基于联盟区块链的碳流数据记录系统').classes('font-bold text-lg')

    with ui.footer(value=False) as footer:
        ui.label('碳流区块链数据记录系统')
    
    with ui.left_drawer(value=True).props('permanent').classes('bg-blue-100') as left_drawer:
        ui.label('基于联盟区块链的碳流数据记录系统').classes('text-xl font-bold')
        ui.separator()
        with ui.column():
            menu()
    
    # Main content area
    with ui.column().classes('p-6 w-full'):
        yield
    
    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon='contact_support').props('fab')