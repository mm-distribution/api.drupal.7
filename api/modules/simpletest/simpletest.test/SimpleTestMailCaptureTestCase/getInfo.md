# SimpleTestMailCaptureTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 462–468 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L462-L468)
- **Class:** [SimpleTestMailCaptureTestCase](../SimpleTestMailCaptureTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
public static function getInfo()
```

## Documentation

```text
Implement getInfo().
```

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'SimpleTest e-mail capturing',
      'description' => 'Test the SimpleTest e-mail capturing logic, the assertMail assertion and the drupalGetMails function.',
      'group' => 'SimpleTest',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
