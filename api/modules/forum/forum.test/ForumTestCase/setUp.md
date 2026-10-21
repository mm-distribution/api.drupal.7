# ForumTestCase::setUp()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 66–90 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L66-L90)
- **Class:** [ForumTestCase](../ForumTestCase.md)
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
    // Create users.
    $this->admin_user = $this->drupalCreateUser(array(
      'access administration pages',
      'administer modules',
      'administer blocks',
      'administer forums',
      'administer menu',
      'administer taxonomy',
      'create forum content',
    ));
    $this->edit_any_topics_user = $this->drupalCreateUser(array(
      'access administration pages',
      'create forum content',
      'edit any forum content',
      'delete any forum content',
    ));
    $this->edit_own_topics_user = $this->drupalCreateUser(array(
      'create forum content',
      'edit own forum content',
      'delete own forum content',
    ));
    $this->web_user = $this->drupalCreateUser(array());
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
