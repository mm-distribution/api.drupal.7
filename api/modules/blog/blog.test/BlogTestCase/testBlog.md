# BlogTestCase::testBlog()

- **Type:** Method
- **File:** [`modules/blog/blog.test`](../_file.md), lines 64–93 · [local source](../../../../../source/modules/blog/blog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test#L64-L93)
- **Class:** [BlogTestCase](../BlogTestCase.md)
- **Module/theme:** blog

## Signature

```php
function testBlog()
```

## Documentation

```text
Login users, create blog nodes, and test blog functionality through the admin and user interfaces.
```

## Code

```php
  function testBlog() {
    // Login the admin user.
    $this->drupalLogin($this->big_user);
    // Enable the recent blog block.
    $edit = array();
    $edit['blocks[blog_recent][region]'] = 'sidebar_second';
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));
    $this->assertResponse(200);
    // Verify ability to change number of recent blog posts in block.
    $edit = array();
    $edit['blog_block_count'] = 5;
    $this->drupalPost('admin/structure/block/manage/blog/recent/configure', $edit, t('Save block'));
    $this->assertEqual(variable_get('blog_block_count', 10), 5, 'Number of recent blog posts changed.');

    // Do basic tests for each user.
    $this->doBasicTests($this->any_user, TRUE);
    $this->doBasicTests($this->own_user, FALSE);

    // Create another blog node for the any blog user.
    $node = $this->drupalCreateNode(array('type' => 'blog', 'uid' => $this->any_user->uid));
    // Verify the own blog user only has access to the blog view node.
    $this->verifyBlogs($this->any_user, $node, FALSE, 403);

    // Create another blog node for the own blog user.
    $node = $this->drupalCreateNode(array('type' => 'blog', 'uid' => $this->own_user->uid));
    // Login the any blog user.
    $this->drupalLogin($this->any_user);
    // Verify the any blog user has access to all the blog nodes.
    $this->verifyBlogs($this->own_user, $node, TRUE);
  }
```

---
_Drupal 7.103 · [modules/blog/blog.test](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
