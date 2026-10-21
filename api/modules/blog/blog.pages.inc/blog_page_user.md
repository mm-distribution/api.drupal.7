# blog_page_user()

- **Type:** Function
- **File:** [`modules/blog/blog.pages.inc`](_file.md), lines 11–50 · [local source](../../../../source/modules/blog/blog.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.pages.inc#L11-L50)
- **Module/theme:** blog

## Signature

```php
function blog_page_user($account)
```

## Documentation

```text
Menu callback; displays a Drupal page containing recent blog entries of a given user.
```

## Code

```php
function blog_page_user($account) {
  global $user;

  drupal_set_title($title = t("@name's blog", array('@name' => format_username($account))), PASS_THROUGH);

  $build = array();

  $query = db_select('node', 'n')->extend('PagerDefault');
  $nids = $query
    ->fields('n', array('nid', 'sticky', 'created'))
    ->condition('type', 'blog')
    ->condition('uid', $account->uid)
    ->condition('status', 1)
    ->orderBy('sticky', 'DESC')
    ->orderBy('created', 'DESC')
    ->limit(variable_get('default_nodes_main', 10))
    ->addTag('node_access')
    ->execute()
    ->fetchCol();

  if (!empty($nids)) {
    $nodes = node_load_multiple($nids);
    $build += node_view_multiple($nodes);
    $build['pager'] = array(
      '#theme' => 'pager',
      '#weight' => 5,
    );
  }
  else {
    if ($account->uid == $user->uid) {
      drupal_set_message(t('You have not created any blog entries.'));
    }
    else {
      drupal_set_message(t('!author has not created any blog entries.', array('!author' => theme('username', array('account' => $account)))));
    }
  }
  drupal_add_feed('blog/' . $account->uid . '/feed', t('RSS - !title', array('!title' => $title)));

  return $build;
}
```

---
_Drupal 7.103 · [modules/blog/blog.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
