# blog_feed_last()

- **Type:** Function
- **File:** [`modules/blog/blog.pages.inc`](_file.md), lines 112–127 · [local source](../../../../source/modules/blog/blog.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.pages.inc#L112-L127)
- **Module/theme:** blog

## Signature

```php
function blog_feed_last()
```

## Documentation

```text
Menu callback; displays an RSS feed containing recent blog entries of all users.
```

## Code

```php
function blog_feed_last() {
  $nids = db_select('node', 'n')
    ->fields('n', array('nid', 'created'))
    ->condition('type', 'blog')
    ->condition('status', 1)
    ->orderBy('created', 'DESC')
    ->range(0, variable_get('feed_default_items', 10))
    ->addTag('node_access')
    ->execute()
    ->fetchCol();

  $channel['title'] = t('!site_name blogs', array('!site_name' => variable_get('site_name', 'Drupal')));
  $channel['link'] = url('blog', array('absolute' => TRUE));

  node_feed($nids, $channel);
}
```

---
_Drupal 7.103 · [modules/blog/blog.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
