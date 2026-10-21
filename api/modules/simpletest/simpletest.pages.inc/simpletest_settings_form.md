# simpletest_settings_form()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.pages.inc`](_file.md), lines 438–495 · [local source](../../../../source/modules/simpletest/simpletest.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc#L438-L495)
- **Module/theme:** simpletest
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function simpletest_settings_form($form, &$form_state)
```

## Documentation

```text
Provides settings form for SimpleTest variables.

@ingroup forms
@see simpletest_settings_form_validate()
```

## Code

```php
function simpletest_settings_form($form, &$form_state) {
  $form['general'] = array(
    '#type' => 'fieldset',
    '#title' => t('General'),
  );
  $form['general']['simpletest_clear_results'] = array(
    '#type' => 'checkbox',
    '#title' => t('Clear results after each complete test suite run'),
    '#description' => t('By default SimpleTest will clear the results after they have been viewed on the results page, but in some cases it may be useful to leave the results in the database. The results can then be viewed at <em>admin/config/development/testing/results/[test_id]</em>. The test ID can be found in the database, simpletest table, or kept track of when viewing the results the first time. Additionally, some modules may provide more analysis or features that require this setting to be disabled.'),
    '#default_value' => variable_get('simpletest_clear_results', TRUE),
  );
  $form['general']['simpletest_verbose'] = array(
    '#type' => 'checkbox',
    '#title' => t('Provide verbose information when running tests'),
    '#description' => t('The verbose data will be printed along with the standard assertions and is useful for debugging. The verbose data will be erased between each test suite run. The verbose data output is very detailed and should only be used when debugging.'),
    '#default_value' => variable_get('simpletest_verbose', TRUE),
  );

  $form['httpauth'] = array(
    '#type' => 'fieldset',
    '#title' => t('HTTP authentication'),
    '#description' => t('HTTP auth settings to be used by the SimpleTest browser during testing. Useful when the site requires basic HTTP authentication.'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
  );
  $form['httpauth']['simpletest_httpauth_method'] = array(
    '#type' => 'select',
    '#title' => t('Method'),
    '#options' => array(
      CURLAUTH_BASIC => t('Basic'),
      CURLAUTH_DIGEST => t('Digest'),
      CURLAUTH_GSSNEGOTIATE => t('GSS negotiate'),
      CURLAUTH_NTLM => t('NTLM'),
      CURLAUTH_ANY => t('Any'),
      CURLAUTH_ANYSAFE => t('Any safe'),
    ),
    '#default_value' => variable_get('simpletest_httpauth_method', CURLAUTH_BASIC),
  );
  $username = variable_get('simpletest_httpauth_username');
  $password = variable_get('simpletest_httpauth_password');
  $form['httpauth']['simpletest_httpauth_username'] = array(
    '#type' => 'textfield',
    '#title' => t('Username'),
    '#default_value' => $username,
  );
  if ($username && $password) {
    $form['httpauth']['simpletest_httpauth_username']['#description'] = t('Leave this blank to delete both the existing username and password.');
  }
  $form['httpauth']['simpletest_httpauth_password'] = array(
    '#type' => 'password',
    '#title' => t('Password'),
  );
  if ($password) {
    $form['httpauth']['simpletest_httpauth_password']['#description'] = t('To change the password, enter the new password here.');
  }

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
