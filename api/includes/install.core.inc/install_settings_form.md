# install_settings_form()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 887–945 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L887-L945)
- **Topics:** [forms](../../topics/forms.md)

## Signature

```php
function install_settings_form($form, &$form_state, &$install_state)
```

## Documentation

```text
Form constructor for a form to configure and rewrite settings.php.

@param $install_state
  An array of information about the current installation state.

@see install_settings_form_validate()
@see install_settings_form_submit()
@ingroup forms
```

## Code

```php
function install_settings_form($form, &$form_state, &$install_state) {
  global $databases;
  $profile = $install_state['parameters']['profile'];
  $install_locale = $install_state['parameters']['locale'];

  drupal_static_reset('conf_path');
  $conf_path = './' . conf_path(FALSE);
  $settings_file = $conf_path . '/settings.php';
  $database = isset($databases['default']['default']) ? $databases['default']['default'] : array();

  drupal_set_title(st('Database configuration'));

  $drivers = drupal_get_database_types();
  $drivers_keys = array_keys($drivers);

  $form['driver'] = array(
    '#type' => 'radios',
    '#title' => st('Database type'),
    '#required' => TRUE,
    '#default_value' => !empty($database['driver']) ? $database['driver'] : current($drivers_keys),
    '#description' => st('The type of database your @drupal data will be stored in.', array('@drupal' => drupal_install_profile_distribution_name())),
  );
  if (count($drivers) == 1) {
    $form['driver']['#disabled'] = TRUE;
    $form['driver']['#description'] .= ' ' . st('Your PHP configuration only supports a single database type, so it has been automatically selected.');
  }

  // Add driver specific configuration options.
  foreach ($drivers as $key => $driver) {
    $form['driver']['#options'][$key] = $driver->name();

    $form['settings'][$key] = $driver->getFormOptions($database);
    $form['settings'][$key]['#prefix'] = '<h2 class="js-hide">' . st('@driver_name settings', array('@driver_name' => $driver->name())) . '</h2>';
    $form['settings'][$key]['#type'] = 'container';
    $form['settings'][$key]['#tree'] = TRUE;
    $form['settings'][$key]['advanced_options']['#parents'] = array($key);
    $form['settings'][$key]['#states'] = array(
      'visible' => array(
        ':input[name=driver]' => array('value' => $key),
      )
    );
  }

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['save'] = array(
    '#type' => 'submit',
    '#value' => st('Save and continue'),
    '#limit_validation_errors' => array(
      array('driver'),
      array(isset($form_state['input']['driver']) ? $form_state['input']['driver'] : current($drivers_keys)),
    ),
    '#submit' => array('install_settings_form_submit'),
  );

  $form['errors'] = array();
  $form['settings_file'] = array('#type' => 'value', '#value' => $settings_file);

  return $form;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
