# _taxonomy_get_tid_from_term()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1407–1409 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1407-L1409)
- **Module/theme:** taxonomy

## Signature

```php
function _taxonomy_get_tid_from_term($term)
```

## Documentation

```text
Helper function for array_map purposes.
```

## Code

```php
function _taxonomy_get_tid_from_term($term) {
  return $term->tid;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
