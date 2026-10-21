# BlogTestCase::verifyBlogs()

- **Type:** Method
- **File:** [`modules/blog/blog.test`](../_file.md), lines 128–176 · [local source](../../../../../source/modules/blog/blog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test#L128-L176)
- **Class:** [BlogTestCase](../BlogTestCase.md)
- **Module/theme:** blog

## Signature

```php
private function verifyBlogs($node_user, $node, $admin, $response = 200)
```

## Documentation

```text
Verify the logged in user has the desired access to the various blog nodes.

@param object $node_user
  The user who creates the node.
@param object $node
  A node object.
@param boolean $admin
  User has 'access administration pages' privilege.
@param integer $response
  HTTP response code.
```

## Code

```php
  private function verifyBlogs($node_user, $node, $admin, $response = 200) {
    $response2 = ($admin) ? 200 : 403;

    // View blog help node.
    $this->drupalGet('admin/help/blog');
    $this->assertResponse($response2);
    if ($response2 == 200) {
      $this->assertTitle(t('Blog | Drupal'), 'Blog help node was displayed');
      $this->assertText(t('Blog'), 'Blog help node was displayed');
    }

    // Verify the blog block was displayed.
    $this->drupalGet('');
    $this->assertResponse(200);
    $this->assertText(t('Recent blog posts'), 'Blog block was displayed');

    // View blog node.
    $this->drupalGet('node/' . $node->nid);
    $this->assertResponse(200);
    $this->assertTitle($node->title . ' | Drupal', 'Blog node was displayed');
    $breadcrumb = array(
      l(t('Home'), NULL),
      l(t('Blogs'), 'blog'),
      l(t("!name's blog", array('!name' => format_username($node_user))), 'blog/' . $node_user->uid),
    );
    $this->assertRaw(theme('breadcrumb', array('breadcrumb' => $breadcrumb)), 'Breadcrumbs were displayed');

    // View blog edit node.
    $this->drupalGet('node/' . $node->nid . '/edit');
    $this->assertResponse($response);
    if ($response == 200) {
      $this->assertTitle('Edit Blog entry ' . $node->title . ' | Drupal', 'Blog edit node was displayed');
    }

    if ($response == 200) {
      // Edit blog node.
      $edit = array();
      $langcode = LANGUAGE_NONE;
      $edit["title"] = 'node/' . $node->nid;
      $edit["body[$langcode][0][value]"] = $this->randomName(256);
      $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
      $this->assertRaw(t('Blog entry %title has been updated.', array('%title' => $edit["title"])), 'Blog node was edited');

      // Delete blog node.
      $this->drupalPost('node/' . $node->nid . '/delete', array(), t('Delete'));
      $this->assertResponse($response);
      $this->assertRaw(t('Blog entry %title has been deleted.', array('%title' => $edit["title"])), 'Blog node was deleted');
    }
  }
```

---
_Drupal 7.103 · [modules/blog/blog.test](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
