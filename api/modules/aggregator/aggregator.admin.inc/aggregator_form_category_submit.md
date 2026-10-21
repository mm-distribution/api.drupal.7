# aggregator_form_category_submit()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 597–633 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L597-L633)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_form_category_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for aggregator_form_category().

@see aggregator_form_category_validate()

@todo Add delete confirmation dialog.
```

## Code

```php
function aggregator_form_category_submit($form, &$form_state) {
  if ($form_state['values']['op'] == t('Delete')) {
    $title = $form_state['values']['title'];
    // Unset the title.
    unset($form_state['values']['title']);
  }
  aggregator_save_category($form_state['values']);
  if (isset($form_state['values']['cid'])) {
    if (isset($form_state['values']['title'])) {
      drupal_set_message(t('The category %category has been updated.', array('%category' => $form_state['values']['title'])));
      if (arg(0) == 'admin') {
        $form_state['redirect'] = 'admin/config/services/aggregator/';
        return;
      }
      else {
        $form_state['redirect'] = 'aggregator/categories/' . $form_state['values']['cid'];
        return;
      }
    }
    else {
      watchdog('aggregator', 'Category %category deleted.', array('%category' => $title));
      drupal_set_message(t('The category %category has been deleted.', array('%category' => $title)));
      if (arg(0) == 'admin') {
        $form_state['redirect'] = 'admin/config/services/aggregator/';
        return;
      }
      else {
        $form_state['redirect'] = 'aggregator/categories/';
        return;
      }
    }
  }
  else {
    watchdog('aggregator', 'Category %category added.', array('%category' => $form_state['values']['title']), WATCHDOG_NOTICE, l(t('view'), 'admin/config/services/aggregator'));
    drupal_set_message(t('The category %category has been added.', array('%category' => $form_state['values']['title'])));
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
