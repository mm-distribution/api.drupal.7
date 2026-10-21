# system_site_maintenance_mode()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2235–2250 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2235-L2250)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_site_maintenance_mode()
```

## Documentation

```text
Form builder; Configure the site's maintenance status.

@ingroup forms
@see system_settings_form()
```

## Code

```php
function system_site_maintenance_mode() {
  $form['maintenance_mode'] = array(
    '#type' => 'checkbox',
    '#title' => t('Put site into maintenance mode'),
    '#default_value' => variable_get('maintenance_mode', 0),
    '#description' => t('When enabled, only users with the "Use the site in maintenance mode" <a href="@permissions-url">permission</a> are able to access your site to perform maintenance; all other visitors see the maintenance mode message configured below. Authorized users can log in directly via the <a href="@user-login">user login</a> page.', array('@permissions-url' => url('admin/people/permissions'), '@user-login' => url('user'))),
  );
  $form['maintenance_mode_message'] = array(
    '#type' => 'textarea',
    '#title' => t('Maintenance mode message'),
    '#default_value' => variable_get('maintenance_mode_message', t('@site is currently under maintenance. We should be back shortly. Thank you for your patience.', array('@site' => variable_get('site_name', 'Drupal')))),
    '#description' => t('Message to show visitors when the site is in maintenance mode.')
  );

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
