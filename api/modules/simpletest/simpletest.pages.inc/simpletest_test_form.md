# simpletest_test_form()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.pages.inc`](_file.md), lines 11–57 · [local source](../../../../source/modules/simpletest/simpletest.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc#L11-L57)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_test_form($form)
```

## Documentation

```text
List tests arranged in groups that can be selected and run.
```

## Code

```php
function simpletest_test_form($form) {
  $form['tests'] = array(
    '#type' => 'fieldset',
    '#title' => t('Tests'),
    '#description' => t('Select the test(s) or test group(s) you would like to run, and click <em>Run tests</em>.'),
  );

  $form['tests']['table'] = array(
    '#theme' => 'simpletest_test_table',
  );

  // Generate the list of tests arranged by group.
  $groups = simpletest_test_get_all();
  foreach ($groups as $group => $tests) {
    $form['tests']['table'][$group] = array(
      '#collapsed' => TRUE,
    );

    foreach ($tests as $class => $info) {
      $form['tests']['table'][$group][$class] = array(
        '#type' => 'checkbox',
        '#title' => $info['name'],
        '#description' => $info['description'],
      );
    }
  }

  // Operation buttons.
  $form['tests']['op'] = array(
    '#type' => 'submit',
    '#value' => t('Run tests'),
  );
  $form['clean'] = array(
    '#type' => 'fieldset',
    '#collapsible' => FALSE,
    '#collapsed' => FALSE,
    '#title' => t('Clean test environment'),
    '#description' => t('Remove tables with the prefix "simpletest" and temporary directories that are left over from tests that crashed. This is intended for developers when creating tests.'),
  );
  $form['clean']['op'] = array(
    '#type' => 'submit',
    '#value' => t('Clean environment'),
    '#submit' => array('simpletest_clean_environment'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
