# comment_count_unpublished()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 311–316 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L311-L316)
- **Module/theme:** comment

## Signature

```php
function comment_count_unpublished()
```

## Documentation

```text
Returns a menu title which includes the number of unapproved comments.
```

## Code

```php
function comment_count_unpublished() {
  $count = db_query('SELECT COUNT(cid) FROM {comment} WHERE status = :status', array(
    ':status' => COMMENT_NOT_PUBLISHED,
  ))->fetchField();
  return t('Unapproved comments (@count)', array('@count' => $count));
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
