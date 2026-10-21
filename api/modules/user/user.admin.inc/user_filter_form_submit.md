# user_filter_form_submit()

- **Type:** Function
- **File:** [`modules/user/user.admin.inc`](_file.md), lines 124–154 · [local source](../../../../source/modules/user/user.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc#L124-L154)
- **Module/theme:** user

## Signature

```php
function user_filter_form_submit($form, &$form_state)
```

## Documentation

```text
Process result from user administration filter form.
```

## Code

```php
function user_filter_form_submit($form, &$form_state) {
  $op = $form_state['values']['op'];
  $filters = user_filters();
  switch ($op) {
    case t('Filter'):
    case t('Refine'):
      // Apply every filter that has a choice selected other than 'any'.
      foreach ($filters as $filter => $options) {
        if (isset($form_state['values'][$filter]) && $form_state['values'][$filter] != '[any]') {
          // Merge an array of arrays into one if necessary.
          $options = ($filter == 'permission') ? form_options_flatten($filters[$filter]['options']) : $filters[$filter]['options'];
          // Only accept valid selections offered on the dropdown, block bad input.
          if (isset($options[$form_state['values'][$filter]])) {
            $_SESSION['user_overview_filter'][] = array($filter, $form_state['values'][$filter]);
          }
        }
      }
      break;
    case t('Undo'):
      array_pop($_SESSION['user_overview_filter']);
      break;
    case t('Reset'):
      $_SESSION['user_overview_filter'] = array();
      break;
    case t('Update'):
      return;
  }

  $form_state['redirect'] = 'admin/people';
  return;
}
```

---
_Drupal 7.103 · [modules/user/user.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
