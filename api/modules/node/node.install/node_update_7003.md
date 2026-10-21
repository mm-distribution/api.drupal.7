# node_update_7003()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 564–568 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L564-L568)
- **Module/theme:** node
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function node_update_7003()
```

## Documentation

```text
Remove the node_counter if the statistics module is uninstalled.
```

## Code

```php
function node_update_7003() {
  if (drupal_get_installed_schema_version('statistics') == SCHEMA_UNINSTALLED) {
    db_drop_table('node_counter');
  }
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
