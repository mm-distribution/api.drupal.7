# poll_node_form_submit()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 445–449 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L445-L449)
- **Module/theme:** poll

## Signature

```php
function poll_node_form_submit(&$form, &$form_state)
```

## Documentation

```text
Form submit handler for node_form().

Upon preview and final submission, we need to renumber poll choices and
create a teaser output.
```

## Code

```php
function poll_node_form_submit(&$form, &$form_state) {
  // Renumber choices.
  $form_state['values']['choice'] = array_values($form_state['values']['choice']);
  $form_state['values']['teaser'] = poll_teaser((object) $form_state['values']);
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
