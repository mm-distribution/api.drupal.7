# ajax_command_replace()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 902–910 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L902-L910)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_replace($selector, $html, $settings = NULL)
```

## Documentation

```text
Creates a Drupal Ajax 'insert/replaceWith' command.

The 'insert/replaceWith' command instructs the client to use jQuery's
replaceWith() method to replace each element matched matched by the given
selector with the given HTML.

This command is implemented by Drupal.ajax.prototype.commands.insert()
defined in misc/ajax.js.

@param $selector
  A jQuery selector string. If the command is a response to a request from
  an #ajax form element then this value can be NULL.
@param $html
  The data to use with the jQuery replaceWith() method.
@param $settings
  An optional array of settings that will be used for this command only.

@return
  An array suitable for use with the ajax_render() function.

See
@link http://docs.jquery.com/Manipulation/replaceWith#content jQuery replaceWith command @endlink
```

## Code

```php
function ajax_command_replace($selector, $html, $settings = NULL) {
  return array(
    'command' => 'insert',
    'method' => 'replaceWith',
    'selector' => $selector,
    'data' => $html,
    'settings' => $settings,
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
