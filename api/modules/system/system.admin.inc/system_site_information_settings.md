# system_site_information_settings()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1507–1573 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1507-L1573)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_site_information_settings()
```

## Documentation

```text
Form builder; The general site information form.

@ingroup forms
@see system_settings_form()
```

## Code

```php
function system_site_information_settings() {
  $form['site_information'] = array(
    '#type' => 'fieldset',
    '#title' => t('Site details'),
  );
  $form['site_information']['site_name'] = array(
    '#type' => 'textfield',
    '#title' => t('Site name'),
    '#default_value' => variable_get('site_name', 'Drupal'),
    '#required' => TRUE
  );
  $form['site_information']['site_slogan'] = array(
    '#type' => 'textfield',
    '#title' => t('Slogan'),
    '#default_value' => variable_get('site_slogan', ''),
    '#description' => t("How this is used depends on your site's theme."),
  );
  $form['site_information']['site_mail'] = array(
    '#type' => 'textfield',
    '#title' => t('E-mail address'),
    '#default_value' => variable_get('site_mail', ini_get('sendmail_from')),
    '#description' => t("The <em>From</em> address in automated e-mails sent during registration and new password requests, and other notifications. (Use an address ending in your site's domain to help prevent this e-mail being flagged as spam.)"),
    '#required' => TRUE,
  );
  $form['front_page'] = array(
    '#type' => 'fieldset',
    '#title' => t('Front page'),
  );
  $form['front_page']['default_nodes_main'] = array(
    '#type' => 'select', '#title' => t('Number of posts on front page'),
    '#default_value' => variable_get('default_nodes_main', 10),
    '#options' => drupal_map_assoc(array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30)),
    '#description' => t('The maximum number of posts displayed on overview pages such as the front page.')
  );
  $form['front_page']['site_frontpage'] = array(
    '#type' => 'textfield',
    '#title' => t('Default front page'),
    '#default_value' => (variable_get('site_frontpage')!='node'?drupal_get_path_alias(variable_get('site_frontpage', 'node')):''),
    '#size' => 40,
    '#description' => t('Optionally, specify a relative URL to display as the front page.  Leave blank to display the default content feed.'),
    '#field_prefix' => url(NULL, array('absolute' => TRUE)) . (variable_get('clean_url', 0) ? '' : '?q='),
  );
  $form['error_page'] = array(
    '#type' => 'fieldset',
    '#title' => t('Error pages'),
  );
  $form['error_page']['site_403'] = array(
    '#type' => 'textfield',
    '#title' => t('Default 403 (access denied) page'),
    '#default_value' => variable_get('site_403', ''),
    '#size' => 40,
    '#description' => t('This page is displayed when the requested document is denied to the current user. Leave blank to display a generic "access denied" page.'),
    '#field_prefix' => url(NULL, array('absolute' => TRUE)) . (variable_get('clean_url', 0) ? '' : '?q=')
  );
  $form['error_page']['site_404'] = array(
    '#type' => 'textfield',
    '#title' => t('Default 404 (not found) page'),
    '#default_value' => variable_get('site_404', ''),
    '#size' => 40,
    '#description' => t('This page is displayed when no other content matches the requested document. Leave blank to display a generic "page not found" page.'),
    '#field_prefix' => url(NULL, array('absolute' => TRUE)) . (variable_get('clean_url', 0) ? '' : '?q=')
  );

  $form['#validate'][] = 'system_site_information_settings_validate';

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
