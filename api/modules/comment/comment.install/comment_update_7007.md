# comment_update_7007()

- **Type:** Function
- **File:** [`modules/comment/comment.install`](_file.md), lines 356–358 · [local source](../../../../source/modules/comment/comment.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install#L356-L358)
- **Module/theme:** comment
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function comment_update_7007()
```

## Documentation

```text
Add an index to the created column.
```

## Code

```php
function comment_update_7007() {
  db_add_index('comment', 'comment_created', array('created'));
}
```

---
_Drupal 7.103 · [modules/comment/comment.install](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.install) · Licensed GPL-2.0-or-later (see LICENSE)._
