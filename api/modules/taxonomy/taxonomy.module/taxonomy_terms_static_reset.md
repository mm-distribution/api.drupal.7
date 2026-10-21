# taxonomy_terms_static_reset()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 958–967 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L958-L967)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_terms_static_reset()
```

## Documentation

```text
Clear all static cache variables for terms.
```

## Code

```php
function taxonomy_terms_static_reset() {
  drupal_static_reset('taxonomy_term_count_nodes');
  drupal_static_reset('taxonomy_get_tree');
  drupal_static_reset('taxonomy_get_tree:parents');
  drupal_static_reset('taxonomy_get_tree:terms');
  drupal_static_reset('taxonomy_get_parents');
  drupal_static_reset('taxonomy_get_parents_all');
  drupal_static_reset('taxonomy_get_children');
  entity_get_controller('taxonomy_term')->resetCache();
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
