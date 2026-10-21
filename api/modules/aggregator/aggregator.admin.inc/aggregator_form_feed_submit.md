# aggregator_form_feed_submit()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 171–207 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L171-L207)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_form_feed_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for aggregator_form_feed().

@see aggregator_form_feed_validate()

@todo Add delete confirmation dialog.
```

## Code

```php
function aggregator_form_feed_submit($form, &$form_state) {
  if ($form_state['values']['op'] == t('Delete')) {
    $title = $form_state['values']['title'];
    // Unset the title.
    unset($form_state['values']['title']);
  }
  aggregator_save_feed($form_state['values']);
  if (isset($form_state['values']['fid'])) {
    if (isset($form_state['values']['title'])) {
      drupal_set_message(t('The feed %feed has been updated.', array('%feed' => $form_state['values']['title'])));
      if (arg(0) == 'admin') {
        $form_state['redirect'] = 'admin/config/services/aggregator/';
        return;
      }
      else {
        $form_state['redirect'] = 'aggregator/sources/' . $form_state['values']['fid'];
        return;
      }
    }
    else {
      watchdog('aggregator', 'Feed %feed deleted.', array('%feed' => $title));
      drupal_set_message(t('The feed %feed has been deleted.', array('%feed' => $title)));
      if (arg(0) == 'admin') {
        $form_state['redirect'] = 'admin/config/services/aggregator/';
        return;
      }
      else {
        $form_state['redirect'] = 'aggregator/sources/';
        return;
      }
    }
  }
  else {
    watchdog('aggregator', 'Feed %feed added.', array('%feed' => $form_state['values']['title']), WATCHDOG_NOTICE, l(t('view'), 'admin/config/services/aggregator'));
    drupal_set_message(t('The feed %feed has been added.', array('%feed' => $form_state['values']['title'])));
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
