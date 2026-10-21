# CommentHelperCase::setUp()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 14–27 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L14-L27)
- **Class:** [CommentHelperCase](../CommentHelperCase.md)
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
    $modules = func_get_args();
    if (isset($modules[0]) && is_array($modules[0])) {
      $modules = $modules[0];
    }
    $modules[] = 'comment';
    parent::setUp($modules);

    // Create users and test node.
    $this->super_user = $this->drupalCreateUser(array('access administration pages', 'administer modules'));
    $this->admin_user = $this->drupalCreateUser(array('administer content types', 'administer comments', 'administer blocks', 'administer actions', 'administer fields'));
    $this->web_user = $this->drupalCreateUser(array('access comments', 'post comments', 'create article content', 'edit own comments'));
    $this->node = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1, 'uid' => $this->web_user->uid));
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
