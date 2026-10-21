# ajax_command_add_css()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 1313–1318 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L1313-L1318)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_add_css($styles)
```

## Documentation

```text
Creates a Drupal Ajax 'add_css' command.

This method will add css via ajax in a cross-browser compatible way.

This command is implemented by Drupal.ajax.prototype.commands.add_css()
defined in misc/ajax.js.

@param $styles
  A string that contains the styles to be added.

@return
  An array suitable for use with the ajax_render() function.

@see misc/ajax.js
```

## Code

```php
function ajax_command_add_css($styles) {
  return array(
    'command' => 'add_css',
    'data' => $styles,
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
