# drupal_register_shutdown_function()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3856–3872 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3856-L3872)
- **Topics:** [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function &drupal_register_shutdown_function($callback = NULL)
```

## Documentation

```text
Registers a function for execution on shutdown.

Wrapper for register_shutdown_function() that catches thrown exceptions to
avoid "Exception thrown without a stack frame in Unknown".

@param $callback
  The shutdown function to register.
@param ...
  Additional arguments to pass to the shutdown function.

@return
  Array of shutdown functions to be executed.

@see register_shutdown_function()
@ingroup php_wrappers
```

## Code

```php
function &drupal_register_shutdown_function($callback = NULL) {
  // We cannot use drupal_static() here because the static cache is reset during
  // batch processing, which breaks batch handling.
  static $callbacks = array();

  if (isset($callback)) {
    // Only register the internal shutdown function once.
    if (empty($callbacks)) {
      register_shutdown_function('_drupal_shutdown_function');
    }
    $args = func_get_args();
    array_shift($args);
    // Save callback and arguments
    $callbacks[] = array('callback' => $callback, 'arguments' => $args);
  }
  return $callbacks;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
