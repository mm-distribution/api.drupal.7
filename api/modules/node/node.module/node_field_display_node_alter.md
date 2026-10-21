# node_field_display_node_alter()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 239–244 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L239-L244)
- **Module/theme:** node
- **Implements:** [hook_field_display_ENTITY_TYPE_alter()](../../field/field.api.php/hook_field_display_ENTITY_TYPE_alter.md)

## Signature

```php
function node_field_display_node_alter(&$display, $context)
```

## Documentation

```text
Implements hook_field_display_ENTITY_TYPE_alter().
```

## Code

```php
function node_field_display_node_alter(&$display, $context) {
  // Hide field labels in search index.
  if ($context['view_mode'] == 'search_index') {
    $display['label'] = 'hidden';
  }
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
