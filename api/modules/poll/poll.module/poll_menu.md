# poll_menu()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 89–121 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L89-L121)
- **Module/theme:** poll
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function poll_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function poll_menu() {
  $items['poll'] = array(
    'title' => 'Polls',
    'page callback' => 'poll_page',
    'access arguments' => array('access content'),
    'type' => MENU_SUGGESTED_ITEM,
    'file' => 'poll.pages.inc',
  );

  $items['node/%node/votes'] = array(
    'title' => 'Votes',
    'page callback' => 'poll_votes',
    'page arguments' => array(1),
    'access callback' => '_poll_menu_access',
    'access arguments' => array(1, 'inspect all votes', FALSE),
    'weight' => 3,
    'type' => MENU_LOCAL_TASK,
    'file' => 'poll.pages.inc',
  );

  $items['node/%node/results'] = array(
    'title' => 'Results',
    'page callback' => 'poll_results',
    'page arguments' => array(1),
    'access callback' => '_poll_menu_access',
    'access arguments' => array(1, 'access content', TRUE),
    'weight' => 3,
    'type' => MENU_LOCAL_TASK,
    'file' => 'poll.pages.inc',
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
