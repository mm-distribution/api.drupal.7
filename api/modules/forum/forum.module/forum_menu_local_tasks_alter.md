# forum_menu_local_tasks_alter()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 164–212 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L164-L212)
- **Module/theme:** forum
- **Implements:** [hook_menu_local_tasks_alter()](../../system/system.api.php/hook_menu_local_tasks_alter.md)

## Signature

```php
function forum_menu_local_tasks_alter(&$data, $router_item, $root_path)
```

## Documentation

```text
Implements hook_menu_local_tasks_alter().
```

## Code

```php
function forum_menu_local_tasks_alter(&$data, $router_item, $root_path) {
  global $user;

  // Add action link to 'node/add/forum' on 'forum' sub-pages.
  if ($root_path == 'forum' || $root_path == 'forum/%') {
    $tid = (isset($router_item['page_arguments'][0]) ? $router_item['page_arguments'][0]->tid : 0);
    $forum_term = forum_forum_load($tid);
    if ($forum_term) {
      $links = array();
      // Loop through all bundles for forum taxonomy vocabulary field.
      $field = field_info_field('taxonomy_forums');
      foreach ($field['bundles']['node'] as $type) {
        if (node_access('create', $type)) {
          $links[$type] = array(
            '#theme' => 'menu_local_action',
            '#link' => array(
              'title' => t('Add new @node_type', array('@node_type' => node_type_get_name($type))),
              'href' => 'node/add/' . str_replace('_', '-', $type) . '/' . $forum_term->tid,
            ),
          );
        }
      }
      if (empty($links)) {
        // Authenticated user does not have access to create new topics.
        if ($user->uid) {
          $links['disallowed'] = array(
            '#theme' => 'menu_local_action',
            '#link' => array(
              'title' => t('You are not allowed to post new content in the forum.'),
            ),
          );
        }
        // Anonymous user does not have access to create new topics.
        else {
          $links['login'] = array(
            '#theme' => 'menu_local_action',
            '#link' => array(
              'title' => t('<a href="@login">Log in</a> to post new content in the forum.', array(
                '@login' => url('user/login', array('query' => drupal_get_destination())),
              )),
              'localized_options' => array('html' => TRUE),
            ),
          );
        }
      }
      $data['actions']['output'] = array_merge($data['actions']['output'], $links);
    }
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
