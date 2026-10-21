# update_manager_install_form()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 498–539 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L498-L539)
- **Module/theme:** update
- **Topics:** [update_manager_install](../../../topics/update_manager_install.md), [forms](../../../topics/forms.md)

## Signature

```php
function update_manager_install_form($form, &$form_state, $context)
```

## Documentation

```text
Form constructor for the install form of the Update Manager module.

This presents a place to enter a URL or upload an archive file to use to
install a new module or theme.

@param $context
  String representing the context from which we're trying to install.
  Allowed values are 'module', 'theme', and 'report'.

@see update_manager_install_form_validate()
@see update_manager_install_form_submit()
@see update_menu()
@ingroup forms
```

## Code

```php
function update_manager_install_form($form, &$form_state, $context) {
  if (!_update_manager_check_backends($form, 'install')) {
    return $form;
  }

  $form['help_text'] = array(
    '#prefix' => '<p>',
    '#markup' => t('You can find <a href="@module_url">modules</a> and <a href="@theme_url">themes</a> on <a href="@drupal_org_url">drupal.org</a>. The following file extensions are supported: %extensions.', array(
      '@module_url' => 'http://drupal.org/project/modules',
      '@theme_url' => 'http://drupal.org/project/themes',
      '@drupal_org_url' => 'http://drupal.org',
      '%extensions' => archiver_get_extensions(),
    )),
    '#suffix' => '</p>',
  );

  $form['project_url'] = array(
    '#type' => 'textfield',
    '#title' => t('Install from a URL'),
    '#description' => t('For example: %url', array('%url' => 'http://ftp.drupal.org/files/projects/name.tar.gz')),
  );

  $form['information'] = array(
    '#prefix' => '<strong>',
    '#markup' => t('Or'),
    '#suffix' => '</strong>',
  );

  $form['project_upload'] = array(
    '#type' => 'file',
    '#title' => t('Upload a module or theme archive to install'),
    '#description' => t('For example: %filename from your local computer', array('%filename' => 'name.tar.gz')),
  );

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Install'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
