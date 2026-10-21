# DrupalTestCase::insertAssert()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 242–269 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L242-L269)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
public static function insertAssert($test_id, $test_class, $status, $message = '', $group = 'Other', array $caller = array())
```

## Documentation

```text
Store an assertion from outside the testing context.

This is useful for inserting assertions that can only be recorded after
the test case has been destroyed, such as PHP fatal errors. The caller
information is not automatically gathered since the caller is most likely
inserting the assertion on behalf of other code. In all other respects
the method behaves just like DrupalTestCase::assert() in terms of storing
the assertion.

@return
  Message ID of the stored assertion.

@see DrupalTestCase::assert()
@see DrupalTestCase::deleteAssert()
```

## Code

```php
  public static function insertAssert($test_id, $test_class, $status, $message = '', $group = 'Other', array $caller = array()) {
    // Convert boolean status to string status.
    if (is_bool($status)) {
      $status = $status ? 'pass' : 'fail';
    }

    $caller += array(
      'function' => t('Unknown'),
      'line' => 0,
      'file' => t('Unknown'),
    );

    $assertion = array(
      'test_id' => $test_id,
      'test_class' => $test_class,
      'status' => $status,
      'message' => $message,
      'message_group' => $group,
      'function' => $caller['function'],
      'line' => $caller['line'],
      'file' => $caller['file'],
    );

    return self::getDatabaseConnection()
      ->insert('simpletest')
      ->fields($assertion)
      ->execute();
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
