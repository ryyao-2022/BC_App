from nicegui import ui

with ui.card().classes("w-full max-w-3xl mx-auto shadow-lg"):
    ui.label("个人资料页面").classes("text-xl font-bold")

    with ui.row().classes("w-full"):
        with ui.card():
            ui.image("./profile.png")

            with ui.card_section():
                ui.label("个人资料图片").classes("text-center font-bold")
                ui.button("更改图片", icon="photo_camera")

        with ui.card().classes("flex-grow"):
            with ui.column().classes("w-full"):
                name_input = ui.input(
                    placeholder="请输入您的名字",
                ).classes("w-full")
                gender_select = ui.select(
                    ["男", "女", "其他"],
                ).classes("w-full")
                eye_color_input = ui.input(
                    placeholder="眼睛颜色",
                ).classes("w-full")
                height_input = ui.number(
                    min=0,
                    max=250,
                    value=170,
                    step=1,
                ).classes("w-full")
                weight_input = ui.number(
                    min=0,
                    max=500,
                    value=60,
                    step=0.1,
                ).classes("w-full")

            with ui.row().classes("justify-end gap-2 q-mt-lg"):
                ui.button("重置", icon="refresh").props("outline")
                ui.button("保存", icon="save").props("color=primary")

ui.run(title="NiceGUI 布局元素")