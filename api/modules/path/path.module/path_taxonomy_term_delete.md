# path_taxonomy_term_delete()

- **Type:** Function
- **File:** [`modules/path/path.module`](_file.md), lines 311–314 · [local source](../../../../source/modules/path/path.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module#L311-L314)
- **Module/theme:** path
- **Implements:** [hook_taxonomy_term_delete()](../../taxonomy/taxonomy.api.php/hook_taxonomy_term_delete.md)

## Signature

```php
function path_taxonomy_term_delete($term)
```

## Documentation

```text
Implements hook_taxonomy_term_delete().
```

## Code

```php
function path_taxonomy_term_delete($term) {
  // Delete all aliases associated with this term.
  path_delete(array('source' => 'taxonomy/term/' . $term->tid));
}
```

---
_Drupal 7.103 · [modules/path/path.module](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module) · Licensed GPL-2.0-or-later (see LICENSE)._
