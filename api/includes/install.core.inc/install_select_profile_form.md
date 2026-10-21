# install_select_profile_form()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1143–1198 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1143-L1198)
- **Topics:** [forms](../../topics/forms.md)

## Signature

```php
function install_select_profile_form($form, &$form_state, $profile_files)
```

## Documentation

```text
Form constructor for the profile selection form.

@param $form_state
  Array of metadata about state of form processing.
@param $profile_files
  Array of .profile files, as returned from file_scan_directory().

@ingroup forms
```

## Code

```php
function install_select_profile_form($form, &$form_state, $profile_files) {
  $profiles = array();
  $names = array();

  foreach ($profile_files as $profile) {
    // TODO: is this right?
    include_once DRUPAL_ROOT . '/' . $profile->uri;

    $details = install_profile_info($profile->name);
    // Don't show hidden profiles. This is used by to hide the testing profile,
    // which only exists to speed up test runs.
    if ($details['hidden'] === TRUE) {
      continue;
    }
    $profiles[$profile->name] = $details;

    // Determine the name of the profile; default to file name if defined name
    // is unspecified.
    $name = isset($details['name']) ? $details['name'] : $profile->name;
    $names[$profile->name] = $name;
  }

  // Display radio buttons alphabetically by human-readable name, but always
  // put the core profiles first (if they are present in the filesystem).
  natcasesort($names);
  if (isset($names['minimal'])) {
    // If the expert ("Minimal") core profile is present, put it in front of
    // any non-core profiles rather than including it with them alphabetically,
    // since the other profiles might be intended to group together in a
    // particular way.
    $names = array('minimal' => $names['minimal']) + $names;
  }
  if (isset($names['standard'])) {
    // If the default ("Standard") core profile is present, put it at the very
    // top of the list. This profile will have its radio button pre-selected,
    // so we want it to always appear at the top.
    $names = array('standard' => $names['standard']) + $names;
  }

  foreach ($names as $profile => $name) {
    $form['profile'][$name] = array(
      '#type' => 'radio',
      '#value' => 'standard',
      '#return_value' => $profile,
      '#title' => $name,
      '#description' => isset($profiles[$profile]['description']) ? $profiles[$profile]['description'] : '',
      '#parents' => array('profile'),
    );
  }
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] =  array(
    '#type' => 'submit',
    '#value' => st('Save and continue'),
  );
  return $form;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
