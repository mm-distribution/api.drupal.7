# node_update_7009()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 809–814 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L809-L814)
- **Module/theme:** node
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function node_update_7009()
```

## Documentation

```text
Convert node languages from the empty string to LANGUAGE_NONE.
```

## Code

```php
function node_update_7009() {
  db_update('node')
    ->fields(array('language' => LANGUAGE_NONE))
    ->condition('language', '')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
