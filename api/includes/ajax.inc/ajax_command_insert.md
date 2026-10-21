# ajax_command_insert()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 868–876 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L868-L876)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_insert($selector, $html, $settings = NULL)
```

## Documentation

```text
Creates a Drupal Ajax 'insert' command using the method in #ajax['method'].

This command instructs the client to insert the given HTML using whichever
jQuery DOM manipulation method has been specified in the #ajax['method']
variable of the element that triggered the request.

This command is implemented by Drupal.ajax.prototype.commands.insert()
defined in misc/ajax.js.

@param $selector
  A jQuery selector string. If the command is a response to a request from
  an #ajax form element then this value can be NULL.
@param $html
  The data to use with the jQuery method.
@param $settings
  An optional array of settings that will be used for this command only.

@return
  An array suitable for use with the ajax_render() function.
```

## Code

```php
function ajax_command_insert($selector, $html, $settings = NULL) {
  return array(
    'command' => 'insert',
    'method' => NULL,
    'selector' => $selector,
    'data' => $html,
    'settings' => $settings,
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
