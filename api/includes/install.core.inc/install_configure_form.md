# install_configure_form()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1495–1547 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1495-L1547)
- **Topics:** [forms](../../topics/forms.md)

## Signature

```php
function install_configure_form($form, &$form_state, &$install_state)
```

## Documentation

```text
Form constructor for a form to configure the new site.

@param $install_state
  An array of information about the current installation state.

@see install_configure_form_validate()
@see install_configure_form_submit()
@ingroup forms
```

## Code

```php
function install_configure_form($form, &$form_state, &$install_state) {
  drupal_set_title(st('Configure site'));

  // Warn about settings.php permissions risk
  $settings_dir = conf_path();
  $settings_file = $settings_dir . '/settings.php';
  // Check that $_POST is empty so we only show this message when the form is
  // first displayed, not on the next page after it is submitted. (We do not
  // want to repeat it multiple times because it is a general warning that is
  // not related to the rest of the installation process; it would also be
  // especially out of place on the last page of the installer, where it would
  // distract from the message that the Drupal installation has completed
  // successfully.)

  $skip_permissions_hardening = variable_get('skip_permissions_hardening', FALSE);
  // Allow system administrators to ignore permissions hardening for the site
  // directory. This allows additional files in the site directory to be
  // updated when they are managed in a version control system.
  if (!$skip_permissions_hardening) {
    if (empty($_POST) && (!drupal_verify_install_file(DRUPAL_ROOT . '/' . $settings_file, FILE_EXIST | FILE_READABLE | FILE_NOT_WRITABLE) || !drupal_verify_install_file(DRUPAL_ROOT . '/' . $settings_dir, FILE_NOT_WRITABLE, 'dir'))) {
      drupal_set_message(st('All necessary changes to %dir and %file have been made, so you should remove write permissions to them now in order to avoid security risks. If you are unsure how to do so, consult the <a href="@handbook_url">online handbook</a>.', array(
        '%dir' => $settings_dir,
        '%file' => $settings_file,
        '@handbook_url' => 'http://drupal.org/server-permissions'
      )), 'warning');
    }
  }

  drupal_add_js(drupal_get_path('module', 'system') . '/system.js');
  // Add JavaScript time zone detection.
  drupal_add_js('misc/timezone.js');
  // We add these strings as settings because JavaScript translation does not
  // work during installation.
  drupal_add_js(array('copyFieldValue' => array('edit-site-mail' => array('edit-account-mail'))), 'setting');
  drupal_add_js('jQuery(function () { Drupal.cleanURLsInstallCheck(); });', 'inline');
  // Add JS to show / hide the 'Email administrator about site updates' elements
  drupal_add_js('jQuery(function () { Drupal.hideEmailAdministratorCheckbox() });', 'inline');
  // Build menu to allow clean URL check.
  menu_rebuild();

  // Cache a fully-built schema. This is necessary for any invocation of
  // index.php because: (1) setting cache table entries requires schema
  // information, (2) that occurs during bootstrap before any module are
  // loaded, so (3) if there is no cached schema, drupal_get_schema() will
  // try to generate one but with no loaded modules will return nothing.
  //
  // This logically could be done during the 'install_finished' task, but the
  // clean URL check requires it now.
  drupal_get_schema(NULL, TRUE);

  // Return the form.
  return _install_configure_form($form, $form_state, $install_state);
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
