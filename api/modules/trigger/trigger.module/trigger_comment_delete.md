# trigger_comment_delete()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 397–399 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L397-L399)
- **Module/theme:** trigger
- **Implements:** [hook_comment_delete()](../../comment/comment.api.php/hook_comment_delete.md)

## Signature

```php
function trigger_comment_delete($comment)
```

## Documentation

```text
Implements hook_comment_delete().
```

## Code

```php
function trigger_comment_delete($comment) {
  _trigger_comment($comment, 'comment_delete');
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
