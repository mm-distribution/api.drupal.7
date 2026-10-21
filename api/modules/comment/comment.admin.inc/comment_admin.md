# comment_admin()

- **Type:** Function
- **File:** [`modules/comment/comment.admin.inc`](_file.md), lines 11–20 · [local source](../../../../source/modules/comment/comment.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc#L11-L20)
- **Module/theme:** comment

## Signature

```php
function comment_admin($type = 'new')
```

## Documentation

```text
Menu callback; present an administrative comment listing.
```

## Code

```php
function comment_admin($type = 'new') {
  $edit = $_POST;

  if (isset($edit['operation']) && ($edit['operation'] == 'delete') && isset($edit['comments']) && $edit['comments']) {
    return drupal_get_form('comment_multiple_delete_confirm');
  }
  else {
    return drupal_get_form('comment_admin_overview', $type);
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
