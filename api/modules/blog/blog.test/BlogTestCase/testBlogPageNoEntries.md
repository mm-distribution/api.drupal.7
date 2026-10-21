# BlogTestCase::testBlogPageNoEntries()

- **Type:** Method
- **File:** [`modules/blog/blog.test`](../_file.md), lines 52–59 · [local source](../../../../../source/modules/blog/blog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test#L52-L59)
- **Class:** [BlogTestCase](../BlogTestCase.md)
- **Module/theme:** blog

## Signature

```php
function testBlogPageNoEntries()
```

## Documentation

```text
View the blog of a user with no blog entries as another user.
```

## Code

```php
  function testBlogPageNoEntries() {
    $this->drupalLogin($this->big_user);

    $this->drupalGet('blog/' . $this->own_user->uid);
    $this->assertResponse(200);
    $this->assertTitle(t("@name's blog", array('@name' => format_username($this->own_user))) . ' | Drupal', 'Blog title was displayed');
    $this->assertText(t('@author has not created any blog entries.', array('@author' => format_username($this->own_user))), 'Users blog displayed with no entries');
  }
```

---
_Drupal 7.103 · [modules/blog/blog.test](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
