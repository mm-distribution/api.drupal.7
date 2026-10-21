# poll_view_voting_validate()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 743–747 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L743-L747)
- **Module/theme:** poll

## Signature

```php
function poll_view_voting_validate($form, &$form_state)
```

## Documentation

```text
Validation function for processing votes
```

## Code

```php
function poll_view_voting_validate($form, &$form_state) {
  if (empty($form_state['values']['choice'])) {
    form_set_error( 'choice', t('Your vote could not be recorded because you did not select any of the choices.'));
  }
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
