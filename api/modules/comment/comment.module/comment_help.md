# comment_help()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 75–89 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L75-L89)
- **Module/theme:** comment
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function comment_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function comment_help($path, $arg) {
  switch ($path) {
    case 'admin/help#comment':
      $output = '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Comment module allows users to comment on site content, set commenting defaults and permissions, and moderate comments. For more information, see the online handbook entry for <a href="@comment">Comment module</a>.', array('@comment' => 'http://drupal.org/documentation/modules/comment/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Default and custom settings') . '</dt>';
      $output .= '<dd>' . t("Each <a href='@content-type'>content type</a> can have its own default comment settings configured as: <em>Open</em> to allow new comments, <em>Hidden</em> to hide existing comments and prevent new comments, or <em>Closed</em> to view existing comments, but prevent new comments. These defaults will apply to all new content created (changes to the settings on existing content must be done manually). Other comment settings can also be customized per content type, and can be overridden for any given item of content. When a comment has no replies, it remains editable by its author, as long as the author has a user account and is logged in.", array('@content-type' => url('admin/structure/types'))) . '</dd>';
      $output .= '<dt>' . t('Comment approval') . '</dt>';
      $output .= '<dd>' . t("Comments from users who have the <em>Skip comment approval</em> permission are published immediately. All other comments are placed in the <a href='@comment-approval'>Unapproved comments</a> queue, until a user who has permission to <em>Administer comments</em> publishes or deletes them. Published comments can be bulk managed on the <a href='@admin-comment'>Published comments</a> administration page.", array('@comment-approval' => url('admin/content/comment/approval'), '@admin-comment' => url('admin/content/comment'))) . '</dd>';
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
