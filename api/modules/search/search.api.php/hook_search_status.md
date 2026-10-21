# hook_search_status()

- **Type:** Hook (documentation function)
- **File:** [`modules/search/search.api.php`](_file.md), lines 94–98 · [local source](../../../../source/modules/search/search.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php#L94-L98)
- **Module/theme:** search
- **Topics:** [hooks](../../../topics/hooks.md), [search](../../../topics/search.md)

## Signature

```php
function hook_search_status()
```

## Documentation

```text
Report the status of indexing.

The core search module only invokes this hook on active modules.
Implementing modules do not need to check whether they are active when
calculating their return values.

@return
 An associative array with the key-value pairs:
 - 'remaining': The number of items left to index.
 - 'total': The total number of items to index.

@ingroup search
```

## Code

```php
function hook_search_status() {
  $total = db_query('SELECT COUNT(*) FROM {node} WHERE status = 1')->fetchField();
  $remaining = db_query("SELECT COUNT(*) FROM {node} n LEFT JOIN {search_dataset} d ON d.type = 'node' AND d.sid = n.nid WHERE n.status = 1 AND d.sid IS NULL OR d.reindex <> 0")->fetchField();
  return array('remaining' => $remaining, 'total' => $total);
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_search_status()".

- [node_search_status()](../../node/node.module/node_search_status.md) — `modules/node/node.module`

---
_Drupal 7.103 · [modules/search/search.api.php](https://github.com/drupal/drupal/blob/7.103/modules/search/search.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
