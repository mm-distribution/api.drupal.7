# poll_more_choices_submit()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 366–379 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L366-L379)
- **Module/theme:** poll

## Signature

```php
function poll_more_choices_submit($form, &$form_state)
```

## Documentation

```text
Submit handler to add more choices to a poll form.

This handler is run regardless of whether JS is enabled or not. It makes
changes to the form state. If the button was clicked with JS disabled, then
the page is reloaded with the complete rebuilt form. If the button was
clicked with JS enabled, then ajax_form_callback() calls poll_choice_js() to
return just the changed part of the form.
```

## Code

```php
function poll_more_choices_submit($form, &$form_state) {
  // If this is a Ajax POST, add 1, otherwise add 5 more choices to the form.
  if ($form_state['values']['poll_more']) {
    $n = $_GET['q'] == 'system/ajax' ? 1 : 5;
    $form_state['choice_count'] = count($form_state['values']['choice']) + $n;
  }
  // Renumber the choices. This invalidates the corresponding key/value
  // associations in $form_state['input'], so clear that out. This requires
  // poll_form() to rebuild the choices with the values in
  // $form_state['node']->choice, which it does.
  $form_state['node']->choice = array_values($form_state['values']['choice']);
  unset($form_state['input']['choice']);
  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
