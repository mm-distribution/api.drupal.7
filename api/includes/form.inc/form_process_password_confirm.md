# form_process_password_confirm()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3018–3041 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3018-L3041)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_process_password_confirm($element)
```

## Documentation

```text
Expand a password_confirm field into two text boxes.
```

## Code

```php
function form_process_password_confirm($element) {
  $element['pass1'] =  array(
    '#type' => 'password',
    '#title' => t('Password'),
    '#value' => empty($element['#value']) ? NULL : $element['#value']['pass1'],
    '#required' => $element['#required'],
    '#attributes' => array('class' => array('password-field')),
  );
  $element['pass2'] =  array(
    '#type' => 'password',
    '#title' => t('Confirm password'),
    '#value' => empty($element['#value']) ? NULL : $element['#value']['pass2'],
    '#required' => $element['#required'],
    '#attributes' => array('class' => array('password-confirm')),
  );
  $element['#element_validate'] = array('password_confirm_validate');
  $element['#tree'] = TRUE;

  if (isset($element['#size'])) {
    $element['pass1']['#size'] = $element['pass2']['#size'] = $element['#size'];
  }

  return $element;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
