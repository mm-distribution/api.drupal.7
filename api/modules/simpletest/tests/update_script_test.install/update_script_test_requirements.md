# update_script_test_requirements()

- **Type:** Function
- **File:** [`modules/simpletest/tests/update_script_test.install`](_file.md), lines 11–51 · [local source](../../../../../source/modules/simpletest/tests/update_script_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update_script_test.install#L11-L51)
- **Module/theme:** batch_test
- **Implements:** [hook_requirements()](../../../system/system.api.php/hook_requirements.md)

## Signature

```php
function update_script_test_requirements($phase)
```

## Documentation

```text
Implements hook_requirements().
```

## Code

```php
function update_script_test_requirements($phase) {
  $requirements = array();

  if ($phase == 'update') {
    // Set a requirements warning or error when the test requests it.
    $requirement_type = variable_get('update_script_test_requirement_type');
    switch ($requirement_type) {
      case REQUIREMENT_WARNING:
        $requirements['update_script_test'] = array(
          'title' => 'Update script test',
          'value' => 'Warning',
          'description' => 'This is a requirements warning provided by the update_script_test module.',
          'severity' => REQUIREMENT_WARNING,
        );
        break;
      case REQUIREMENT_ERROR:
        $requirements['update_script_test'] = array(
          'title' => 'Update script test',
          'value' => 'Error',
          'description' => 'This is a requirements error provided by the update_script_test module.',
          'severity' => REQUIREMENT_ERROR,
        );
        break;
      case REQUIREMENT_INFO:
        $requirements['update_script_test_stop'] = array(
          'title' => 'Update script test stop',
          'value' => 'Error',
          'description' => 'This is a requirements error provided by the update_script_test module to stop the page redirect for the info.',
          'severity' => REQUIREMENT_ERROR,
        );
        $requirements['update_script_test'] = array(
          'title' => 'Update script test',
          'description' => 'This is a requirements info provided by the update_script_test module.',
          'severity' => REQUIREMENT_INFO,
        );
        break;
    }
  }

  return $requirements;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/update_script_test.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/update_script_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
