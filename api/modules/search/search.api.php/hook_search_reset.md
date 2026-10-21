# hook_search_reset()

- **Type:** Hook (documentation function)
- **File:** [`modules/search/search.api.php`](_file.md), lines 73–78 · [local source](../../../../source/modules/search/search.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php#L73-L78)
- **Module/theme:** search
- **Topics:** [hooks](../../../topics/hooks.md), [search](../../../topics/search.md)

## Signature

```php
function hook_search_reset()
```

## Documentation

```text
Take action when the search index is going to be rebuilt.

Modules that use hook_update_index() should update their indexing
bookkeeping so that it starts from scratch the next time
hook_update_index() is called.

@ingroup search
```

## Code

```php
function hook_search_reset() {
  db_update('search_dataset')
    ->fields(array('reindex' => REQUEST_TIME))
    ->condition('type', 'node')
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_search_reset()".

- [node_search_reset()](../../node/node.module/node_search_reset.md) — `modules/node/node.module`

---
_Drupal 7.103 · [modules/search/search.api.php](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
