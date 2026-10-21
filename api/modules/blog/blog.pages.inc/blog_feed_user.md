# blog_feed_user()

- **Type:** Function
- **File:** [`modules/blog/blog.pages.inc`](_file.md), lines 90–107 · [local source](../../../../source/modules/blog/blog.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.pages.inc#L90-L107)
- **Module/theme:** blog

## Signature

```php
function blog_feed_user($account)
```

## Documentation

```text
Menu callback; displays an RSS feed containing recent blog entries of a given user.
```

## Code

```php
function blog_feed_user($account) {

  $nids = db_select('node', 'n')
    ->fields('n', array('nid', 'created'))
    ->condition('type', 'blog')
    ->condition('uid', $account->uid)
    ->condition('status', 1)
    ->orderBy('created', 'DESC')
    ->range(0, variable_get('feed_default_items', 10))
    ->addTag('node_access')
    ->execute()
    ->fetchCol();

  $channel['title'] = t("!name's blog", array('!name' => format_username($account)));
  $channel['link'] = url('blog/' . $account->uid, array('absolute' => TRUE));

  node_feed($nids, $channel);
}
```

---
_Drupal 7.103 · [modules/blog/blog.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
