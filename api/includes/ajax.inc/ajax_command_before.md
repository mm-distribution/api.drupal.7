# ajax_command_before()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 1067–1075 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L1067-L1075)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_before($selector, $html, $settings = NULL)
```

## Documentation

```text
Creates a Drupal Ajax 'insert/before' command.

The 'insert/before' command instructs the client to use jQuery's before()
method to insert the given HTML content before each of elements matched by
the given selector.

This command is implemented by Drupal.ajax.prototype.commands.insert()
defined in misc/ajax.js.

@param $selector
  A jQuery selector string. If the command is a response to a request from
  an #ajax form element then this value can be NULL.
@param $html
  The data to use with the jQuery before() method.
@param $settings
  An optional array of settings that will be used for this command only.

@return
  An array suitable for use with the ajax_render() function.

@see http://docs.jquery.com/Manipulation/before#content
```

## Code

```php
function ajax_command_before($selector, $html, $settings = NULL) {
  return array(
    'command' => 'insert',
    'method' => 'before',
    'selector' => $selector,
    'data' => $html,
    'settings' => $settings,
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
