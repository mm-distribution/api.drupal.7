# DrupalTestCase::randomName()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 688–696 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L688-L696)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
public static function randomName($length = 8)
```

## Documentation

```text
Generates a random string containing letters and numbers.

The string will always start with a letter. The letters may be upper or
lower case. This method is better for restricted inputs that do not
accept certain characters. For example, when testing input fields that
require machine readable values (i.e. without spaces and non-standard
characters) this method is best.

Do not use this method when testing unvalidated user input. Instead, use
DrupalWebTestCase::randomString().

@param $length
  Length of random string to generate.

@return
  Randomly generated string.

@see DrupalWebTestCase::randomString()
```

## Code

```php
  public static function randomName($length = 8) {
    $values = array_merge(range(65, 90), range(97, 122), range(48, 57));
    $max = count($values) - 1;
    $str = chr(mt_rand(97, 122));
    for ($i = 1; $i < $length; $i++) {
      $str .= chr($values[mt_rand(0, $max)]);
    }
    return $str;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
