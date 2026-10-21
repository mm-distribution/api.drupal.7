# comment_menu()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 220–291 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L220-L291)
- **Module/theme:** comment
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function comment_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function comment_menu() {
  $items['admin/content/comment'] = array(
    'title' => 'Comments',
    'description' => 'List and edit site comments and the comment approval queue.',
    'page callback' => 'comment_admin',
    'access arguments' => array('administer comments'),
    'type' => MENU_LOCAL_TASK | MENU_NORMAL_ITEM,
    'file' => 'comment.admin.inc',
  );
  // Tabs begin here.
  $items['admin/content/comment/new'] = array(
    'title' => 'Published comments',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );
  $items['admin/content/comment/approval'] = array(
    'title' => 'Unapproved comments',
    'title callback' => 'comment_count_unpublished',
    'page arguments' => array('approval'),
    'access arguments' => array('administer comments'),
    'type' => MENU_LOCAL_TASK,
  );
  $items['comment/%'] = array(
    'title' => 'Comment permalink',
    'page callback' => 'comment_permalink',
    'page arguments' => array(1),
    'access arguments' => array('access comments'),
  );
  $items['comment/%/view'] = array(
    'title' => 'View comment',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );
  // Every other comment path uses %, but this one loads the comment directly,
  // so we don't end up loading it twice (in the page and access callback).
  $items['comment/%comment/edit'] = array(
    'title' => 'Edit',
    'page callback' => 'comment_edit_page',
    'page arguments' => array(1),
    'access callback' => 'comment_access',
    'access arguments' => array('edit', 1),
    'type' => MENU_LOCAL_TASK,
    'weight' => 0,
  );
  $items['comment/%/approve'] = array(
    'title' => 'Approve',
    'page callback' => 'comment_approve',
    'page arguments' => array(1),
    'access arguments' => array('administer comments'),
    'file' => 'comment.pages.inc',
    'weight' => 1,
  );
  $items['comment/%/delete'] = array(
    'title' => 'Delete',
    'page callback' => 'comment_confirm_delete_page',
    'page arguments' => array(1),
    'access arguments' => array('administer comments'),
    'type' => MENU_LOCAL_TASK,
    'file' => 'comment.admin.inc',
    'weight' => 2,
  );
  $items['comment/reply/%node'] = array(
    'title' => 'Add new comment',
    'page callback' => 'comment_reply',
    'page arguments' => array(2),
    'access callback' => 'node_access',
    'access arguments' => array('view', 2),
    'file' => 'comment.pages.inc',
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
