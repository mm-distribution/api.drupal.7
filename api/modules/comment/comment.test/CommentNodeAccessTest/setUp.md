# CommentNodeAccessTest::setUp()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1512–1520 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1512-L1520)
- **Class:** [CommentNodeAccessTest](../CommentNodeAccessTest.md)
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
    parent::setUp('search', 'node_access_test');
    node_access_rebuild();

    // Create users and test node.
    $this->admin_user = $this->drupalCreateUser(array('administer content types', 'administer comments', 'administer blocks'));
    $this->web_user = $this->drupalCreateUser(array('access comments', 'post comments', 'create article content', 'edit own comments', 'node test view'));
    $this->node = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1, 'uid' => $this->web_user->uid));
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
