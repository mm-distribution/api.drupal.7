# BlogTestCase::verifyBlogLinks()

- **Type:** Method
- **File:** [`modules/blog/blog.test`](../_file.md), lines 184–212 · [local source](../../../../../source/modules/blog/blog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test#L184-L212)
- **Class:** [BlogTestCase](../BlogTestCase.md)
- **Module/theme:** blog

## Signature

```php
private function verifyBlogLinks($user)
```

## Documentation

```text
Verify the blog links are displayed to the logged in user.

@param object $user
  The logged in user.
```

## Code

```php
  private function verifyBlogLinks($user) {
    // Confirm blog entries link exists on the user page.
    $this->drupalGet('user/' . $user->uid);
    $this->assertResponse(200);
    $this->assertText(t('View recent blog entries'), 'View recent blog entries link was displayed');

    // Confirm the recent blog entries link goes to the user's blog page.
    $this->clickLink('View recent blog entries');
    $this->assertTitle(t("@name's blog | Drupal", array('@name' => format_username($user))), 'View recent blog entries link target was correct');

    // Confirm a blog page was displayed.
    $this->drupalGet('blog');
    $this->assertResponse(200);
    $this->assertTitle('Blogs | Drupal', 'Blog page was displayed');
    $this->assertText(t('Home'), 'Breadcrumbs were displayed');
    $this->assertLink(t('Create new blog entry'));

    // Confirm a blog page was displayed per user.
    $this->drupalGet('blog/' . $user->uid);
    $this->assertTitle(t("@name's blog | Drupal", array('@name' => format_username($user))), 'User blog node was displayed');

    // Confirm a blog feed was displayed.
    $this->drupalGet('blog/feed');
    $this->assertTitle(t('Drupal blogs'), 'Blog feed was displayed');

    // Confirm a blog feed was displayed per user.
    $this->drupalGet('blog/' . $user->uid . '/feed');
    $this->assertTitle(t("@name's blog", array('@name' => format_username($user))), 'User blog feed was displayed');
  }
```

---
_Drupal 7.103 · [modules/blog/blog.test](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
