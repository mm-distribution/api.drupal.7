# taxonomy_term_edit_access()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 375–377 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L375-L377)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_term_edit_access($term)
```

## Documentation

```text
Return edit access for a given term.
```

## Code

```php
function taxonomy_term_edit_access($term) {
  return user_access("edit terms in $term->vid") || user_access('administer taxonomy');
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
