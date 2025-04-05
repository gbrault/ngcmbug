# NICEGUI / CODEMIRROR BUG

- use the vs-code env (see launch.json): make sure you have justmycode=false
- create a env with the requirements.txt
- using the example.html: works well
- using example_bug.html (see the code): add a char
- seems that this char 🔄 is the issue but this one 💾 works

this trigger the following error

```
Cannot apply change set to a document with the wrong length
Traceback (most recent call last):
  File "d:\SeaDev\ngcmbug\env\Lib\site-packages\nicegui\events.py", line 436, in handle_event
    result = cast(Callable[[EventT], Any], handler)(arguments)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "d:\SeaDev\ngcmbug\env\Lib\site-packages\nicegui\elements\mixins\value_element.py", line 40, in handle_change
    self.set_value(self._event_args_to_value(e))
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "d:\SeaDev\ngcmbug\env\Lib\site-packages\nicegui\elements\codemirror.py", line 335, in _event_args_to_value
    new_value = changeset.apply(self.value)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "d:\SeaDev\ngcmbug\env\Lib\site-packages\nicegui\elements\codemirror.py", line 363, in apply
    raise ValueError('Cannot apply change set to a document with the wrong length')
ValueError: Cannot apply change set to a document with the wrong length
```