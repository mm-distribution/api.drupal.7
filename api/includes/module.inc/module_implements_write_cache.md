# module_implements_write_cache()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 899–910 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L899-L910)
- **Topics:** [hooks](../../topics/hooks.md)

## Signature

```php
function module_implements_write_cache()
```

## Documentation

```text
Writes the hook implementation cache.

@see module_implements()
```

## Code

```php
function module_implements_write_cache() {
  // The list of implementations includes vital modules only before full
  // bootstrap, so do not write cache if we are not fully bootstrapped yet.
  if (drupal_get_bootstrap_phase() != DRUPAL_BOOTSTRAP_FULL) {
    return;
  }
  $implementations = &drupal_static('module_implements');
  if (isset($implementations['#write_cache'])) {
    unset($implementations['#write_cache']);
    cache_set('module_implements', $implementations, 'cache_bootstrap');
  }
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
