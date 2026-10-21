# system_regional_settings()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1938–2015 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1938-L2015)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_regional_settings()
```

## Documentation

```text
Form builder; Configure the site regional settings.

@ingroup forms
@see system_settings_form()
@see system_regional_settings_submit()
```

## Code

```php
function system_regional_settings() {
  include_once DRUPAL_ROOT . '/includes/locale.inc';
  $countries = country_get_list();

  // Date settings:
  $zones = system_time_zones();

  $form['locale'] = array(
    '#type' => 'fieldset',
    '#title' => t('Locale'),
  );

  $form['locale']['site_default_country'] = array(
    '#type' => 'select',
    '#title' => t('Default country'),
    '#empty_value' => '',
    '#default_value' => variable_get('site_default_country', ''),
    '#options' => $countries,
    '#attributes' => array('class' => array('country-detect')),
  );

  $form['locale']['date_first_day'] = array(
    '#type' => 'select',
    '#title' => t('First day of week'),
    '#default_value' => variable_get('date_first_day', 0),
    '#options' => array(0 => t('Sunday'), 1 => t('Monday'), 2 => t('Tuesday'), 3 => t('Wednesday'), 4 => t('Thursday'), 5 => t('Friday'), 6 => t('Saturday')),
  );

  $form['timezone'] = array(
    '#type' => 'fieldset',
    '#title' => t('Time zones'),
  );

  $form['timezone']['date_default_timezone'] = array(
    '#type' => 'select',
    '#title' => t('Default time zone'),
    '#default_value' => variable_get('date_default_timezone', date_default_timezone_get()),
    '#options' => $zones,
  );

  $configurable_timezones = variable_get('configurable_timezones', 1);
  $form['timezone']['configurable_timezones'] = array(
    '#type' => 'checkbox',
    '#title' => t('Users may set their own time zone.'),
    '#default_value' => $configurable_timezones,
  );

  $form['timezone']['configurable_timezones_wrapper'] =  array(
    '#type' => 'container',
    '#states' => array(
      // Hide the user configured timezone settings when users are forced to use
      // the default setting.
      'invisible' => array(
        'input[name="configurable_timezones"]' => array('checked' => FALSE),
      ),
    ),
  );
  $form['timezone']['configurable_timezones_wrapper']['empty_timezone_message'] = array(
    '#type' => 'checkbox',
    '#title' => t('Remind users at login if their time zone is not set.'),
    '#default_value' => variable_get('empty_timezone_message', 0),
    '#description' => t('Only applied if users may set their own time zone.')
  );

  $form['timezone']['configurable_timezones_wrapper']['user_default_timezone'] = array(
    '#type' => 'radios',
    '#title' => t('Time zone for new users'),
    '#default_value' => variable_get('user_default_timezone', DRUPAL_USER_TIMEZONE_DEFAULT),
    '#options' => array(
      DRUPAL_USER_TIMEZONE_DEFAULT => t('Default time zone.'),
      DRUPAL_USER_TIMEZONE_EMPTY   => t('Empty time zone.'),
      DRUPAL_USER_TIMEZONE_SELECT  => t('Users may set their own time zone at registration.'),
    ),
    '#description' => t('Only applied if users may set their own time zone.')
  );

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
