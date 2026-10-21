# search_permission()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 124–136 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L124-L136)
- **Module/theme:** search
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function search_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function search_permission() {
  return array(
    'administer search' => array(
      'title' => t('Administer search'),
    ),
    'search content' => array(
      'title' => t('Use search'),
    ),
    'use advanced search' => array(
      'title' => t('Use advanced search'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
