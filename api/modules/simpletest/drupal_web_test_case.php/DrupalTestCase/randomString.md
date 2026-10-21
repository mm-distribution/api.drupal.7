# DrupalTestCase::randomString()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 660–666 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L660-L666)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
public static function randomString($length = 8)
```

## Documentation

```text
Generates a random string of ASCII characters of codes 32 to 126.

The generated string includes alpha-numeric characters and common
miscellaneous characters. Use this method when testing general input
where the content is not restricted.

Do not use this method when special characters are not possible (e.g., in
machine or file names that have already been validated); instead,
use DrupalWebTestCase::randomName().

@param $length
  Length of random string to generate.

@return
  Randomly generated string.

@see DrupalWebTestCase::randomName()
```

## Code

```php
  public static function randomString($length = 8) {
    $str = '';
    for ($i = 0; $i < $length; $i++) {
      $str .= chr(mt_rand(32, 126));
    }
    return $str;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
