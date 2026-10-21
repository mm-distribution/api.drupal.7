# taxonomy_taxonomy_term_delete()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 2022–2027 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L2022-L2027)
- **Module/theme:** taxonomy
- **Topics:** [taxonomy_index](../../../topics/taxonomy_index.md)
- **Implements:** [hook_taxonomy_term_delete()](../taxonomy.api.php/hook_taxonomy_term_delete.md)

## Signature

```php
function taxonomy_taxonomy_term_delete($term)
```

## Documentation

```text
Implements hook_taxonomy_term_delete().
```

## Code

```php
function taxonomy_taxonomy_term_delete($term) {
  if (variable_get('taxonomy_maintain_index_table', TRUE)) {
    // Clean up the {taxonomy_index} table when terms are deleted.
    db_delete('taxonomy_index')->condition('tid', $term->tid)->execute();
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
