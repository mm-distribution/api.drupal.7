# ForumIndexTestCase::setUp()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 684–690 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L684-L690)
- **Class:** [ForumIndexTestCase](../ForumIndexTestCase.md)
- **Module/theme:** forum

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('taxonomy', 'comment', 'forum');

    // Create a test user.
    $web_user = $this->drupalCreateUser(array('create forum content', 'edit own forum content', 'edit any forum content', 'administer nodes'));
    $this->drupalLogin($web_user);
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
