# node_update_7004()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 573–589 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L573-L589)
- **Module/theme:** node
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function node_update_7004()
```

## Documentation

```text
Extend the existing default preview and teaser settings to all node types.
```

## Code

```php
function node_update_7004() {
  // Get original settings and all types.
  $original_length = variable_get('teaser_length', 600);
  $original_preview = variable_get('node_preview', 0);

  // Map old preview setting to new values order.
  $original_preview ? $original_preview = 2 : $original_preview = 1;
  node_type_cache_reset();

  // Apply original settings to all types.
  foreach (_update_7000_node_get_types() as $type => $type_object) {
    variable_set('teaser_length_' . $type, $original_length);
    variable_set('node_preview_' . $type, $original_preview);
  }
  // Delete old variable but leave 'teaser_length' for aggregator module upgrade.
  variable_del('node_preview');
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
