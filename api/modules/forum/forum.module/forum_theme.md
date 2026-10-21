# forum_theme()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 57–84 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L57-L84)
- **Module/theme:** forum
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function forum_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function forum_theme() {
  return array(
    'forums' => array(
      'template' => 'forums',
      'variables' => array('forums' => NULL, 'topics' => NULL, 'parents' => NULL, 'tid' => NULL, 'sortby' => NULL, 'forum_per_page' => NULL),
    ),
    'forum_list' => array(
      'template' => 'forum-list',
      'variables' => array('forums' => NULL, 'parents' => NULL, 'tid' => NULL),
    ),
    'forum_topic_list' => array(
      'template' => 'forum-topic-list',
      'variables' => array('tid' => NULL, 'topics' => NULL, 'sortby' => NULL, 'forum_per_page' => NULL),
    ),
    'forum_icon' => array(
      'template' => 'forum-icon',
      'variables' => array('new_posts' => NULL, 'num_posts' => 0, 'comment_mode' => 0, 'sticky' => 0, 'first_new' => FALSE),
    ),
    'forum_submitted' => array(
      'template' => 'forum-submitted',
      'variables' => array('topic' => NULL),
    ),
    'forum_form' => array(
      'render element' => 'form',
      'file' => 'forum.admin.inc',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
