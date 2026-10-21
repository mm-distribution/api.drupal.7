# DrupalAlterTestCase::testDrupalAlter()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 24–67 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L24-L67)
- **Class:** [DrupalAlterTestCase](../DrupalAlterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalAlter()
```

## Documentation

_No docblock in source._

## Code

```php
  function testDrupalAlter() {
    // This test depends on Bartik, so make sure that it is always the current
    // active theme.
    global $theme, $base_theme_info;
    $theme = 'bartik';
    $base_theme_info = array();

    $array = array('foo' => 'bar');
    $entity = new stdClass();
    $entity->foo = 'bar';

    // Verify alteration of a single argument.
    $array_copy = $array;
    $array_expected = array('foo' => 'Drupal theme');
    drupal_alter('drupal_alter', $array_copy);
    $this->assertEqual($array_copy, $array_expected, 'Single array was altered.');

    $entity_copy = clone $entity;
    $entity_expected = clone $entity;
    $entity_expected->foo = 'Drupal theme';
    drupal_alter('drupal_alter', $entity_copy);
    $this->assertEqual($entity_copy, $entity_expected, 'Single object was altered.');

    // Verify alteration of multiple arguments.
    $array_copy = $array;
    $array_expected = array('foo' => 'Drupal theme');
    $entity_copy = clone $entity;
    $entity_expected = clone $entity;
    $entity_expected->foo = 'Drupal theme';
    $array2_copy = $array;
    $array2_expected = array('foo' => 'Drupal theme');
    drupal_alter('drupal_alter', $array_copy, $entity_copy, $array2_copy);
    $this->assertEqual($array_copy, $array_expected, 'First argument to drupal_alter() was altered.');
    $this->assertEqual($entity_copy, $entity_expected, 'Second argument to drupal_alter() was altered.');
    $this->assertEqual($array2_copy, $array2_expected, 'Third argument to drupal_alter() was altered.');

    // Verify alteration order when passing an array of types to drupal_alter().
    // common_test_module_implements_alter() places 'block' implementation after
    // other modules.
    $array_copy = $array;
    $array_expected = array('foo' => 'Drupal block theme');
    drupal_alter(array('drupal_alter', 'drupal_alter_foo'), $array_copy);
    $this->assertEqual($array_copy, $array_expected, 'hook_TYPE_alter() implementations ran in correct order.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
