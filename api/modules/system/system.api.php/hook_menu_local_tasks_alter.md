# hook_menu_local_tasks_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1451–1483 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1451-L1483)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_menu_local_tasks_alter(&$data, $router_item, $root_path)
```

## Documentation

```text
Alter tabs and actions displayed on the page before they are rendered.

This hook is invoked by menu_local_tasks(). The system-determined tabs and
actions are passed in by reference. Additional tabs or actions may be added,
or existing items altered.

Each tab or action is an associative array containing:
- #theme: The theme function to use to render.
- #link: An associative array containing:
  - title: The localized title of the link.
  - href: The system path to link to.
  - localized_options: An array of options to pass to l().
- #active: Whether the link should be marked as 'active'.

@param $data
  An associative array containing:
  - actions: An associative array containing:
    - count: The amount of actions determined by the menu system, which can
      be ignored.
    - output: A list of of actions, each one being an associative array
      as described above.
  - tabs: An indexed array (list) of tab levels (up to 2 levels), each
    containing an associative array:
    - count: The amount of tabs determined by the menu system. This value
      does not need to be altered if there is more than one tab.
    - output: A list of of tabs, each one being an associative array as
      described above.
@param $router_item
  The menu system router item of the page.
@param $root_path
  The path to the root item for this set of tabs.
```

## Code

```php
function hook_menu_local_tasks_alter(&$data, $router_item, $root_path) {
  // Add an action linking to node/add to all pages.
  $data['actions']['output'][] = array(
    '#theme' => 'menu_local_task',
    '#link' => array(
      'title' => t('Add new content'),
      'href' => 'node/add',
      'localized_options' => array(
        'attributes' => array(
          'title' => t('Add new content'),
        ),
      ),
    ),
  );

  // Add a tab linking to node/add to all pages.
  $data['tabs'][0]['output'][] = array(
    '#theme' => 'menu_local_task',
    '#link' => array(
      'title' => t('Example tab'),
      'href' => 'node/add',
      'localized_options' => array(
        'attributes' => array(
          'title' => t('Add new content'),
        ),
      ),
    ),
    // Define whether this link is active. This can be omitted for
    // implementations that add links to pages outside of the current page
    // context.
    '#active' => ($router_item['path'] == $root_path),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_menu_local_tasks_alter()".

- [blog_menu_local_tasks_alter()](../../blog/blog.module/blog_menu_local_tasks_alter.md) — `modules/blog/blog.module`
- [forum_menu_local_tasks_alter()](../../forum/forum.module/forum_menu_local_tasks_alter.md) — `modules/forum/forum.module`
- [node_menu_local_tasks_alter()](../../node/node.module/node_menu_local_tasks_alter.md) — `modules/node/node.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
