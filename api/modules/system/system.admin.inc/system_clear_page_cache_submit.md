# system_clear_page_cache_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1805–1807 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1805-L1807)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_clear_page_cache_submit($form, &$form_state)
```

## Documentation

```text
Submit callback; clear the page cache.

@ingroup forms
```

## Code

```php
function system_clear_page_cache_submit($form, &$form_state) {
  cache_clear_all('*', 'cache_page', TRUE);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
