# _forum_node_check_node_type()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 255–260 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L255-L260)
- **Module/theme:** forum

## Signature

```php
function _forum_node_check_node_type($node)
```

## Documentation

```text
Checks whether a node can be used in a forum, based on its content type.

@param $node
  A node object.

@return
  Boolean indicating if the node can be assigned to a forum.
```

## Code

```php
function _forum_node_check_node_type($node) {
  // Fetch information about the forum field.
  $field = field_info_instance('node', 'taxonomy_forums', $node->type);

  return is_array($field);
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
