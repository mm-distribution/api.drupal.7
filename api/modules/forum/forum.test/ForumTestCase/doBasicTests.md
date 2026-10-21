# ForumTestCase::doBasicTests()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 470–479 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L470-L479)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

## Signature

```php
private function doBasicTests($user, $admin)
```

## Documentation

```text
Runs basic tests on the indicated user.

@param $user
  The logged in user.
@param $admin
  User has 'access administration pages' privilege.
```

## Code

```php
  private function doBasicTests($user, $admin) {
    // Login the user.
    $this->drupalLogin($user);
    // Attempt to create forum topic under a container.
    $this->createForumTopic($this->container, TRUE);
    // Create forum node.
    $node = $this->createForumTopic($this->forum, FALSE);
    // Verify the user has access to all the forum nodes.
    $this->verifyForums($user, $node, $admin);
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
