# bootstrap_invoke_all()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1403–1415 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1403-L1415)

## Signature

```php
function bootstrap_invoke_all($hook)
```

## Documentation

```text
Invokes a bootstrap hook in all bootstrap modules that implement it.

@param $hook
  The name of the bootstrap hook to invoke.

@see bootstrap_hooks()
```

## Code

```php
function bootstrap_invoke_all($hook) {
  // Bootstrap modules should have been loaded when this function is called, so
  // we don't need to tell module_list() to reset its internal list (and we
  // therefore leave the first parameter at its default value of FALSE). We
  // still pass in TRUE for the second parameter, though; in case this is the
  // first time during the bootstrap that module_list() is called, we want to
  // make sure that its internal cache is primed with the bootstrap modules
  // only.
  foreach (module_list(FALSE, TRUE) as $module) {
    drupal_load('module', $module);
    module_invoke($module, $hook);
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
