from nicegui import ui


def menu() -> None:
    """碳流区块链应用菜单"""
    with ui.column().classes('w-full gap-2'):
        # 首页
        ui.button('🏠 首页', on_click=lambda: ui.navigate('/')).props('flat').classes('w-full text-left text-base')
        
        ui.separator().classes('my-2')
        
        # 碳流区块链框架
        ui.button('⛓️ 碳流区块链框架', on_click=lambda: ui.navigate('/framework')).props('flat').classes('w-full text-left text-base')
        
        # 链上信息浏览
        ui.button('🔍 链上信息浏览', on_click=lambda: ui.navigate('/onchain')).props('flat').classes('w-full text-left text-base')
        
        # 碳流信息溯源
        ui.button('🔐 碳流信息溯源', on_click=lambda: ui.navigate('/traceability')).props('flat').classes('w-full text-left text-base')