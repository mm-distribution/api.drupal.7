# template_preprocess_forum_icon()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 1239–1259 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L1239-L1259)
- **Module/theme:** forum

## Signature

```php
function template_preprocess_forum_icon(&$variables)
```

## Documentation

```text
Preprocesses variables for forum-icon.tpl.php.

@param $variables
  An array containing the following elements:
  - new_posts: Indicates whether or not the topic contains new posts.
  - num_posts: The total number of posts in all topics.
  - comment_mode: An integer indicating whether comments are open, closed,
    or hidden.
  - sticky: Indicates whether the topic is sticky.
  - first_new: Indicates whether this is the first topic with new posts.

@see forum-icon.tpl.php
@see theme_forum_icon()
```

## Code

```php
function template_preprocess_forum_icon(&$variables) {
  $variables['hot_threshold'] = variable_get('forum_hot_topic', 15);
  if ($variables['num_posts'] > $variables['hot_threshold']) {
    $variables['icon_class'] = $variables['new_posts'] ? 'hot-new' : 'hot';
    $variables['icon_title'] = $variables['new_posts'] ? t('Hot topic, new comments') : t('Hot topic');
  }
  else {
    $variables['icon_class'] = $variables['new_posts'] ? 'new' : 'default';
    $variables['icon_title'] = $variables['new_posts'] ? t('New comments') : t('Normal topic');
  }

  if ($variables['comment_mode'] == COMMENT_NODE_CLOSED || $variables['comment_mode'] == COMMENT_NODE_HIDDEN) {
    $variables['icon_class'] = 'closed';
    $variables['icon_title'] = t('Closed topic');
  }

  if ($variables['sticky'] == 1) {
    $variables['icon_class'] = 'sticky';
    $variables['icon_title'] = t('Sticky topic');
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
