# _node_access_test_node_write()

- **Type:** Function
- **File:** [`modules/node/tests/node_access_test.module`](_file.md), lines 223–230 · [local source](../../../../../source/modules/node/tests/node_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module#L223-L230)
- **Module/theme:** node_test

## Signature

```php
function _node_access_test_node_write($node)
```

## Documentation

```text
Helper for node insert/update.
```

## Code

```php
function _node_access_test_node_write($node) {
  if (isset($node->private)) {
    db_merge('node_access_test')
      ->key(array('nid' => $node->nid))
      ->fields(array('private' => (int) $node->private))
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/node/tests/node_access_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
