# node_node_type_update()

- **Type:** Function
- **File:** [`modules/node/content_types.inc`](_file.md), lines 380–388 · [local source](../../../../source/modules/node/content_types.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc#L380-L388)
- **Module/theme:** node
- **Implements:** [hook_node_type_update()](../node.api.php/hook_node_type_update.md)

## Signature

```php
function node_node_type_update($info)
```

## Documentation

```text
Implements hook_node_type_update().
```

## Code

```php
function node_node_type_update($info) {
  if (!empty($info->old_type) && $info->old_type != $info->type) {
    $update_count = node_type_update_nodes($info->old_type, $info->type);

    if ($update_count) {
      drupal_set_message(format_plural($update_count, 'Changed the content type of 1 post from %old-type to %type.', 'Changed the content type of @count posts from %old-type to %type.', array('%old-type' => $info->old_type, '%type' => $info->type)));
    }
  }
}
```

---
_Drupal 7.103 · [modules/node/content_types.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
