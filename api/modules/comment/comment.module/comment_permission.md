# comment_permission()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 398–416 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L398-L416)
- **Module/theme:** comment
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function comment_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function comment_permission() {
  return array(
    'administer comments' => array(
      'title' => t('Administer comments and comment settings'),
    ),
    'access comments' => array(
      'title' => t('View comments'),
    ),
    'post comments' => array(
      'title' => t('Post comments'),
    ),
    'skip comment approval' => array(
      'title' => t('Skip comment approval'),
    ),
    'edit own comments' => array(
      'title' => t('Edit own comments'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
