# image_toolkit_invoke()

- **Type:** Function
- **File:** [`includes/image.inc`](_file.md), lines 93–101 · [local source](../../../source/includes/image.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L93-L101)
- **Topics:** [image](../../topics/image.md)

## Signature

```php
function image_toolkit_invoke($method, stdClass $image, array $params = array())
```

## Documentation

```text
Invokes the given method using the currently selected toolkit.

@param $method
  A string containing the method to invoke.
@param $image
  An image object returned by image_load().
@param $params
  An optional array of parameters to pass to the toolkit method.

@return
  Mixed values (typically Boolean indicating successful operation).
```

## Code

```php
function image_toolkit_invoke($method, stdClass $image, array $params = array()) {
  $function = 'image_' . $image->toolkit . '_' . $method;
  if (function_exists($function)) {
    array_unshift($params, $image);
    return call_user_func_array($function, $params);
  }
  watchdog('image', 'The selected image handling toolkit %toolkit can not correctly process %function.', array('%toolkit' => $image->toolkit, '%function' => $function), WATCHDOG_ERROR);
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/image.inc](https://github.com/drupal/drupal/blob/7.103/includes/image.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
