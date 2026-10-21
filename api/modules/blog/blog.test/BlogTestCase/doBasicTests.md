# BlogTestCase::doBasicTests()

- **Type:** Method
- **File:** [`modules/blog/blog.test`](../_file.md), lines 103–114 · [local source](../../../../../source/modules/blog/blog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test#L103-L114)
- **Class:** [BlogTestCase](../BlogTestCase.md)
- **Module/theme:** blog

## Signature

```php
private function doBasicTests($user, $admin)
```

## Documentation

```text
Run basic tests on the indicated user.

@param object $user
  The logged in user.
@param boolean $admin
  User has 'access administration pages' privilege.
```

## Code

```php
  private function doBasicTests($user, $admin) {
    // Login the user.
    $this->drupalLogin($user);
    // Create blog node.
    $node = $this->drupalCreateNode(array('type' => 'blog'));
    // Verify the user has access to all the blog nodes.
    $this->verifyBlogs($user, $node, $admin);
    // Create one more node to test the blog page with more than one node
    $this->drupalCreateNode(array('type' => 'blog', 'uid' => $user->uid));
    // Verify the blog links are displayed.
    $this->verifyBlogLinks($user);
  }
```

---
_Drupal 7.103 · [modules/blog/blog.test](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
