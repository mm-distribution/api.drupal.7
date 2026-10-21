# CommentAnonymous::setUp()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1088–1091 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1088-L1091)
- **Class:** [CommentAnonymous](../CommentAnonymous.md)
- **Module/theme:** comment

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();
    variable_set('user_register', USER_REGISTER_VISITORS);
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
