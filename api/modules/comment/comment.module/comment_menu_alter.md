# comment_menu_alter()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 296–306 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L296-L306)
- **Module/theme:** comment
- **Implements:** [hook_menu_alter()](../../system/system.api.php/hook_menu_alter.md)

## Signature

```php
function comment_menu_alter(&$items)
```

## Documentation

```text
Implements hook_menu_alter().
```

## Code

```php
function comment_menu_alter(&$items) {
  // Add comments to the description for admin/content.
  $items['admin/content']['description'] = 'Administer content and comments.';

  // Adjust the Field UI tabs on admin/structure/types/manage/[node-type].
  // See comment_entity_info().
  $items['admin/structure/types/manage/%comment_node_type/comment/fields']['title'] = 'Comment fields';
  $items['admin/structure/types/manage/%comment_node_type/comment/fields']['weight'] = 3;
  $items['admin/structure/types/manage/%comment_node_type/comment/display']['title'] = 'Comment display';
  $items['admin/structure/types/manage/%comment_node_type/comment/display']['weight'] = 4;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
