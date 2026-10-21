# ajax_command_alert()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 840–845 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L840-L845)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_alert($text)
```

## Documentation

```text
Creates a Drupal Ajax 'alert' command.

The 'alert' command instructs the client to display a JavaScript alert
dialog box.

This command is implemented by Drupal.ajax.prototype.commands.alert()
defined in misc/ajax.js.

@param $text
  The message string to display to the user.

@return
  An array suitable for use with the ajax_render() function.
```

## Code

```php
function ajax_command_alert($text) {
  return array(
    'command' => 'alert',
    'text' => $text,
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
