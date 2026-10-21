# trigger_comment_update()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 390–392 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L390-L392)
- **Module/theme:** trigger
- **Implements:** [hook_comment_update()](../../comment/comment.api.php/hook_comment_update.md)

## Signature

```php
function trigger_comment_update($comment)
```

## Documentation

```text
Implements hook_comment_update().
```

## Code

```php
function trigger_comment_update($comment) {
  _trigger_comment($comment, 'comment_update');
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
