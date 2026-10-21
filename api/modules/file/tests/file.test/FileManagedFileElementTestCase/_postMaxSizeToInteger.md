# FileManagedFileElementTestCase::_postMaxSizeToInteger()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 522–528 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L522-L528)
- **Class:** [FileManagedFileElementTestCase](../FileManagedFileElementTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
protected function _postMaxSizeToInteger($string)
```

## Documentation

```text
Converts php.ini post_max_size value to integer.

@param $string
  The value from php.ini.

@return int
  Converted value.
```

## Code

```php
  protected function _postMaxSizeToInteger($string) {
    sscanf($string, '%u%c', $number, $suffix);
    if (isset($suffix)) {
      $number = $number * pow(1024, strpos(' KMG', strtoupper($suffix)));
    }
    return $number;
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
