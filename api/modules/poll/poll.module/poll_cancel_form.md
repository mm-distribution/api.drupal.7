# poll_cancel_form()

- **Type:** Function
- **File:** [`modules/poll/poll.module`](_file.md), lines 936–950 · [local source](../../../../source/modules/poll/poll.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module#L936-L950)
- **Module/theme:** poll
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function poll_cancel_form($form, &$form_state, $nid)
```

## Documentation

```text
Builds the cancel form for a poll.

@ingroup forms
@see poll_cancel()
```

## Code

```php
function poll_cancel_form($form, &$form_state, $nid) {
  $form_state['cache'] = TRUE;

  // Store the nid so we can get to it in submit functions.
  $form['#nid'] = $nid;

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Cancel your vote'),
    '#submit' => array('poll_cancel')
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/poll/poll.module](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.module) · Licensed GPL-2.0-or-later (see LICENSE)._
