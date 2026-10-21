# search_uninstall()

- **Type:** Function
- **File:** [`modules/search/search.install`](_file.md), lines 11–16 · [local source](../../../../source/modules/search/search.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.install#L11-L16)
- **Module/theme:** search
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function search_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function search_uninstall() {
  variable_del('minimum_word_size');
  variable_del('overlap_cjk');
  variable_del('search_cron_limit');
  variable_del('search_logging');
}
```

---
_Drupal 7.103 · [modules/search/search.install](https://github.com/drupal/drupal/blob/7.103/modules/search/search.install) · Licensed GPL-2.0-or-later (see LICENSE)._
