# system_ip_blocking_form()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1433–1450 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1433-L1450)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_ip_blocking_form($form, $form_state, $default_ip)
```

## Documentation

```text
Define the form for blocking IP addresses.

@ingroup forms
@see system_ip_blocking_form_validate()
@see system_ip_blocking_form_submit()
```

## Code

```php
function system_ip_blocking_form($form, $form_state, $default_ip) {
  $form['ip'] = array(
    '#title' => t('IP address'),
    '#type' => 'textfield',
    '#size' => 48,
    '#maxlength' => 40,
    '#default_value' => $default_ip,
    '#description' => t('Enter a valid IP address.'),
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Add'),
  );
  $form['#submit'][] = 'system_ip_blocking_form_submit';
  $form['#validate'][] = 'system_ip_blocking_form_validate';
  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
