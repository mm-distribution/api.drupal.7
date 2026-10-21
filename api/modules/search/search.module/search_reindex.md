# search_reindex()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 310–331 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L310-L331)
- **Module/theme:** search

## Signature

```php
function search_reindex($sid = NULL, $module = NULL, $reindex = FALSE)
```

## Documentation

```text
Clears a part of or the entire search index.

@param $sid
  (optional) The ID of the item to remove from the search index. If
  specified, $module must also be given. Omit both $sid and $module to clear
  the entire search index.
@param $module
  (optional) The machine-readable name of the module for the item to remove
  from the search index.
```

## Code

```php
function search_reindex($sid = NULL, $module = NULL, $reindex = FALSE) {
  if ($module == NULL && $sid == NULL) {
    module_invoke_all('search_reset');
  }
  else {
    db_delete('search_dataset')
      ->condition('sid', $sid)
      ->condition('type', $module)
      ->execute();
    db_delete('search_index')
      ->condition('sid', $sid)
      ->condition('type', $module)
      ->execute();
    // Don't remove links if re-indexing.
    if (!$reindex) {
      db_delete('search_node_links')
        ->condition('sid', $sid)
        ->condition('type', $module)
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
