# _node_access_rebuild_batch_finished()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3728–3737 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3728-L3737)
- **Module/theme:** node
- **Topics:** [node_access](../../../topics/node_access.md)

## Signature

```php
function _node_access_rebuild_batch_finished($success, $results, $operations)
```

## Documentation

```text
Implements callback_batch_finished().

Performs post-processing for node_access_rebuild().

@param bool $success
  A boolean indicating whether the re-build process has completed.
@param array $results
  An array of results information.
@param array $operations
  An array of function calls (not used in this function).
```

## Code

```php
function _node_access_rebuild_batch_finished($success, $results, $operations) {
  if ($success) {
    drupal_set_message(t('The content access permissions have been rebuilt.'));
    node_access_needs_rebuild(FALSE);
  }
  else {
    drupal_set_message(t('The content access permissions have not been properly rebuilt.'), 'error');
  }
  cache_clear_all();
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
