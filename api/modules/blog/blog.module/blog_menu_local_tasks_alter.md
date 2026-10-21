# blog_menu_local_tasks_alter()

- **Type:** Function
- **File:** [`modules/blog/blog.module`](_file.md), lines 140–167 · [local source](../../../../source/modules/blog/blog.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module#L140-L167)
- **Module/theme:** blog
- **Implements:** [hook_menu_local_tasks_alter()](../../system/system.api.php/hook_menu_local_tasks_alter.md)

## Signature

```php
function blog_menu_local_tasks_alter(&$data, $router_item, $root_path)
```

## Documentation

```text
Implements hook_menu_local_tasks_alter().
```

## Code

```php
function blog_menu_local_tasks_alter(&$data, $router_item, $root_path) {
  global $user;

  // Add action link to 'node/add/blog' on 'blog' page.
  if ($root_path == 'blog') {
    $item = menu_get_item('node/add/blog');
    if ($item['access']) {
      $item['title'] = t('Create new blog entry');
      $data['actions']['output'][] = array(
        '#theme' => 'menu_local_action',
        '#link' => $item,
      );
    }
  }
  // Provide a helper action link to the author on the 'blog/%' page.
  elseif ($root_path == 'blog/%' && isset($router_item['page_arguments'][0]->uid) && $router_item['page_arguments'][0]->uid == $user->uid) {
    $data['actions']['output']['blog'] = array(
      '#theme' => 'menu_local_action',
    );
    if (user_access('create blog content')) {
      $data['actions']['output']['blog']['#link']['title'] = t('Post new blog entry.');
      $data['actions']['output']['blog']['#link']['href'] = 'node/add/blog';
    }
    else {
      $data['actions']['output']['blog']['#link']['title'] = t('You are not allowed to post a new blog entry.');
    }
  }
}
```

---
_Drupal 7.103 · [modules/blog/blog.module](https://github.com/drupal/drupal/blob/7.103/modules/blog/blog.module) · Licensed GPL-2.0-or-later (see LICENSE)._
