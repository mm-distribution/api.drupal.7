# system_clear_cache_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1795–1798 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1795-L1798)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_clear_cache_submit($form, &$form_state)
```

## Documentation

```text
Submit callback; clear system caches.

@ingroup forms
```

## Code

```php
function system_clear_cache_submit($form, &$form_state) {
  drupal_flush_all_caches();
  drupal_set_message(t('Caches cleared.'));
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
