# ajax_command_changed()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 1122–1128 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L1122-L1128)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_changed($selector, $asterisk = '')
```

## Documentation

```text
Creates a Drupal Ajax 'changed' command.

This command instructs the client to mark each of the elements matched by the
given selector as 'ajax-changed'.

This command is implemented by Drupal.ajax.prototype.commands.changed()
defined in misc/ajax.js.

@param $selector
  A jQuery selector string. If the command is a response to a request from
  an #ajax form element then this value can be NULL.
@param $asterisk
  An optional CSS selector which must be inside $selector. If specified,
  an asterisk will be appended to the HTML inside the $asterisk selector.

@return
  An array suitable for use with the ajax_render() function.
```

## Code

```php
function ajax_command_changed($selector, $asterisk = '') {
  return array(
    'command' => 'changed',
    'selector' => $selector,
    'asterisk' => $asterisk,
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
