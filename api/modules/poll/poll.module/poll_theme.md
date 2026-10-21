# poll_theme()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 32–65 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L32-L65)
- **Module/theme:** poll
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function poll_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function poll_theme() {
  $theme_hooks = array(
    'poll_vote' => array(
      'template' => 'poll-vote',
      'render element' => 'form',
    ),
    'poll_choices' => array(
      'render element' => 'form',
    ),
    'poll_results' => array(
      'template' => 'poll-results',
      'variables' => array('raw_title' => NULL, 'results' => NULL, 'votes' => NULL, 'raw_links' => NULL, 'block' => NULL, 'nid' => NULL, 'vote' => NULL),
    ),
    'poll_bar' => array(
      'template' => 'poll-bar',
      'variables' => array('title' => NULL, 'votes' => NULL, 'total_votes' => NULL, 'vote' => NULL, 'block' => NULL),
    ),
  );
  // The theme system automatically discovers the theme's functions and
  // templates that implement more targeted "suggestions" of generic theme
  // hooks. But suggestions implemented by a module must be explicitly
  // registered.
  $theme_hooks += array(
    'poll_results__block' => array(
      'template' => 'poll-results--block',
      'variables' => $theme_hooks['poll_results']['variables'],
    ),
    'poll_bar__block' => array(
      'template' => 'poll-bar--block',
      'variables' => $theme_hooks['poll_bar']['variables'],
    ),
  );
  return $theme_hooks;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
