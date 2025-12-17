from nicegui import ui
from pages import framework, onchain, traceability

def create() -> None:
    ui.page('/framework/')(framework.content)
    ui.page('/onchain/')(onchain.content)
    ui.page('/traceability/')(traceability.content)


if __name__ == '__main__':
    create()