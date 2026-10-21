# path_taxonomy_term_update()

- **Type:** Function
- **File:** [`modules/path/path.module`](_file.md), lines 287–306 · [local source](../../../../source/modules/path/path.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module#L287-L306)
- **Module/theme:** path
- **Implements:** [hook_taxonomy_term_update()](../../taxonomy/taxonomy.api.php/hook_taxonomy_term_update.md)

## Signature

```php
function path_taxonomy_term_update($term)
```

## Documentation

```text
Implements hook_taxonomy_term_update().
```

## Code

```php
function path_taxonomy_term_update($term) {
  if (isset($term->path)) {
    $path = $term->path;
    $path['alias'] = trim($path['alias']);
    // Delete old alias if user erased it.
    if (!empty($path['pid']) && empty($path['alias'])) {
      path_delete($path['pid']);
    }
    // Only save a non-empty alias.
    if (!empty($path['alias'])) {
      // Ensure fields for programmatic executions.
      $path['source'] = 'taxonomy/term/' . $term->tid;
      // Core does not provide a way to store the term language but contrib
      // modules can do it so we need to take this into account.
      $langcode = entity_language('taxonomy_term', $term);
      $path['language'] = !empty($langcode) ? $langcode : LANGUAGE_NONE;
      path_save($path);
    }
  }
}
```

---
_Drupal 7.103 · [modules/path/path.module](https://github.com/drupal/drupal/blob/7.103/modules/path/path.module) · Licensed GPL-2.0-or-later (see LICENSE)._
