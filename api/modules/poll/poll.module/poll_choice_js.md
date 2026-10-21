# poll_choice_js()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 435–437 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L435-L437)
- **Module/theme:** poll

## Signature

```php
function poll_choice_js($form, $form_state)
```

## Documentation

```text
Ajax callback in response to new choices being added to the form.

This returns the new page content to replace the page content made obsolete
by the form submission.

@see poll_more_choices_submit()
```

## Code

```php
function poll_choice_js($form, $form_state) {
  return $form['choice_wrapper']['choice'];
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
