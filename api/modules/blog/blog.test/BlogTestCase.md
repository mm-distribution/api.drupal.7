# BlogTestCase

- **Type:** Class
- **File:** [`modules/blog/blog.test`](_file.md), lines 8–213 · [local source](../../../../source/modules/blog/blog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test#L8-L213)
- **Module/theme:** blog

## Signature

```php
class BlogTestCase extends DrupalWebTestCase
```

## Documentation

_No docblock in source._

## Properties

### $big_user

```php
protected $big_user;
```

### $own_user

```php
protected $own_user;
```

### $any_user

```php
protected $any_user;
```

## Methods (derived index)

- [getInfo()](BlogTestCase/getInfo.md)
- [setUp()](BlogTestCase/setUp.md) — Enable modules and create users with specific permissions.
- [testUnprivilegedUser()](BlogTestCase/testUnprivilegedUser.md) — Confirm that the "You are not allowed to post a new blog entry." message shows up if a user submitted blog entries, has been denied that permission, and goes to the blog page.
- [testBlogPageNoEntries()](BlogTestCase/testBlogPageNoEntries.md) — View the blog of a user with no blog entries as another user.
- [testBlog()](BlogTestCase/testBlog.md) — Login users, create blog nodes, and test blog functionality through the admin and user interfaces.
- [doBasicTests()](BlogTestCase/doBasicTests.md) — Run basic tests on the indicated user.
- [verifyBlogs()](BlogTestCase/verifyBlogs.md) — Verify the logged in user has the desired access to the various blog nodes.
- [verifyBlogLinks()](BlogTestCase/verifyBlogLinks.md) — Verify the blog links are displayed to the logged in user.

---
_Drupal 7.103 · [modules/blog/blog.test](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
