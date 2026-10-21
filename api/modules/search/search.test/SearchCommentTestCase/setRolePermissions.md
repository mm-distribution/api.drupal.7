# SearchCommentTestCase::setRolePermissions()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 917–923 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L917-L923)
- **Class:** [SearchCommentTestCase](../SearchCommentTestCase.md)
- **Module/theme:** search

## Signature

```php
function setRolePermissions($rid, $access_comments = FALSE, $search_content = TRUE)
```

## Documentation

```text
Set permissions for role.
```

## Code

```php
  function setRolePermissions($rid, $access_comments = FALSE, $search_content = TRUE) {
    $permissions = array(
      'access comments' => $access_comments,
      'search content' => $search_content,
    );
    user_role_change_permissions($rid, $permissions);
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
