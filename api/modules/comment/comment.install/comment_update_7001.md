# comment_update_7001()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 141–157 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L141-L157)
- **Module/theme:** comment
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function comment_update_7001()
```

## Documentation

```text
Change comment status from published being 0 to being 1
```

## Code

```php
function comment_update_7001() {
  // Choose a temporary status value different from the existing status values.
  $tmp_status = db_query('SELECT MAX(status) FROM {comments}')->fetchField() + 1;

  $changes = array(
    0 => $tmp_status,
    1 => 0,
    $tmp_status => 1,
  );

  foreach ($changes as $old => $new) {
    db_update('comments')
      ->fields(array('status' => $new))
      ->condition('status', $old)
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
