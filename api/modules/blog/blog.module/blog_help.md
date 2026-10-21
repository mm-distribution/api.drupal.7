# blog_help()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 39–57 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L39-L57)
- **Module/theme:** blog
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function blog_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function blog_help($path, $arg) {
  switch ($path) {
    case 'admin/help#blog':
      $output = '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t("The Blog module allows registered users to maintain an online journal, or <em>blog</em>. Blogs are made up of individual <em>blog entries</em>. By default, the blog entries are displayed by creation time in descending order, with comments enabled, and are promoted to the site's front page. For more information, see the online handbook entry for <a href='@blog'>Blog module</a>.", array('@blog' => 'http://drupal.org/documentation/modules/blog/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Single-user blogs') . '</dt>';
      $output .= '<dd>' . t("Each user's blog entries are automatically displayed with a link to the user's main blog page. You can create as many single-user blogs as you have site users with permission to create blog content.") . '</dd>';
      $output .= '<dt>' . t('Multi-user blogs') . '</dt>';
      $output .= '<dd>' . t("Blog entries from each single-user blog are also aggregated into one central multi-user blog, which displays the blog content of all users in a single listing.") . '</dd>';
      $output .= '<dt>' . t('Navigation') . '</dt>';
      $output .= '<dd>' . t("There is an optional <em>Blogs</em> menu item added to the Navigation menu, which displays all blogs available on your site, and a <em>My blog</em> item displaying the current user's blog entries.") . '</dd>';
      $output .= '<dt>' . t('Blocks') . '</dt>';
      $output .= '<dd>' . t('The Blog module also creates a default <em>Recent blog posts</em> block that may be enabled at the <a href="@blocks">blocks administration page</a>.', array('@blocks' => url('admin/structure/block'))) . '</dd>';
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
