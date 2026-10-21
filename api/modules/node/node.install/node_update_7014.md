# node_update_7014()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 933–935 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L933-L935)
- **Module/theme:** node
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function node_update_7014()
```

## Documentation

```text
Add an index on {node}.language.
```

## Code

```php
function node_update_7014() {
  db_add_index('node', 'language', array('language'));
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
