# module_exists()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 279–282 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L279-L282)

## Signature

```php
function module_exists($module)
```

## Documentation

```text
Determines whether a given module exists.

@param string $module
  The name of the module (without the .module extension).

@return bool
  TRUE if the module is both installed and enabled, FALSE otherwise.
```

## Code

```php
function module_exists($module) {
  $list = module_list();
  return isset($list[$module]);
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
