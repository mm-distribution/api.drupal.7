# ajax_command_css()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 1150–1156 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L1150-L1156)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_css($selector, $argument)
```

## Documentation

```text
Creates a Drupal Ajax 'css' command.

The 'css' command will instruct the client to use the jQuery css() method
to apply the CSS arguments to elements matched by the given selector.

This command is implemented by Drupal.ajax.prototype.commands.css()
defined in misc/ajax.js.

@param $selector
  A jQuery selector string. If the command is a response to a request from
  an #ajax form element then this value can be NULL.
@param $argument
  An array of key/value pairs to set in the CSS for the selector.

@return
  An array suitable for use with the ajax_render() function.

@see http://docs.jquery.com/CSS/css#properties
```

## Code

```php
function ajax_command_css($selector, $argument) {
  return array(
    'command' => 'css',
    'selector' => $selector,
    'argument' => $argument,
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
