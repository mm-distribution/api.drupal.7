# search_is_active()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 235–238 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L235-L238)
- **Module/theme:** search

## Signature

```php
function search_is_active()
```

## Documentation

```text
Determines access for the ?q=search path.
```

## Code

```php
function search_is_active() {
  // This path cannot be accessed if there are no active modules.
  return user_access('search content') && search_get_info();
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
