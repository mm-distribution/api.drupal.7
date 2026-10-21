# blog_menu()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 101–135 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L101-L135)
- **Module/theme:** blog
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function blog_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function blog_menu() {
  $items['blog'] = array(
    'title' => 'Blogs',
    'page callback' => 'blog_page_last',
    'access arguments' => array('access content'),
    'type' => MENU_SUGGESTED_ITEM,
    'file' => 'blog.pages.inc',
  );
  $items['blog/%user_uid_optional'] = array(
    'title' => 'My blog',
    'page callback' => 'blog_page_user',
    'page arguments' => array(1),
    'access callback' => 'blog_page_user_access',
    'access arguments' => array(1),
    'file' => 'blog.pages.inc',
  );
  $items['blog/%user/feed'] = array(
    'title' => 'Blogs',
    'page callback' => 'blog_feed_user',
    'page arguments' => array(1),
    'access callback' => 'blog_page_user_access',
    'access arguments' => array(1),
    'type' => MENU_CALLBACK,
    'file' => 'blog.pages.inc',
  );
  $items['blog/feed'] = array(
    'title' => 'Blogs',
    'page callback' => 'blog_feed_last',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
    'file' => 'blog.pages.inc',
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
