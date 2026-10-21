# trigger_comment_insert()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 383–385 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L383-L385)
- **Module/theme:** trigger
- **Implements:** [hook_comment_insert()](../../comment/comment.api.php/hook_comment_insert.md)

## Signature

```php
function trigger_comment_insert($comment)
```

## Documentation

```text
Implements hook_comment_insert().
```

## Code

```php
function trigger_comment_insert($comment) {
  _trigger_comment($comment, 'comment_insert');
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
