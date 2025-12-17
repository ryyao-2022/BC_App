import home_pages
import theme
from pages import framework, onchain, traceability

from nicegui import app, ui

# Current page state
current_page = {'name': 'home'}
content_container = None


def show_page(page_name: str) -> None:
    """Update the displayed page content"""
    current_page['name'] = page_name
    content_container.clear()
    
    with content_container:
        if page_name == 'home':
            home_pages.content()
        elif page_name == 'framework':
            framework.content()
        elif page_name == 'onchain':
            onchain.content()
        elif page_name == 'traceability':
            traceability.content()


# Main page with persistent menu
@ui.page('/')
def index_page() -> None:
    global content_container
    
    ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
    
    with ui.header().classes(replace='row items-center py-3') as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
        ui.label('总菜单').classes('font-bold text-lg')

    with ui.footer(value=False) as footer:
        ui.label('碳流区块链数据记录系统')
    
    with ui.left_drawer(value=True).props('permanent').classes('bg-blue-100') as left_drawer:
        ui.label('基于联盟区块链的碳流数据记录系统').classes('text-xl font-bold')
        ui.separator()
        
        # Menu with navigation callbacks
        with ui.column().classes('w-full gap-2'):
            ui.button('🏠 首页', on_click=lambda: show_page('home')).props('flat').classes('w-full text-left text-base')
            ui.separator().classes('my-2')
            ui.button('⛓️ 碳流区块链框架', on_click=lambda: show_page('framework')).props('flat').classes('w-full text-left text-base')
            ui.button('🔍 链上信息浏览', on_click=lambda: show_page('onchain')).props('flat').classes('w-full text-left text-base')
            ui.button('🔐 碳流信息溯源', on_click=lambda: show_page('traceability')).props('flat').classes('w-full text-left text-base')
    
    # Main content area
    with ui.column().classes('p-6 w-full') as content_container:
        show_page('home')
    
    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon='contact_support').props('fab')


ui.run(title='碳流区块链数据记录系统')