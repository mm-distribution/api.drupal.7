# trigger_comment_presave()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 376–378 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L376-L378)
- **Module/theme:** trigger
- **Implements:** [hook_comment_presave()](../../comment/comment.api.php/hook_comment_presave.md)

## Signature

```php
function trigger_comment_presave($comment)
```

## Documentation

```text
Implements hook_comment_presave().
```

## Code

```php
function trigger_comment_presave($comment) {
  _trigger_comment($comment, 'comment_presave');
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
