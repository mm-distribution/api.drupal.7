# node_update_7015()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 940–945 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L940-L945)
- **Module/theme:** node
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function node_update_7015()
```

## Documentation

```text
Enable node types that may have been erroneously disabled in Drupal 7.36.
```

## Code

```php
function node_update_7015() {
  db_update('node_type')
    ->fields(array('disabled' => 0))
    ->condition('base', 'node_content')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
