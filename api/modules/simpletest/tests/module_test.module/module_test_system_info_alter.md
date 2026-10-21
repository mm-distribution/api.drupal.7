# module_test_system_info_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.module`](_file.md), lines 17–55 · [local source](../../../../../source/modules/simpletest/tests/module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module#L17-L55)
- **Module/theme:** batch_test
- **Implements:** [hook_system_info_alter()](../../../system/system.api.php/hook_system_info_alter.md)

## Signature

```php
function module_test_system_info_alter(&$info, $file, $type)
```

## Documentation

```text
Implements hook_system_info_alter().

Manipulate module dependencies to test dependency chains.
```

## Code

```php
function module_test_system_info_alter(&$info, $file, $type) {
  if (variable_get('dependency_test', FALSE) == 'missing dependency') {
    if ($file->name == 'forum') {
      // Make forum module depend on poll.
      $info['dependencies'][] = 'poll';
    }
    elseif ($file->name == 'poll') {
      // Make poll depend on a made-up module.
      $info['dependencies'][] = 'foo';
    }
  }
  elseif (variable_get('dependency_test', FALSE) == 'dependency') {
    if ($file->name == 'forum') {
      // Make the forum module depend on poll.
      $info['dependencies'][] = 'poll';
    }
    elseif ($file->name == 'poll') {
      // Make poll depend on php module.
      $info['dependencies'][] = 'php';
    }
  }
  elseif (variable_get('dependency_test', FALSE) == 'version dependency') {
    if ($file->name == 'forum') {
      // Make the forum module depend on poll.
      $info['dependencies'][] = 'poll';
    }
    elseif ($file->name == 'poll') {
      // Make poll depend on a specific version of php module.
      $info['dependencies'][] = 'php (1.x)';
    }
    elseif ($file->name == 'php') {
      // Set php module to a version compatible with the above.
      $info['version'] = '7.x-1.0';
    }
  }
  if ($file->name == 'seven' && $type == 'theme') {
    $info['regions']['test_region'] = t('Test region');
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
