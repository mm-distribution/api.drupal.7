# DrupalTestCase::deleteAssert()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 281–286 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L281-L286)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
public static function deleteAssert($message_id)
```

## Documentation

```text
Delete an assertion record by message ID.

@param $message_id
  Message ID of the assertion to delete.
@return
  TRUE if the assertion was deleted, FALSE otherwise.

@see DrupalTestCase::insertAssert()
```

## Code

```php
  public static function deleteAssert($message_id) {
    return (bool) self::getDatabaseConnection()
      ->delete('simpletest')
      ->condition('message_id', $message_id)
      ->execute();
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
