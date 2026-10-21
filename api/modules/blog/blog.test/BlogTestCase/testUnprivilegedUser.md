# BlogTestCase::testUnprivilegedUser()

- **Type:** Method
- **File:** [`modules/blog/blog.test`](../_file.md), lines 37–47 · [local source](../../../../../source/modules/blog/blog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test#L37-L47)
- **Class:** [BlogTestCase](../BlogTestCase.md)
- **Module/theme:** blog

## Signature

```php
function testUnprivilegedUser()
```

## Documentation

```text
Confirm that the "You are not allowed to post a new blog entry." message
shows up if a user submitted blog entries, has been denied that
permission, and goes to the blog page.
```

## Code

```php
  function testUnprivilegedUser() {
    // Create a blog node for a user with no blog permissions.
    $this->drupalCreateNode(array('type' => 'blog', 'uid' => $this->big_user->uid));

    $this->drupalLogin($this->big_user);

    $this->drupalGet('blog/' . $this->big_user->uid);
    $this->assertResponse(200);
    $this->assertTitle(t("@name's blog", array('@name' => format_username($this->big_user))) . ' | Drupal', 'Blog title was displayed');
    $this->assertText(t('You are not allowed to post a new blog entry.'), 'No new entries can be posted without the right permission');
  }
```

---
_Drupal 7.103 · [modules/blog/blog.test](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
