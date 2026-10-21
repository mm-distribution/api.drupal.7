# _drupal_render_exception_safe()

- **Type:** Function
- **File:** [`includes/errors.inc`](_file.md), lines 132–134 · [local source](../../../source/includes/errors.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc#L132-L134)

## Signature

```php
function _drupal_render_exception_safe($exception)
```

## Documentation

```text
Renders an exception error message without further exceptions.

@param $exception
  The exception object that was thrown.
@return
  An error message.
```

## Code

```php
function _drupal_render_exception_safe($exception) {
  return check_plain(strtr('%type: !message in %function (line %line of %file).', _drupal_decode_exception($exception)));
}
```

---
_Drupal 7.103 · [includes/errors.inc](https://github.com/drupal/drupal/blob/7.103/includes/errors.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
