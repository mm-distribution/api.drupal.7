# system_user_timezone()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2039–2061 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2039-L2061)
- **Module/theme:** system

## Signature

```php
function system_user_timezone(&$form, &$form_state)
```

## Documentation

```text
Add the time zone field to the user edit and register forms.
```

## Code

```php
function system_user_timezone(&$form, &$form_state) {
  global $user;

  $account = $form['#user'];

  $form['timezone'] = array(
    '#type' => 'fieldset',
    '#title' => t('Locale settings'),
    '#weight' => 6,
    '#collapsible' => TRUE,
  );
  $form['timezone']['timezone'] = array(
    '#type' => 'select',
    '#title' => t('Time zone'),
    '#default_value' => isset($account->timezone) ? $account->timezone : ($account->uid == $user->uid ? variable_get('date_default_timezone', '') : ''),
    '#options' => system_time_zones($account->uid != $user->uid),
    '#description' => t('Select the desired local time and time zone. Dates and times throughout this site will be displayed using this time zone.'),
  );
  if (!isset($account->timezone) && $account->uid == $user->uid && empty($form_state['input']['timezone'])) {
    $form['timezone']['timezone']['#attributes'] = array('class' => array('timezone-detect'));
    drupal_add_js('misc/timezone.js');
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
