# _install_configure_form()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1771–1879 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1771-L1879)
- **Topics:** [forms](../../topics/forms.md)

## Signature

```php
function _install_configure_form($form, &$form_state, &$install_state)
```

## Documentation

```text
Form constructor for a site configuration form.

@param $install_state
  An array of information about the current installation state.

@see install_configure_form()
@see install_configure_form_validate()
@see install_configure_form_submit()
@ingroup forms
```

## Code

```php
function _install_configure_form($form, &$form_state, &$install_state) {
  include_once DRUPAL_ROOT . '/includes/locale.inc';

  $form['site_information'] = array(
    '#type' => 'fieldset',
    '#title' => st('Site information'),
    '#collapsible' => FALSE,
  );
  $form['site_information']['site_name'] = array(
    '#type' => 'textfield',
    '#title' => st('Site name'),
    '#required' => TRUE,
    '#weight' => -20,
  );
  $form['site_information']['site_mail'] = array(
    '#type' => 'textfield',
    '#title' => st('Site e-mail address'),
    '#default_value' => ini_get('sendmail_from'),
    '#description' => st("Automated e-mails, such as registration information, will be sent from this address. Use an address ending in your site's domain to help prevent these e-mails from being flagged as spam."),
    '#required' => TRUE,
    '#weight' => -15,
  );
  $form['admin_account'] = array(
    '#type' => 'fieldset',
    '#title' => st('Site maintenance account'),
    '#collapsible' => FALSE,
  );

  $form['admin_account']['account']['#tree'] = TRUE;
  $form['admin_account']['account']['name'] = array('#type' => 'textfield',
    '#title' => st('Username'),
    '#maxlength' => USERNAME_MAX_LENGTH,
    '#description' => st('Spaces are allowed; punctuation is not allowed except for periods, hyphens, and underscores.'),
    '#required' => TRUE,
    '#weight' => -10,
    '#attributes' => array('class' => array('username')),
  );

  $form['admin_account']['account']['mail'] = array('#type' => 'textfield',
    '#title' => st('E-mail address'),
    '#maxlength' => EMAIL_MAX_LENGTH,
    '#required' => TRUE,
    '#weight' => -5,
  );
  $form['admin_account']['account']['pass'] = array(
    '#type' => 'password_confirm',
    '#required' => TRUE,
    '#size' => 25,
    '#weight' => 0,
  );

  $form['server_settings'] = array(
    '#type' => 'fieldset',
    '#title' => st('Server settings'),
    '#collapsible' => FALSE,
  );

  $countries = country_get_list();
  $form['server_settings']['site_default_country'] = array(
    '#type' => 'select',
    '#title' => st('Default country'),
    '#empty_value' => '',
    '#default_value' => variable_get('site_default_country', NULL),
    '#options' => $countries,
    '#description' => st('Select the default country for the site.'),
    '#weight' => 0,
  );

  $form['server_settings']['date_default_timezone'] = array(
    '#type' => 'select',
    '#title' => st('Default time zone'),
    '#default_value' => date_default_timezone_get(),
    '#options' => system_time_zones(),
    '#description' => st('By default, dates in this site will be displayed in the chosen time zone.'),
    '#weight' => 5,
    '#attributes' => array('class' => array('timezone-detect')),
  );

  $form['server_settings']['clean_url'] = array(
    '#type' => 'hidden',
    '#default_value' => 0,
    '#attributes' => array('id' => 'edit-clean-url', 'class' => array('install')),
  );

  $form['update_notifications'] = array(
    '#type' => 'fieldset',
    '#title' => st('Update notifications'),
    '#collapsible' => FALSE,
  );
  $form['update_notifications']['update_status_module'] = array(
    '#type' => 'checkboxes',
    '#options' => array(
      1 => st('Check for updates automatically'),
      2 => st('Receive e-mail notifications'),
    ),
    '#default_value' => array(1, 2),
    '#description' => st('The system will notify you when updates and important security releases are available for installed components. Anonymous information about your site is sent to <a href="@drupal">Drupal.org</a>.', array('@drupal' => 'http://drupal.org')),
    '#weight' => 15,
  );

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => st('Save and continue'),
    '#weight' => 15,
  );

  return $form;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
