# SearchCommentTestCase

- **Type:** Class
- **File:** [`modules/search/search.test`](_file.md), lines 754–980 · [local source](../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L754-L980)
- **Module/theme:** search

## Signature

```php
class SearchCommentTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test integration searching comments.
```

## Properties

### $admin_user

```php
protected $admin_user;
```

### $comment_subject

```php
protected $comment_subject;
```

### $admin_role

```php
protected $admin_role;
```

### $node

```php
protected $node;
```

## Methods (derived index)

- [getInfo()](SearchCommentTestCase/getInfo.md)
- [setUp()](SearchCommentTestCase/setUp.md)
- [testSearchResultsComment()](SearchCommentTestCase/testSearchResultsComment.md) — Verify that comments are rendered using proper format in search results.
- [testSearchResultsCommentAccess()](SearchCommentTestCase/testSearchResultsCommentAccess.md) — Verify access rules for comment indexing with different permissions.
- [setRolePermissions()](SearchCommentTestCase/setRolePermissions.md) — Set permissions for role.
- [checkCommentAccess()](SearchCommentTestCase/checkCommentAccess.md) — Update search index and search for comment.
- [testAddNewComment()](SearchCommentTestCase/testAddNewComment.md) — Verify that 'add new comment' does not appear in search results or index.

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
