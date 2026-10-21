# trigger_comment_view()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 404–406 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L404-L406)
- **Module/theme:** trigger
- **Implements:** [hook_comment_view()](../../comment/comment.api.php/hook_comment_view.md)

## Signature

```php
function trigger_comment_view($comment)
```

## Documentation

```text
Implements hook_comment_view().
```

## Code

```php
function trigger_comment_view($comment) {
  _trigger_comment($comment, 'comment_view');
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
