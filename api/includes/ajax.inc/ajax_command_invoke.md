# ajax_command_invoke()

- **Type:** Function
- **File:** [`includes/ajax.inc`](_file.md), lines 1243–1250 · [local source](../../../source/includes/ajax.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L1243-L1250)
- **Topics:** [ajax_commands](../../topics/ajax_commands.md)

## Signature

```php
function ajax_command_invoke($selector, $method, array $arguments = array())
```

## Documentation

```text
Creates a Drupal Ajax 'invoke' command.

The 'invoke' command will instruct the client to invoke the given jQuery
method with the supplied arguments on the elements matched by the given
selector. Intended for simple jQuery commands, such as attr(), addClass(),
removeClass(), toggleClass(), etc.

This command is implemented by Drupal.ajax.prototype.commands.invoke()
defined in misc/ajax.js.

@param $selector
  A jQuery selector string. If the command is a response to a request from
  an #ajax form element then this value can be NULL.
@param $method
  The jQuery method to invoke.
@param $arguments
  (optional) A list of arguments to the jQuery $method, if any.

@return
  An array suitable for use with the ajax_render() function.
```

## Code

```php
function ajax_command_invoke($selector, $method, array $arguments = array()) {
  return array(
    'command' => 'invoke',
    'selector' => $selector,
    'method' => $method,
    'arguments' => $arguments,
  );
}
```

---
_Drupal 7.103 · [includes/ajax.inc](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
