# ajax_command_restripe()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 1267–1272 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L1267-L1272)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_restripe($selector)
```

## Documentation

```text
Creates a Drupal Ajax 'restripe' command.

The 'restripe' command instructs the client to restripe a table. This is
usually used after a table has been modified by a replace or append command.

This command is implemented by Drupal.ajax.prototype.commands.restripe()
defined in misc/ajax.js.

@param $selector
  A jQuery selector string.

@return
  An array suitable for use with the ajax_render() function.
```

## Code

```php
function ajax_command_restripe($selector) {
  return array(
    'command' => 'restripe',
    'selector' => $selector,
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
