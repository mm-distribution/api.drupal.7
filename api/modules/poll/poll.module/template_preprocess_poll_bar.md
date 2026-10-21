# template_preprocess_poll_bar()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 922–928 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L922-L928)
- **Module/theme:** poll

## Signature

```php
function template_preprocess_poll_bar(&$variables)
```

## Documentation

```text
Preprocess the poll_bar theme hook.

Inputs: $title, $votes, $total_votes, $voted, $block

@see poll-bar.tpl.php
@see poll-bar--block.tpl.php
```

## Code

```php
function template_preprocess_poll_bar(&$variables) {
  if ($variables['block']) {
    $variables['theme_hook_suggestions'][] = 'poll_bar__block';
  }
  $variables['title'] = check_plain($variables['title']);
  $variables['percentage'] = round($variables['votes'] * 100 / max($variables['total_votes'], 1));
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
