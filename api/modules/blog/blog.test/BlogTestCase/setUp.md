# BlogTestCase::setUp()

- **Type:** Method
- **File:** [`modules/blog/blog.test`](../_file.md), lines 24–30 · [local source](../../../../../source/modules/blog/blog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test#L24-L30)
- **Class:** [BlogTestCase](../BlogTestCase.md)
- **Module/theme:** blog

## Signature

```php
function setUp()
```

## Documentation

```text
Enable modules and create users with specific permissions.
```

## Code

```php
  function setUp() {
    parent::setUp('blog');
    // Create users.
    $this->big_user = $this->drupalCreateUser(array('administer blocks'));
    $this->own_user = $this->drupalCreateUser(array('create blog content', 'edit own blog content', 'delete own blog content'));
    $this->any_user = $this->drupalCreateUser(array('create blog content', 'edit any blog content', 'delete any blog content', 'access administration pages'));
  }
```

---
_Drupal 7.103 · [modules/blog/blog.test](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
