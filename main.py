from nicegui import ui
from pathlib import Path

html_file = Path('example_bug.html')

# Load file content initially
initial_content = html_file.read_text(encoding="utf8") if html_file.exists() else "<!-- Start typing your HTML here -->"

# Create CodeMirror editor
editor = ui.codemirror(value=initial_content, language='html').classes('w-full').style('height: 80vh;')

# Save file button
def save():
    html_file.write_text(editor.value, encoding="utf8")
    ui.notify('HTML saved!')

# Reload file button
def load():
    editor.value = html_file.read_text(encoding="utf8")
    ui.notify('HTML loaded!')

with ui.row().classes('mt-4'):
    ui.button('💾 Save', on_click=save).props('color=primary')
    ui.button('🔄 Reload', on_click=load).props('color=secondary')

ui.run(show=False, reload=False, port=8081, title='HTML Editor')
