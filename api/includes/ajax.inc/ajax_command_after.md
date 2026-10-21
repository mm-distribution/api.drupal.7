# ajax_command_after()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 1034–1042 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L1034-L1042)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_after($selector, $html, $settings = NULL)
```

## Documentation

```text
Creates a Drupal Ajax 'insert/after' command.

The 'insert/after' command instructs the client to use jQuery's after()
method to insert the given HTML content after each element matched by
the given selector.

This command is implemented by Drupal.ajax.prototype.commands.insert()
defined in misc/ajax.js.

@param $selector
  A jQuery selector string. If the command is a response to a request from
  an #ajax form element then this value can be NULL.
@param $html
  The data to use with the jQuery after() method.
@param $settings
  An optional array of settings that will be used for this command only.

@return
  An array suitable for use with the ajax_render() function.

@see http://docs.jquery.com/Manipulation/after#content
```

## Code

```php
function ajax_command_after($selector, $html, $settings = NULL) {
  return array(
    'command' => 'insert',
    'method' => 'after',
    'selector' => $selector,
    'data' => $html,
    'settings' => $settings,
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
