# ajax_command_remove()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 1096–1101 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L1096-L1101)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_remove($selector)
```

## Documentation

```text
Creates a Drupal Ajax 'remove' command.

The 'remove' command instructs the client to use jQuery's remove() method
to remove each of elements matched by the given selector, and everything
within them.

This command is implemented by Drupal.ajax.prototype.commands.remove()
defined in misc/ajax.js.

@param $selector
  A jQuery selector string. If the command is a response to a request from
  an #ajax form element then this value can be NULL.

@return
  An array suitable for use with the ajax_render() function.

@see http://docs.jquery.com/Manipulation/remove#expr
```

## Code

```php
function ajax_command_remove($selector) {
  return array(
    'command' => 'remove',
    'selector' => $selector,
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
