# ajax_command_data()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 1212–1219 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L1212-L1219)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_data($selector, $name, $value)
```

## Documentation

```text
Creates a Drupal Ajax 'data' command.

The 'data' command instructs the client to attach the name=value pair of
data to the selector via jQuery's data cache.

This command is implemented by Drupal.ajax.prototype.commands.data()
defined in misc/ajax.js.

@param $selector
  A jQuery selector string. If the command is a response to a request from
  an #ajax form element then this value can be NULL.
@param $name
  The name or key (in the key value pair) of the data attached to this
  selector.
@param $value
  The value of the data. Not just limited to strings can be any format.

@return
  An array suitable for use with the ajax_render() function.

@see http://docs.jquery.com/Core/data#namevalue
```

## Code

```php
function ajax_command_data($selector, $name, $value) {
  return array(
    'command' => 'data',
    'selector' => $selector,
    'name' => $name,
    'value' => $value,
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
