# template_preprocess_poll_vote()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 794–804 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L794-L804)
- **Module/theme:** poll

## Signature

```php
function template_preprocess_poll_vote(&$variables)
```

## Documentation

```text
Themes the voting form for a poll.

Inputs: $form
```

## Code

```php
function template_preprocess_poll_vote(&$variables) {
  $form = $variables['form'];
  $variables['choice'] = drupal_render($form['choice']);
  $variables['title'] = check_plain($form['#node']->title);
  $variables['vote'] = drupal_render($form['vote']);
  $variables['rest'] = drupal_render_children($form);
  $variables['block'] = $form['#block'];
  if ($variables['block']) {
    $variables['theme_hook_suggestions'][] = 'poll_vote__block';
  }
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
