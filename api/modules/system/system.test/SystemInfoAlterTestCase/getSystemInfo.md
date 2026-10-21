# SystemInfoAlterTestCase::getSystemInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2498–2501 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2498-L2501)
- **Class:** [SystemInfoAlterTestCase](../SystemInfoAlterTestCase.md)
- **Module/theme:** system

## Signature

```php
function getSystemInfo($name, $type)
```

## Documentation

```text
Returns the info array as it is stored in {system}.

@param $name
  The name of the record in {system}.
@param $type
  The type of record in {system}.

@return
  Array of info, or FALSE if the record is not found.
```

## Code

```php
  function getSystemInfo($name, $type) {
    $raw_info = db_query("SELECT info FROM {system} WHERE name = :name AND type = :type", array(':name' => $name, ':type' => $type))->fetchField();
    return $raw_info ? unserialize($raw_info) : FALSE;
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
